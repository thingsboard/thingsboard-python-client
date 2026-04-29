
# TableSortOrder

`tb_paas_client.models.TableSortOrder`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **column** | **str** |  | [optional] |
| **direction** | [**TableSortDirection**](TableSortDirection.md) |  | [optional] |



## Referenced Types

#### TableSortDirection (enum)
`ASC` | `DESC`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.column`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TableSortOrder.model_validate(data)` or `TableSortOrder.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

