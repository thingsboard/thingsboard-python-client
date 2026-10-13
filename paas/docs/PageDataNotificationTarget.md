
# PageDataNotificationTarget

`tb_paas_client.models.PageDataNotificationTarget`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[NotificationTarget]**](NotificationTarget.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### NotificationTarget
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | NotificationTargetId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| name | str |  |  |
| configuration | NotificationTargetConfig |  |  |

#### NotificationTargetConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| description | str |  | [optional] |
| type | str |  |  |

#### MicrosoftTeamsNotificationTargetConfig  *(extends NotificationTargetConfig, type=`MICROSOFT_TEAMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| webhook_url | str |  |  |
| channel_name | str |  |  |
| use_old_api | bool |  | [optional] |
| email | str |  | [optional] |
| first_name | str |  | [optional] |
| id | object |  | [optional] |
| last_name | str |  | [optional] |
| title | str |  | [optional] |

#### PlatformUsersNotificationTargetConfig  *(extends NotificationTargetConfig, type=`PLATFORM_USERS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| users_filter | UsersFilter |  |  |

#### SlackNotificationTargetConfig  *(extends NotificationTargetConfig, type=`SLACK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| conversation_type | SlackConversationType |  | [optional] |
| conversation | SlackConversation |  |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

#### UsersFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AffectedTenantAdministratorsFilter  *(extends UsersFilter, type=`AFFECTED_TENANT_ADMINISTRATORS`)*
*See UsersFilter for properties.*

#### AffectedUserFilter  *(extends UsersFilter, type=`AFFECTED_USER`)*
*See UsersFilter for properties.*

#### AllUsersFilter  *(extends UsersFilter, type=`ALL_USERS`)*
*See UsersFilter for properties.*

#### CustomerUsersFilter  *(extends UsersFilter, type=`CUSTOMER_USERS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | UUID |  |  |

#### OriginatorEntityOwnerUsersFilter  *(extends UsersFilter, type=`ORIGINATOR_ENTITY_OWNER_USERS`)*
*See UsersFilter for properties.*

#### SystemAdministratorsFilter  *(extends UsersFilter, type=`SYSTEM_ADMINISTRATORS`)*
*See UsersFilter for properties.*

#### TenantAdministratorsFilter  *(extends UsersFilter, type=`TENANT_ADMINISTRATORS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tenants_ids | List[UUID] |  | [optional] |
| tenant_profiles_ids | List[UUID] |  | [optional] |

#### UserGroupListFilter  *(extends UsersFilter, type=`USER_GROUP_LIST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| groups_ids | List[UUID] |  |  |

#### UserListFilter  *(extends UsersFilter, type=`USER_LIST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| users_ids | List[UUID] |  |  |

#### UserRoleFilter  *(extends UsersFilter, type=`USER_ROLE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| roles_ids | List[UUID] |  |  |

#### SlackConversationType (enum)
`DIRECT` | `PUBLIC_CHANNEL` | `PRIVATE_CHANNEL`

#### SlackConversation
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SlackConversationType |  |  |
| id | str |  |  |
| name | str |  |  |
| whole_name | str |  | [optional] |
| email | str |  | [optional] |
| title | str |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataNotificationTarget.model_validate(data)` or `PageDataNotificationTarget.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

