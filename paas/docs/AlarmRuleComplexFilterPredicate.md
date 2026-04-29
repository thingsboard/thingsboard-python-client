
# AlarmRuleComplexFilterPredicate

`tb_paas_client.models.AlarmRuleComplexFilterPredicate`

**Extends:** **AlarmRuleKeyFilterPredicate**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **operation** | [**AlarmRuleComplexOperation**](AlarmRuleComplexOperation.md) |  | [optional] |
| **predicates** | [**List[AlarmRuleKeyFilterPredicate]**](AlarmRuleKeyFilterPredicate.md) |  | [optional] |



## Referenced Types

#### AlarmRuleKeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AlarmRuleComplexOperation (enum)
`AND` | `OR`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.operation`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmRuleComplexFilterPredicate.model_validate(data)` or `AlarmRuleComplexFilterPredicate.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

