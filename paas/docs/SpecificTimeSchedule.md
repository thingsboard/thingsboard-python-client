
# SpecificTimeSchedule

`tb_paas_client.models.SpecificTimeSchedule`

**Extends:** **AlarmSchedule**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timezone** | **str** |  | [optional] |
| **days_of_week** | **List[int]** |  | [optional] |
| **starts_on** | **int** |  | [optional] |
| **ends_on** | **int** |  | [optional] |



## Referenced Types

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.timezone`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SpecificTimeSchedule.model_validate(data)` or `SpecificTimeSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

