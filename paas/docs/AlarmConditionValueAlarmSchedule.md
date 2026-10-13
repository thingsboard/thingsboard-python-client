
# AlarmConditionValueAlarmSchedule

`tb_paas_client.models.AlarmConditionValueAlarmSchedule`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **static_value** | [**AlarmSchedule**](AlarmSchedule.md) |  | [optional] |
| **dynamic_value_argument** | **str** |  | [optional] |



## Referenced Types

#### AlarmSchedule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AnyTimeSchedule  *(extends AlarmSchedule, type=`ANY_TIME`)*
*See AlarmSchedule for properties.*

#### CustomTimeSchedule  *(extends AlarmSchedule, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| items | List[CustomTimeScheduleItem] |  | [optional] |

#### SpecificTimeSchedule  *(extends AlarmSchedule, type=`SPECIFIC_TIME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timezone | str |  | [optional] |
| days_of_week | List[int] |  | [optional] |
| starts_on | int |  | [optional] |
| ends_on | int |  | [optional] |

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
- **Attribute access:** `obj.static_value`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmConditionValueAlarmSchedule.model_validate(data)` or `AlarmConditionValueAlarmSchedule.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

