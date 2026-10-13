
# MergedUserPermissions

`tb_pe_client.models.MergedUserPermissions`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **generic_permissions** | **Dict[str, List[Operation]]** | Map of permissions defined using generic roles ('Customer Administrator', etc) | [optional] |
| **group_permissions** | [**Dict[str, MergedGroupPermissionInfo]**](MergedGroupPermissionInfo.md) | Map of permissions defined using group roles ('Read' or 'Write' access to specific entity group, etc) | [optional] |
| **read_group_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read permissions per entity type. Used on the UI to enable/disable certain components. | [optional] |
| **read_entity_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read permissions per resource. Used on the UI to enable/disable certain components. | [optional] |
| **read_attr_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read entity attributes permissions per resource. Used on the UI to enable/disable certain tabs. | [optional] |
| **read_ts_permissions** | [**Dict[str, MergedGroupTypePermissionInfo]**](MergedGroupTypePermissionInfo.md) | Map of read entity time-series permissions per resource. Used on the UI to enable/disable certain tabs. | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### MergedGroupPermissionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| operations | List[Operation] |  | [optional] |

#### MergedGroupTypePermissionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_group_ids | List[EntityGroupId] | List of Entity Groups in case of group roles are assigned to the user (user group) | [optional] |
| has_generic_read | bool | Indicates if generic permission assigned to the user group. | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### Operation (enum)
`ALL` | `CREATE` | `READ` | `WRITE` | `DELETE` | `RPC_CALL` | `READ_CREDENTIALS` | `WRITE_CREDENTIALS` | `READ_ATTRIBUTES` | `WRITE_ATTRIBUTES` | … (21 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.generic_permissions`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MergedUserPermissions.model_validate(data)` or `MergedUserPermissions.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

