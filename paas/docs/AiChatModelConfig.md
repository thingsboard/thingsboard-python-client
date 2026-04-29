
# AiChatModelConfig

`tb_paas_client.models.AiChatModelConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] |



## Referenced Types

#### AiModelType (enum)
`CHAT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.model_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AiChatModelConfig.model_validate(data)` or `AiChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

