
# WidgetTypeInfo

`tb_pe_client.models.WidgetTypeInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**WidgetTypeId**](WidgetTypeId.md) | JSON object with the Widget Type Id. Specify this field to update the Widget Type. Referencing non-existing Widget Type Id will cause error. Omit this field to create new Widget Type. | [optional] |
| **created_time** | **int** | Timestamp of the Widget Type creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **fqn** | **str** | Unique FQN that is used in dashboards as a reference widget type | [optional] [readonly] |
| **name** | **str** | Widget name used in search and UI | [optional] [readonly] |
| **deprecated** | **bool** | Whether widget type is deprecated. | [optional] |
| **scada** | **bool** | Whether widget type is SCADA symbol. | [optional] |
| **version** | **int** |  | [optional] |
| **image** | **str** | Base64 encoded widget thumbnail | [optional] [readonly] |
| **description** | **str** | Description of the widget type | [optional] [readonly] |
| **tags** | **List[str]** | Tags of the widget type | [optional] |
| **widget_type** | **str** | Type of the widget (timeseries, latest, control, alarm or static) | [optional] [readonly] |
| **bundles** | [**List[WidgetBundleInfo]**](WidgetBundleInfo.md) | Bundles | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### WidgetBundleInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `WidgetTypeInfo.model_validate(data)` or `WidgetTypeInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

