
# OAuth2Client

`tb_pe_client.models.OAuth2Client`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**OAuth2ClientId**](OAuth2ClientId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **additional_info** | **object** | Additional info of OAuth2 client. Must include: 'providerName' (string, name of the OAuth2 provider). | |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id | [optional] |
| **title** | **str** | Oauth2 client title | |
| **mapper_config** | [**OAuth2MapperConfig**](OAuth2MapperConfig.md) | Config for mapping OAuth2 log in response to platform entities | |
| **client_id** | **str** | OAuth2 client ID. Cannot be empty | |
| **client_secret** | **str** | OAuth2 client secret. Cannot be empty | |
| **authorization_uri** | **str** | Authorization URI of the OAuth2 provider. Cannot be empty | |
| **access_token_uri** | **str** | Access token URI of the OAuth2 provider. Cannot be empty | |
| **scope** | **List[str]** | OAuth scopes that will be requested from OAuth2 platform. Cannot be empty | |
| **user_info_uri** | **str** | User info URI of the OAuth2 provider | [optional] |
| **user_name_attribute_name** | **str** | Name of the username attribute in OAuth2 provider response. Cannot be empty | |
| **jwk_set_uri** | **str** | JSON Web Key URI of the OAuth2 provider | [optional] |
| **client_authentication_method** | **str** | Client authentication method to use: 'BASIC' or 'POST'. Cannot be empty | |
| **login_button_label** | **str** | OAuth2 provider label. Cannot be empty | |
| **login_button_icon** | **str** | Log in button icon for OAuth2 provider | [optional] |
| **platforms** | [**List[PlatformType]**](PlatformType.md) | List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed) | [optional] |
| **name** | **str** |  | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) |  | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### OAuth2MapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| allow_user_creation | bool | Whether user should be created if not yet present on the platform after successful authentication | [optional] |
| activate_user | bool | Whether user credentials should be activated when user is created after successful authentication | [optional] |
| type | MapperType | Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified |  |
| basic | OAuth2BasicMapperConfig | Mapper config for BASIC and GITHUB mapper types | [optional] |
| custom | OAuth2CustomMapperConfig | Mapper config for CUSTOM mapper type | [optional] |

#### PlatformType (enum)
`WEB` | `ANDROID` | `IOS`

#### MapperType (enum)
`BASIC` | `CUSTOM` | `GITHUB` | `APPLE`

#### OAuth2BasicMapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| email_attribute_key | str | Email attribute key of OAuth2 principal attributes. Must be specified for BASIC mapper type and cannot be specified for GITHUB type | [optional] |
| first_name_attribute_key | str | First name attribute key | [optional] |
| last_name_attribute_key | str | Last name attribute key | [optional] |
| tenant_name_strategy | TenantNameStrategyType | Tenant naming strategy. For DOMAIN type, domain for tenant name will be taken from the email (substring before '@') |  |
| tenant_name_pattern | str | Tenant name pattern for CUSTOM naming strategy. OAuth2 attributes in the pattern can be used by enclosing attribute key in '%{' and '}' | [optional] |
| customer_name_pattern | str | Customer name pattern. When creating a user on the first OAuth2 log in, if specified, customer name will be used to create or find existing customer in the platform and assign customerId to the user | [optional] |
| default_dashboard_name | str | Name of the tenant's dashboard to set as default dashboard for newly created user | [optional] |
| always_full_screen | bool | Whether default dashboard should be open in full screen | [optional] |
| parent_customer_name_pattern | str |  | [optional] |
| user_groups_name_pattern | List[str] |  | [optional] |

#### OAuth2CustomMapperConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| url | str |  | [optional] |
| username | str |  | [optional] |
| password | str |  | [optional] |
| send_token | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### TenantNameStrategyType (enum)
`DOMAIN` | `EMAIL` | `CUSTOM`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `OAuth2Client.model_validate(data)` or `OAuth2Client.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

