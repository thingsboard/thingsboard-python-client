
# AgentAppStepType

`tb_paas_client.models.AgentAppStepType`

## Enum Values


* `COMPOSE_TEMPLATE` (value: `'COMPOSE_TEMPLATE'`)

* `COMPOSE` (value: `'COMPOSE'`)

* `COMPOSE_START` (value: `'COMPOSE_START'`)

* `COMPOSE_DOWN` (value: `'COMPOSE_DOWN'`)

* `ROLLBACK` (value: `'ROLLBACK'`)

* `BACKUP_VOLUME` (value: `'BACKUP_VOLUME'`)

* `BACKUP_VOLUME_REMOVE` (value: `'BACKUP_VOLUME_REMOVE'`)

* `COMPOSE_RESTART` (value: `'COMPOSE_RESTART'`)

* `RUN_JOB` (value: `'RUN_JOB'`)

* `AGENT_PREPARE` (value: `'AGENT_PREPARE'`)

* `AGENT_FINALIZE` (value: `'AGENT_FINALIZE'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppStepType.model_validate(data)` or `AgentAppStepType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

