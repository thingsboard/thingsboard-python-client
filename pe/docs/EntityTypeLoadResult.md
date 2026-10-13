
# EntityTypeLoadResult

`tb_pe_client.models.EntityTypeLoadResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **created** | **int** |  | [optional] |
| **updated** | **int** |  | [optional] |
| **deleted** | **int** |  | [optional] |
| **groups_created** | **int** |  | [optional] |
| **groups_updated** | **int** |  | [optional] |
| **groups_deleted** | **int** |  | [optional] |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityTypeLoadResult.model_validate(data)` or `EntityTypeLoadResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

