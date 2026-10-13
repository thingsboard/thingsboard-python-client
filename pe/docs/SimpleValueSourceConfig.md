
# SimpleValueSourceConfig

`tb_pe_client.models.SimpleValueSourceConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**ValueSourceType**](ValueSourceType.md) |  | [optional] |
| **value** | **float** |  | [optional] |
| **latest_key_type** | **str** |  | [optional] |
| **latest_key** | **str** |  | [optional] |
| **entity_key_type** | **str** |  | [optional] |
| **entity_alias** | **str** |  | [optional] |
| **entity_key** | **str** |  | [optional] |



## Referenced Types

#### ValueSourceType (enum)
`CONSTANT` | `LATESTKEY` | `ENTITY`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SimpleValueSourceConfig.model_validate(data)` or `SimpleValueSourceConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

