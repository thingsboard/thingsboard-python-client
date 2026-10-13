
# StepFieldBoolean

`tb_paas_client.models.StepFieldBoolean`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **value** | **bool** |  | [optional] |
| **user_choice** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StepFieldBoolean.model_validate(data)` or `StepFieldBoolean.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

