# CustomMenuControllerApi

`ThingsboardClient` methods:

```python
CustomMenu client.create_custom_menu(custom_menu_info: CustomMenuInfo, assign_to_list: Optional[List[str]] = None, force: Optional[bool] = None)  # Create Custom Menu (createCustomMenu)
CustomMenuDeleteResult client.delete_custom_menu(custom_menu_id: UUID, force: Optional[bool] = None)  # Delete custom menu (deleteCustomMenu)
CustomMenuConfig client.get_custom_menu(if_none_match: Optional[str] = None)  # Get end-user Custom Menu configuration (getCustomMenu)
List[EntityInfo] client.get_custom_menu_assignee_list(custom_menu_id: UUID)  # Get Custom Menu assignee list (getCustomMenuAssigneeList)
CustomMenuConfig client.get_custom_menu_config(custom_menu_id: UUID)  # Get Custom Menu configuration by id (getCustomMenuConfig)
CustomMenuInfo client.get_custom_menu_info_by_id(custom_menu_id: UUID)  # Get Custom Menu Info (getCustomMenuInfoById)
PageDataCustomMenuInfo client.get_custom_menu_infos(page_size: int, page: int, scope: Optional[CMScope] = None, assignee_type: Optional[CMAssigneeType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get all custom menus configured at user level (getCustomMenuInfos)
None client.update_custom_menu_assignee_list(id: UUID, assignee_type: CMAssigneeType, force: Optional[bool] = None, request_body: Optional[List[str]] = None)  # Update custom menu assignee list (updateCustomMenuAssigneeList)
CustomMenu client.update_custom_menu_config(custom_menu_id: UUID, custom_menu_config: CustomMenuConfig)  # Update Custom Menu configuration based on the provided Custom Menu Id (updateCustomMenuConfig)
None client.update_custom_menu_name(custom_menu_id: UUID, body: str)  # Update Custom Menu name based on the provided Custom Menu Id (updateCustomMenuName)
```


## create_custom_menu

```python
CustomMenu client.create_custom_menu(custom_menu_info: CustomMenuInfo, assign_to_list: Optional[List[str]] = None, force: Optional[bool] = None)
```

**POST** `/api/customMenu`

Create Custom Menu (createCustomMenu)

The api is designed to create Custom Menu without configuration. Is not applicable for update.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_info** | **CustomMenuInfo** |  | |
| **assign_to_list** | **List[str]** | A list of entity ids, separated by comma ',' | [optional] |
| **force** | **bool** | Use force if you want to create default menu that conflicts with the existing one (old one will be update NO_ASSIGN assignee type) | [optional] |

### Return type

**CustomMenu**


## delete_custom_menu

```python
CustomMenuDeleteResult client.delete_custom_menu(custom_menu_id: UUID, force: Optional[bool] = None)
```

**DELETE** `/api/customMenu/{customMenuId}`

Delete custom menu (deleteCustomMenu)

Deletes the custom menu based on the provided Custom Menu Id. Referencing non-existing custom menu Id will cause an error. If the custom menu is assigned to the list of users or customers bad request is returned.To delete a custom menu that has assignee list set 'force' request param to true 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **force** | **bool** | Force set to true will unassign menu before deletion | [optional] |

### Return type

**CustomMenuDeleteResult**


## get_custom_menu

```python
CustomMenuConfig client.get_custom_menu(if_none_match: Optional[str] = None)
```

**GET** `/api/customMenu`

Get end-user Custom Menu configuration (getCustomMenu)

Fetch the Custom Menu configuration object for the authorized user. The custom menu is configured in the white labeling parameters and has one of three user scopes:SYSTEM, TENANT, CUSTOMER and four assignee type: NO_ASSIGN, ALL, CUSTOMERS, USERS.There are three default (assignee type: ALL) menus configured on the system level for each scope and if no other menu is configured for user, system configuration of the corresponding scope will be applied.If a custom menu with assignee type ALL is configured on the tenant level, it overrides the menu configuration of the corresponding scope on the system level. If a custom menu with assignee type USER_GROUPS is configured on the tenant level, it overrides default tenant menu.If a custom menu with assignee type CUSTOMERS is configured on tenant level for specific customer, it will be applied to all customer users.If a custom menu with assignee type ALL is configured on the customer level, it overrides the menu assigned on tenant level.If a custom menu with assignee type USER_GROUPS is configured on the customer level, it overrides default customer menu.If a custom menu is assigned to specific user, it overrides all other configuration.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **if_none_match** | **str** |  | [optional] |

