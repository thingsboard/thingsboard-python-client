
# EntityData

`tb_pe_client.models.EntityData`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **read_attrs** | **bool** |  | [optional] |
| **read_ts** | **bool** |  | [optional] |
| **latest** | **Dict[str, Dict[str, TsValue]]** |  | [optional] |
| **timeseries** | **Dict[str, List[TsValue]]** |  | [optional] |
| **agg_latest** | [**Dict[str, ComparisonTsValue]**](ComparisonTsValue.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ComparisonTsValue
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| current | TsValue |  | [optional] |
| previous | TsValue |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### TsValue
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ts | int |  | [optional] |
| value | str |  | [optional] |
| count | int |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityData.model_validate(data)` or `EntityData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

