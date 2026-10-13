
# ComposeDownStep

`tb_paas_client.models.ComposeDownStep`

**Extends:** **AgentAppStep**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **state** | [**ComposeDownStepState**](ComposeDownStepState.md) |  | [optional] |



## Referenced Types

#### AgentAppStep
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID |  | [optional] |
| next_id | UUID |  | [optional] |
| title | str |  | [optional] |
| template_only | bool |  | [optional] |
| condition | str |  | [optional] |
| stateful | bool |  | [optional] |
| type | AgentAppStepType |  | [optional] |

#### ComposeDownStepState  *(extends AgentAppStepState)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| service_image_regex_patterns | StepFieldListString |  | [optional] |
| remove_volumes | StepFieldBoolean |  | [optional] |

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

#### AgentAppStepState
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AgentAppStepType |  | [optional] |

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

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.state`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ComposeDownStep.model_validate(data)` or `ComposeDownStep.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

