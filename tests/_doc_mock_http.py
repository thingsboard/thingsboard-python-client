"""
HTTP mock used by the doc-snippet validation tests.

Monkeypatches ``urllib3.PoolManager.request`` at the class level so both the
mainline ``RESTClientObject`` path and ``_AuthManager._raw_post`` (which
constructs its own ``PoolManager``) land in the same dispatcher.

Each registered route is a (HTTP method, path regex, status, payload bytes)
tuple. The dispatcher records every call so tests can verify that the
snippet hit the expected endpoints with the expected body shape.
"""

import json
import re
from urllib.parse import urlparse

import urllib3


class _FakeResp:
    """Minimal duck-typed urllib3 response.

    Both ``RESTResponse`` (which reads ``.status``, ``.reason``, ``.data``,
    ``.headers``) and ``_AuthManager._raw_post`` (which reads ``.status`` and
    ``.data``) are satisfied by this shape.
    """

    def __init__(self, status: int, data: bytes, headers=None, reason: str = "OK"):
        self.status = status
        self.reason = reason
        self.data = data
        self.headers = headers or {"Content-Type": "application/json"}

    def read(self, *args, **kwargs) -> bytes:
        return self.data

    def release_conn(self) -> None:
        pass

    def close(self) -> None:
        pass


class MockHttp:
    """Route-based mock that records every call made by the client."""

    def __init__(self) -> None:
        self.routes: list = []
        self.calls: list = []

    def add(
        self,
        method: str,
        path_regex: str,
        status: int = 200,
        json_body=None,
        raw_body: bytes = None,
    ) -> None:
        """Register a route. ``json_body`` is JSON-encoded; ``raw_body`` is bytes-as-is."""
        if raw_body is not None:
            payload = raw_body
        elif json_body is None:
            payload = b""
        else:
            payload = json.dumps(json_body).encode()
        self.routes.append((method.upper(), re.compile(path_regex), status, payload))

    def patch(self, monkeypatch) -> None:
        mock = self

        def _patched_request(
            self,
            method,
            url,
            fields=None,
            headers=None,
            body=None,
            **kwargs,
        ):
            parsed = urlparse(url)
            path = parsed.path
            query = parsed.query
            req_body = body
            if isinstance(req_body, str):
                req_body = req_body.encode()
            mock.calls.append(
                {
                    "method": method.upper(),
                    "path": path,
                    "query": query,
                    "body": req_body,
                    "headers": headers or {},
                }
            )
            for idx, (r_method, r_pattern, r_status, r_payload) in enumerate(mock.routes):
                if r_method != method.upper():
                    continue
                if r_pattern.fullmatch(path):
                    # When the same (method, pattern) is registered more than
                    # once, treat each registration as a single-use queue entry
                    # so a sequence of calls hits each registered response in
                    # order. Otherwise the route remains so repeat calls to a
                    # single registration keep succeeding.
                    has_duplicate = any(
                        rm == r_method and rp.pattern == r_pattern.pattern
                        for rm, rp, _, _ in mock.routes[idx + 1 :]
                    )
                    if has_duplicate:
                        mock.routes.pop(idx)
                    return _FakeResp(r_status, r_payload)
            registered = ", ".join(f"{m} {p.pattern}" for m, p, _, _ in mock.routes)
            raise AssertionError(
                f"Unrouted request: {method.upper()} {path}?{query} (registered: {registered})"
            )

        monkeypatch.setattr(urllib3.PoolManager, "request", _patched_request, raising=True)

    def find_calls(self, method: str, path_regex: str) -> list:
        rx = re.compile(path_regex)
        return [c for c in self.calls if c["method"] == method.upper() and rx.fullmatch(c["path"])]

    def assert_called(self, method: str, path_regex: str, times: int = 1) -> list:
        matches = self.find_calls(method, path_regex)
        assert len(matches) == times, (
            f"Expected {times} call(s) to {method} {path_regex}, got {len(matches)}. "
            f"All calls: {[(c['method'], c['path']) for c in self.calls]}"
        )
        return matches


# ---------------------------------------------------------------------------
# Canned response payloads shared by CE and PE snippet tests
# ---------------------------------------------------------------------------

DEVICE_UUID = "11111111-1111-1111-1111-111111111111"
ASSET_UUID = "22222222-2222-2222-2222-222222222222"
CUSTOMER_UUID = "33333333-3333-3333-3333-333333333333"
DEVICE_GROUP_UUID = "44444444-4444-4444-4444-444444444444"
USER_GROUP_UUID = "55555555-5555-5555-5555-555555555555"
ROLE_UUID = "66666666-6666-6666-6666-666666666666"
USER_UUID = "77777777-7777-7777-7777-777777777777"
TENANT_UUID = "88888888-8888-8888-8888-888888888888"

MOCK_USER_EMAIL = "tenant@thingsboard.org"


def device_payload(name: str, device_type: str = "default") -> dict:
    return {
        "id": {"id": DEVICE_UUID, "entityType": "DEVICE"},
        "name": name,
        "type": device_type,
        "tenantId": {"id": TENANT_UUID, "entityType": "TENANT"},
    }


def asset_payload(name: str, asset_type: str = "building") -> dict:
    return {
        "id": {"id": ASSET_UUID, "entityType": "ASSET"},
        "name": name,
        "type": asset_type,
        "tenantId": {"id": TENANT_UUID, "entityType": "TENANT"},
    }


def user_payload(email: str = MOCK_USER_EMAIL) -> dict:
    return {
        "id": {"id": USER_UUID, "entityType": "USER"},
        "email": email,
        "authority": "TENANT_ADMIN",
        "tenantId": {"id": TENANT_UUID, "entityType": "TENANT"},
    }
