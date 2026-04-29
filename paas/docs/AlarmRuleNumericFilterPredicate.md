
# AlarmRuleNumericFilterPredicate

`tb_paas_client.models.AlarmRuleNumericFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**AlarmRuleNumericOperation**](AlarmRuleNumericOperation.md) |  | |
| **value** | [**AlarmConditionValueDouble**](AlarmConditionValueDouble.md) |  | |



## Referenced Types

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleNumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### AlarmConditionValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| static_value | float |  | [optional] |
| dynamic_value_argument | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleNumericFilterPredicate.model_validate(data)` or `AlarmRuleNumericFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

