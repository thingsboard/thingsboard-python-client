
# RunJobStepState

`tb_pe_client.models.RunJobStepState`

**Extends:** **AgentAppStepState**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **image** | [**StepFieldString**](StepFieldString.md) |  | [optional] |
| **entrypoint** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **cmd** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **env** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **binds** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **networks** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **pull_images** | [**StepFieldBoolean**](StepFieldBoolean.md) |  | [optional] |
| **retries** | [**StepFieldInteger**](StepFieldInteger.md) |  | [optional] |
| **network_from_service_image_regex_pattern** | [**StepFieldString**](StepFieldString.md) |  | [optional] |



## Referenced Types

#### AgentAppStepState
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AgentAppStepType |  | [optional] |

#### StepFieldString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | str |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldListString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| user_choice | bool |  | [optional] |
| value | List[str] |  | [optional] |

#### StepFieldBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | bool |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | int |  | [optional] |
| user_choice | bool |  | [optional] |

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.image`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RunJobStepState.model_validate(data)` or `RunJobStepState.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

