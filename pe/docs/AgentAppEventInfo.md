
# AgentAppEventInfo

`tb_pe_client.models.AgentAppEventInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AgentAppEventId**](AgentAppEventId.md) | JSON object with the Agent App Event Id. | [optional] |
| **created_time** | **int** | Timestamp of the event creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **application_id** | [**AgentApplicationId**](AgentApplicationId.md) |  | [optional] |
| **agent_id** | [**AgentId**](AgentId.md) |  | [optional] |
| **application_name** | **str** |  | [optional] |
| **action_type** | [**AgentAppEventActionType**](AgentAppEventActionType.md) |  | [optional] |
| **start_status** | [**ProcessingStartStatus**](ProcessingStartStatus.md) |  | [optional] |
| **processing_status** | [**AgentProcessingStatus**](AgentProcessingStatus.md) |  | [optional] |
| **current_step_id** | **UUID** |  | [optional] |
| **current_activity** | **str** |  | [optional] |
| **error_message** | **str** |  | [optional] |
| **updated_time** | **int** |  | [optional] |
| **step_states** | [**Dict[str, AgentAppEventStepStatesValue]**](AgentAppEventStepStatesValue.md) |  | [optional] |
| **bulk_action_id** | **UUID** |  | [optional] |
| **resolved_arguments** | **Dict[str, str]** |  | [optional] |
| **winner_container_id** | **str** |  | [optional] |
| **finalize_deadline_ts** | **int** |  | [optional] |
| **context_metadata** | **Dict[str, str]** |  | [optional] |
| **agent_name** | **str** | Name of the Agent that owns the Application. | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentAppEventActionType (enum)
`INSTALL` | `UPDATE` | `DELETE` | `RESTART` | `ROLLBACK` | `UPGRADE` | `AGENT_UPGRADE`

#### ProcessingStartStatus (enum)
`DELIVERY_FAIL` | `PENDING` | `DELIVERED`

#### AgentProcessingStatus (enum)
`PENDING` | `QUEUED` | `PROCESSING` | `FINISHED` | `ERROR` | `START_FAILED`

#### AgentAppEventStepStatesValue
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AgentAppStepType |  | [optional] |
| backup_volumes | StepFieldListString |  | [optional] |
| service_image_regex_patterns | StepFieldListString |  | [optional] |
| remove_volumes | StepFieldBoolean |  | [optional] |
| pull_images | StepFieldBoolean |  | [optional] |
| failed_event_id | StepFieldAgentAppEventId |  | [optional] |
| image | StepFieldString |  | [optional] |
| entrypoint | StepFieldListString |  | [optional] |
| cmd | StepFieldListString |  | [optional] |
| env | StepFieldListString |  | [optional] |
| binds | StepFieldListString |  | [optional] |
| networks | StepFieldListString |  | [optional] |
| retries | StepFieldInteger |  | [optional] |
| network_from_service_image_regex_pattern | StepFieldString |  | [optional] |

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
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppEventInfo.model_validate(data)` or `AgentAppEventInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

