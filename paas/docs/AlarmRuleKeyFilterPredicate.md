
# AlarmRuleKeyFilterPredicate

`tb_paas_client.models.AlarmRuleKeyFilterPredicate`

Filter predicate for alarm rule key-based filtering

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### AlarmRuleBooleanFilterPredicate  *(type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleBooleanOperation |  |  |
| value | AlarmConditionValueBoolean |  |  |

#### AlarmRuleComplexFilterPredicate  *(type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleComplexOperation |  | [optional] |
| predicates | List[AlarmRuleKeyFilterPredicate] |  | [optional] |

#### NoDataFilterPredicate  *(type=`NO_DATA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| unit | TimeUnit |  |  |
| duration | AlarmConditionValueLong |  |  |

#### AlarmRuleNumericFilterPredicate  *(type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleNumericOperation |  |  |
| value | AlarmConditionValueDouble |  |  |

#### AlarmRuleStringFilterPredicate  *(type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleStringOperation |  |  |
| value | AlarmConditionValueString |  |  |
| ignore_case | bool |  | [optional] |

## Referenced Types

#### AlarmRuleBooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### AlarmConditionValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | bool |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmRuleComplexOperation (enum)
`AND` | `OR`

#### TimeUnit (enum)
`NANOSECONDS` | `MICROSECONDS` | `MILLISECONDS` | `SECONDS` | `MINUTES` | `HOURS` | `DAYS`

#### AlarmConditionValueLong
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | int |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmRuleNumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### AlarmConditionValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | float |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

#### AlarmRuleStringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### AlarmConditionValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | str |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleKeyFilterPredicate.model_validate(data)` or `AlarmRuleKeyFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

