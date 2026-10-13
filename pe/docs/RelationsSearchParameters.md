
# RelationsSearchParameters

`tb_pe_client.models.RelationsSearchParameters`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **root_id** | **UUID** | Root entity id to start search from. | [optional] |
| **root_type** | [**EntityType**](EntityType.md) | Type of the root entity. | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) | Type of the root entity. | [optional] |
| **relation_type_group** | [**RelationTypeGroup**](RelationTypeGroup.md) | Type of the relation. | [optional] |
| **max_level** | **int** | Maximum level of the search depth. | [optional] |
| **fetch_last_level_only** | **bool** | Fetch entities that match the last level of search. Useful to find Devices that are strictly 'maxLevel' relations away from the root entity. | [optional] |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### RelationTypeGroup (enum)
`COMMON` | `DASHBOARD` | `FROM_ENTITY_GROUP` | `RULE_CHAIN` | `RULE_NODE` | `EDGE` | `EDGE_AUTO_ASSIGN_RULE_CHAIN` | `AGENT`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.root_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationsSearchParameters.model_validate(data)` or `RelationsSearchParameters.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

