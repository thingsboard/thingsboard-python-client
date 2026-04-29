
# RuleChainMetaData

`tb_paas_client.models.RuleChainMetaData`

A JSON value representing the rule chain metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with Rule Chain Id. | [readonly] |
| **version** | **int** | Version of the Rule Chain | [optional] |
| **first_node_index** | **int** | Index of the first rule node in the 'nodes' list | |
| **nodes** | [**List[RuleNode]**](RuleNode.md) | List of rule node JSON objects | |
| **connections** | [**List[NodeConnectionInfo]**](NodeConnectionInfo.md) | List of JSON objects that represent connections between rule nodes | |
| **rule_chain_connections** | [**List[RuleChainConnectionInfo]**](RuleChainConnectionInfo.md) | List of JSON objects that represent connections between rule nodes and other rule chains. | |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### RuleNode
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | RuleNodeId | JSON object with the Rule Node Id. Specify this field to update the Rule Node. Referencing non-existing Rule Node Id will cause error. Omit this field to create new rule node. | [optional] |
| created_time | int | Timestamp of the rule node creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the rule node. May include: 'layoutX' (number, X coordinate for visualization), 'layoutY' (number, Y coordinate for visualization), 'description' (string). | [optional] |
| rule_chain_id | RuleChainId | JSON object with the Rule Chain Id. | [optional] [readonly] |
| type | str | Full Java Class Name of the rule node implementation. | [optional] |
| name | str | User defined name of the rule node. Used on UI and for logging. | [optional] |
| debug_settings | DebugSettings | Debug settings object. | [optional] |
| singleton_mode | bool | Enable/disable singleton mode. | [optional] |
| queue_name | str | Queue name. | [optional] |
| configuration_version | int | Version of rule node configuration. | [optional] |
| configuration | object | JSON with the rule node configuration. Structure depends on the rule node implementation. | [optional] |
| external_id | RuleNodeId |  | [optional] |
| debug_mode | bool |  | [optional] |

#### NodeConnectionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| from_index | int | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection. |  |
| to_index | int | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'to' part of the connection. |  |
| type | str | Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure' |  |

#### RuleChainConnectionInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| from_index | int | Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection. |  |
| target_rule_chain_id | RuleChainId | JSON object with the Rule Chain Id. |  |
| additional_info | object | JSON object with the additional information about the connection. |  |
| type | str | Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure' |  |

#### DebugSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failures_enabled | bool | Debug failures. | [optional] |
| all_enabled | bool | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| all_enabled_until | int | Timestamp of the end time for the processing debug events. | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.rule_chain_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainMetaData.model_validate(data)` or `RuleChainMetaData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

