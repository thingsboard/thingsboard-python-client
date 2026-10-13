
# PageDataTenantInfo

`tb_paas_client.models.PageDataTenantInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[TenantInfo]**](TenantInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TenantInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | TenantId | JSON object with the tenant Id. Specify this field to update the tenant. Referencing non-existing tenant Id will cause error. Omit this field to create new tenant. | [optional] |
| created_time | int | Timestamp of the tenant creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the tenant. May include: 'description' (string), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean, whether to hide the dashboard toolbar). | [optional] |
| country | str | Country | [optional] |
| state | str | State | [optional] |
| city | str | City | [optional] |
| address | str | Address Line 1 | [optional] |
| address2 | str | Address Line 2 | [optional] |
| zip | str | Zip code | [optional] |
| phone | str | Phone number | [optional] |
| email | str | Email | [optional] |
| title | str | Title of the tenant |  |
| region | str | Geo region of the tenant | [optional] |
| tenant_profile_id | TenantProfileId | JSON object with Tenant Profile Id | [optional] |
| version | int |  | [optional] |
| active | bool |  | [optional] |
| last_inactive_ts | int |  | [optional] |
| current_period_start_ts | int |  | [optional] |
| addon_data | TenantAddonData |  | [optional] |
| edge_license_version | int |  | [optional] |
| tenant_profile_name | str | Tenant Profile name | [optional] |
| name | str | Name of the tenant. Read-only, duplicated from title for backward compatibility | [optional] [readonly] |

#### TenantAddonData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| max_devices | int |  | [optional] |
| max_assets | int |  | [optional] |
| max_customers | int |  | [optional] |
| max_users | int |  | [optional] |
| max_integrations | int |  | [optional] |
| max_converters | int |  | [optional] |
| max_calculated_fields_per_entity | int |  | [optional] |
| max_transport_messages | int |  | [optional] |
| max_transport_data_points | int |  | [optional] |
| max_re_executions | int |  | [optional] |
| max_js_executions | int |  | [optional] |
| max_dp_storage_days | int |  | [optional] |
| max_created_alarms | int |  | [optional] |
| max_emails | int |  | [optional] |
| max_sms | int |  | [optional] |
| max_ai_credits | int |  | [optional] |
| edge_enabled | bool |  | [optional] |
| max_edges | int |  | [optional] |
| trendz_enabled | bool |  | [optional] |
| white_labeling_enabled | bool |  | [optional] |
| default | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataTenantInfo.model_validate(data)` or `PageDataTenantInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

