
# PageDataMobileAppBundleInfo

`tb_paas_client.models.PageDataMobileAppBundleInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[MobileAppBundleInfo]**](MobileAppBundleInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### MobileAppBundleInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | MobileAppBundleId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id | [optional] |
| title | str | Application bundle title. Cannot be empty |  |
| description | str | Application bundle description. | [optional] |
| android_app_id | MobileAppId | Android application id | [optional] |
| ios_app_id | MobileAppId | IOS application id | [optional] |
| layout_config | MobileLayoutConfig | Application layout configuration | [optional] |
| self_registration_params | MobileSelfRegistrationParams | Application self registration configuration | [optional] |
| oauth2_enabled | bool | Whether OAuth2 settings are enabled or not | [optional] |
| android_pkg_name | str | Android package name | [optional] |
| ios_pkg_name | str | IOS package name | [optional] |
| oauth2_client_infos | List[OAuth2ClientInfo] | List of available oauth2 clients | [optional] |
| qr_code_enabled | bool | Indicates if qr code is available for bundle | [optional] |
| name | str | Mobile app bundle title | [optional] [readonly] |

#### MobileLayoutConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| pages | List[MobilePage] |  | [optional] |

#### OAuth2ClientInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | OAuth2ClientId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| title | str | Oauth2 client registration title (e.g. My google) | [optional] |
| provider_name | str | Oauth2 client provider name (e.g. Google) | [optional] |
| platforms | List[PlatformType] | List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed) | [optional] |
| name | str |  | [optional] [readonly] |

#### MobilePage
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | MobilePageType |  |  |
| visible | bool |  | [optional] |

#### CustomMobilePage  *(extends MobilePage, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str | Page label | [optional] |
| icon | str | URL of the page icon | [optional] |
| path | str | Path to custom page | [optional] |

#### DashboardPage  *(extends MobilePage, type=`DASHBOARD`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str | Page label | [optional] |
| icon | str | URL of the page icon | [optional] |
| dashboard_id | str | Dashboard id | [optional] |

#### DefaultMobilePage  *(extends MobilePage, type=`DEFAULT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str | Page label | [optional] |
| icon | str | URL of the page icon | [optional] |
| id | DefaultPageId | Identifier for default page | [optional] |

#### WebViewPage  *(extends MobilePage, type=`WEB_VIEW`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| label | str | Page label | [optional] |
| icon | str | URL of the page icon | [optional] |
| url | str | Url | [optional] |

#### SelfRegistrationParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SelfRegistrationType |  |  |
| enabled | bool |  | [optional] |
| title | str |  | [optional] |
| captcha | CaptchaParams |  | [optional] |
| permissions | List[GroupPermission] |  | [optional] |
| notification_recipient | NotificationTargetId |  | [optional] |
| sign_up_fields | List[SignUpField] |  | [optional] |
| customer_title_prefix | str |  | [optional] |
| show_privacy_policy | bool |  | [optional] |
| show_terms_of_use | bool |  | [optional] |
| default_dashboard | DefaultDashboardParams |  | [optional] |
| home_dashboard | HomeDashboardParams |  | [optional] |
| customer_group_id | EntityGroupId |  | [optional] |
| custom_menu_id | CustomMenuId |  | [optional] |

#### MobileSelfRegistrationParams  *(extends SelfRegistrationParams, type=`MOBILE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| privacy_policy | str | Privacy policy text. Supports HTML. | [optional] |
| redirect | MobileRedirectParams | Mobile redirect params. |  |
| terms_of_use | str | Terms of User text. Supports HTML. | [optional] |

#### WebSelfRegistrationParams  *(extends SelfRegistrationParams, type=`WEB`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| domain_id | DomainId | Domain name for self registration URL. Typically this matches the domain name from the Login White Labeling page. |  |
| privacy_policy | str | Privacy policy text. Supports HTML. | [optional] |
| terms_of_use | str | Terms of User text. Supports HTML. | [optional] |

#### MobileRedirectParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| scheme | str | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |
| host | str | Mobile application verification settings. Used for callback to mobile application once user is registered. | [optional] |

#### PlatformType (enum)
`WEB` | `ANDROID` | `IOS`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

#### MobilePageType (enum)
`DEFAULT` | `DASHBOARD` | `WEB_VIEW` | `CUSTOM`

#### SelfRegistrationType (enum)
`WEB` | `MOBILE`

#### CaptchaParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version | str |  |  |

#### EnterpriseCaptchaParams  *(extends CaptchaParams, version=`enterprise`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| project_id | str | Your Google Cloud project ID | [optional] |
| service_account_credentials | str | Service account credentials | [optional] |
| service_account_credentials_file_name | str | Service account credentials file name | [optional] |
| android_key | str | The reCAPTCHA key associated with android app. | [optional] |
| ios_key | str | The reCAPTCHA key associated with iOS app. | [optional] |
| log_action_name | str | Optional action name used for logging | [optional] |

#### V2CaptchaParams  *(extends CaptchaParams, version=`v2`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| site_key | str | Captcha site key for 'I'm not a robot' validation | [optional] |
| log_action_name | str | Optional action name used for logging (for captcha version 'v3' and 'enterprise') | [optional] |
| secret_key | str | Secret key to validate the Captcha. Should match the Captcha Site Key. | [optional] |

#### V3CaptchaParams  *(extends CaptchaParams, version=`v3`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| site_key | str | Captcha site key for 'I'm not a robot' validation | [optional] |
| log_action_name | str | Optional action name used for logging (for captcha version 'v3' and 'enterprise') | [optional] |
| secret_key | str | Secret key to validate the Captcha. Should match the Captcha Site Key. | [optional] |

#### GroupPermission
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | GroupPermissionId | JSON object with the Group Permission Id. Specify this field to update the Group Permission. Referencing non-existing Group Permission Id will cause error. Omit this field to create new Group Permission. | [optional] |
| created_time | int | Timestamp of the group permission creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with the Tenant Id. | [optional] [readonly] |
| user_group_id | EntityGroupId | JSON object with the User Group Id. Represents the user group that will have permissions to perform operations against the corresponding entity group. |  |
| role_id | RoleId | JSON object with the Role Id. Represents the set of permissions. The role type (GENERIC or GROUP) determines whether 'entityGroupId' is required. |  |
| entity_group_id | EntityGroupId | JSON object with the Entity Group Id. Required when using a GROUP role — specifies the entity group to which the permissions apply. Must be null or omitted when using a GENERIC role. | [optional] |
| entity_group_type | EntityType | Type of the entities in the group: DEVICE, ASSET, CUSTOMER, etc. Auto-populated from the referenced entity group. Null for generic permissions. | [optional] [readonly] |
| is_public | bool |  | [optional] |
| name | str | Name of the Group Permissions. Auto-generated | [optional] [readonly] |
| public | bool |  | [optional] |

#### SignUpField
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | SignUpFieldId | Signup field id |  |
| label | str | Signup field label |  |
| required | bool | Indicates if field is required | [optional] |

#### DefaultDashboardParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Default dashboard Id to assign for the new user. | [optional] |
| fullscreen | bool | Set default dashboard to full screen mode. | [optional] |

#### HomeDashboardParams
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Home dashboard Id to assign for the new user. | [optional] |
| hide_toolbar | bool | Indicates if hide toolbar should be hidden. | [optional] |

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### DefaultPageId (enum)
`HOME` | `ALARMS` | `DEVICES` | `CUSTOMERS` | `ASSETS` | `AUDIT_LOGS` | `NOTIFICATIONS` | `DEVICE_LIST` | `DASHBOARDS`

#### SignUpFieldId (enum)
`EMAIL` | `PASSWORD` | `REPEAT_PASSWORD` | `FIRST_NAME` | `LAST_NAME` | `PHONE` | `COUNTRY` | `CITY` | `STATE` | `ZIP` | … (12 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataMobileAppBundleInfo.model_validate(data)` or `PageDataMobileAppBundleInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

