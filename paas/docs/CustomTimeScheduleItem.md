
# CustomTimeScheduleItem

`tb_paas_client.models.CustomTimeScheduleItem`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **enabled** | **bool** |  | [optional] |
| **day_of_week** | **int** |  | [optional] |
| **starts_on** | **int** |  | [optional] |
| **ends_on** | **int** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.enabled`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomTimeScheduleItem.model_validate(data)` or `CustomTimeScheduleItem.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

