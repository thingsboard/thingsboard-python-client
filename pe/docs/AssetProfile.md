
# AssetProfile

`tb_pe_client.models.AssetProfile`

A JSON value representing the asset profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AssetProfileId**](AssetProfileId.md) | JSON object with the asset profile Id. Specify this field to update the asset profile. Referencing non-existing asset profile Id will cause error. Omit this field to create new asset profile. | [optional] |
| **created_time** | **int** | Timestamp of the profile creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the profile. | [optional] [readonly] |
| **name** | **str** | Unique Asset Profile Name in scope of Tenant. | [optional] |
| **description** | **str** | Asset Profile description.  | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of asset profiles in the grid view.  | [optional] |
| **default_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the rule chain. If present, the specified rule chain will be used to process all messages related to asset, including asset updates, telemetry, attribute updates, etc. Otherwise, the root rule chain will be used to process those messages. | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to asset details. | [optional] |
| **default_queue_name** | **str** | Rule engine queue name. If present, the specified queue will be used to store all unprocessed messages related to asset, including asset updates, telemetry, attribute updates, etc. Otherwise, the 'Main' queue will be used to store those messages. | [optional] |
| **default_edge_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the edge rule chain. If present, the specified edge rule chain will be used on the edge to process all messages related to asset, including asset updates, telemetry, attribute updates, etc. Otherwise, the edge root rule chain will be used to process those messages. | [optional] |
| **version** | **int** |  | [optional] |
| **default** | **bool** | Used to mark the default profile. Default profile is used when the asset profile is not specified during asset creation. | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AssetProfile.model_validate(data)` or `AssetProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

