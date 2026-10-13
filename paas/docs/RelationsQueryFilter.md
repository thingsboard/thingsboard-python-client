
# RelationsQueryFilter

`tb_paas_client.models.RelationsQueryFilter`

**Extends:** **EntityFilter**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **root_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |
| **multi_root** | **bool** |  | [optional] |
| **multi_root_entities_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **multi_root_entity_ids** | **List[str]** |  | [optional] |
| **direction** | [**EntitySearchDirection**](EntitySearchDirection.md) |  | [optional] |
| **filters** | [**List[RelationEntityTypeFilter]**](RelationEntityTypeFilter.md) |  | [optional] |
| **max_level** | **int** |  | [optional] |
| **fetch_last_level_only** | **bool** |  | [optional] |
| **negate** | **bool** |  | [optional] |
| **root_state_entity** | **bool** |  | [optional] |
| **default_state_entity** | [**AliasEntityId**](AliasEntityId.md) |  | [optional] |



## Referenced Types

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AliasEntityId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alias_entity_type | AliasEntityType |  | [optional] |
| entity_type | EntityType |  |  |
| id | UUID | ID of the entity, time-based UUID v1 |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### RelationEntityTypeFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relation_type | str | Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages'). | [optional] |
| entity_types | List[EntityType] | Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET'). | [optional] |
| negate | bool | Negate relation type between root entity and other entity. | [optional] |

#### AliasEntityType (enum)
`CURRENT_CUSTOMER` | `CURRENT_TENANT` | `CURRENT_USER` | `CURRENT_USER_OWNER`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.root_entity`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RelationsQueryFilter.model_validate(data)` or `RelationsQueryFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

