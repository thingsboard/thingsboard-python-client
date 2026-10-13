
# AlarmRuleBooleanFilterPredicate

`tb_paas_client.models.AlarmRuleBooleanFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**AlarmRuleBooleanOperation**](AlarmRuleBooleanOperation.md) |  | |
| **value** | [**AlarmConditionValueBoolean**](AlarmConditionValueBoolean.md) |  | |



## Referenced Types

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

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
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleBooleanFilterPredicate.model_validate(data)` or `AlarmRuleBooleanFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

