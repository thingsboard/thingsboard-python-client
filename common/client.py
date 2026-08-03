#
# Copyright 2026 ThingsBoard, Inc.
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
client.py — ThingsboardClient: the public-facing entry point for ThingsBoard Python clients.

This file lives in common/ and is copied verbatim into each edition package directory
by generate-client.sh. Use only relative imports and stdlib; no edition-specific imports.

ThingsboardClient wires:
  - _AuthManager for JWT/API key authentication and automatic token refresh
  - _RetryingRESTClient for transparent HTTP 429 retry with exponential backoff
  - __getattr__ delegation to per-controller API classes via _CONTROLLER_MAP
"""

import importlib

from ._auth import _AuthManager
from ._controller_map import _CONTROLLER_ATTR_MAP, _CONTROLLER_MAP
from ._retry import _RetryingRESTClient
from .api_client import ApiClient
from .configuration import Configuration
from .models.login_request import LoginRequest


class ThingsboardClient:
    """User-facing ThingsBoard client.

    Wraps the generated per-controller APIs with authentication management and
    transparent 429 retry. Supports three authentication modes, plus unauthenticated:

    1. Username + password (JWT):
         ThingsboardClient(url, username, password)
         Eagerly authenticates via /api/auth/login on construction.

    2. API key:
         ThingsboardClient(url, api_key="your-api-key")
         Sets X-Authorization: ApiKey <key> header; no login call made.

    3. Pre-existing token:
         ThingsboardClient(url, token="jwt", refresh_token="jwt")
         Injects an externally obtained JWT; no login call made.
         refresh_token is optional — omit it for a token that is never refreshed.

    The three modes are mutually exclusive — passing more than one raises ValueError.
    All auth arguments are optional: omitting them yields an unauthenticated client
    that sends no X-Authorization header, which is what the /api/noauth endpoints want.

    Context manager usage:
         with ThingsboardClient(url, api_key="key") as client:
             devices = client.get_tenant_devices(page_size=10, page=0)
    """

    def __init__(
        self,
        url: str,
        username: "str | None" = None,
        password: "str | None" = None,
        api_key: "str | None" = None,
        token: "str | None" = None,
        refresh_token: "str | None" = None,
        max_retries: int = 3,
        initial_retry_delay_ms: int = 1_000,
        max_retry_delay_ms: int = 30_000,
        retry_on_rate_limit: bool = True,
    ):
        """Construct ThingsboardClient and authenticate.

        Args:
            url: Base URL of the ThingsBoard server (e.g. "http://tb:9090").
            username: Username for JWT authentication.
            password: Password for JWT authentication.
            api_key: API key for X-Authorization: ApiKey authentication.
            token: Pre-existing JWT access token.
            refresh_token: Pre-existing JWT refresh token (used with token=). Omit it
                to install a token that is never refreshed.
            max_retries: Maximum retry attempts on HTTP 429 (default 3).
            initial_retry_delay_ms: Base backoff delay in milliseconds (default 1000).
            max_retry_delay_ms: Maximum backoff cap in milliseconds (default 30000).
            retry_on_rate_limit: If True (default), wraps rest_client with
                _RetryingRESTClient. If False, uses plain RESTClientObject.

        Raises:
            ValueError: If more than one of username=, api_key= or token= is given;
                if password= is given without username= or vice versa; or if
                refresh_token= is given without token=.
        """
        # Must be the very first assignment — prevents __getattr__ infinite recursion
        # if __init__ raises partway through (before self.api_client is set).
        self._controllers: dict = {}

        # The three auth modes share a single X-Authorization slot, so combining
        # them is ambiguous: whichever ran last would win, and under api_key auth
        # the refresh hook is a no-op, so a JWT installed alongside a key would be
        # frozen at its initial value and never refreshed.
        modes = [
            name
            for name, value in (("username", username), ("api_key", api_key), ("token", token))
            if value is not None
        ]
        if len(modes) > 1:
            raise ValueError(
                "ThingsboardClient authentication modes are mutually exclusive; "
                f"got {', '.join(modes)}"
            )
        # password= and refresh_token= are only read by their own mode's branch, so
        # on their own they would be silently dropped and surface later as a 401.
        if password is not None and username is None:
            raise ValueError("password= requires username=")
        if refresh_token is not None and token is None:
            raise ValueError("refresh_token= requires token=")
        # LoginRequest.password is a required StrictStr, so without this the caller
        # gets a pydantic ValidationError from inside the generated model instead.
        if username is not None and password is None:
            raise ValueError("username= requires password=")

        configuration = Configuration(host=url)

        auth_manager = _AuthManager(url, api_key)

        # Install the refresh hook so the hook fires before every API request
        configuration.refresh_api_key_hook = auth_manager.hook

        # Build the ApiClient
        api_client = ApiClient(configuration=configuration)

        # Optionally replace the default RESTClientObject with the retrying version
        if retry_on_rate_limit:
            api_client.rest_client = _RetryingRESTClient(
                configuration,
                max_retries,
                initial_retry_delay_ms,
                max_retry_delay_ms,
            )

        self.api_client = api_client
        self._auth_manager = auth_manager

        # JWT eager login
        if username is not None:
            from .api.login_endpoint_api import LoginEndpointApi

            login_api = LoginEndpointApi(api_client)
            response = login_api.login(LoginRequest(username=username, password=password))
            auth_manager.on_login(username, password, response.token, response.refresh_token)

        # Pre-existing token
        if token is not None:
            auth_manager.set_external_token(token, refresh_token)

        # Seed the header slot for whichever mode ran — see _AuthManager.install_header.
        auth_manager.install_header(configuration)

    # ------------------------------------------------------------------
    # Controller delegation
    # ------------------------------------------------------------------

    def _get_or_create_controller(self, cls_name: str, module_path: str):
        """Return (and cache) the controller instance for the given class.

        All controllers share self.api_client so they use the same auth/retry
        configuration as the ThingsboardClient that created them.
        """
        if cls_name not in self._controllers:
            module = importlib.import_module(module_path)
            cls = getattr(module, cls_name)
            self._controllers[cls_name] = cls(self.api_client)
        return self._controllers[cls_name]

    def __getattr__(self, name: str):
        """Delegate attribute/method access to the correct per-controller API.

        Lookup order:
          1. _CONTROLLER_ATTR_MAP — named controller shorthand (e.g. device_controller)
          2. _CONTROLLER_MAP — individual API method delegation

        Raises AttributeError for anything not in either map.
        """
        # Guard against infinite recursion if _controllers was not yet set
        # (can happen if __init__ raises before self._controllers = {}).
        if "_controllers" not in self.__dict__:
            raise AttributeError(name)

        # 1. Named controller attribute (e.g. client.device_controller)
        if name in _CONTROLLER_ATTR_MAP:
            module_path, cls_name = _CONTROLLER_ATTR_MAP[name]
            return self._get_or_create_controller(cls_name, module_path)

        # 2. Method delegation (e.g. client.get_tenant_devices)
        if name in _CONTROLLER_MAP:
            module_path, cls_name = _CONTROLLER_MAP[name]
            controller = self._get_or_create_controller(cls_name, module_path)
            return getattr(controller, name)

        raise AttributeError(f"'{type(self).__name__}' object has no attribute {name!r}")

    # ------------------------------------------------------------------
    # Token accessors
    # ------------------------------------------------------------------

    def get_token(self) -> "str | None":
        """Return the current access token (JWT or API key), or None."""
        return self._auth_manager.get_token()

    def get_refresh_token(self) -> "str | None":
        """Return the current refresh token, or None if not available."""
        return self._auth_manager.get_refresh_token()

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def close(self) -> None:
        """Release connection pool resources.

        Calls pool_manager.clear() on the underlying urllib3 pool to cleanly
        close all open connections. Automatically called by __exit__.
        """
        self.api_client.rest_client.pool_manager.clear()

    def __enter__(self) -> "ThingsboardClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.close()
        return False
