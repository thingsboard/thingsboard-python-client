"""
Unit tests for ThingsboardClient — WRAP-01 through WRAP-04.

All tests import from tb_ce_client.client — the committed overlay copy of
common/client.py. conftest.py adds ce/ to sys.path so this works without packaging.
"""

import unittest
from unittest.mock import ANY, MagicMock, patch

from tb_ce_client._retry import _RetryingRESTClient
from tb_ce_client.client import ThingsboardClient
from tb_ce_client.rest import RESTClientObject

from tests._jwt import make_refresh_token, make_token

URL = "http://tb-server:9090"

# Patch the login endpoint at its module path so the mock survives module eviction
# and re-import by test_split.py's lazy-load tests.
_LOGIN_PATCH_TARGET = "tb_ce_client.api.login_endpoint_api.LoginEndpointApi.login"


def _mock_login_response(token="test.jwt.token", refresh_token="test.jwt.refresh"):
    """Build a mock LoginResponse object."""
    resp = MagicMock()
    resp.token = token
    resp.refresh_token = refresh_token
    return resp


def _logged_in_client(token="test.jwt.token", refresh_token="test.jwt.refresh"):
    """Construct a ThingsboardClient through a mocked username/password login."""
    resp = _mock_login_response(token, refresh_token)
    with patch(_LOGIN_PATCH_TARGET, return_value=resp):
        return ThingsboardClient(URL, "user@tb.io", "pass123")


class TestThingsboardClientJWTLogin(unittest.TestCase):
    """WRAP-01, AUTH-01 integration: username/password login flow."""

    def _assert_header_slot(self, client, token, prefix):
        """The X-Authorization slot holds this token under this prefix."""
        cfg = client.api_client.configuration
        self.assertEqual(cfg.api_key.get("ApiKeyForm"), token)
        self.assertEqual(cfg.api_key_prefix.get("ApiKeyForm"), prefix)

    def test_jwt_login(self):
        """ThingsboardClient(url, username, password) calls login() and stores tokens."""
        mock_resp = _mock_login_response()
        with patch(_LOGIN_PATCH_TARGET, return_value=mock_resp) as mock_login:
            client = ThingsboardClient(URL, "user@tb.io", "pass123")
        mock_login.assert_called_once()
        # Token stored in auth manager
        self.assertEqual(client.get_token(), mock_resp.token)

    def test_jwt_login_emits_x_authorization_header(self):
        """AUTH-01: auth_settings() yields the header an API request actually sends."""
        client = _logged_in_client()
        auth = client.api_client.configuration.auth_settings()
        self.assertIn("ApiKeyForm", auth)
        self.assertEqual(auth["ApiKeyForm"]["key"], "X-Authorization")
        self.assertEqual(auth["ApiKeyForm"]["value"], "Bearer test.jwt.token")

    def test_jwt_header_follows_token_rotation(self):
        """AUTH-02: seeding at login does not freeze the first token.

        Covers the whole seed -> hook -> refresh chain: the client logs in with an
        already-expired access token, and reading auth_settings() drives the hook
        through a real /api/auth/token refresh before the header is assembled.
        """
        client = _logged_in_client(
            token=make_token(exp_offset_s=-3600),
            refresh_token=make_refresh_token(exp_offset_s=86400),
        )
        rotated = make_token(exp_offset_s=3600)
        refreshed = {"token": rotated, "refreshToken": make_refresh_token(exp_offset_s=172800)}
        with patch.object(client._auth_manager, "_raw_post", return_value=refreshed) as mock_post:
            auth = client.api_client.configuration.auth_settings()
        mock_post.assert_called_once_with("/api/auth/token", ANY)
        self.assertEqual(auth["ApiKeyForm"]["value"], f"Bearer {rotated}")

    def test_api_key_auth(self):
        """WRAP-01, AUTH-05: api_key sets header without calling login()."""
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            client = ThingsboardClient(URL, api_key="test-key")
        mock_login.assert_not_called()
        self._assert_header_slot(client, "test-key", "ApiKey")

    def test_preexisting_token(self):
        """WRAP-01, AUTH-06: pre-existing token sets header without login()."""
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            client = ThingsboardClient(
                URL, token="jwt.payload.sig", refresh_token="jwt.refresh.sig"
            )
        mock_login.assert_not_called()
        self._assert_header_slot(client, "jwt.payload.sig", "Bearer")
        self.assertEqual(client.get_refresh_token(), "jwt.refresh.sig")

    def test_preexisting_token_without_refresh_token(self):
        """token= alone is valid — the token is simply never refreshed.

        The mutual-exclusion and companion checks deliberately do not pair token= with
        refresh_token=, so this pins the asymmetry the docstring describes. The refresh
        token is None rather than "", matching get_refresh_token()'s documented contract.
        """
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            client = ThingsboardClient(URL, token="jwt.payload.sig")
        mock_login.assert_not_called()
        self._assert_header_slot(client, "jwt.payload.sig", "Bearer")
        self.assertIsNone(client.get_refresh_token())

    def test_no_auth_leaves_header_slot_absent(self):
        """A client built without auth kwargs creates no ApiKeyForm slot.

        Legitimate for the /api/noauth endpoints: construction must not raise, and
        auth_settings() must stay empty so no X-Authorization header is sent.
        """
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            client = ThingsboardClient(URL)
        mock_login.assert_not_called()
        cfg = client.api_client.configuration
        self.assertNotIn("ApiKeyForm", cfg.api_key)
        self.assertEqual(cfg.auth_settings(), {})


