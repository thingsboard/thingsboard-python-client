
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
| permissions | object | Set of permissions granted by this role. The JSON shape depends on the role 'type':  * GENERIC — JSON object mapping `Resource` enum names to arrays of `Operation` enum names allowed on that resource. The wildcard entry `{\"ALL\":[\"ALL\"]}` grants every operation on every resource.  * GROUP — JSON array of `Operation` enum names that apply to the entity group this role is bound to via `GroupPermission.entityGroupId`. Only operations with `allowedForGroupRole=true` may appear (see `Operation` enum). The wildcard entry `[\"ALL\"]` grants every supported operation on the bound entity group. |  |
| excluded_permissions | object | Operations to subtract from those granted by `permissions`. Only applicable to GENERIC roles — setting this on a GROUP role is rejected by validation. Same shape as the GENERIC variant of `permissions`: a JSON object mapping `Resource` enum names to non-empty arrays of `Operation` enum names. At evaluation time, for each resource the listed operations are removed from the resolved permission set (e.g. `permissions={\"ALL\":[\"ALL\"]}` combined with `excludedPermissions={\"DEVICE\":[\"DELETE\"]}` grants everything except deleting devices). May be null or an empty object when no exclusions apply. | [optional] |
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

