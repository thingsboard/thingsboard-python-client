
# StepFieldString

`tb_pe_client.models.StepFieldString`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **value** | **str** |  | [optional] |
| **user_choice** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `StepFieldString.model_validate(data)` or `StepFieldString.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

