
# Queue

`tb_pe_client.models.Queue`

A JSON value representing the queue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**QueueId**](QueueId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **name** | **str** |  | [optional] |
| **topic** | **str** |  | [optional] |
| **poll_interval** | **int** |  | [optional] |
| **partitions** | **int** |  | [optional] |
| **consumer_per_partition** | **bool** |  | [optional] |
| **pack_processing_timeout** | **int** |  | [optional] |
| **submit_strategy** | [**SubmitStrategy**](SubmitStrategy.md) |  | [optional] |
| **processing_strategy** | [**ProcessingStrategy**](ProcessingStrategy.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### SubmitStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SubmitStrategyType |  | [optional] |
| batch_size | int |  | [optional] |

#### ProcessingStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ProcessingStrategyType |  | [optional] |
| retries | int |  | [optional] |
| failure_percentage | float |  | [optional] |
| pause_between_retries | int |  | [optional] |
| max_pause_between_retries | int |  | [optional] |

#### SubmitStrategyType (enum)
`BURST` | `BATCH` | `SEQUENTIAL_BY_ORIGINATOR` | `SEQUENTIAL_BY_TENANT` | `SEQUENTIAL`

#### ProcessingStrategyType (enum)
`SKIP_ALL_FAILURES` | `SKIP_ALL_FAILURES_AND_TIMED_OUT` | `RETRY_ALL` | `RETRY_FAILED` | `RETRY_TIMED_OUT` | `RETRY_FAILED_AND_TIMED_OUT`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Queue.model_validate(data)` or `Queue.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

