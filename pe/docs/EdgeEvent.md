
# EdgeEvent

`tb_pe_client.models.EdgeEvent`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EdgeEventId**](EdgeEventId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **seq_id** | **int** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **edge_id** | [**EdgeId**](EdgeId.md) |  | [optional] |
| **action** | [**EdgeEventActionType**](EdgeEventActionType.md) |  | [optional] |
| **entity_id** | **UUID** |  | [optional] |
| **uid** | **str** |  | [optional] |
| **type** | [**EdgeEventType**](EdgeEventType.md) |  | [optional] |
| **body** | **object** |  | [optional] |
| **entity_group_id** | **UUID** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EdgeEventId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EdgeEventActionType (enum)
`ADDED` | `UPDATED` | `DELETED` | `POST_ATTRIBUTES` | `ATTRIBUTES_UPDATED` | `ATTRIBUTES_DELETED` | `TIMESERIES_UPDATED` | `CREDENTIALS_UPDATED` | `RELATION_ADD_OR_UPDATE` | `RELATION_DELETED` | … (26 values total)

#### EdgeEventType (enum)
`DASHBOARD` | `ASSET` | `DEVICE` | `DEVICE_PROFILE` | `ASSET_PROFILE` | `ENTITY_VIEW` | `ALARM` | `ALARM_COMMENT` | `RULE_CHAIN` | `RULE_CHAIN_METADATA` | … (45 values total)

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeEvent.model_validate(data)` or `EdgeEvent.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

