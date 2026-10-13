
# AgentAppEventStepStatesValue

`tb_pe_client.models.AgentAppEventStepStatesValue`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**AgentAppStepType**](AgentAppStepType.md) |  | [optional] |
| **backup_volumes** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **service_image_regex_patterns** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **remove_volumes** | [**StepFieldBoolean**](StepFieldBoolean.md) |  | [optional] |
| **pull_images** | [**StepFieldBoolean**](StepFieldBoolean.md) |  | [optional] |
| **failed_event_id** | [**StepFieldAgentAppEventId**](StepFieldAgentAppEventId.md) |  | [optional] |
| **image** | [**StepFieldString**](StepFieldString.md) |  | [optional] |
| **entrypoint** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **cmd** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **env** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **binds** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **networks** | [**StepFieldListString**](StepFieldListString.md) |  | [optional] |
| **retries** | [**StepFieldInteger**](StepFieldInteger.md) |  | [optional] |
| **network_from_service_image_regex_pattern** | [**StepFieldString**](StepFieldString.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

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

#### StepFieldAgentAppEventId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | AgentAppEventId |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | str |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | int |  | [optional] |
| user_choice | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppEventStepStatesValue.model_validate(data)` or `AgentAppEventStepStatesValue.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

