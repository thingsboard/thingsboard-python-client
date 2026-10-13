
# EntityGroupFilter

`tb_paas_client.models.EntityGroupFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **group_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **entity_group** | **str** |  | [optional] |
| **group_state_entity** | **bool** |  | [optional] |
| **default_state_group_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **default_state_entity_group** | **str** |  | [optional] |



## Referenced Types

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.group_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityGroupFilter.model_validate(data)` or `EntityGroupFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

