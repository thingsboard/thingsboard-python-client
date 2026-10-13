
# AliasEntityId

`tb_paas_client.models.AliasEntityId`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alias_entity_type** | [**AliasEntityType**](AliasEntityType.md) |  | [optional] |
| **entity_type** | [**EntityType**](EntityType.md) |  | |
| **id** | **UUID** | ID of the entity, time-based UUID v1 | |



## Referenced Types

#### AliasEntityType (enum)
`CURRENT_CUSTOMER` | `CURRENT_TENANT` | `CURRENT_USER` | `CURRENT_USER_OWNER`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.alias_entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AliasEntityId.model_validate(data)` or `AliasEntityId.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

