
# RuleChainData

`tb_paas_client.models.RuleChainData`

A JSON value representing the rule chains.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rule_chains** | [**List[RuleChain]**](RuleChain.md) | List of the Rule Chain objects. | |
| **metadata** | [**List[RuleChainMetaData]**](RuleChainMetaData.md) | List of the Rule Chain metadata objects. | |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### RuleChain
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | RuleChainId | JSON object with the Rule Chain Id. Specify this field to update the Rule Chain. Referencing non-existing Rule Chain Id will cause error. Omit this field to create new rule chain. | [optional] |
| created_time | int | Timestamp of the rule chain creation, in milliseconds | [optional] [readonly] |
| additional_info | object |  | [optional] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| name | str | Rule Chain name |  |
| type | RuleChainType | Rule Chain type. 'EDGE' rule chains are processing messages on the edge devices only. | [optional] |
| first_rule_node_id | RuleNodeId | JSON object with Rule Chain Id. Pointer to the first rule node that should receive all messages pushed to this rule chain. | [optional] |
| root | bool | Indicates root rule chain. The root rule chain process messages from all devices and entities by default. User may configure default rule chain per device profile. | [optional] |
| debug_mode | bool | Reserved for future usage. | [optional] |
| configuration | object |  | [optional] |
| version | int |  | [optional] |

#### RuleChainMetaData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| rule_chain_id | RuleChainId | JSON object with Rule Chain Id. | [readonly] |
| version | int | Version of the Rule Chain | [optional] |
| first_node_index | int | Index of the first rule node in the 'nodes' list |  |
| nodes | List[RuleNode] | List of rule node JSON objects |  |
| connections | List[NodeConnectionInfo] | List of JSON objects that represent connections between rule nodes |  |
| rule_chain_connections | List[RuleChainConnectionInfo] | List of JSON objects that represent connections between rule nodes and other rule chains. |  |

#### RuleChainType (enum)
`CORE` | `EDGE`

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
- **Attribute access:** `obj.rule_chains`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RuleChainData.model_validate(data)` or `RuleChainData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

