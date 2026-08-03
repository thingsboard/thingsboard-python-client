# ThingsBoard Python Client

Auto-generated Python REST clients for ThingsBoard IoT platform. Available for Community Edition (CE), Professional Edition (PE), and PaaS.

## Quickstart

### Install

```
pip install tb-ce-client       # Community Edition
# pip install tb-pe-client     # Professional Edition
# pip install tb-paas-client   # PaaS
```

### Authenticate

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient(
    "http://localhost:9090",
    username="tenant@thingsboard.org",
    password="tenant",
)
```

### Make an API call

```python
devices = client.get_tenant_devices(page_size=10, page=0)
for device in devices.data:
    print(device.name, device.id.get_id())
```

### Handle errors

```python
from tb_ce_client.exceptions import ApiException, NotFoundException

try:
    device = client.get_device_by_id(device_id="nonexistent-id")
except NotFoundException:
    print("Device not found")
except ApiException as e:
    print(f"API error {e.status}: {e.body}")
```

## Authentication modes

**Username and password (JWT):** Authenticates at construction time via `/api/auth/login`.

```python
from tb_ce_client import ThingsboardClient

client = ThingsboardClient(
    "http://localhost:9090",
    username="tenant@thingsboard.org",
    password="tenant",
)
```

**API key:** Sets `X-Authorization: ApiKey <key>` header on every request; no login call is made.

```python
client = ThingsboardClient("http://localhost:9090", api_key="your-api-key")
```

**Pre-existing token:** Injects an externally obtained JWT; no login call is made.

```python
client = ThingsboardClient(
    "http://localhost:9090",
    token="eyJhbGciOi...",
    refresh_token="eyJhbGciOi...",
)
```

**No authentication:** All auth arguments are optional. Omit them to get a client that
sends no `X-Authorization` header, for use with the `/api/noauth` endpoints.

```python
client = ThingsboardClient("http://localhost:9090")
```

The three authenticated modes are mutually exclusive — passing more than one raises
`ValueError`, as does passing `username=` without `password=` or vice versa, or
`refresh_token=` without `token=`. `token=` on its own is valid; it simply means the
token is never refreshed.

## Resource cleanup

Use the client as a context manager so `close()` is called automatically on exit:

```python
with ThingsboardClient("http://localhost:9090", username="tenant@thingsboard.org", password="tenant") as client:
    devices = client.get_tenant_devices(page_size=10, page=0)
```

## Available editions

| Edition | Package | Install |
|---------|---------|---------|
| Community Edition | `tb-ce-client` | `pip install tb-ce-client` |
| Professional Edition | `tb-pe-client` | `pip install tb-pe-client` |
| PaaS | `tb-paas-client` | `pip install tb-paas-client` |

## Links

- [API documentation](ce/docs/) — per-controller and model reference for CE
- [Usage examples](ce/docs/tb-examples.md) — copy-paste examples for common operations
- [ThingsBoard](https://thingsboard.io) — official platform site
