
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
| customer_id | CustomerId | JSON object with Customer Id. | [optional] [readonly] |
| name | str | Role Name |  |
| type | RoleType | Type of the role: generic or group |  |
| permissions | object | JSON object with the set of permissions. Structure is specific for role type |  |
| excluded_permissions | object | JSON object with the set of excluded permissions. Only applicable for generic roles. Structure is the same as permissions | [optional] |
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

