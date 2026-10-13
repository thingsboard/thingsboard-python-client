
# SkipReason

`tb_pe_client.models.SkipReason`

## Enum Values


* `VERSION_MISMATCH` (value: `'VERSION_MISMATCH'`)

* `ACTIVE_EVENT` (value: `'ACTIVE_EVENT'`)

* `RATE_LIMIT_EXCEEDED` (value: `'RATE_LIMIT_EXCEEDED'`)

* `ERROR` (value: `'ERROR'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SkipReason.model_validate(data)` or `SkipReason.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

