
# PageDataUser

`tb_pe_client.models.PageDataUser`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[User]**](User.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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

#### Authority (enum)
`SYS_ADMIN` | `TENANT_ADMIN` | `CUSTOMER_USER` | `REFRESH_TOKEN` | `PRE_VERIFICATION_TOKEN` | `MFA_CONFIGURATION_TOKEN`

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataUser.model_validate(data)` or `PageDataUser.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

