#
# Copyright © 2026-2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
_auth.py — JWT token state, automatic refresh, clock-skew compensation, re-login, and
the refresh_api_key_hook callback for the ThingsBoard Python client.

This file lives in common/ and is copied verbatim into each edition package directory
by generate-client.sh. Use only relative imports and stdlib; no edition-specific imports.
"""

import base64
import json
import logging
import threading
import time

import urllib3

logger = logging.getLogger(__name__)

# Matches Java's AuthManager.AVG_REQUEST_TIMEOUT (30 seconds in ms)
AVG_REQUEST_TIMEOUT_MS = 30_000

# Wall-clock ceiling for a single raw auth call. urllib3 defaults to no timeout at all,
# and every API thread now blocks behind an in-flight refresh, so an unresponsive auth
# endpoint would otherwise hang the whole process rather than one thread.
#
# Applied as Timeout(total=...) rather than a bare float, which would set connect and
# read separately and leave total unbounded. Because _AUTH_RETRIES makes exactly one
# request — no retry, no redirect — total is the whole ceiling; urllib3 gives each
# attempt its own budget, so any allowance there would multiply this number.
DEFAULT_AUTH_TIMEOUT_MS = 30_000

# Retry policy for the raw auth calls, spelled out rather than left to urllib3, so that
# exactly one request goes out and DEFAULT_AUTH_TIMEOUT_MS means what it says.
#
# No retries: Retry.DEFAULT is total=3, and its connection-error branch never consults
# allowed_methods, so this POST would retry and cost 4x the ceiling above. Auth POSTs are
# not idempotent, and the timeout exists precisely to bound how long every other thread
# sits blocked, so a single attempt is the deliberate trade — a caller wanting tolerance
# should retry ThingsboardClient(...) itself, since urllib3 has no global deadline that
# would let us have both.
#
# No redirects either, which is a departure from the generated RESTClientObject:
#   - urllib3 clones the timeout per hop instead of drawing down a shared budget, so
#     following N redirects costs (1 + N) x auth_timeout_ms on the one round-trip every
#     other API thread is blocked behind.
#   - the body is re-sent to whatever Location names, with no same-origin restriction,
#     so a redirect out of the configured server hands username/password to a third host
#     and _do_login would install the token it returns.
# The case this gives up is a deployment that redirects auth (a proxy forcing https,
# path normalisation). Failing loudly is the better answer there: on an http -> https
# redirect the credentials have already gone out in cleartext, so the fix is to pass the
# final auth URL as url=, which _raw_post's error tells the caller to do.
#
# total is set explicitly: it defaults to 10, and leaving it there would contradict the
# "exactly one request" this whole block is for, even though the per-class zeros already
# exhaust first. urllib3 normalises redirect=False to 0.
_AUTH_RETRIES = urllib3.Retry(total=0, connect=0, read=0, status=0, other=0, redirect=False)

# Security scheme name and prefixes dictated by the generated configuration.py.
# Keep them in one place so a spec regeneration that renames the scheme has a
# single owner instead of literals scattered across client.py and _auth.py.
_SECURITY_SCHEME = "ApiKeyForm"
_JWT_PREFIX = "Bearer"
_API_KEY_PREFIX = "ApiKey"


# ---------------------------------------------------------------------------
# _TokenInfo
# ---------------------------------------------------------------------------


class _TokenInfo:
    """Immutable value object holding JWT token state.

    All timestamps are in milliseconds since epoch.
    clock_diff = iat_ms_from_server - local_now_ms at login time (may be negative).
    """

    __slots__ = ("token", "refresh_token", "token_exp_ts", "refresh_exp_ts", "clock_diff")

    def __init__(
        self,
        token: "str | None",
        refresh_token: "str | None",
        token_exp_ts: int,
        refresh_exp_ts: int,
        clock_diff: int,
    ):
        self.token = token
        self.refresh_token = refresh_token
        self.token_exp_ts = token_exp_ts  # -1 means unknown / invalid
        self.refresh_exp_ts = refresh_exp_ts  # -1 means unknown / invalid
        self.clock_diff = clock_diff  # server_clock - local_clock offset in ms


# Sentinel used before first login
_TokenInfo.EMPTY = _TokenInfo(None, None, -1, -1, 0)  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------
# JWT helpers
# ---------------------------------------------------------------------------


def _parse_jwt_claim_ms(jwt: str, claim: str) -> int:
    """Decode JWT payload (base64url) and return the named claim value * 1000 (ms).

    Returns -1 on any error (missing parts, bad base64, missing claim, type error).
    No signature verification — ThingsBoard tokens are trusted from the server.
    """
    try:
        # JWT structure: header.payload.signature — we only need the payload
        payload_b64 = jwt.split(".")[1]
        # JWT strips base64 padding — add it back before decoding
        padding = (4 - len(payload_b64) % 4) % 4
        payload_bytes = base64.urlsafe_b64decode(payload_b64 + "=" * padding)
        claims = json.loads(payload_bytes)
        return int(claims[claim]) * 1000
    except Exception:
        return -1


# ---------------------------------------------------------------------------
# _AuthManager
# ---------------------------------------------------------------------------


class _AuthManager:
    """Manages JWT token state and implements the refresh_api_key_hook.

    Mirrors the Java ThingsboardClient.java inner AuthManager class.

    Thread safety: a threading.Condition guards the _refreshing flag so that only
    one concurrent API thread performs a refresh. The others block until that
    refresh finishes and then use its result — they must not proceed meanwhile,
    since the token they would send is the expired one being replaced.

    The auth mode is decided once in __init__ and never re-derived per request.
    """

    def __init__(
        self,
        base_url: str,
        api_key: "str | None" = None,
        auth_timeout_ms: int = DEFAULT_AUTH_TIMEOUT_MS,
    ):
        """
        Args:
            base_url: ThingsBoard server URL (e.g. "http://tb-server:9090").
                      Trailing slashes are stripped.
            api_key:  The API key string for API key auth, or None for JWT auth
                      (username/password or an externally supplied token).
            auth_timeout_ms: Ceiling for a single /api/auth call, in milliseconds.
                      Bounds how long every other thread can be blocked behind a
                      refresh, so it is a knob a slow on-prem server or a
                      latency-sensitive caller will want to change.
        """
        # urllib3.Timeout rejects a non-positive total, but it would only raise inside
        # _raw_post — where _do_refresh_token and _do_login catch Exception and log —
        # so a bad value would construct fine and then silently never refresh.
        if auth_timeout_ms <= 0:
            raise ValueError(f"auth_timeout_ms must be positive; got {auth_timeout_ms}")
        self._auth_timeout_s = auth_timeout_ms / 1000
        self._base_url = base_url.rstrip("/")
        self._is_api_key = api_key is not None
        self._header_prefix = _API_KEY_PREFIX if self._is_api_key else _JWT_PREFIX
        self._refresh_state = threading.Condition()
        self._refreshing = False
        self._username = None
        self._password = None

        if self._is_api_key:
            self._token_info = _TokenInfo(api_key, None, -1, -1, 0)
        else:
            self._token_info = _TokenInfo.EMPTY  # type: ignore[attr-defined]

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def on_login(self, username: str, password: str, token: str, refresh_token: str) -> None:
        """Store credentials and build token state from the login response tokens."""
        self._username = username
        self._password = password
        self._token_info = self._build_token_info(token, refresh_token)

    def set_external_token(self, token: str, refresh_token: "str | None" = None) -> None:
        """Set a pre-existing token without storing login credentials.

        refresh_token is passed through as-is so that omitting it leaves
        get_refresh_token() returning None, as its docstring promises.
        """
        self._token_info = self._build_token_info(token, refresh_token)

    def get_token(self) -> "str | None":
        """Return the current access token, or None if not yet set."""
        return self._token_info.token

    def get_refresh_token(self) -> "str | None":
        """Return the current refresh token, or None if not available."""
        return self._token_info.refresh_token

    def install_header(self, configuration) -> None:
        """Write the current token into configuration's X-Authorization slots.

        Configuration.auth_settings() emits the header only when the security
        scheme is already present in configuration.api_key, so the slot has to be
        seeded at construction time before the hook can ever take over.
        """
        token = self._token_info.token
        if not token:
            # No auth configured (e.g. /api/noauth usage) — leave the slot absent
            # so auth_settings() emits no header at all.
            return
        configuration.api_key[_SECURITY_SCHEME] = token
        configuration.api_key_prefix[_SECURITY_SCHEME] = self._header_prefix

    def hook(self, configuration) -> None:
        """refresh_api_key_hook implementation.

        Called by Configuration.get_api_key_with_prefix() immediately before
        every API request assembles its X-Authorization header. Checks token
        expiry and refreshes if needed, then updates configuration.api_key.
        """
        if self._is_api_key:
            # API key auth — hook is a no-op; the key is set at construction time
            return
        self._refresh_if_needed()
        self.install_header(configuration)

    # ------------------------------------------------------------------
    # Internal refresh logic
    # ------------------------------------------------------------------

    def _refresh_if_needed(self) -> None:
        """Check token expiry and trigger refresh if the estimated server time
        exceeds the token expiry (with AVG_REQUEST_TIMEOUT buffer)."""
        with self._refresh_state:
            if self._refreshing:
                # Another thread is already refreshing. Block rather than return:
                # returning here would send the expired token that thread is busy
                # replacing, and nothing retries the resulting 401.
                self._refresh_state.wait_for(lambda: not self._refreshing)
                # Its outcome is ours. Refreshing again on failure would multiply one
                # failed round-trip by however many threads were waiting.
                return
            info = self._token_info
            if info.token is None or info.token_exp_ts < 0:
                # No token or unknown expiry — nothing to refresh
                return
            now_ms = int(time.time() * 1000)
            estimated_server_time = now_ms + info.clock_diff + AVG_REQUEST_TIMEOUT_MS
            if estimated_server_time <= info.token_exp_ts:
                # Token still valid
                return
            # Token is (about to be) expired — claim the refresh slot
            self._refreshing = True

        try:
            info = self._token_info
            now_ms = int(time.time() * 1000)
            estimated_server_time = now_ms + info.clock_diff + AVG_REQUEST_TIMEOUT_MS
            if info.refresh_token and estimated_server_time < info.refresh_exp_ts:
                self._do_refresh_token(info)
            elif self._username:
                self._do_login()
        finally:
            with self._refresh_state:
                self._refreshing = False
                self._refresh_state.notify_all()

    def _do_refresh_token(self, info: "_TokenInfo") -> None:
        """POST to /api/auth/token with the refresh token. Falls back to login on error."""
        try:
            body = json.dumps({"refreshToken": info.refresh_token}).encode()
            resp = self._raw_post("/api/auth/token", body)
            self._token_info = self._build_token_info(resp["token"], resp["refreshToken"])
        except Exception as exc:
            logger.warning("Token refresh failed: %s", exc)
            if self._username:
                self._do_login()

    def _do_login(self) -> None:
        """POST to /api/auth/login with stored credentials. Logs error on failure."""
        try:
            body = json.dumps({"username": self._username, "password": self._password}).encode()
            resp = self._raw_post("/api/auth/login", body)
            self._token_info = self._build_token_info(resp["token"], resp["refreshToken"])
        except Exception as exc:
            logger.error("Re-login failed: %s", exc)

    def _raw_post(self, path: str, body: bytes) -> dict:
        """Low-level urllib3 POST that bypasses the ApiClient interceptor.

        Auth calls MUST use raw urllib3 to avoid interceptor recursion —
        if we used ApiClient here, the hook would fire again while already
        inside the hook, causing infinite recursion (mirrors Java's pattern
        of using a separate raw HttpClient for AuthManager calls).

        Bounded by auth_timeout_ms and _AUTH_RETRIES: this call is on the critical path
        for every thread waiting on a refresh, so it makes exactly one request — no
        retry, no redirect. See _AUTH_RETRIES for why both trades are deliberate.
        """
        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            self._base_url + path,
            body=body,
            headers={"Content-Type": "application/json"},
            timeout=urllib3.Timeout(total=self._auth_timeout_s),
            retries=_AUTH_RETRIES,
        )
        if response.status != 200:
            # 3xx arrives here rather than being followed — say so, since the remedy is
            # specific and not guessable from the status alone.
            hint = (
                "; auth requests do not follow redirects, so pass the final auth URL as url="
                if 300 <= response.status < 400
                else ""
            )
            raise RuntimeError(f"Auth request to {path} returned HTTP {response.status}{hint}")
        return json.loads(response.data)

    def _build_token_info(self, token: str, refresh_token: "str | None") -> "_TokenInfo":
        """Parse JWT claims from token and refresh_token; compute clock_diff."""
        now_ms = int(time.time() * 1000)
        token_exp = _parse_jwt_claim_ms(token, "exp")
        refresh_exp = _parse_jwt_claim_ms(refresh_token, "exp") if refresh_token else -1
        iat = _parse_jwt_claim_ms(token, "iat")
        # clock_diff: positive means server clock is ahead of local clock
        clock_diff = (iat - now_ms) if iat >= 0 else 0
        return _TokenInfo(token, refresh_token, token_exp, refresh_exp, clock_diff)
