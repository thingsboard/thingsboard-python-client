
# OtaPackageInfo

`tb_paas_client.models.OtaPackageInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**OtaPackageId**](OtaPackageId.md) | JSON object with the ota package Id. Specify existing ota package Id to update the ota package. Referencing non-existing ota package id will cause error. Omit this field to create new ota package. | [optional] |
| **created_time** | **int** | Timestamp of the ota package creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | OTA Package description. | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Tenant Id of the ota package can't be changed. | [optional] [readonly] |
| **device_profile_id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with Device Profile Id. Device Profile Id of the ota package can't be changed. | [optional] |
| **type** | [**OtaPackageType**](OtaPackageType.md) | OTA Package type. | [optional] |
| **title** | **str** | OTA Package title. | [optional] |
| **version** | **str** | OTA Package version. | [optional] |
| **tag** | **str** | OTA Package tag. | [optional] [readonly] |
| **url** | **str** | OTA Package url. | [optional] |
| **has_data** | **bool** | Indicates OTA Package 'has data'. Field is returned from DB ('true' if data exists or url is set).  If OTA Package 'has data' is 'false' we can not assign the OTA Package to the Device or Device Profile. | [optional] [readonly] |
| **file_name** | **str** | OTA Package file name. | [optional] [readonly] |
| **content_type** | **str** | OTA Package content type. | [optional] [readonly] |
| **checksum_algorithm** | [**ChecksumAlgorithm**](ChecksumAlgorithm.md) | OTA Package checksum algorithm. | [optional] [readonly] |
| **checksum** | **str** | OTA Package checksum. | [optional] [readonly] |
| **data_size** | **int** | OTA Package data size. | [optional] [readonly] |
| **name** | **str** |  | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### OtaPackageType (enum)
`FIRMWARE` | `SOFTWARE`

#### ChecksumAlgorithm (enum)
`MD5` | `SHA256` | `SHA384` | `SHA512` | `CRC32` | `MURMUR3_32` | `MURMUR3_128`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OtaPackageInfo.model_validate(data)` or `OtaPackageInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

