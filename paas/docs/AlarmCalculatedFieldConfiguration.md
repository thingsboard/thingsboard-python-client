
# AlarmCalculatedFieldConfiguration

`tb_paas_client.models.AlarmCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **arguments** | [**Dict[str, Argument]**](Argument.md) |  | |
| **create_rules** | [**Dict[str, AlarmRule]**](AlarmRule.md) |  | |
| **clear_rule** | [**AlarmRule**](AlarmRule.md) |  | [optional] |
| **propagate** | **bool** |  | [optional] |
| **propagate_to_owner** | **bool** |  | [optional] |
| **propagate_to_owner_hierarchy** | **bool** |  | [optional] |
| **propagate_to_tenant** | **bool** |  | [optional] |
| **propagate_relation_types** | **List[str]** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### CalculatedFieldConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| output | Output |  | [optional] |
| type | str |  |  |

#### Argument
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ref_entity_id | EntityId |  | [optional] |
| ref_dynamic_source_configuration | CfArgumentDynamicSourceConfiguration |  | [optional] |
| ref_entity_key | ReferencedEntityKey |  | [optional] |
| default_value | str |  | [optional] |
| limit | int |  | [optional] |
| time_window | int |  | [optional] |

#### AlarmRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| condition | AlarmCondition |  |  |
| alarm_details | str |  | [optional] |
| dashboard_id | DashboardId |  | [optional] |

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

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

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

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

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

#### EntitySearchDirection (enum)
`FROM` | `TO`

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
- **Attribute access:** `obj.arguments`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmCalculatedFieldConfiguration.model_validate(data)` or `AlarmCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

