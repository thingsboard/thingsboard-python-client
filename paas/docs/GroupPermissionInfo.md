
# GroupPermissionInfo

`tb_paas_client.models.GroupPermissionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**GroupPermissionId**](GroupPermissionId.md) | JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission. | [optional] |
| **created_time** | **int** | Timestamp of the group permission creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with the Tenant Id. | [optional] [readonly] |
| **user_group_id** | [**EntityGroupId**](EntityGroupId.md) | JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group. | |
| **role_id** | [**RoleId**](RoleId.md) | JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required. | |
| **entity_group_id** | [**EntityGroupId**](EntityGroupId.md) | JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role. | [optional] |
| **entity_group_type** | [**EntityType**](EntityType.md) | Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions. | [optional] [readonly] |
| **role** | [**Role**](Role.md) | Represent set of permissions. | [optional] |
| **entity_group_name** | **str** | Entity Group Name. | [optional] |
| **entity_group_owner_id** | [**EntityId**](EntityId.md) | Entity Group Owner Id (Tenant or Customer). | [optional] |
| **entity_group_owner_name** | **str** | Name of the entity group owner (Tenant or Customer title). | [optional] |
| **user_group_name** | **str** | User Group Name. | [optional] |
| **user_group_owner_id** | [**EntityId**](EntityId.md) | User Group Owner Id (Tenant or Customer). | [optional] |
| **user_group_owner_name** | **str** | Name of the user group owner (Tenant or Customer title). | [optional] |
| **name** | **str** | Name of the Group Permissions. Auto-generated | [optional] [readonly] |
| **public** | **bool** |  | [optional] |
| **read_only** | **bool** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### Role
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | RoleId | JSON object with the Role Id. Specify this field to update the Role. Referencing non-existing Role Id will cause error. Omit this field to create new Role. | [optional] |
| created_time | int | Timestamp of the role creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the role. May include: 'description' (string). | [optional] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. Optional: when omitted the Role is owned by the tenant. When the request is made by a Customer user, the value is forced to the user's own Customer Id. | [optional] |
| name | str | Role Name |  |
| type | RoleType | Type of the role: generic or group |  |
| permissions | object | Set of permissions granted by this role. The JSON shape depends on the role 'type':  * GENERIC — JSON object mapping `Resource` enum names to arrays of `Operation` enum names allowed on that resource. The wildcard entry `{\"ALL\":[\"ALL\"]}` grants every operation on every resource.  * GROUP — JSON array of `Operation` enum names that apply to the entity group this role is bound to via `GroupPermission.entityGroupId`. Only operations with `allowedForGroupRole=true` may appear (see `Operation` enum). The wildcard entry `[\"ALL\"]` grants every supported operation on the bound entity group. |  |
| excluded_permissions | object | Operations to subtract from those granted by `permissions`. Only applicable to GENERIC roles — setting this on a GROUP role is rejected by validation. Same shape as the GENERIC variant of `permissions`: a JSON object mapping `Resource` enum names to non-empty arrays of `Operation` enum names. At evaluation time, for each resource the listed operations are removed from the resolved permission set (e.g. `permissions={\"ALL\":[\"ALL\"]}` combined with `excludedPermissions={\"DEVICE\":[\"DELETE\"]}` grants everything except deleting devices). May be null or an empty object when no exclusions apply. | [optional] |
| version | int |  | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### RoleType (enum)
`GENERIC` | `GROUP`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GroupPermissionInfo.model_validate(data)` or `GroupPermissionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

