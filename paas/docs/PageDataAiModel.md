
# PageDataAiModel

`tb_paas_client.models.PageDataAiModel`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[AiModel]**](AiModel.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AiModel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AiModelId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId | JSON object representing the ID of the tenant associated with this AI model | [optional] [readonly] |
| version | int | Version of the AI model record; increments automatically whenever the record is changed | [optional] [readonly] |
| name | str | Display name for this AI model configuration; not the technical model identifier |  |
| configuration | AiModelConfig | Configuration of the AI model | [optional] |

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

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

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
| file_name | str |  | [optional] |
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

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAiModel.model_validate(data)` or `PageDataAiModel.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

