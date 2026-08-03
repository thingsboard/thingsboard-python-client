"""
Unit tests for common._auth module.
Covers AUTH-01 through AUTH-06 requirements.
"""

import time
import unittest
from unittest.mock import MagicMock, patch

from common._auth import _AuthManager, _parse_jwt_claim_ms
from tests._jwt import _make_jwt, _make_refresh_token, _make_token

# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------


def _mock_configuration():
    """Return a minimal mock Configuration object."""
    config = MagicMock()
    config.api_key = {}
    config.api_key_prefix = {}
    return config


# ---------------------------------------------------------------------------
# Tests for _parse_jwt_claim_ms
# ---------------------------------------------------------------------------


class TestParseJwtClaimMs(unittest.TestCase):
    def test_parse_exp_claim(self):
        """_parse_jwt_claim_ms returns exp * 1000 for a valid JWT."""
        exp_seconds = int(time.time()) + 3600
        jwt = _make_jwt({"exp": exp_seconds, "iat": int(time.time())})
        result = _parse_jwt_claim_ms(jwt, "exp")
        self.assertEqual(result, exp_seconds * 1000)

    def test_parse_iat_claim(self):
        """_parse_jwt_claim_ms returns iat * 1000 for the iat claim."""
        iat_seconds = int(time.time())
        jwt = _make_jwt({"exp": iat_seconds + 3600, "iat": iat_seconds})
        result = _parse_jwt_claim_ms(jwt, "iat")
        self.assertEqual(result, iat_seconds * 1000)

    def test_invalid_jwt_returns_minus_one(self):
        """_parse_jwt_claim_ms returns -1 for an invalid JWT string."""
        self.assertEqual(_parse_jwt_claim_ms("invalid", "exp"), -1)
        self.assertEqual(_parse_jwt_claim_ms("", "exp"), -1)
        self.assertEqual(_parse_jwt_claim_ms("a.b", "exp"), -1)

    def test_missing_claim_returns_minus_one(self):
        """_parse_jwt_claim_ms returns -1 when the claim key is absent."""
        jwt = _make_jwt({"sub": "user@example.com"})
        self.assertEqual(_parse_jwt_claim_ms(jwt, "exp"), -1)

    def test_malformed_base64_returns_minus_one(self):
        """_parse_jwt_claim_ms returns -1 for non-base64 payload."""
        self.assertEqual(_parse_jwt_claim_ms("header.!!!.sig", "exp"), -1)


# ---------------------------------------------------------------------------
# AUTH-01: JWT Login
# ---------------------------------------------------------------------------


class TestJwtLogin(unittest.TestCase):
    def test_jwt_login(self):
        """on_login stores credentials and builds _TokenInfo from provided JWTs."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        token = _make_token(exp_offset_s=3600, iat_offset_s=0)
        refresh = _make_refresh_token(exp_offset_s=86400)

        auth.on_login("user@tb.io", "password", token, refresh)

        self.assertEqual(auth.get_token(), token)
        self.assertEqual(auth.get_refresh_token(), refresh)
        # token_info should have valid expiry times
        info = auth._token_info
        self.assertGreater(info.token_exp_ts, 0)
        self.assertGreater(info.refresh_exp_ts, 0)
        # clock_diff should be close to 0 (iat_offset_s=0)
        self.assertAlmostEqual(info.clock_diff, 0, delta=5000)


# ---------------------------------------------------------------------------
# AUTH-02: Auto-refresh
# ---------------------------------------------------------------------------


class TestHookRefreshesExpiredToken(unittest.TestCase):
    def test_hook_refreshes_expired_token(self):
        """hook() calls /api/auth/token when access token is expired but refresh is valid."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        # expired access token (exp in the past)
        old_token = _make_token(exp_offset_s=-3600, iat_offset_s=0)
        # valid refresh token
        refresh = _make_refresh_token(exp_offset_s=86400)
        auth.on_login("user@tb.io", "password", old_token, refresh)

        new_token = _make_token(exp_offset_s=7200, iat_offset_s=0)
        new_refresh = _make_refresh_token(exp_offset_s=172800)
        new_response_data = {"token": new_token, "refreshToken": new_refresh}

        with patch.object(auth, "_raw_post", return_value=new_response_data) as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        mock_post.assert_called_once_with("/api/auth/token", unittest.mock.ANY)
        self.assertEqual(config.api_key["ApiKeyForm"], new_token)
        self.assertEqual(config.api_key_prefix["ApiKeyForm"], "Bearer")

    def test_hook_skips_when_token_valid(self):
        """hook() does not call HTTP when access token is still valid."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        # token valid for an hour
        token = _make_token(exp_offset_s=3600, iat_offset_s=0)
        refresh = _make_refresh_token(exp_offset_s=86400)
        auth.on_login("user@tb.io", "password", token, refresh)

        with patch.object(auth, "_raw_post") as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        mock_post.assert_not_called()
        self.assertEqual(config.api_key["ApiKeyForm"], token)
        self.assertEqual(config.api_key_prefix["ApiKeyForm"], "Bearer")


# ---------------------------------------------------------------------------
# AUTH-03: Clock-skew compensation
# ---------------------------------------------------------------------------


class TestClockSkewCompensation(unittest.TestCase):
    def test_clock_skew_compensation(self):
        """clock_diff is computed from iat; a 5s server-ahead skew is absorbed into estimates."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        # iat is 5 seconds ahead of "now" (simulates server clock being 5s ahead)
        skew_s = 5
        token = _make_token(exp_offset_s=skew_s + 35, iat_offset_s=skew_s)
        refresh = _make_refresh_token(exp_offset_s=86400)

        auth.on_login("user@tb.io", "password", token, refresh)

        # clock_diff should be approximately +5000 ms
        self.assertAlmostEqual(auth._token_info.clock_diff, skew_s * 1000, delta=2000)

        # With AVG_REQUEST_TIMEOUT=30s and clock_diff=+5s, estimated_server_time = now + 5s + 30s = now + 35s
        # token_exp = now + 40s (skew+35 from actual now).
        # estimated_server_time (now+35s) < token_exp (now+40s) --> should NOT refresh
        with patch.object(auth, "_raw_post") as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        mock_post.assert_not_called()