class TestThingsboardClientAuthArgValidation(unittest.TestCase):
    """The three auth modes share one X-Authorization slot, so mixing them is rejected."""

    def test_api_key_with_username_rejected(self):
        """api_key= plus username= raises before any login call is made.

        Allowing both would install a JWT under api_key auth, where the refresh
        hook is a no-op — the token would be frozen and every request would start
        failing with 401 once it expired.
        """
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            with self.assertRaisesRegex(ValueError, "username, api_key"):
                ThingsboardClient(URL, "user@tb.io", "pass123", api_key="test-key")
        mock_login.assert_not_called()

    def test_api_key_with_token_rejected(self):
        """api_key= plus token= raises."""
        with self.assertRaisesRegex(ValueError, "api_key, token"):
            ThingsboardClient(URL, api_key="test-key", token="jwt.payload.sig")

    def test_username_with_token_rejected(self):
        """username= plus token= raises."""
        with patch(_LOGIN_PATCH_TARGET):
            with self.assertRaisesRegex(ValueError, "username, token"):
                ThingsboardClient(URL, "user@tb.io", "pass123", token="jwt.payload.sig")

    def test_all_three_modes_rejected(self):
        """All three at once raises and the message names every colliding mode."""
        with patch(_LOGIN_PATCH_TARGET):
            with self.assertRaisesRegex(ValueError, "username, api_key, token"):
                ThingsboardClient(
                    URL, "user@tb.io", "pass123", api_key="test-key", token="jwt.payload.sig"
                )

    def test_password_without_username_rejected(self):
        """password= alone would be silently dropped, so it raises instead."""
        with self.assertRaisesRegex(ValueError, "password= requires username="):
            ThingsboardClient(URL, password="pass123")

    def test_refresh_token_without_token_rejected(self):
        """refresh_token= alone would be silently dropped, so it raises instead."""
        with self.assertRaisesRegex(ValueError, "refresh_token= requires token="):
            ThingsboardClient(URL, refresh_token="jwt.payload.sig")

    def test_username_without_password_rejected(self):
        """username= alone raises here rather than as a pydantic error from LoginRequest."""
        with patch(_LOGIN_PATCH_TARGET) as mock_login:
            with self.assertRaisesRegex(ValueError, "username= requires password="):
                ThingsboardClient(URL, "user@tb.io")
        mock_login.assert_not_called()


