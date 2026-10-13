
# GitHubModelsChatModelConfig

`tb_paas_client.models.GitHubModelsChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_config** | [**GitHubModelsProviderConfig**](GitHubModelsProviderConfig.md) |  | |
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

#### GitHubModelsProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| personal_access_token | str |  |  |

#### AiModelType (enum)
`CHAT`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.provider_config`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GitHubModelsChatModelConfig.model_validate(data)` or `GitHubModelsChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

