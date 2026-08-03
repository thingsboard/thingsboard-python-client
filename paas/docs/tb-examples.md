# Usage Examples

> Examples use `tb_ce_client`. Substitute `tb_pe_client` or `tb_paas_client` for other editions.

## JWT Login

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient(
    "http://localhost:9090",
    username="tenant@thingsboard.org",
    password="tenant",
)
print("Logged in, token:", client.get_token()[:20], "...")
```

## API Key Login

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient("http://localhost:9090", api_key="your-api-key")
```

## Pre-existing Token

Injects an externally obtained JWT; no login call is made.

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient(
    "http://localhost:9090",
    token="eyJhbGciOi...",
    refresh_token="eyJhbGciOi...",
)
```

## No Authentication

All auth arguments are optional. Omit them for a client that sends no
`X-Authorization` header, for use with the `/api/noauth` endpoints.

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient("http://localhost:9090")
```

The three authenticated modes above are mutually exclusive — passing more than one
raises `ValueError`, as does passing `username=` without `password=` or vice versa, or
`refresh_token=` without `token=`. `token=` on its own is valid; it simply means the
token is never refreshed.

## Context Manager

```python
from tb_ce_client import ThingsboardClient
from tb_ce_client.exceptions import ApiException

with ThingsboardClient("http://localhost:9090", username="tenant@thingsboard.org", password="tenant") as client:
    try:
        devices = client.get_tenant_devices(page_size=10, page=0)
        for device in devices.data:
            print(device.name, device.id.get_id())
    except ApiException as e:
        print(f"Error {e.status}: {e.reason}")
# Connection pool released automatically
```

## List Devices

```python
# Paginated device listing — returns PageDataDevice
devices = client.get_tenant_devices(page_size=10, page=0)
print(f"Total devices: {devices.total_elements}")
for device in devices.data:
    print(f"  {device.name} (id={device.id.get_id()})")

# Check if more pages exist
if devices.has_next:
    page2 = client.get_tenant_devices(page_size=10, page=1)
```

## Push Telemetry

```python
import json

device_id = "784f394c-42b6-435a-983c-b7beff2784f9"
client.save_entity_telemetry(
    entity_type="DEVICE",
    entity_id=device_id,
    scope="ANY",
    body=json.dumps({"temperature": 26.5, "humidity": 87}),
)
```

The `body` parameter accepts a JSON string, not a Python dict.

## List Alarms

```python
# Paginated alarm listing — returns PageDataAlarmInfo
alarms = client.get_all_alarms(page_size=10, page=0)
for alarm in alarms.data:
    print(f"  [{alarm.severity}] {alarm.type}: {alarm.status}")
```

## Error Handling

```python
from tb_ce_client.exceptions import ApiException, NotFoundException

try:
    device = client.get_device_by_id(device_id="nonexistent-id")
except NotFoundException:
    print("Device not found")
except ApiException as e:
    print(f"API error {e.status}: {e.body}")
```

## Read Attributes

```python
# Read server-scope attributes for a device
attrs = client.get_attributes(
    entity_type="DEVICE",
    entity_id=device_id,
    keys="active,lastConnectTime",
)
for attr in attrs:
    print(f"  {attr.key} = {attr.value}")
```

## Save Attributes

```python
import json

client.save_entity_attributes_v2(
    entity_type="DEVICE",
    entity_id=device_id,
    scope="SHARED_SCOPE",
    body=json.dumps({"targetTemperature": 22}),
)
```
