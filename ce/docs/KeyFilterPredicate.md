
# KeyFilterPredicate

`tb_ce_client.models.KeyFilterPredicate`

Filter predicate for key-based filtering

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### BooleanFilterPredicate  *(type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | BooleanOperation |  | [optional] |
| value | FilterPredicateValueBoolean | The value associated with the filter predicate | [optional] |

#### ComplexFilterPredicate  *(type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleComplexOperation |  | [optional] |
| predicates | List[KeyFilterPredicate] |  | [optional] |

#### NumericFilterPredicate  *(type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | NumericOperation |  | [optional] |
| value | FilterPredicateValueDouble | The value associated with the filter predicate | [optional] |

#### StringFilterPredicate  *(type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | StringOperation |  | [optional] |
| value | FilterPredicateValueString | The value associated with the filter predicate | [optional] |
| ignore_case | bool |  | [optional] |

## Referenced Types

#### BooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### FilterPredicateValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | bool |  | [optional] |
| user_value | bool |  | [optional] |
| dynamic_value | DynamicValueBoolean |  | [optional] |

#### AlarmRuleComplexOperation (enum)
`AND` | `OR`

#### NumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### FilterPredicateValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | float |  | [optional] |
| user_value | float |  | [optional] |
| dynamic_value | DynamicValueDouble |  | [optional] |

#### StringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### FilterPredicateValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | str |  | [optional] |
| user_value | str |  | [optional] |
| dynamic_value | DynamicValueString |  | [optional] |

#### DynamicValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | bool |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | float |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `KeyFilterPredicate.model_validate(data)` or `KeyFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

