
# BackupVolumesStepState

`tb_paas_client.models.BackupVolumesStepState`

**Extends:** **AgentAppStepState**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **backup_volumes** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |



## Referenced Types

#### AgentAppStepState
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AgentAppStepType |  | [optional] |

#### StepFieldListString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| user_choice | bool |  | [optional] |
| value | List[str] |  | [optional] |

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.backup_volumes`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BackupVolumesStepState.model_validate(data)` or `BackupVolumesStepState.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

