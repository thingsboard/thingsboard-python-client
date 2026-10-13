
# Integration

`tb_pe_client.models.Integration`

A JSON value representing the integration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**IntegrationId**](IntegrationId.md) | JSON object with the Integration Id. Specify this field to update the Integration. Referencing non-existing Integration Id will cause error. Omit this field to create new Integration. | [optional] |
| **created_time** | **int** | Timestamp of the integration creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **name** | **str** | Integration Name | |
| **type** | [**IntegrationType**](IntegrationType.md) | The type of the integration | |
| **debug_mode** | **bool** | Enable/disable debug.  | [optional] |
| **debug_settings** | [**DebugSettings**](DebugSettings.md) | Debug settings object. | [optional] |
| **enabled** | **bool** | Boolean flag to enable/disable the integration | [optional] |
| **remote** | **bool** | Boolean flag to enable/disable the integration to be executed remotely. Remote integration is launched in a separate microservice. Local integration is executed by the platform core | [optional] |
| **allow_create_devices_or_assets** | **bool** | Boolean flag to allow/disallow the integration to create devices or assets that send message and do not exist in the system yet | [optional] |
| **edge_template** | **bool** | Boolean flag that specifies that is regular or edge template integration | [optional] |
| **version** | **int** |  | [optional] |
| **default_converter_id** | [**ConverterId**](ConverterId.md) | JSON object with the Uplink Converter Id | |
| **downlink_converter_id** | [**ConverterId**](ConverterId.md) | JSON object with the Downlink Converter Id | [optional] |
| **routing_key** | **str** | String value used by HTTP based integrations for the base URL construction and by the remote integrations. Remote integration uses this value along with the 'secret' for kind of security and validation to be able to connect to the platform using Grpc | |
| **secret** | **str** | String value used by the remote integrations. Remote integration uses this value along with the 'routingKey' for kind of security and validation to be able to connect to the platform using Grpc | [optional] |
| **configuration** | **object** | JSON object representing integration configuration. Each integration type has specific configuration with the connectivity parameters (like 'host' and 'port' for MQTT type or 'baseUrl' for HTTP based type, etc.) and other important parameters dependent on the integration type | |
| **additional_info** | **object** | Additional parameters of the integration | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

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
- **Deserialize:** `Integration.model_validate(data)` or `Integration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

