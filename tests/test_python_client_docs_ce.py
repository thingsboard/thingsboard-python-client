"""
Mirrors every Python code snippet from the CE Python client documentation page
(``/docs/reference/python-client/``). Each snippet appears character-for-character
with two allowances:

- placeholder values (``"{BASE_URL}"``, ``"YOUR_API_KEY_VALUE"``, ``"YOUR_DEVICE_ID"``,
  ``"YOUR_ASSET_ID"``, ``"nonexistent-id"``, ``"tenant@thingsboard.org"`` / ``"tenant"``)
  are swapped for real test values;
- ``print(...)`` calls inside the snippet are replaced with equivalent ``assert``
  checks, so the test actually verifies behavior instead of only syntax.

HTTP is mocked at the ``urllib3.PoolManager.request`` level via the helper in
``_doc_mock_http`` — the snippets never reach the network.
"""

import json

import pytest

from ._doc_mock_http import (
    ASSET_UUID,
    DEVICE_UUID,
    MOCK_USER_EMAIL,
    MockHttp,
    asset_payload,
    device_payload,
    user_payload,
)

MOCK_URL = "http://tb.test:9090"
API_KEY = "test-api-key"


@pytest.fixture
def mock_http(monkeypatch):
    http = MockHttp()
    http.patch(monkeypatch)
    return http


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#quickstart
# ---------------------------------------------------------------------------


def test_quickstart(mock_http):
    mock_http.add("POST", r"/api/device", json_body=device_payload("Quickstart Device"))
    mock_http.add(
        "POST",
        rf"/api/plugins/telemetry/DEVICE/{DEVICE_UUID}/timeseries/ANY",
        json_body=None,
    )
    mock_http.add("DELETE", rf"/api/device/{DEVICE_UUID}", json_body=None)

    # === doc snippet ===
    import json
    from tb_ce_client import ThingsboardClient
    from tb_ce_client.models import Device

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        saved = client.save_device(Device(name="Quickstart Device", type="default"))
        device_id = str(saved.id.id)

        client.save_entity_telemetry(
            entity_type="DEVICE",
            entity_id=device_id,
            scope="ANY",
            body=json.dumps({"temperature": 22.4}),
        )
        assert saved.name == "Quickstart Device"

        client.delete_device(device_id=device_id)

    # post-snippet verification
    mock_http.assert_called("POST", r"/api/device")
    telemetry_calls = mock_http.assert_called(
        "POST", rf"/api/plugins/telemetry/DEVICE/{DEVICE_UUID}/timeseries/ANY"
    )
    assert json.loads(telemetry_calls[0]["body"]) == {"temperature": 22.4}
    mock_http.assert_called("DELETE", rf"/api/device/{DEVICE_UUID}")


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#api-key-recommended
# ---------------------------------------------------------------------------


def test_authentication_via_api_key(mock_http):
    mock_http.add("GET", r"/api/auth/user", json_body=user_payload())

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        assert client.get_user().email == MOCK_USER_EMAIL

    mock_http.assert_called("GET", r"/api/auth/user")


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#username-and-password-jwt
# ---------------------------------------------------------------------------


def test_authentication_via_credentials(mock_http):
    mock_http.add(
        "POST",
        r"/api/auth/login",
        json_body={"token": "mock.jwt.token", "refreshToken": "mock.jwt.refresh"},
    )
    mock_http.add("GET", r"/api/auth/user", json_body=user_payload())

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient

    with ThingsboardClient(
        MOCK_URL,
        username=MOCK_USER_EMAIL,
        password="tenant",
    ) as client:
        assert client.get_user().email == MOCK_USER_EMAIL

    mock_http.assert_called("POST", r"/api/auth/login")
    mock_http.assert_called("GET", r"/api/auth/user")


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#rate-limit-handling
# ---------------------------------------------------------------------------


def test_rate_limit_handling_builder_options(mock_http):
    # The snippet only constructs a client; api_key auth makes no HTTP calls
    # on construction, so no routes need to be registered.

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient

    client = ThingsboardClient(
        MOCK_URL,
        api_key=API_KEY,
        max_retries=3,                # default 3
        initial_retry_delay_ms=1_000, # default 1 s
        max_retry_delay_ms=30_000,    # default 30 s
    )

    # post-snippet verification: the tuned client was constructed and exposes the API surface
    assert callable(client.get_tenant_devices)
    client.close()
    assert mock_http.calls == []


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#working-with-entities
# ---------------------------------------------------------------------------


def test_working_with_entities(mock_http):
    mock_http.add("POST", r"/api/device", json_body=device_payload("Test Device"))
    mock_http.add("GET", rf"/api/device/{DEVICE_UUID}", json_body=device_payload("Test Device"))
    mock_http.add("DELETE", rf"/api/device/{DEVICE_UUID}", json_body=None)

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient
    from tb_ce_client.models import Device

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        new_device = Device(name="Test Device", type="default")
        saved = client.save_device(new_device)
        device_id = str(saved.id.id)  # saved.id is EntityId wrapper, .id is the UUID

        fetched = client.get_device_by_id(device_id=device_id)
        assert fetched.name == "Test Device"

        client.delete_device(device_id=device_id)

    mock_http.assert_called("POST", r"/api/device")
    mock_http.assert_called("GET", rf"/api/device/{DEVICE_UUID}")
    mock_http.assert_called("DELETE", rf"/api/device/{DEVICE_UUID}")


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#push-telemetry
# ---------------------------------------------------------------------------


