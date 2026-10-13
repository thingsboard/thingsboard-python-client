
# RelationEntityTypeFilter

`tb_pe_client.models.RelationEntityTypeFilter`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **relation_type** | **str** | Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages'). | [optional] |
| **entity_types** | [**List[EntityType]**](EntityType.md) | Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET'). | [optional] |
| **negate** | **bool** | Negate relation type between root entity and other entity. | [optional] |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.relation_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationEntityTypeFilter.model_validate(data)` or `RelationEntityTypeFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

