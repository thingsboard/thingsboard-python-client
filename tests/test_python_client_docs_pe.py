"""
Mirrors every Python code snippet from the PE Python client documentation page
(``/docs/pe/reference/python-client/``). Each snippet appears character-for-character
with two allowances:

- placeholder values (``"{BASE_URL}"``, ``"YOUR_API_KEY_VALUE"``, ``"YOUR_DEVICE_ID"``,
  ``"YOUR_ASSET_ID"``, ``"YOUR_CUSTOMER_ID"``, ``"YOUR_DEVICE_GROUP_ID"``,
  ``"nonexistent-id"``, ``"tenant@thingsboard.org"`` / ``"tenant"``) are swapped for
  real test values;
- ``print(...)`` calls inside the snippet are replaced with equivalent ``assert``
  checks.

HTTP is mocked at the ``urllib3.PoolManager.request`` level via the helper in
``_doc_mock_http``.
"""

import json

import pytest

from ._doc_mock_http import (
    ASSET_UUID,
    CUSTOMER_UUID,
    DEVICE_GROUP_UUID,
    DEVICE_UUID,
    MOCK_USER_EMAIL,
    MockHttp,
    ROLE_UUID,
    TENANT_UUID,
    USER_GROUP_UUID,
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


def _entity_group_payload(name: str, group_type: str = "DEVICE") -> dict:
    return {
        "id": {"id": DEVICE_GROUP_UUID, "entityType": "ENTITY_GROUP"},
        "name": name,
        "type": group_type,
        "ownerIds": [{"id": TENANT_UUID, "entityType": "TENANT"}],
    }


def _role_payload(name: str, role_type: str = "GROUP") -> dict:
    return {
        "id": {"id": ROLE_UUID, "entityType": "ROLE"},
        "name": name,
        "type": role_type,
    }


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#quickstart
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
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.models import Device

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

    mock_http.assert_called("POST", r"/api/device")
    telemetry_calls = mock_http.assert_called(
        "POST", rf"/api/plugins/telemetry/DEVICE/{DEVICE_UUID}/timeseries/ANY"
    )
    assert json.loads(telemetry_calls[0]["body"]) == {"temperature": 22.4}
    mock_http.assert_called("DELETE", rf"/api/device/{DEVICE_UUID}")


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#api-key-recommended
# ---------------------------------------------------------------------------


def test_authentication_via_api_key(mock_http):
    mock_http.add("GET", r"/api/auth/user", json_body=user_payload())

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        assert client.get_user().email == MOCK_USER_EMAIL

    mock_http.assert_called("GET", r"/api/auth/user")


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#username-and-password-jwt
# ---------------------------------------------------------------------------


def test_authentication_via_credentials(mock_http):
    mock_http.add(
        "POST",
        r"/api/auth/login",
        json_body={"token": "mock.jwt.token", "refreshToken": "mock.jwt.refresh"},
    )
    mock_http.add("GET", r"/api/auth/user", json_body=user_payload())

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient

    with ThingsboardClient(
        MOCK_URL,
        username=MOCK_USER_EMAIL,
        password="tenant",
    ) as client:
        assert client.get_user().email == MOCK_USER_EMAIL

    mock_http.assert_called("POST", r"/api/auth/login")
    mock_http.assert_called("GET", r"/api/auth/user")


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#rate-limit-handling
# ---------------------------------------------------------------------------


def test_rate_limit_handling_builder_options(mock_http):
    # === doc snippet ===
    from tb_pe_client import ThingsboardClient

    client = ThingsboardClient(
        MOCK_URL,
        api_key=API_KEY,
        max_retries=3,  # default 3
        initial_retry_delay_ms=1_000,  # default 1 s
        max_retry_delay_ms=30_000,  # default 30 s
    )

    assert callable(client.get_tenant_devices)
    client.close()
    assert mock_http.calls == []


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#working-with-entities
# ---------------------------------------------------------------------------


def test_working_with_entities(mock_http):
    mock_http.add("POST", r"/api/device", json_body=device_payload("Test Device"))
    mock_http.add("GET", rf"/api/device/{DEVICE_UUID}", json_body=device_payload("Test Device"))
    mock_http.add("DELETE", rf"/api/device/{DEVICE_UUID}", json_body=None)

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.models import Device

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
# /docs/pe/reference/python-client/#push-telemetry
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
    from tb_pe_client import ThingsboardClient

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
# /docs/pe/reference/python-client/#read-and-write-attributes
# ---------------------------------------------------------------------------


def test_read_modify_write_attributes(mock_http):
    real_asset_id = ASSET_UUID
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
    from tb_pe_client import ThingsboardClient

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

    save_calls = mock_http.assert_called(
        "POST", rf"/api/plugins/telemetry/ASSET/{real_asset_id}/attributes/SERVER_SCOPE"
    )
    assert json.loads(save_calls[0]["body"]) == {"deviceCount": 5}


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#paginated-tenant-list
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
    from tb_pe_client import ThingsboardClient

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        page = 0  # pages are zero-indexed
        while True:
            devices = client.get_tenant_devices(page_size=100, page=page)
            for device in devices.data:
                assert device.name and device.id.id
            if not devices.has_next:
                break
            page += 1

    mock_http.assert_called("GET", r"/api/tenant/devices", times=1)


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#filtered-query-with-entity-data-query-api
# ---------------------------------------------------------------------------


def test_entity_data_query_count_filtered(mock_http):
    counts = iter([b"3", b"2"])

    def _route_with_dynamic_count():
        next_body = next(counts)
        mock_http.add("POST", r"/api/entitiesQuery/count", raw_body=next_body)

    _route_with_dynamic_count()
    _route_with_dynamic_count()

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.models import (
        EntityCountQuery,
        EntityTypeFilter,
        KeyFilter,
        EntityKey,
        BooleanFilterPredicate,
        FilterPredicateValueBoolean,
    )

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        type_filter = EntityTypeFilter(entity_type="DEVICE")

        total = client.count_entities_by_query(EntityCountQuery(entity_filter=type_filter))
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
# /docs/pe/reference/python-client/#create-and-populate-a-group  (PE-only)
# ---------------------------------------------------------------------------


def test_create_and_populate_group(mock_http):
    real_device_id = DEVICE_UUID
    mock_http.add("POST", r"/api/entityGroup", json_body=_entity_group_payload("Acme Devices"))
    mock_http.add(
        "POST",
        rf"/api/entityGroup/{DEVICE_GROUP_UUID}/addEntities",
        json_body=None,
    )

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.models import EntityGroup

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        device_group = EntityGroup(name="Acme Devices", type="DEVICE")
        saved_group = client.save_entity_group(entity_group=device_group)
        device_group_id = str(saved_group.id.id)

        # add_entities_to_entity_group takes a list of raw UUID strings
        client.add_entities_to_entity_group(
            entity_group_id=device_group_id,
            request_body=[real_device_id],
        )

    save_calls = mock_http.assert_called("POST", r"/api/entityGroup")
    assert json.loads(save_calls[0]["body"])["name"] == "Acme Devices"
    add_calls = mock_http.assert_called(
        "POST", rf"/api/entityGroup/{DEVICE_GROUP_UUID}/addEntities"
    )
    assert json.loads(add_calls[0]["body"]) == [real_device_id]


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#share-with-a-customer  (PE-only)
# ---------------------------------------------------------------------------


def test_share_with_customer(mock_http):
    real_customer_id = CUSTOMER_UUID
    real_device_group_id = DEVICE_GROUP_UUID

    mock_http.add("POST", r"/api/role", json_body=_role_payload("Acme Device Readers"))
    mock_http.add(
        "GET",
        rf"/api/entityGroup/all/CUSTOMER/{real_customer_id}/USER",
        json_body={
            "id": {"id": USER_GROUP_UUID, "entityType": "ENTITY_GROUP"},
            "name": "All",
            "type": "USER",
            "ownerIds": [{"id": real_customer_id, "entityType": "CUSTOMER"}],
        },
    )
    mock_http.add(
        "POST",
        rf"/api/entityGroup/{real_device_group_id}/{USER_GROUP_UUID}/{ROLE_UUID}/share",
        json_body=None,
    )

    # === doc snippet ===
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.models import Role

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        customer_id = real_customer_id
        device_group_id = real_device_group_id

        role = Role(name="Acme Device Readers", type="GROUP")
        saved_role = client.save_role(role=role)
        role_id = str(saved_role.id.id)

        all_users = client.get_entity_group_all_by_owner_and_type(
            owner_type="CUSTOMER",
            owner_id=customer_id,
            group_type="USER",
        )
        user_group_id = str(all_users.id.id)

        client.share_entity_group_to_child_owner_user_group(
            entity_group_id=device_group_id,
            user_group_id=user_group_id,
            role_id=role_id,
        )

    # post-snippet verification: each of the three calls was made exactly once
    mock_http.assert_called("POST", r"/api/role")
    mock_http.assert_called("GET", rf"/api/entityGroup/all/CUSTOMER/{real_customer_id}/USER")
    mock_http.assert_called(
        "POST",
        rf"/api/entityGroup/{real_device_group_id}/{USER_GROUP_UUID}/{ROLE_UUID}/share",
    )


# ---------------------------------------------------------------------------
# /docs/pe/reference/python-client/#error-handling
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
    from tb_pe_client import ThingsboardClient
    from tb_pe_client.exceptions import ApiException, NotFoundException

    with ThingsboardClient(MOCK_URL, api_key=API_KEY) as client:
        try:
            device = client.get_device_by_id(device_id="nonexistent-id")
        except NotFoundException:
            caught_404["value"] = True
        except ApiException as e:
            pytest.fail(f"API error {e.status}: {e.body}")

    assert caught_404["value"], "Snippet did not enter the 404 branch"


_ = (asset_payload,)
