
# ApiKey

`tb_paas_client.models.ApiKey`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**ApiKeyId**](ApiKeyId.md) | JSON object with the API Key Id. Specify this field to update the API Key. Referencing non-existing API Key Id will cause error. Omit this field to create new API Key. | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the API key cannot be changed. | [optional] [readonly] |
| **user_id** | [**UserId**](UserId.md) | JSON object with User Id. User Id of the API key cannot be changed. | [optional] |
| **expiration_time** | **int** | Expiration time of the API key. | [optional] |
| **description** | **str** | API Key description. | |
| **enabled** | **bool** | Enabled/disabled API key. | [optional] |
| **value** | **str** | API key value | |
| **expired** | **bool** | Indicates if the API key is expired based on current time. Returns false if expirationTime is 0 (no expiry). | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ApiKey.model_validate(data)` or `ApiKey.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

