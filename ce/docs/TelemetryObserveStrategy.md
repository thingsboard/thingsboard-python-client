
# TelemetryObserveStrategy

`tb_ce_client.models.TelemetryObserveStrategy`

Observation strategy for telemetry. SINGLE (0): one resource equals one single observe request. COMPOSITE_ALL (1): all resources in one composite observe request. COMPOSITE_BY_OBJECT (2): grouped composite observe requests by object.

## Enum Values


* `SINGLE` (value: `'SINGLE'`)

* `COMPOSITE_ALL` (value: `'COMPOSITE_ALL'`)

* `COMPOSITE_BY_OBJECT` (value: `'COMPOSITE_BY_OBJECT'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TelemetryObserveStrategy.model_validate(data)` or `TelemetryObserveStrategy.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

