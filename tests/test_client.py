"""
Unit tests for ThingsboardClient — WRAP-01 through WRAP-04.

All tests import from tb_ce_client.client (after common/ is copied to ce/).
conftest.py adds ce/ to sys.path so this works without packaging.
"""

import unittest
from unittest.mock import MagicMock, patch

from tb_ce_client._retry import _RetryingRESTClient

# conftest.py handles sys.path; this import will work once client.py is copied
from tb_ce_client.client import ThingsboardClient
from tb_ce_client.rest import RESTClientObject

URL = "http://tb-server:9090"
TOKEN = "test.jwt.token"
REFRESH_TOKEN = "test.jwt.refresh"

# Module-path patch target, so the mock works even if the module was evicted
# and re-imported by test_split.py lazy-load tests.
LOGIN_TARGET = "tb_ce_client.api.login_endpoint_api.LoginEndpointApi.login"


def _mock_login_response(token=TOKEN, refresh_token=REFRESH_TOKEN):
    """Build a mock LoginResponse object."""
    resp = MagicMock()
    resp.token = token
    resp.refresh_token = refresh_token
    return resp


def _login_client(token=TOKEN, refresh_token=REFRESH_TOKEN, **kwargs):
    """Construct a JWT client with login() mocked; return (client, mock_login)."""
    with patch(LOGIN_TARGET, return_value=_mock_login_response(token, refresh_token)) as mock_login:
        client = ThingsboardClient(URL, "user@tb.io", "pass123", **kwargs)
    return client, mock_login


class TestThingsboardClientJWTLogin(unittest.TestCase):
    """WRAP-01, AUTH-01 integration: username/password login flow."""

    def test_jwt_login(self):
        """ThingsboardClient(url, username, password) calls login() and stores tokens."""
        client, mock_login = _login_client()
        mock_login.assert_called_once()
        # Token stored in auth manager
        self.assertEqual(client.get_token(), TOKEN)

    def test_jwt_login_seeds_configuration_api_key(self):
        """AUTH-01: the login token is installed into configuration, not only the auth manager.

        Without the seed, auth_settings() never emits X-Authorization and every
        request goes out unauthenticated — see the comment in client.py.
        """
        client, _ = _login_client()
        cfg = client.api_client.configuration
        self.assertEqual(cfg.api_key.get("ApiKeyForm"), TOKEN)
        self.assertEqual(cfg.api_key_prefix.get("ApiKeyForm"), "Bearer")

    def test_jwt_login_emits_x_authorization_header(self):
        """AUTH-01: auth_settings() yields the header an API request actually sends."""
        client, _ = _login_client()
        auth = client.api_client.configuration.auth_settings()
        self.assertIn("ApiKeyForm", auth)
        self.assertEqual(auth["ApiKeyForm"]["key"], "X-Authorization")
        self.assertEqual(auth["ApiKeyForm"]["value"], f"Bearer {TOKEN}")

    def test_jwt_header_follows_token_rotation(self):
        """AUTH-02: seeding at login does not freeze the first token — the hook
        runs before every request, so refresh / re-login is picked up."""
        client, _ = _login_client()
        # Simulate what _do_refresh_token / _do_login do on expiry: swap in new tokens.
        client._auth_manager.on_login(
            "user@tb.io", "pass123", "rotated.jwt.token", "rotated.jwt.refresh"
        )
        auth = client.api_client.configuration.auth_settings()
        self.assertEqual(auth["ApiKeyForm"]["value"], "Bearer rotated.jwt.token")

    def test_api_key_auth(self):
        """WRAP-01, AUTH-05: api_key sets header without calling login()."""
        with patch(LOGIN_TARGET) as mock_login:
            client = ThingsboardClient(URL, api_key="test-key")
        mock_login.assert_not_called()
        cfg = client.api_client.configuration
        self.assertEqual(cfg.api_key.get("ApiKeyForm"), "test-key")
        self.assertEqual(cfg.api_key_prefix.get("ApiKeyForm"), "ApiKey")

    def test_preexisting_token(self):
        """WRAP-01, AUTH-06: pre-existing token sets header without login()."""
        with patch(LOGIN_TARGET) as mock_login:
            client = ThingsboardClient(
                URL, token="jwt.payload.sig", refresh_token="jwt.payload.sig"
            )
        mock_login.assert_not_called()
        cfg = client.api_client.configuration
        self.assertEqual(cfg.api_key.get("ApiKeyForm"), "jwt.payload.sig")


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
        client, _ = _login_client(token="access.jwt.here")
        self.assertEqual(client.get_token(), "access.jwt.here")

    def test_get_refresh_token_jwt(self):
        """get_refresh_token() returns the refresh JWT after login."""
        client, _ = _login_client(refresh_token="refresh.jwt.here")
        self.assertEqual(client.get_refresh_token(), "refresh.jwt.here")


if __name__ == "__main__":
    unittest.main()
