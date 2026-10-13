
# AgentAppEventActionType

`tb_paas_client.models.AgentAppEventActionType`

## Enum Values


* `INSTALL` (value: `'INSTALL'`)

* `UPDATE` (value: `'UPDATE'`)

* `DELETE` (value: `'DELETE'`)

* `RESTART` (value: `'RESTART'`)

* `ROLLBACK` (value: `'ROLLBACK'`)

* `UPGRADE` (value: `'UPGRADE'`)

* `AGENT_UPGRADE` (value: `'AGENT_UPGRADE'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppEventActionType.model_validate(data)` or `AgentAppEventActionType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