### Return type

**CustomMenuConfig**


## get_custom_menu_assignee_list

```python
List[EntityInfo] client.get_custom_menu_assignee_list(custom_menu_id: UUID)
```

**GET** `/api/customMenu/{customMenuId}/assigneeList`

Get Custom Menu assignee list (getCustomMenuAssigneeList)

Fetch the list of Entity Info objects that represents users or customers, or empty list if custom menu is not assigned or has NO_ASSIGN/ALL assignee type.  Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[EntityInfo]**


## get_custom_menu_config

```python
CustomMenuConfig client.get_custom_menu_config(custom_menu_id: UUID)
```

**GET** `/api/customMenu/{customMenuId}/config`

Get Custom Menu configuration by id (getCustomMenuConfig)

Fetch the Custom Menu configuration based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**CustomMenuConfig**


## get_custom_menu_info_by_id

```python
CustomMenuInfo client.get_custom_menu_info_by_id(custom_menu_id: UUID)
```

**GET** `/api/customMenu/{customMenuId}/info`

Get Custom Menu Info (getCustomMenuInfoById)

Fetch the Custom Menu Info object based on the provided Custom Menu Id.   Security check is performed to verify that the user has 'READ' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**CustomMenuInfo**


## get_custom_menu_infos

```python
PageDataCustomMenuInfo client.get_custom_menu_infos(page_size: int, page: int, scope: Optional[CMScope] = None, assignee_type: Optional[CMAssigneeType] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customMenu/infos`

Get all custom menus configured at user level (getCustomMenuInfos)

Returns a page of custom menu info objects owned by the tenant or the customer of a current user, scope and assigneeType request parameters can be used to filter the result.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **scope** | **CMScope** | Custom menu scope. | [optional] [enum: SYSTEM, TENANT, CUSTOMER] |
| **assignee_type** | **CMAssigneeType** | Custom menu assignee type. | [optional] [enum: NO_ASSIGN, ALL, CUSTOMERS, USERS, USER_GROUPS] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the custom menu name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomMenuInfo**


## update_custom_menu_assignee_list

```python
None client.update_custom_menu_assignee_list(id: UUID, assignee_type: CMAssigneeType, force: Optional[bool] = None, request_body: Optional[List[str]] = None)
```

**PUT** `/api/customMenu/{id}/assign/{assigneeType}`

Update custom menu assignee list (updateCustomMenuAssigneeList)

The api designed to update the list of assignees or assignee type based on the provided Custom Menu Id. To change assignee type, put new assignee type in path parameter.  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |
| **assignee_type** | **CMAssigneeType** |  | [enum: NO_ASSIGN, ALL, CUSTOMERS, USERS, USER_GROUPS] |
| **force** | **bool** | Use force if you want to override default menu | [optional] |
| **request_body** | **List[str]** |  | [optional] |

### Return type

None (empty response body)


## update_custom_menu_config

```python
CustomMenu client.update_custom_menu_config(custom_menu_id: UUID, custom_menu_config: CustomMenuConfig)
```

**PUT** `/api/customMenu/{customMenuId}/config`

Update Custom Menu configuration based on the provided Custom Menu Id (updateCustomMenuConfig)

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **custom_menu_config** | **CustomMenuConfig** |  | |

### Return type

**CustomMenu**


## update_custom_menu_name

```python
None client.update_custom_menu_name(custom_menu_id: UUID, body: str)
```

**PUT** `/api/customMenu/{customMenuId}/name`

Update Custom Menu name based on the provided Custom Menu Id (updateCustomMenuName)

  Security check is performed to verify that the user has 'WRITE' permission for the custom menu with specified id.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **custom_menu_id** | **UUID** | A string value representing the custom menu id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** |  | |

### Return type

None (empty response body)

