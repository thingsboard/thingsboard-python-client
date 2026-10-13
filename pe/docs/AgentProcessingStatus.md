
# AgentProcessingStatus

`tb_pe_client.models.AgentProcessingStatus`

## Enum Values


* `PENDING` (value: `'PENDING'`)

* `QUEUED` (value: `'QUEUED'`)

* `PROCESSING` (value: `'PROCESSING'`)

* `FINISHED` (value: `'FINISHED'`)

* `ERROR` (value: `'ERROR'`)

* `START_FAILED` (value: `'START_FAILED'`)



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentProcessingStatus.model_validate(data)` or `AgentProcessingStatus.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

