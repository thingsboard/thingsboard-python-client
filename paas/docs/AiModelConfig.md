
# AiModelConfig

`tb_paas_client.models.AiModelConfig`

Root configuration for AI models

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **provider** | **str** |  | |



## Subtypes

#### AmazonBedrockChatModelConfig  *(provider=`AMAZON_BEDROCK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | AmazonBedrockProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### AnthropicChatModelConfig  *(provider=`ANTHROPIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | AnthropicProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### AzureOpenAiChatModelConfig  *(provider=`AZURE_OPENAI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | AzureOpenAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### GitHubModelsChatModelConfig  *(provider=`GITHUB_MODELS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | GitHubModelsProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### GoogleAiGeminiChatModelConfig  *(provider=`GOOGLE_AI_GEMINI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | GoogleAiGeminiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### GoogleVertexAiGeminiChatModelConfig  *(provider=`GOOGLE_VERTEX_AI_GEMINI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | GoogleVertexAiGeminiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### MistralAiChatModelConfig  *(provider=`MISTRAL_AI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | MistralAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### OllamaChatModelConfig  *(provider=`OLLAMA`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | OllamaProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| top_k | int |  | [optional] |
| context_length | int |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

#### OpenAiChatModelConfig  *(provider=`OPENAI`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider_config | OpenAiProviderConfig |  |  |
| model_id | str |  |  |
| temperature | float |  | [optional] |
| top_p | float |  | [optional] |
| frequency_penalty | float |  | [optional] |
| presence_penalty | float |  | [optional] |
| max_output_tokens | int |  | [optional] |
| timeout_seconds | int |  | [optional] |
| max_retries | int |  | [optional] |
| model_type | AiModelType |  | [optional] [readonly] |

## Referenced Types

#### AmazonBedrockProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| region | str |  |  |
| access_key_id | str |  |  |
| secret_access_key | str |  |  |

#### AiModelType (enum)
`CHAT`

#### AnthropicProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### AzureOpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| endpoint | str |  |  |
| service_version | str |  | [optional] |
| api_key | str |  |  |

#### GitHubModelsProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| personal_access_token | str |  |  |

#### GoogleAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### GoogleVertexAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| file_name | str |  | [optional] |
| project_id | str |  |  |
| location | str |  |  |
| service_account_key | str |  |  |

#### MistralAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### OllamaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  |  |
| auth | OllamaAuth |  |  |

#### OpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  | [optional] |
| api_key | str |  | [optional] |

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
- **Attribute access:** `obj.provider`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AiModelConfig.model_validate(data)` or `AiModelConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

