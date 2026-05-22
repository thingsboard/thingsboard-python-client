
# PageDataEntityGroupInfo

`tb_pe_client.models.PageDataEntityGroupInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[EntityGroupInfo]**](EntityGroupInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityGroupInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityGroupId | JSON object with the EntityGroupId Id. Specify this field to update the Entity Group. Referencing non-existing Entity Group Id will cause error. Omit this field to create new Entity Group. | [optional] |
| created_time | int | Timestamp of the entity group creation, in milliseconds | [optional] [readonly] |
| type | TypeEnum |  |  |
| name | str | Name of the entity group |  |
| owner_id | EntityId | JSON object with the owner of the group - Tenant or Customer Id. When omitted or null on creation, defaults to the current user's owner (Tenant for tenant admins, Customer for customer users). | [optional] |
| additional_info | object | Additional parameters of the entity group. May include: 'description' (string), 'isPublic' (boolean, whether this group is shared publicly), 'publicCustomerId' (string, UUID of the public customer associated with this group). | [optional] |
| configuration | object | JSON with the configuration for UI components: list of columns, settings, actions, etc | [optional] |
| version | int |  | [optional] |
| owner_ids | List[EntityId] | List of the entity group owners. |  |
| edge_group_all | bool | Indicates special edge group 'All' that contains all entities and can't be deleted. | [optional] [readonly] |
| group_all | bool | Indicates special group 'All' that contains all entities and can't be deleted. | [optional] |
| tenant_id | TenantId |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataEntityGroupInfo.model_validate(data)` or `PageDataEntityGroupInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

