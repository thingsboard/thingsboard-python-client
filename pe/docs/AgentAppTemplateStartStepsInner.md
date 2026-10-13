
# AgentAppTemplateStartStepsInner

`tb_pe_client.models.AgentAppTemplateStartStepsInner`

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
| **state** | [**RunJobStepState**](RunJobStepState.md) |  | [optional] |
| **compose_templates** | **Dict[str, object]** |  | [optional] |



## Referenced Types

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

#### RunJobStepState  *(extends AgentAppStepState)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| image | StepFieldString |  | [optional] |
| entrypoint | StepFieldListString |  | [optional] |
| cmd | StepFieldListString |  | [optional] |
| env | StepFieldListString |  | [optional] |
| binds | StepFieldListString |  | [optional] |
| networks | StepFieldListString |  | [optional] |
| pull_images | StepFieldBoolean |  | [optional] |
| retries | StepFieldInteger |  | [optional] |
| network_from_service_image_regex_pattern | StepFieldString |  | [optional] |

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

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppTemplateStartStepsInner.model_validate(data)` or `AgentAppTemplateStartStepsInner.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

