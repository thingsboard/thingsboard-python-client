
# EntityDataDiff

`tb_paas_client.models.EntityDataDiff`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **current_version** | [**EntityExportData**](EntityExportData.md) |  | [optional] |
| **other_version** | [**EntityExportData**](EntityExportData.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityExportData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity | ExportableEntity |  | [optional] |
| relations | List[EntityRelation] |  | [optional] |
| attributes | Dict[str, List[AttributeExportData]] | Map of attributes where key is the scope of attributes and value is the list of attributes for that scope | [optional] |
| calculated_fields | List[CalculatedField] |  | [optional] |
| entity_type | EntityType |  |  |

#### AiModelExportData  *(extends EntityExportData, entity_type=`AI_MODEL`)*
*See EntityExportData for properties.*

#### AssetExportData  *(extends EntityExportData, entity_type=`ASSET`)*
*See EntityExportData for properties.*

#### AssetProfileExportData  *(extends EntityExportData, entity_type=`ASSET_PROFILE`)*
*See EntityExportData for properties.*

#### ConverterExportData  *(extends EntityExportData, entity_type=`CONVERTER`)*
*See EntityExportData for properties.*

#### CustomerExportData  *(extends EntityExportData, entity_type=`CUSTOMER`)*
*See EntityExportData for properties.*

#### DashboardExportData  *(extends EntityExportData, entity_type=`DASHBOARD`)*
*See EntityExportData for properties.*

#### DeviceExportData  *(extends EntityExportData, entity_type=`DEVICE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| credentials | DeviceCredentials |  | [optional] |

#### DeviceProfileExportData  *(extends EntityExportData, entity_type=`DEVICE_PROFILE`)*
*See EntityExportData for properties.*

#### EntityGroupExportData  *(extends EntityExportData, entity_type=`ENTITY_GROUP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| permissions | List[GroupPermission] | Group permissions to apply to this group on import. Meaningful only for USER groups; ignored for groups of any other type. Each entry's userGroupId, roleId, and entityGroupId may use the external IDs of other entities in this payload or the IDs of entities that already exist on the target tenant; the importer resolves them against the target tenant. System-tenant roles are not allowed and will be rejected. Leave null to skip permission management for this group. | [optional] |
| group_ota_packages | List[DeviceGroupOtaPackage] | OTA package assignments to apply to this group on import. Meaningful only for DEVICE groups; ignored for groups of any other type. Each entry's otaPackageId and groupId may reference external IDs of entities in this payload or IDs of entities that already exist on the target tenant. Leave null to skip OTA assignment management for this group. | [optional] |
| group_entities | bool | Marker indicating that the group's member entities are intended to be transported alongside this payload. Used by flows that convey members through a side channel (notably the version control flow, which stores members in a separate git index). The solution import API does not consume this flag and does not require it to be set. Safe to leave false (default). | [optional] |
| member_ids | List[UUID] | External IDs of the entities that should be members of this group after import. Each ID is resolved against the target tenant — by other entity in this payload, by external ID, or by existing internal ID — and the matching entities are added to the group. The import fails if any listed member cannot be resolved. Must be null for the special 'All' group (whose membership is implicit and managed by the platform). Leave null to skip membership wiring; existing membership on the target tenant is left untouched. | [optional] |

#### EntityViewExportData  *(extends EntityExportData, entity_type=`ENTITY_VIEW`)*
*See EntityExportData for properties.*

#### IntegrationExportData  *(extends EntityExportData, entity_type=`INTEGRATION`)*
*See EntityExportData for properties.*

#### NotificationRuleExportData  *(extends EntityExportData, entity_type=`NOTIFICATION_RULE`)*
*See EntityExportData for properties.*

#### NotificationTargetExportData  *(extends EntityExportData, entity_type=`NOTIFICATION_TARGET`)*
*See EntityExportData for properties.*

#### NotificationTemplateExportData  *(extends EntityExportData, entity_type=`NOTIFICATION_TEMPLATE`)*
*See EntityExportData for properties.*

#### OtaPackageExportData  *(extends EntityExportData, entity_type=`OTA_PACKAGE`)*
*See EntityExportData for properties.*

#### ReportTemplateExportData  *(extends EntityExportData, entity_type=`REPORT_TEMPLATE`)*
*See EntityExportData for properties.*

#### RoleExportData  *(extends EntityExportData, entity_type=`ROLE`)*
*See EntityExportData for properties.*

#### RuleChainExportData  *(extends EntityExportData, entity_type=`RULE_CHAIN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| meta_data | RuleChainMetaData |  | [optional] |

#### SchedulerEventExportData  *(extends EntityExportData, entity_type=`SCHEDULER_EVENT`)*
*See EntityExportData for properties.*

#### TbResourceExportData  *(extends EntityExportData, entity_type=`TB_RESOURCE`)*
*See EntityExportData for properties.*

#### UserExportData  *(extends EntityExportData, entity_type=`USER`)*
*See EntityExportData for properties.*

#### WidgetsBundleExportData  *(extends EntityExportData, entity_type=`WIDGETS_BUNDLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| widgets | List[object] | List of widgets in the bundle | [optional] |
| fqns | List[str] |  | [optional] |

#### WidgetTypeExportData  *(extends EntityExportData, entity_type=`WIDGET_TYPE`)*
*See EntityExportData for properties.*

#### ExportableEntity
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| created_time | int |  | [optional] |
| id | EntityId |  | [optional] |
| name | str |  | [optional] |
| tenant_id | TenantId |  | [optional] |

#### EntityRelation
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| var_from | EntityId | JSON object with [from] Entity Id. |  |
| to | EntityId | JSON object with [to] Entity Id. |  |
| type | str | String value of relation type. |  |
| type_group | RelationTypeGroup | Represents the type group of the relation. |  |
| version | int |  | [optional] |
| additional_info | object | Additional parameters of the relation. | [optional] |

#### CalculatedField
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | CalculatedFieldId | JSON object with the Calculated Field Id. Referencing non-existing Calculated Field Id will cause error. | [optional] |
| created_time | int | Timestamp of the calculated field creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| entity_id | EntityId |  | [optional] |
| type | CalculatedFieldType |  | [optional] |
| name | str | User defined name of the calculated field. | [optional] |
| debug_settings | DebugSettings | Debug settings object. | [optional] |
| configuration_version | int | Version of calculated field configuration. | [optional] |
| configuration | CalculatedFieldConfiguration |  |  |
| version | int |  | [optional] |
| additional_info | object | Additional parameters of the calculated field | [optional] |
| debug_mode | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### RelationTypeGroup (enum)
`COMMON` | `DASHBOARD` | `FROM_ENTITY_GROUP` | `RULE_CHAIN` | `RULE_NODE` | `EDGE` | `EDGE_AUTO_ASSIGN_RULE_CHAIN`

#### CalculatedFieldType (enum)
`SIMPLE` | `SCRIPT` | `GEOFENCING` | `ALARM` | `PROPAGATION` | `RELATED_ENTITIES_AGGREGATION` | `ENTITY_AGGREGATION`

#### DebugSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failures_enabled | bool | Debug failures. | [optional] |
| all_enabled | bool | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| all_enabled_until | int | Timestamp of the end time for the processing debug events. | [optional] |

#### CalculatedFieldConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| output | Output |  | [optional] |
| type | str |  |  |

#### AlarmCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`ALARM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | Dict[str, Argument] |  |  |
| create_rules | Dict[str, AlarmRule] |  |  |
| clear_rule | AlarmRule |  | [optional] |
| propagate | bool |  | [optional] |
| propagate_to_owner | bool |  | [optional] |
| propagate_to_owner_hierarchy | bool |  | [optional] |
| propagate_to_tenant | bool |  | [optional] |
| propagate_relation_types | List[str] |  | [optional] |

#### EntityAggregationCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`ENTITY_AGGREGATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | Dict[str, Argument] |  |  |
| metrics | Dict[str, AggMetric] |  |  |
| interval | AggInterval |  |  |
| watermark | Watermark |  | [optional] |
| produce_intermediate_result | bool |  | [optional] |

#### GeofencingCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`GEOFENCING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_coordinates | EntityCoordinates |  |  |
| zone_groups | Dict[str, ZoneGroupConfiguration] |  |  |
| scheduled_update_enabled | bool |  | [optional] |
| scheduled_update_interval | int |  | [optional] |

#### PropagationCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`PROPAGATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | Dict[str, Argument] |  |  |
| expression | str |  | [optional] |
| relation | RelationPathLevel |  |  |
| apply_expression_to_resolved_arguments | bool |  | [optional] |

#### RelatedEntitiesAggregationCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`RELATED_ENTITIES_AGGREGATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relation | RelationPathLevel |  |  |
| arguments | Dict[str, Argument] |  |  |
| deduplication_interval_in_sec | int |  | [optional] |
| metrics | Dict[str, AggMetric] |  |  |
| use_latest_ts | bool |  | [optional] |
| scheduled_update_interval | int |  | [optional] |
| scheduled_update_enabled | bool |  | [optional] |

#### ScriptCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`SCRIPT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | Dict[str, Argument] |  |  |
| expression | str |  | [optional] |

#### SimpleCalculatedFieldConfiguration  *(extends CalculatedFieldConfiguration, type=`SIMPLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | Dict[str, Argument] |  |  |
| expression | str |  | [optional] |
| use_latest_ts | bool |  | [optional] |

#### DeviceCredentials
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | DeviceCredentialsId | The Id is automatically generated during device creation. Use 'getDeviceCredentialsByDeviceId' to obtain the id based on device id. Use 'updateDeviceCredentials' to update device credentials. | [readonly] |
| created_time | int | Timestamp of the device credentials creation, in milliseconds | [optional] |
| device_id | DeviceId | JSON object with the device Id. |  |
| credentials_type | DeviceCredentialsType | Type of the credentials | [optional] |
| credentials_id | str | Unique Credentials Id per platform instance. Used to lookup credentials from the database. By default, new access token for your device. Depends on the type of the credentials. |  |
| credentials_value | str | Value of the credentials. Null in case of ACCESS_TOKEN credentials type. Base64 value in case of X509_CERTIFICATE. Complex object in case of MQTT_BASIC and LWM2M_CREDENTIALS | [optional] |
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

#### GroupPermission
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | GroupPermissionId | JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission. | [optional] |
| created_time | int | Timestamp of the group permission creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with the Tenant Id. | [optional] [readonly] |
| user_group_id | EntityGroupId | JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group. |  |
| role_id | RoleId | JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required. |  |
| entity_group_id | EntityGroupId | JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role. | [optional] |
| entity_group_type | EntityType | Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions. | [optional] [readonly] |
| is_public | bool |  | [optional] |
| name | str | Name of the Group Permissions. Auto-generated | [optional] [readonly] |
| public | bool |  | [optional] |

#### DeviceGroupOtaPackage
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID |  | [optional] |
| group_id | EntityGroupId |  | [optional] |
| ota_package_type | OtaPackageType |  | [optional] |
| ota_package_id | OtaPackageId |  | [optional] |
| ota_package_update_time | int |  | [optional] |

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| decimals_by_default | int |  | [optional] |
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

#### AttributesOutput  *(extends Output, type=`ATTRIBUTES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | AttributesOutputStrategy |  | [optional] |

#### TimeSeriesOutput  *(extends Output, type=`TIME_SERIES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesOutputStrategy |  | [optional] |

#### DeviceCredentialsId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### DeviceCredentialsType (enum)
`ACCESS_TOKEN` | `X509_CERTIFICATE` | `MQTT_BASIC` | `LWM2_M_CREDENTIALS`

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

#### OtaPackageType (enum)
`FIRMWARE` | `SOFTWARE`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### Argument
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ref_entity_id | EntityId |  | [optional] |
| ref_dynamic_source_configuration | CfArgumentDynamicSourceConfiguration |  | [optional] |
| ref_entity_key | ReferencedEntityKey |  | [optional] |
| default_value | str |  | [optional] |
| limit | int |  | [optional] |
| time_window | int |  | [optional] |

#### EntityCoordinates
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| latitude_key_name | str |  |  |
| longitude_key_name | str |  |  |

#### ZoneGroupConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ref_entity_id | EntityId |  | [optional] |
| ref_dynamic_source_configuration | CfArgumentDynamicSourceConfiguration |  | [optional] |
| perimeter_key_name | str |  |  |
| report_strategy | GeofencingReportStrategy |  |  |
| create_relations_with_matched_zones | bool |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |

#### AlarmRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | AlarmCondition |  |  |
| alarm_details | str |  | [optional] |
| dashboard_id | DashboardId |  | [optional] |

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

#### AggMetric
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| function | AggFunction |  | [optional] |
| filter | str |  | [optional] |
| input | AggInput |  | [optional] |
| default_value | float |  | [optional] |

#### AggInterval
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CustomInterval  *(extends AggInterval, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |
| duration_sec | int |  |  |

#### DayInterval  *(extends AggInterval, type=`DAY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### HourInterval  *(extends AggInterval, type=`HOUR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### MonthInterval  *(extends AggInterval, type=`MONTH`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### QuarterInterval  *(extends AggInterval, type=`QUARTER`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### WeekInterval  *(extends AggInterval, type=`WEEK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### WeekSunSatInterval  *(extends AggInterval, type=`WEEK_SUN_SAT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### YearInterval  *(extends AggInterval, type=`YEAR`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tz | str |  |  |
| offset_sec | int |  | [optional] |

#### Watermark
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| duration | int |  | [optional] |

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeSeriesImmediateOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ttl | int |  | [optional] |
| save_time_series | bool |  | [optional] |
| save_latest | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### TimeSeriesRuleChainOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`RULE_CHAIN`)*
*See TimeSeriesOutputStrategy for properties.*

#### AttributesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributesImmediateOutputStrategy  *(extends AttributesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| send_attributes_updated_notification | bool |  | [optional] |
| update_attributes_only_on_value_change | bool |  | [optional] |
| save_attribute | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### AttributesRuleChainOutputStrategy  *(extends AttributesOutputStrategy, type=`RULE_CHAIN`)*
*See AttributesOutputStrategy for properties.*

#### CfArgumentDynamicSourceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CurrentOwnerDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`CURRENT_OWNER`)*
*See CfArgumentDynamicSourceConfiguration for properties.*

#### RelationPathQueryDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`RELATION_PATH_QUERY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| levels | List[RelationPathLevel] |  | [optional] |

#### ReferencedEntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| type | ArgumentType |  | [optional] |
| scope | AttributeScope |  | [optional] |

#### GeofencingReportStrategy (enum)
`REPORT_TRANSITION_EVENTS_ONLY` | `REPORT_PRESENCE_STATUS_ONLY` | `REPORT_TRANSITION_EVENTS_AND_PRESENCE_STATUS`

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### AlarmCondition
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| expression | AlarmConditionExpression |  |  |
| schedule | AlarmConditionValueAlarmSchedule |  | [optional] |
| type | str |  |  |

#### DurationAlarmCondition  *(extends AlarmCondition, type=`DURATION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| unit | TimeUnit |  |  |
| value | AlarmConditionValueLong |  |  |

#### RepeatingAlarmCondition  *(extends AlarmCondition, type=`REPEATING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| count | AlarmConditionValueInteger |  |  |

#### SimpleAlarmCondition  *(extends AlarmCondition, type=`SIMPLE`)*
*See AlarmCondition for properties.*

#### AggFunction (enum)
`MIN` | `MAX` | `SUM` | `AVG` | `COUNT` | `COUNT_UNIQUE`

#### AggInput
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AggFunctionInput  *(extends AggInput, type=`function`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| function | str |  | [optional] |

#### AggKeyInput  *(extends AggInput, type=`key`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |

#### ArgumentType (enum)
`TS_LATEST` | `ATTRIBUTE` | `TS_ROLLING`

#### AlarmConditionExpression
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### SimpleAlarmConditionExpression  *(extends AlarmConditionExpression, type=`SIMPLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| filters | List[AlarmConditionFilter] |  |  |
| operation | AlarmRuleComplexOperation |  | [optional] |

#### TbelAlarmConditionExpression  *(extends AlarmConditionExpression, type=`TBEL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| expression | str |  |  |

#### AlarmConditionValueAlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | AlarmSchedule |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AnyTimeSchedule  *(extends AlarmSchedule, type=`ANY_TIME`)*
*See AlarmSchedule for properties.*

#### CustomTimeSchedule  *(extends AlarmSchedule, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| items | List[CustomTimeScheduleItem] |  | [optional] |

#### SpecificTimeSchedule  *(extends AlarmSchedule, type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| days_of_week | List[int] |  | [optional] |
| starts_on | int |  | [optional] |
| ends_on | int |  | [optional] |

#### TimeUnit (enum)
`NANOSECONDS` | `MICROSECONDS` | `MILLISECONDS` | `SECONDS` | `MINUTES` | `HOURS` | `DAYS`

#### AlarmConditionValueLong
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmConditionValueInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmConditionFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| argument | str |  |  |
| value_type | EntityKeyValueType |  |  |
| operation | AlarmRuleComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  |  |

#### AlarmRuleComplexOperation (enum)
`AND` | `OR`

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleBooleanFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleBooleanOperation |  |  |
| value | AlarmConditionValueBoolean |  |  |

#### AlarmRuleComplexFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  | [optional] |

#### NoDataFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`NO_DATA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| unit | TimeUnit |  |  |
| duration | AlarmConditionValueLong |  |  |

#### AlarmRuleNumericFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleNumericOperation |  |  |
| value | AlarmConditionValueDouble |  |  |

#### AlarmRuleStringFilterPredicate  *(extends AlarmRuleKeyFilterPredicate, type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleStringOperation |  |  |
| value | AlarmConditionValueString |  |  |
| ignore_case | bool |  | [optional] |

#### CustomTimeScheduleItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| day_of_week | int |  | [optional] |
| starts_on | int |  | [optional] |
| ends_on | int |  | [optional] |

#### AlarmRuleStringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### AlarmConditionValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | str |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmRuleNumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### AlarmConditionValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | float |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmRuleBooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### AlarmConditionValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | bool |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.current_version`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataDiff.model_validate(data)` or `EntityDataDiff.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

