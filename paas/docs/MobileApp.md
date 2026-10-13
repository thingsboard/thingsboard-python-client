
# MobileApp

`tb_paas_client.models.MobileApp`

A JSON value representing the Mobile Application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**MobileAppId**](MobileAppId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **pkg_name** | **str** | Application package name. Cannot be empty | |
| **title** | **str** | Application title | [optional] |
| **app_secret** | **str** | Application secret. The length must be at least 16 characters | |
| **platform_type** | [**PlatformType**](PlatformType.md) | Application platform type: ANDROID or IOS | |
| **status** | [**MobileAppStatus**](MobileAppStatus.md) | Application status: PUBLISHED, DEPRECATED, SUSPENDED, DRAFT | |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) | Application version info | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) | Application store information | [optional] |
| **name** | **str** | Mobile app package name | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### PlatformType (enum)
`WEB` | `ANDROID` | `IOS`

#### MobileAppStatus (enum)
`DRAFT` | `PUBLISHED` | `DEPRECATED` | `SUSPENDED`

#### MobileAppVersionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| min_version | str | Minimum supported version | [optional] |
| min_version_release_notes | str | Release notes of minimum supported version | [optional] |
| latest_version | str | Latest supported version | [optional] |
| latest_version_release_notes | str | Release notes of latest supported version | [optional] |

#### StoreInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| app_id | str |  | [optional] |
| sha256_cert_fingerprints | str |  | [optional] |
| store_link | str |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MobileApp.model_validate(data)` or `MobileApp.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

