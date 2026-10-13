
# CustomMenuConfig

`tb_paas_client.models.CustomMenuConfig`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **items** | [**List[MenuItem]**](MenuItem.md) |  | [optional] |



## Referenced Types

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
- **Attribute access:** `obj.items`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `CustomMenuConfig.model_validate(data)` or `CustomMenuConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