# ---------------------------------------------------------------------------
# AUTH-04: Re-login fallback
# ---------------------------------------------------------------------------


class TestReloginOnRefreshExpiry(unittest.TestCase):
    def test_relogin_on_refresh_expiry(self):
        """hook() calls /api/auth/login when both access and refresh tokens are expired."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        expired_token = _make_token(exp_offset_s=-7200, iat_offset_s=0)
        expired_refresh = _make_refresh_token(exp_offset_s=-3600)
        auth.on_login("user@tb.io", "password", expired_token, expired_refresh)

        new_token = _make_token(exp_offset_s=3600, iat_offset_s=0)
        new_refresh = _make_refresh_token(exp_offset_s=86400)
        new_response_data = {"token": new_token, "refreshToken": new_refresh}

        with patch.object(auth, "_raw_post", return_value=new_response_data) as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        mock_post.assert_called_once_with("/api/auth/login", unittest.mock.ANY)
        self.assertEqual(config.api_key["ApiKeyForm"], new_token)

    def test_refresh_failure_falls_back_to_relogin(self):
        """When refresh fails, _do_login is called as fallback (AUTH-04)."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        # expired access token, but valid refresh token so _do_refresh_token will be tried first
        expired_token = _make_token(exp_offset_s=-7200, iat_offset_s=0)
        valid_refresh = _make_refresh_token(exp_offset_s=86400)
        auth.on_login("user@tb.io", "password", expired_token, valid_refresh)

        new_token = _make_token(exp_offset_s=3600, iat_offset_s=0)
        new_refresh = _make_refresh_token(exp_offset_s=86400)
        new_response_data = {"token": new_token, "refreshToken": new_refresh}

        call_count = [0]

        def side_effect(path, body):
            call_count[0] += 1
            if call_count[0] == 1:
                raise RuntimeError("refresh endpoint down")
            return new_response_data

        with patch.object(auth, "_raw_post", side_effect=side_effect) as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        # First call should be to /api/auth/token, second to /api/auth/login
        calls = mock_post.call_args_list
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][0][0], "/api/auth/token")
        self.assertEqual(calls[1][0][0], "/api/auth/login")
        self.assertEqual(config.api_key["ApiKeyForm"], new_token)


# ---------------------------------------------------------------------------
# AUTH-05: API key passthrough
# ---------------------------------------------------------------------------


class TestApiKeyAuthNoRefresh(unittest.TestCase):
    def test_api_key_auth_no_refresh(self):
        """hook() returns immediately for api_key auth without making HTTP calls."""
        auth = _AuthManager("http://tb:9090", "api_key", "test-key-12345")

        with patch.object(auth, "_raw_post") as mock_post:
            config = _mock_configuration()
            auth.hook(config)

        mock_post.assert_not_called()
        # api_key auth hook should not modify configuration.api_key
        self.assertNotIn("ApiKeyForm", config.api_key)


# ---------------------------------------------------------------------------
# AUTH-06: Pre-existing token
# ---------------------------------------------------------------------------


class TestPreexistingToken(unittest.TestCase):
    def test_preexisting_token(self):
        """set_external_token parses exp times correctly from provided JWTs."""
        auth = _AuthManager("http://tb:9090", "jwt", None)
        now_s = int(time.time())
        token = _make_jwt({"exp": now_s + 3600, "iat": now_s})
        refresh = _make_jwt({"exp": now_s + 86400})

        auth.set_external_token(token, refresh)

        info = auth._token_info
        self.assertAlmostEqual(info.token_exp_ts, (now_s + 3600) * 1000, delta=5000)
        self.assertAlmostEqual(info.refresh_exp_ts, (now_s + 86400) * 1000, delta=5000)
        # No credentials stored — re-login should not be attempted on expiry
        self.assertIsNone(auth._username)
        self.assertIsNone(auth._password)


if __name__ == "__main__":
    unittest.main()
