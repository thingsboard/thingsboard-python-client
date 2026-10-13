
# BlobEntityWithCustomerInfo

`tb_pe_client.models.BlobEntityWithCustomerInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**BlobEntityId**](BlobEntityId.md) | JSON object with the blob entity Id. Referencing non-existing blob entity Id will cause error | [optional] |
| **created_time** | **int** | Timestamp of the blob entity creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the blob entity | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] [readonly] |
| **name** | **str** | blob entity name | [optional] [readonly] |
| **type** | **str** | blob entity type | [optional] [readonly] |
| **content_type** | **Content_typeEnum** | blob content type | [optional] [readonly] |
| **customer_title** | **str** | Title of the customer | [optional] |
| **customer_is_public** | **bool** | Parameter that specifies if customer is public | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |


### Enum: Content_typeEnum

| Name | Value |
|---- | -----|
| &#39;application/pdf&#39; | 'application/pdf' |
| &#39;image/jpeg&#39; | 'image/jpeg' |
| &#39;image/png&#39; | 'image/png' |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BlobEntityWithCustomerInfo.model_validate(data)` or `BlobEntityWithCustomerInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

