
# AgentApplicationInfo

`tb_pe_client.models.AgentApplicationInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AgentApplicationId**](AgentApplicationId.md) | JSON object with the Agent Application Id. | [optional] |
| **created_time** | **int** | Timestamp of the agent application creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. | [optional] [readonly] |
| **agent_id** | [**AgentId**](AgentId.md) | Agent this application belongs to | |
| **name** | **str** | Application name (not unique across tenant) | [optional] |
| **template_version** | **str** | Template version this application is based on | |
| **desired_template_version** | **str** |  | [optional] |
| **app_type** | [**AgentApplicationType**](AgentApplicationType.md) | Application type | |
| **config** | [**DockerComposeConfig**](DockerComposeConfig.md) |  | [optional] |
| **version** | **int** |  | [optional] |
| **project_name** | **str** |  | [optional] |
| **pending_deletion** | **bool** |  | [optional] |
| **origin** | [**AgentApplicationOrigin**](AgentApplicationOrigin.md) | Origin of the application (INSTALLED or DISCOVERED) | [optional] |
| **application_profile_id** | [**AgentAppProfileId**](AgentAppProfileId.md) | Application Profile Id. When set, config is read-only and inherited from the profile. | [optional] |
| **profile_config_version** | **int** |  | [optional] |
| **current_version** | **str** | Current version of the template this application is based on. | [optional] [readonly] |
| **next_version** | **str** | Next version available for upgrade. | [optional] [readonly] |
| **profile_config_outdated** | **bool** | True if the app's config is outdated relative to its profile. | [optional] [readonly] |
| **profile_name** | **str** | Name of the application profile this app is based on. | [optional] [readonly] |
| **profile_template_version** | **str** | Template version of the application profile this app is based on. | [optional] [readonly] |
| **agent_name** | **str** | Name of the owning agent. | [optional] [readonly] |
| **related_entity_id** | [**EntityId**](EntityId.md) | Related entity id (Edge or Gateway device) currently assigned to this application. | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentApplicationType (enum)
`GENERIC` | `EDGE` | `GATEWAY`

#### DockerComposeConfig  *(extends AgentAppConfig)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| compose | object |  | [optional] |
| compose_type | str |  | [optional] |

#### AgentApplicationOrigin (enum)
`INSTALLED` | `DISCOVERED` | `AUTO_PROVISIONED`

#### AgentAppConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | List[AgentAppArgument] |  | [optional] |
| edge_routing_key | str |  | [optional] |
| type | AgentAppConfigType |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### AgentAppArgument
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str | Argument name, referenced in the compose as ${tb.<name>}. | [optional] |
| source_type | AgentAppArgumentSource | Source entity the value is resolved from. | [optional] |
| source_entity_id | EntityId | Concrete source entity id. Required when sourceType references a specific entity (DEVICE, ASSET, CUSTOMER, EDGE); ignored for the context-derived sources. | [optional] |
| value_type | AgentAppArgumentValueType | Whether the value is read from an attribute or the latest telemetry. | [optional] |
| scope | AttributeScope | Attribute scope. Applicable only when valueType is ATTRIBUTE. Defaults to SERVER_SCOPE. | [optional] |
| key | str | Attribute or latest telemetry key to read. | [optional] |
| default_value | str | Optional fallback value used when the source has no value for the key. | [optional] |
| format | AgentAppArgumentFormat | How the resolved value is injected into the compose: STRING (quoted) or JSON (raw, for arrays/objects/numbers when the placeholder is the whole value). Defaults to STRING. | [optional] |

#### AgentAppConfigType (enum)
`DOCKER_COMPOSE`

#### AgentAppArgumentSource (enum)
`AGENT` | `OWNER` | `RELATED_ENTITY` | `TENANT` | `DEVICE` | `ASSET` | `CUSTOMER` | `EDGE`

#### AgentAppArgumentValueType (enum)
`ATTRIBUTE` | `LATEST_TELEMETRY`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### AgentAppArgumentFormat (enum)
`STRING` | `JSON`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentApplicationInfo.model_validate(data)` or `AgentApplicationInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

