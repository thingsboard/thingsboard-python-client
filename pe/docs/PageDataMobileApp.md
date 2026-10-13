
# PageDataMobileApp

`tb_pe_client.models.PageDataMobileApp`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[MobileApp]**](MobileApp.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### MobileApp
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | MobileAppId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id | [optional] |
| pkg_name | str | Application package name. Cannot be empty |  |
| title | str | Application title | [optional] |
| app_secret | str | Application secret. The length must be at least 16 characters |  |
| platform_type | PlatformType | Application platform type: ANDROID or IOS |  |
| status | MobileAppStatus | Application status: PUBLISHED, DEPRECATED, SUSPENDED, DRAFT |  |
| version_info | MobileAppVersionInfo | Application version info | [optional] |
| store_info | StoreInfo | Application store information | [optional] |
| name | str | Mobile app package name | [optional] [readonly] |

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
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataMobileApp.model_validate(data)` or `PageDataMobileApp.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

