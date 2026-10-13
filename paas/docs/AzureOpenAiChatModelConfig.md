
# AzureOpenAiChatModelConfig

`tb_paas_client.models.AzureOpenAiChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_config** | [**AzureOpenAiProviderConfig**](AzureOpenAiProviderConfig.md) |  | |
| **model_id** | **str** |  | |
| **temperature** | **float** |  | [optional] |
| **top_p** | **float** |  | [optional] |
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

#### AzureOpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| endpoint | str |  |  |
| service_version | str |  | [optional] |
| api_key | str |  |  |

#### AiModelType (enum)
`CHAT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.provider_config`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AzureOpenAiChatModelConfig.model_validate(data)` or `AzureOpenAiChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

