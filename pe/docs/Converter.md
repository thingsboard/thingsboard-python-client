
# Converter

`tb_pe_client.models.Converter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**ConverterId**](ConverterId.md) | JSON object with the Converter Id. Specify this field to update the Converter. Referencing non-existing Converter Id will cause error. Omit this field to create new Converter. | [optional] |
| **created_time** | **int** | Timestamp of the converter creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **name** | **str** | Unique Converter Name in scope of Tenant | |
| **type** | [**ConverterType**](ConverterType.md) | The type of the converter to process incoming or outgoing messages | |
| **integration_type** | [**IntegrationType**](IntegrationType.md) | The type of the integration to which the converter is dedicated | [optional] |
| **debug_mode** | **bool** | Enable/disable debug.  | [optional] |
| **debug_settings** | [**DebugSettings**](DebugSettings.md) | Debug settings object. | [optional] |
| **configuration** | **object** | JSON object representing converter configuration. It should contain one of two possible fields: 'decoder' or 'encoder'. The former is used when the converter has UPLINK type, the latter is used - when DOWNLINK type. It can contain both 'decoder' and 'encoder' fields, when the correct one is specified for the appropriate converter type, another one can be set to 'null' | [optional] |
| **additional_info** | **object** | Additional parameters of the converter | [optional] |
| **edge_template** | **bool** | Boolean flag that specifies that is regular or edge template converter | [optional] |
| **converter_version** | **int** |  | [optional] |
| **version** | **int** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ConverterType (enum)
`UPLINK` | `DOWNLINK`

#### IntegrationType (enum)
`OCEANCONNECT` | `SIGFOX` | `THINGPARK` | `TPE` | `CHIRPSTACK` | `PARTICLE` | `TMOBILE_IOT_CDP` | `HTTP` | `MQTT` | `PUB_SUB` | … (29 values total)

#### DebugSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failures_enabled | bool | Debug failures. | [optional] |
| all_enabled | bool | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| all_enabled_until | int | Timestamp of the end time for the processing debug events. | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Converter.model_validate(data)` or `Converter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

