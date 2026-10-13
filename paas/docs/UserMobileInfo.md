
# UserMobileInfo

`tb_paas_client.models.UserMobileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **user** | [**User**](User.md) |  | [optional] |
| **store_info** | [**StoreInfo**](StoreInfo.md) |  | [optional] |
| **version_info** | [**MobileAppVersionInfo**](MobileAppVersionInfo.md) |  | [optional] |
| **home_dashboard_info** | [**HomeDashboardInfo**](HomeDashboardInfo.md) |  | [optional] |
| **pages** | **object** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### User
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UserId | JSON object with the User Id. Specify this field to update the device. Referencing non-existing User Id will cause error. Omit this field to create new customer. | [optional] |
| created_time | int | Timestamp of the user creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the user. May include: 'defaultDashboardId' (string, UUID of the default dashboard), 'defaultDashboardFullscreen' (boolean), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean), 'lang' (string, user locale, e.g. 'en_US'), 'authProviderName' (string, name of the authentication provider). | [optional] |
| tenant_id | TenantId | JSON object with the Tenant Id. | [optional] |
| customer_id | CustomerId | JSON object with the Customer Id. | [optional] |
| email | str | Email of the user |  |
| authority | Authority | Authority |  |
| first_name | str | First name of the user | [optional] |
| last_name | str | Last name of the user | [optional] |
| phone | str | Phone number of the user | [optional] |
| custom_menu_id | CustomMenuId |  | [optional] |
| version | int |  | [optional] |
| name | str | Duplicates the email of the user, readonly | [optional] [readonly] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### StoreInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| app_id | str |  | [optional] |
| sha256_cert_fingerprints | str |  | [optional] |
| store_link | str |  | [optional] |

#### MobileAppVersionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| min_version | str | Minimum supported version | [optional] |
| min_version_release_notes | str | Release notes of minimum supported version | [optional] |
| latest_version | str | Latest supported version | [optional] |
| latest_version_release_notes | str | Release notes of latest supported version | [optional] |

#### HomeDashboardInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dashboard_id | DashboardId | JSON object with the dashboard Id. | [optional] |
| hide_dashboard_toolbar | bool | Hide dashboard toolbar flag. Useful for rendering dashboards on mobile. | [optional] |

#### Authority (enum)
`SYS_ADMIN` | `TENANT_ADMIN` | `CUSTOMER_USER` | `BILLING_ADMIN` | `BILLING_SERVICE` | `REFRESH_TOKEN` | `PRE_VERIFICATION_TOKEN` | `MFA_CONFIGURATION_TOKEN`

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.user`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserMobileInfo.model_validate(data)` or `UserMobileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

