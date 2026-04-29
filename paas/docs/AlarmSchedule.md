
# AlarmSchedule

`tb_paas_client.models.AlarmSchedule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### AnyTimeSchedule  *(type=`ANY_TIME`)*
*(no additional properties)*

#### CustomTimeSchedule  *(type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| items | List[CustomTimeScheduleItem] |  | [optional] |

#### SpecificTimeSchedule  *(type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| days_of_week | List[int] |  | [optional] |
| starts_on | int |  | [optional] |
| ends_on | int |  | [optional] |

## Referenced Types

#### CustomTimeScheduleItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| day_of_week | int |  | [optional] |
| starts_on | int |  | [optional] |
| ends_on | int |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmSchedule.model_validate(data)` or `AlarmSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