class TestThingsboardClientStructure(unittest.TestCase):
    """WRAP-02: ThingsboardClient has api_client and _auth_manager attributes."""

    def test_has_api_client_and_auth_manager(self):
        """ThingsboardClient exposes api_client and _auth_manager attributes."""
        client = ThingsboardClient(URL, api_key="k")
        self.assertTrue(hasattr(client, "api_client"))
        self.assertTrue(hasattr(client, "_auth_manager"))


class TestThingsboardClientContextManager(unittest.TestCase):
    """WRAP-03: Context manager protocol."""

    def test_context_manager(self):
        """with ThingsboardClient(...) as client: returns self, no exception."""
        with ThingsboardClient(URL, api_key="k") as client:
            self.assertIsInstance(client, ThingsboardClient)

    def test_enter_returns_self(self):
        """__enter__ returns the client instance."""
        client = ThingsboardClient(URL, api_key="k")
        result = client.__enter__()
        self.assertIs(result, client)


class TestThingsboardClientPoolCleanup(unittest.TestCase):
    """WRAP-04: Connection pool cleanup."""

    def test_pool_cleanup_on_close(self):
        """close() calls pool_manager.clear()."""
        client = ThingsboardClient(URL, api_key="k")
        mock_clear = MagicMock()
        client.api_client.rest_client.pool_manager.clear = mock_clear
        client.close()
        mock_clear.assert_called_once()

    def test_pool_cleanup_on_exit(self):
        """__exit__ (via context manager) calls pool_manager.clear()."""
        client = ThingsboardClient(URL, api_key="k")
        mock_clear = MagicMock()
        client.api_client.rest_client.pool_manager.clear = mock_clear
        with client:
            pass
        mock_clear.assert_called_once()


class TestThingsboardClientRetry(unittest.TestCase):
    """RESL-04 integration: retry_on_rate_limit flag."""

    def test_retry_enabled_by_default(self):
        """Default: rest_client is _RetryingRESTClient."""
        client = ThingsboardClient(URL, api_key="k")
        self.assertIsInstance(client.api_client.rest_client, _RetryingRESTClient)

    def test_retry_disabled(self):
        """retry_on_rate_limit=False: rest_client is plain RESTClientObject (not retrying)."""
        client = ThingsboardClient(URL, api_key="k", retry_on_rate_limit=False)
        self.assertNotIsInstance(client.api_client.rest_client, _RetryingRESTClient)
        self.assertIsInstance(client.api_client.rest_client, RESTClientObject)


class TestThingsboardClientRefreshHook(unittest.TestCase):
    """AUTH-02 integration: refresh_api_key_hook is installed."""

    def test_refresh_hook_installed(self):
        """configuration.refresh_api_key_hook is not None after construction."""
        client = ThingsboardClient(URL, api_key="k")
        hook = client.api_client.configuration.refresh_api_key_hook
        self.assertIsNotNone(hook)
        self.assertTrue(callable(hook))


class TestThingsboardClientTokenAccessors(unittest.TestCase):
    """get_token() and get_refresh_token() delegation to _auth_manager."""

    def test_get_token_api_key(self):
        """get_token() returns the API key when using api_key auth."""
        client = ThingsboardClient(URL, api_key="my-api-key")
        self.assertEqual(client.get_token(), "my-api-key")

    def test_get_token_jwt(self):
        """get_token() returns the JWT after successful login."""
        client = _logged_in_client(token="access.jwt.here")
        self.assertEqual(client.get_token(), "access.jwt.here")

    def test_get_refresh_token_jwt(self):
        """get_refresh_token() returns the refresh JWT after login."""
        client = _logged_in_client(refresh_token="refresh.jwt.here")
        self.assertEqual(client.get_refresh_token(), "refresh.jwt.here")


if __name__ == "__main__":
    unittest.main()
