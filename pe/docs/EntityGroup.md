
# EntityGroup

`tb_pe_client.models.EntityGroup`

A JSON value representing the entity group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EntityGroupId**](EntityGroupId.md) | JSON object with the EntityGroupId Id. Specify this field to update the Entity Group. Referencing non-existing Entity Group Id will cause error. Omit this field to create new Entity Group. | [optional] |
| **created_time** | **int** | Timestamp of the entity group creation, in milliseconds | [optional] [readonly] |
| **type** | **TypeEnum** |  | |
| **name** | **str** | Name of the entity group | |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with the owner of the group - Tenant or Customer Id. When omitted or null on creation, defaults to the current user's owner (Tenant for tenant admins, Customer for customer users). | [optional] |
| **additional_info** | **object** | Additional parameters of the entity group. May include: 'description' (string), 'isPublic' (boolean, whether this group is shared publicly), 'publicCustomerId' (string, UUID of the public customer associated with this group). | [optional] |
| **configuration** | **object** | JSON with the configuration for UI components: list of columns, settings, actions, etc  | [optional] |
| **version** | **int** |  | [optional] |
| **edge_group_all** | **bool** | Indicates special edge group 'All' that contains all entities and can't be deleted. | [optional] [readonly] |
| **group_all** | **bool** | Indicates special group 'All' that contains all entities and can't be deleted. | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |


### Enum: TypeEnum

| Name | Value |
|---- | -----|
| &#39;TENANT&#39; | 'TENANT' |
| &#39;CUSTOMER&#39; | 'CUSTOMER' |
| &#39;USER&#39; | 'USER' |
| &#39;DASHBOARD&#39; | 'DASHBOARD' |
| &#39;ASSET&#39; | 'ASSET' |
| &#39;DEVICE&#39; | 'DEVICE' |
| &#39;ALARM&#39; | 'ALARM' |
| &#39;ENTITY_GROUP&#39; | 'ENTITY_GROUP' |
| &#39;CONVERTER&#39; | 'CONVERTER' |
| &#39;INTEGRATION&#39; | 'INTEGRATION' |
| &#39;RULE_CHAIN&#39; | 'RULE_CHAIN' |
| &#39;RULE_NODE&#39; | 'RULE_NODE' |
| &#39;SCHEDULER_EVENT&#39; | 'SCHEDULER_EVENT' |
| &#39;BLOB_ENTITY&#39; | 'BLOB_ENTITY' |
| &#39;REPORT_TEMPLATE&#39; | 'REPORT_TEMPLATE' |
| &#39;REPORT&#39; | 'REPORT' |
| &#39;ENTITY_VIEW&#39; | 'ENTITY_VIEW' |
| &#39;WIDGETS_BUNDLE&#39; | 'WIDGETS_BUNDLE' |
| &#39;WIDGET_TYPE&#39; | 'WIDGET_TYPE' |
| &#39;ROLE&#39; | 'ROLE' |
| &#39;GROUP_PERMISSION&#39; | 'GROUP_PERMISSION' |
| &#39;TENANT_PROFILE&#39; | 'TENANT_PROFILE' |
| &#39;DEVICE_PROFILE&#39; | 'DEVICE_PROFILE' |
| &#39;ASSET_PROFILE&#39; | 'ASSET_PROFILE' |
| &#39;API_USAGE_STATE&#39; | 'API_USAGE_STATE' |
| &#39;TB_RESOURCE&#39; | 'TB_RESOURCE' |
| &#39;OTA_PACKAGE&#39; | 'OTA_PACKAGE' |
| &#39;EDGE&#39; | 'EDGE' |
| &#39;RPC&#39; | 'RPC' |
| &#39;QUEUE&#39; | 'QUEUE' |
| &#39;NOTIFICATION_TARGET&#39; | 'NOTIFICATION_TARGET' |
| &#39;NOTIFICATION_TEMPLATE&#39; | 'NOTIFICATION_TEMPLATE' |
| &#39;NOTIFICATION_REQUEST&#39; | 'NOTIFICATION_REQUEST' |
| &#39;NOTIFICATION&#39; | 'NOTIFICATION' |
| &#39;NOTIFICATION_RULE&#39; | 'NOTIFICATION_RULE' |
| &#39;QUEUE_STATS&#39; | 'QUEUE_STATS' |
| &#39;OAUTH2_CLIENT&#39; | 'OAUTH2_CLIENT' |
| &#39;DOMAIN&#39; | 'DOMAIN' |
| &#39;MOBILE_APP&#39; | 'MOBILE_APP' |
| &#39;MOBILE_APP_BUNDLE&#39; | 'MOBILE_APP_BUNDLE' |
| &#39;CALCULATED_FIELD&#39; | 'CALCULATED_FIELD' |
| &#39;JOB&#39; | 'JOB' |
| &#39;SECRET&#39; | 'SECRET' |
| &#39;ADMIN_SETTINGS&#39; | 'ADMIN_SETTINGS' |
| &#39;AI_MODEL&#39; | 'AI_MODEL' |
| &#39;API_KEY&#39; | 'API_KEY' |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityGroup.model_validate(data)` or `EntityGroup.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

