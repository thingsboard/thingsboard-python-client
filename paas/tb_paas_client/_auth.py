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
        token,
        refresh_token,
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

    Thread safety: a threading.Lock protects the _refreshing flag so that only
    one concurrent API thread triggers a refresh call. Other threads wait at the
    lock and skip the refresh once the first thread completes.
    """

    def __init__(self, base_url: str, auth_type: str, api_key=None):
        """
        Args:
            base_url:  ThingsBoard server URL (e.g. "http://tb-server:9090").
                       Trailing slashes are stripped.
            auth_type: Either 'jwt' (username/password or token) or 'api_key'.
            api_key:   The API key string when auth_type='api_key', else None.
        """
        self._base_url = base_url.rstrip("/")
        # Resolve the auth mode once: it never changes, and every later decision
        # (initial token state, header prefix, whether the hook refreshes) follows
        # from it. Keeping the string comparison here means an unexpected auth_type
        # can't be read as api_key by one branch and jwt by another.
        self._is_api_key = auth_type == "api_key"
        self._header_prefix = _API_KEY_PREFIX if self._is_api_key else _JWT_PREFIX
        self._lock = threading.Lock()
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

    def set_external_token(self, token: str, refresh_token=None) -> None:
        """Set a pre-existing token without storing login credentials."""
        self._token_info = self._build_token_info(token, refresh_token or "")

    def get_token(self):
        """Return the current access token, or None if not yet set."""
        return self._token_info.token

    def get_refresh_token(self):
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
        with self._lock:
            if self._refreshing:
                # Another thread is already refreshing — skip
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
            with self._lock:
                self._refreshing = False

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
        """
        http = urllib3.PoolManager()
        response = http.request(
            "POST",
            self._base_url + path,
            body=body,
            headers={"Content-Type": "application/json"},
        )
        if response.status != 200:
            raise RuntimeError(f"Auth request to {path} returned HTTP {response.status}")
        return json.loads(response.data)

    def _build_token_info(self, token: str, refresh_token: str) -> "_TokenInfo":
        """Parse JWT claims from token and refresh_token; compute clock_diff."""
        now_ms = int(time.time() * 1000)
        token_exp = _parse_jwt_claim_ms(token, "exp")
        refresh_exp = _parse_jwt_claim_ms(refresh_token, "exp") if refresh_token else -1
        iat = _parse_jwt_claim_ms(token, "iat")
        # clock_diff: positive means server clock is ahead of local clock
        clock_diff = (iat - now_ms) if iat >= 0 else 0
        return _TokenInfo(token, refresh_token, token_exp, refresh_exp, clock_diff)
