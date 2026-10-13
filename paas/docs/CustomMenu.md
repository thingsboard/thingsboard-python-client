
# CustomMenu

`tb_paas_client.models.CustomMenu`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**CustomMenuId**](CustomMenuId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the menu. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id that owns the menu. | [optional] [readonly] |
| **name** | **str** | Custom menu name | |
| **scope** | [**CMScope**](CMScope.md) | Custom menu scope. Possible values: SYSTEM, TENANT, CUSTOMER | |
| **assignee_type** | [**CMAssigneeType**](CMAssigneeType.md) | Custom menu assignee type. Possible values are: All (all users of specified scope), CUSTOMERS (specified customers), USERS (specified list of users), NO_ASSIGN (no assignees), USER_GROUPS (user groups) | |
| **user_group_names** | **List[str]** | User group names menu is applied to | [optional] |
| **config** | [**CustomMenuConfig**](CustomMenuConfig.md) | Custom menu configuration | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### CustomMenuId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### CMScope (enum)
`SYSTEM` | `TENANT` | `CUSTOMER`

#### CMAssigneeType (enum)
`NO_ASSIGN` | `ALL` | `CUSTOMERS` | `USERS` | `USER_GROUPS`

#### CustomMenuConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| items | List[MenuItem] |  | [optional] |

#### MenuItem
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | MenuItemType | Menu item type |  |
| visible | bool |  | [optional] |

#### CustomMenuItem  *(extends MenuItem, type=`CUSTOM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str | Name of the menu item |  |
| icon | str | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| menu_item_type | CMItemType | Type of menu item (LINK or SECTION). LINK type means item has no child items, SECTION type should have at least one child |  |
| link_type | CMItemLinkType | Type of menu item (URL or DASHBOARD) | [optional] |
| dashboard_id | str | Id of the Dashboard to open, when user clicks the menu item | [optional] |
| hide_dashboard_toolbar | bool | Hide the dashboard toolbar | [optional] |
| url | str | URL to open in the iframe, when user clicks the menu item | [optional] |
| set_access_token | bool | Set the access token of the current user to a new dashboard | [optional] |
| visible | bool | Mark if menu item is visible for user | [optional] |
| pages | List[CustomMenuItem] | List of child menu items | [optional] |

#### DefaultMenuItem  *(extends MenuItem, type=`DEFAULT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Unique identifier for predefined menu items | [optional] [readonly] |
| name | str | Name of the menu item | [optional] |
| icon | str | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| visible | bool | Mark if menu item is visible for user | [optional] |
| pages | List[DefaultMenuItem] | List of child menu items | [optional] |

#### HomeMenuItem  *(extends MenuItem, type=`HOME`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | str | Unique identifier for predefined menu items | [optional] [readonly] |
| name | str | Name of the menu item | [optional] |
| icon | str | URL of the menu item icon. Overrides 'materialIcon' | [optional] |
| pages | List[DefaultMenuItem] | List of child menu items | [optional] |
| home_type | HomeMenuItemType | DEFAULT or DASHBOARD. DASHBOARD means default home page presentation changed to refer to dashboard | [optional] |
| dashboard_id | str | Id of the Dashboard to open, when user clicks the menu item | [optional] |
| hide_dashboard_toolbar | bool | Hide the dashboard toolbar | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

#### MenuItemType (enum)
`HOME` | `DEFAULT` | `CUSTOM`

#### HomeMenuItemType (enum)
`DEFAULT` | `DASHBOARD`

#### CMItemType (enum)
`LINK` | `SECTION`

#### CMItemLinkType (enum)
`URL` | `DASHBOARD`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenu.model_validate(data)` or `CustomMenu.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

