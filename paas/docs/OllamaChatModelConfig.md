
# OllamaChatModelConfig

`tb_paas_client.models.OllamaChatModelConfig`

**Extends:** **AiModelConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider_config** | [**OllamaProviderConfig**](OllamaProviderConfig.md) |  | |
| **model_id** | **str** |  | |
| **temperature** | **float** |  | [optional] |
| **top_p** | **float** |  | [optional] |
| **top_k** | **int** |  | [optional] |
| **context_length** | **int** |  | [optional] |
| **max_output_tokens** | **int** |  | [optional] |
| **timeout_seconds** | **int** |  | [optional] |
| **max_retries** | **int** |  | [optional] |
| **model_type** | [**AiModelType**](AiModelType.md) |  | [optional] [readonly] |



## Referenced Types

#### AiModelConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider | str |  |  |

#### OllamaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  |  |
| auth | OllamaAuth |  |  |

#### AiModelType (enum)
`CHAT`

#### OllamaAuth
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### Basic  *(extends OllamaAuth, type=`BASIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| username | str |  |  |
| password | str |  |  |

#### ModelNone  *(extends OllamaAuth, type=`NONE`)*
*See OllamaAuth for properties.*

#### Token  *(extends OllamaAuth, type=`TOKEN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| token | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.provider_config`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OllamaChatModelConfig.model_validate(data)` or `OllamaChatModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

