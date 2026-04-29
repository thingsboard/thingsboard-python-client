
# AvailableEntityKeysV2

`tb_paas_client.models.AvailableEntityKeysV2`

Contains unique time series and attribute key names discovered from entities matching a query, optionally including a sample value for each key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **total_entities** | **int** | Total number of entities that matched the query filter. | |
| **entity_types** | [**List[EntityType]**](EntityType.md) | Set of entity types found among the matched entities. | |
| **timeseries** | [**List[KeyInfo]**](KeyInfo.md) |  | [optional] |
| **attributes** | **Dict[str, List[KeyInfo]]** | Map of attribute scope to the list of unique attribute keys available on the matched entities. Only scopes supported by the matched entity types are included. Omitted when attribute keys were not requested or when none of the requested scopes apply to the matched entity types. | [optional] |



## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### KeyInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str | Key name. |  |
| sample | KeySample | Most recent sample value for this key across the matched entities. Omitted when samples were not requested. | [optional] |

#### KeySample
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ts | int | Timestamp in milliseconds since epoch. |  |
| value | object |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.total_entities`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AvailableEntityKeysV2.model_validate(data)` or `AvailableEntityKeysV2.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

