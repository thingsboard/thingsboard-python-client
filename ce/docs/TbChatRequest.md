
# TbChatRequest

`tb_ce_client.models.TbChatRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **system_message** | **str** | A system-level instruction that frames the user's input, setting the persona, tone, and constraints for the generated response | [optional] |
| **user_message** | [**TbUserMessage**](TbUserMessage.md) | The actual user prompt that will be answered by the AI model | |
| **chat_model_config** | [**AiModelConfig**](AiModelConfig.md) | Configuration of the AI chat model that should execute the request | |



## Referenced Types

#### TbUserMessage
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| contents | List[TbContent] | A list of content parts that make up the complete user prompt |  |

#### AiModelConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provider | str |  |  |

#### AmazonBedrockChatModelConfig  *(extends AiModelConfig, provider=`AMAZON_BEDROCK`)*
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

#### AnthropicChatModelConfig  *(extends AiModelConfig, provider=`ANTHROPIC`)*
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

#### AzureOpenAiChatModelConfig  *(extends AiModelConfig, provider=`AZURE_OPENAI`)*
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

#### GitHubModelsChatModelConfig  *(extends AiModelConfig, provider=`GITHUB_MODELS`)*
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

#### GoogleAiGeminiChatModelConfig  *(extends AiModelConfig, provider=`GOOGLE_AI_GEMINI`)*
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

#### GoogleVertexAiGeminiChatModelConfig  *(extends AiModelConfig, provider=`GOOGLE_VERTEX_AI_GEMINI`)*
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

#### MistralAiChatModelConfig  *(extends AiModelConfig, provider=`MISTRAL_AI`)*
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

#### OllamaChatModelConfig  *(extends AiModelConfig, provider=`OLLAMA`)*
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

#### OpenAiChatModelConfig  *(extends AiModelConfig, provider=`OPENAI`)*
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

#### TbContent
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| content_type | str |  |  |

#### TbTextContent  *(extends TbContent, content_type=`TEXT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| text | str | The text content |  |

#### OpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  | [optional] |
| api_key | str |  | [optional] |

#### AiModelType (enum)
`CHAT`

#### AzureOpenAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| endpoint | str |  |  |
| service_version | str |  | [optional] |
| api_key | str |  |  |

#### GoogleAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### GoogleVertexAiGeminiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| file_name | str |  |  |
| project_id | str |  |  |
| location | str |  |  |
| service_account_key | str |  |  |

#### MistralAiProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### AnthropicProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_key | str |  |  |

#### AmazonBedrockProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| region | str |  |  |
| access_key_id | str |  |  |
| secret_access_key | str |  |  |

#### GitHubModelsProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| personal_access_token | str |  |  |

#### OllamaProviderConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| base_url | str |  |  |
| auth | OllamaAuth |  |  |

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

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.system_message`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TbChatRequest.model_validate(data)` or `TbChatRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

