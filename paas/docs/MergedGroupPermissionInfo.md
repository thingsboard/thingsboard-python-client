
# MergedGroupPermissionInfo

`tb_paas_client.models.MergedGroupPermissionInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_type** | [**EntityType**](EntityType.md) |  | [optional] |
| **operations** | [**List[Operation]**](Operation.md) |  | [optional] |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

#### Operation (enum)
`ALL` | `CREATE` | `READ` | `WRITE` | `DELETE` | `RPC_CALL` | `READ_CREDENTIALS` | `WRITE_CREDENTIALS` | `READ_ATTRIBUTES` | `WRITE_ATTRIBUTES` | … (21 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `MergedGroupPermissionInfo.model_validate(data)` or `MergedGroupPermissionInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

