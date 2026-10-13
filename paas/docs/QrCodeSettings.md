
# QrCodeSettings

`tb_paas_client.models.QrCodeSettings`

A JSON value representing the mobile apps configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**QrCodeSettingsId**](QrCodeSettingsId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **use_system_settings** | **bool** | Use settings from system level | [optional] |
| **use_default_app** | **bool** | Type of application: true means use default Thingsboard app | [optional] |
| **mobile_app_bundle_id** | [**MobileAppBundleId**](MobileAppBundleId.md) | Mobile app bundle. | [optional] |
| **qr_code_config** | [**QRCodeConfig**](QRCodeConfig.md) | QR code config configuration. | |
| **android_enabled** | **bool** | Indicates if google play link is available | [optional] |
| **ios_enabled** | **bool** | Indicates if apple store link is available | [optional] |
| **google_play_link** | **str** |  | [optional] [readonly] |
| **app_store_link** | **str** |  | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### QrCodeSettingsId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### QRCodeConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| show_on_home_page | bool |  | [optional] |
| badge_enabled | bool |  | [optional] |
| qr_code_label_enabled | bool |  | [optional] |
| badge_position | BadgePosition |  | [optional] |
| qr_code_label | str |  | [optional] |

#### BadgePosition (enum)
`RIGHT` | `LEFT`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `QrCodeSettings.model_validate(data)` or `QrCodeSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

