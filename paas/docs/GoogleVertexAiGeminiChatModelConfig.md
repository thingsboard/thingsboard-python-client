
# GoogleVertexAiGeminiChatModelConfig

`tb_paas_client.models.GoogleVertexAiGeminiChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_config** | [**GoogleVertexAiGeminiProviderConfig**](GoogleVertexAiGeminiProviderConfig.md) |  | |
| **model_id** | **str** |  | |
| **temperature** | **float** |  | [optional] |
| **top_p** | **float** |  | [optional] |
| **top_k** | **int** |  | [optional] |
| **frequency_penalty** | **float** |  | [optional] |
| **presence_penalty** | **float** |  | [optional] |
| **max_output_tokens** | **int** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **max_retries** | **int** |  | [optional] |
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] [readonly] |



## Referenced Types

#### AiModelConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider | str |  |  |

#### GoogleVertexAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| file_name | str |  | [optional] |
| project_id | str |  |  |
| location | str |  |  |
| service_account_key | str |  |  |

#### AiModelType (enum)
`CHAT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.provider_config`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GoogleVertexAiGeminiChatModelConfig.model_validate(data)` or `GoogleVertexAiGeminiChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

