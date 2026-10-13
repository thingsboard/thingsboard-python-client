
# AgentAppStep

`tb_pe_client.models.AgentAppStep`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **UUID** |  | [optional] |
| **next_id** | **UUID** |  | [optional] |
| **title** | **str** |  | [optional] |
| **template_only** | **bool** |  | [optional] |
| **condition** | **str** |  | [optional] |
| **stateful** | **bool** |  | [optional] |
| **type** | [**AgentAppStepType**](AgentAppStepType.md) |  | [optional] |



## Referenced Types

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppStep.model_validate(data)` or `AgentAppStep.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

