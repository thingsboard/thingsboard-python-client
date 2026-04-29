
# PageDataRole

`tb_paas_client.models.PageDataRole`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[Role]**](Role.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### Role
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | RoleId | JSON object with the Role Id. Specify this field to update the Role. Referencing non-existing Role Id will cause error. Omit this field to create new Role. | [optional] |
| created_time | int | Timestamp of the role creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the role. May include: 'description' (string). | [optional] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. | [optional] [readonly] |
| name | str | Role Name |  |
| type | RoleType | Type of the role: generic or group |  |
| permissions | object | JSON object with the set of permissions. Structure is specific for role type |  |
| excluded_permissions | object | JSON object with the set of excluded permissions. Only applicable for generic roles. Structure is the same as permissions | [optional] |
| version | int |  | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### RoleType (enum)
`GENERIC` | `GROUP`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataRole.model_validate(data)` or `PageDataRole.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