def test_push_telemetry(mock_http):
    real_device_id = DEVICE_UUID
    mock_http.add(
        "POST",
        rf"/api/plugins/telemetry/DEVICE/{real_device_id}/timeseries/ANY",
        json_body=None,
    )

    # === doc snippet ===
    import json
    from tb_ce_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        device_id = real_device_id
        client.save_entity_telemetry(
            entity_type="DEVICE",
            entity_id=device_id,
            scope="ANY",  # required by URL path; server-ignored for telemetry
            body=json.dumps({"temperature": 26.5, "humidity": 87}),
        )

    calls = mock_http.assert_called(
        "POST", rf"/api/plugins/telemetry/DEVICE/{real_device_id}/timeseries/ANY"
    )
    assert json.loads(calls[0]["body"]) == {"temperature": 26.5, "humidity": 87}


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#read-and-write-attributes
# ---------------------------------------------------------------------------


def test_read_modify_write_attributes(mock_http):
    real_asset_id = ASSET_UUID
    # GET returns one existing attribute with value 4 (the snippet will increment to 5)
    mock_http.add(
        "GET",
        rf"/api/plugins/telemetry/ASSET/{real_asset_id}/values/attributes/SERVER_SCOPE",
        json_body=[{"key": "deviceCount", "value": 4, "lastUpdateTs": 0}],
    )
    mock_http.add(
        "POST",
        rf"/api/plugins/telemetry/ASSET/{real_asset_id}/attributes/SERVER_SCOPE",
        json_body=None,
    )

    # === doc snippet ===
    import json
    from tb_ce_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        asset_id = real_asset_id

        attrs = client.get_attributes_by_scope(
            entity_type="ASSET",
            entity_id=asset_id,
            scope="SERVER_SCOPE",
            keys="deviceCount",  # comma-separated; pass "k1,k2,k3" for multiple
        )

        current = int(attrs[0].value) if attrs else 0
        updated = current + 1

        client.save_entity_attributes_v2(
            entity_type="ASSET",
            entity_id=asset_id,
            scope="SERVER_SCOPE",
            body=json.dumps({"deviceCount": updated}),
        )

    # post-snippet verification: snippet posted exactly current+1
    save_calls = mock_http.assert_called(
        "POST", rf"/api/plugins/telemetry/ASSET/{real_asset_id}/attributes/SERVER_SCOPE"
    )
    assert json.loads(save_calls[0]["body"]) == {"deviceCount": 5}


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#paginated-tenant-list
# ---------------------------------------------------------------------------


def test_paginated_tenant_list(mock_http):
    mock_http.add(
        "GET",
        r"/api/tenant/devices",
        json_body={
            "data": [
                device_payload("Page Device A"),
                device_payload("Page Device B"),
            ],
            "totalPages": 1,
            "totalElements": 2,
            "hasNext": False,
        },
    )

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        page = 0  # pages are zero-indexed
        while True:
            devices = client.get_tenant_devices(page_size=100, page=page)
            for device in devices.data:
                assert device.name and device.id.id
            if not devices.has_next:
                break
            page += 1

    # post-snippet verification: pagination terminated and made exactly one call
    mock_http.assert_called("GET", r"/api/tenant/devices", times=1)


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#filtered-query-with-entity-data-query-api
# ---------------------------------------------------------------------------


def test_entity_data_query_count_filtered(mock_http):
    # The route is called twice — once with no key_filters (total=3), then with
    # the active filter (active=2). The mock returns the same body, but the
    # snippet drives both branches and asserts the actual value match.
    counts = iter([b"3", b"2"])

    def _route_with_dynamic_count():
        next_body = next(counts)
        mock_http.add("POST", r"/api/entitiesQuery/count", raw_body=next_body)

    _route_with_dynamic_count()
    _route_with_dynamic_count()

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient
    from tb_ce_client.models import (
        EntityCountQuery, EntityTypeFilter, KeyFilter, EntityKey,
        BooleanFilterPredicate, FilterPredicateValueBoolean,
    )

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        type_filter = EntityTypeFilter(entity_type="DEVICE")

        total = client.count_entities_by_query(
            EntityCountQuery(entity_filter=type_filter)
        )
        assert total == 3

        active_filter = KeyFilter(
            key=EntityKey(type="ATTRIBUTE", key="active"),
            value_type="BOOLEAN",
            predicate=BooleanFilterPredicate(
                operation="EQUAL",
                value=FilterPredicateValueBoolean(default_value=True),
            ),
        )
        active = client.count_entities_by_query(
            EntityCountQuery(entity_filter=type_filter, key_filters=[active_filter])
        )
        assert active == 2

    mock_http.assert_called("POST", r"/api/entitiesQuery/count", times=2)


# ---------------------------------------------------------------------------
# /docs/reference/python-client/#error-handling
# ---------------------------------------------------------------------------


def test_error_handling_404(mock_http):
    mock_http.add(
        "GET",
        r"/api/device/nonexistent-id",
        status=404,
        json_body={"status": 404, "message": "Device not found"},
    )

    caught_404 = {"value": False}

    # === doc snippet ===
    from tb_ce_client import ThingsboardClient
    from tb_ce_client.exceptions import ApiException, NotFoundException

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        try:
            device = client.get_device_by_id(device_id="nonexistent-id")
        except NotFoundException:
            caught_404["value"] = True
        except ApiException as e:
            pytest.fail(f"API error {e.status}: {e.body}")

    assert caught_404["value"], "Snippet did not enter the 404 branch"


# Reference unused-but-meaningful imports/symbols so static checkers don't flag them.
_ = (asset_payload,)  # used in PE module; re-exported via the shared mock module
