
# AvailableEntityKeys

`tb_ce_client.models.AvailableEntityKeys`

Contains unique time series and attribute key names discovered from entities matching a query. Used primarily for UI hints such as autocomplete suggestions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_types** | [**List[EntityType]**](EntityType.md) | Set of entity types found among the matched entities. | |
| **timeseries** | **List[str]** | List of unique time series key names available on the matched entities. | |
| **attribute** | **List[str]** | List of unique attribute key names available on the matched entities. | |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.entity_types`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AvailableEntityKeys.model_validate(data)` or `AvailableEntityKeys.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

