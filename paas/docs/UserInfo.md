
# UserInfo

`tb_paas_client.models.UserInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**UserId**](UserId.md) | JSON object with the User Id. Specify this field to update the device. Referencing non-existing User Id will cause error. Omit this field to create new customer. | [optional] |
| **created_time** | **int** | Timestamp of the user creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the user. May include: 'defaultDashboardId' (string, UUID of the default dashboard), 'defaultDashboardFullscreen' (boolean), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean), 'lang' (string, user locale, e.g. 'en_US'), 'authProviderName' (string, name of the authentication provider). | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with the Tenant Id. | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with the Customer Id. | [optional] |
| **email** | **str** | Email of the user | |
| **authority** | [**Authority**](Authority.md) | Authority | |
| **first_name** | **str** | First name of the user | [optional] |
| **last_name** | **str** | Last name of the user | [optional] |
| **phone** | **str** | Phone number of the user | [optional] |
| **custom_menu_id** | [**CustomMenuId**](CustomMenuId.md) |  | [optional] |
| **version** | **int** |  | [optional] |
| **owner_name** | **str** | Owner name | [optional] [readonly] |
| **groups** | [**List[EntityInfo]**](EntityInfo.md) | Groups | [optional] |
| **name** | **str** | Duplicates the email of the user, readonly | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### Authority (enum)
`SYS_ADMIN` | `TENANT_ADMIN` | `CUSTOMER_USER` | `BILLING_ADMIN` | `BILLING_SERVICE` | `REFRESH_TOKEN` | `PRE_VERIFICATION_TOKEN` | `MFA_CONFIGURATION_TOKEN`

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `UserInfo.model_validate(data)` or `UserInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

