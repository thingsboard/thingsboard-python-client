
# PageDataCustomerInfo

`tb_paas_client.models.PageDataCustomerInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[CustomerInfo]**](CustomerInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### CustomerInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | CustomerId | JSON object with the customer Id. Specify this field to update the customer. Referencing non-existing customer Id will cause error. Omit this field to create new customer. | [optional] |
| created_time | int | Timestamp of the customer creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the customer. May include: 'description' (string), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean, whether to hide the dashboard toolbar), 'isPublic' (boolean, whether this is a public customer). | [optional] |
| country | str | Country | [optional] |
| state | str | State | [optional] |
| city | str | City | [optional] |
| address | str | Address Line 1 | [optional] |
| address2 | str | Address Line 2 | [optional] |
| zip | str | Zip code | [optional] |
| phone | str | Phone number | [optional] |
| email | str | Email | [optional] |
| title | str | Title of the customer |  |
| tenant_id | TenantId | JSON object with Tenant Id | [optional] |
| parent_customer_id | CustomerId | JSON object with parent Customer Id | [optional] |
| version | int |  | [optional] |
| custom_menu_id | CustomMenuId |  | [optional] |
| owner_name | str | Owner name | [optional] [readonly] |
| groups | List[EntityInfo] | Groups | [optional] |
| customer_id | CustomerId | JSON object with parent Customer Id | [optional] [readonly] |
| name | str | Name of the customer. Read-only, duplicated from title for backward compatibility | [optional] [readonly] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

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
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataCustomerInfo.model_validate(data)` or `PageDataCustomerInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

