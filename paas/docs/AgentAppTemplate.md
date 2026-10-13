
# AgentAppTemplate

`tb_paas_client.models.AgentAppTemplate`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **app_type** | [**AgentApplicationType**](AgentApplicationType.md) | Application type | |
| **config_type** | [**AgentAppConfigType**](AgentAppConfigType.md) | Config type (e.g. 'DOCKER_COMPOSE'); the compose body lives in the template's compose-template step, not here | [optional] |
| **current_version** | **str** | Current template version | |
| **next_version** | **str** | Next template version | [optional] |
| **start_steps** | [**List[AgentAppTemplateStartStepsInner]**](AgentAppTemplateStartStepsInner.md) | Start steps | [optional] |
| **upgrade_steps** | [**List[AgentAppTemplateStartStepsInner]**](AgentAppTemplateStartStepsInner.md) | Upgrade steps | [optional] |
| **delete_steps** | [**List[AgentAppTemplateStartStepsInner]**](AgentAppTemplateStartStepsInner.md) | Delete steps | [optional] |
| **rollback_steps** | [**List[AgentAppTemplateStartStepsInner]**](AgentAppTemplateStartStepsInner.md) | Rollback steps | [optional] |
| **restart_steps** | [**List[AgentAppTemplateStartStepsInner]**](AgentAppTemplateStartStepsInner.md) | Restart steps | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentApplicationType (enum)
`GENERIC` | `EDGE` | `GATEWAY`

#### AgentAppConfigType (enum)
`DOCKER_COMPOSE`

#### AgentAppTemplateStartStepsInner
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID |  | [optional] |
| next_id | UUID |  | [optional] |
| title | str |  | [optional] |
| template_only | bool |  | [optional] |
| condition | str |  | [optional] |
| stateful | bool |  | [optional] |
| type | AgentAppStepType |  | [optional] |
| state | RunJobStepState |  | [optional] |
| compose_templates | Dict[str, object] |  | [optional] |

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

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.tenant_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppTemplate.model_validate(data)` or `AgentAppTemplate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

