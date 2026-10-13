# UserControllerApi

`ThingsboardClient` methods:

```python
None client.delete_general_user_settings(paths: str)  # Delete user settings (deleteGeneralUserSettings)
None client.delete_user(user_id: str)  # Delete User (deleteUser)
None client.delete_user_settings_by_type(paths: str, type: str)  # Delete user settings by type (deleteUserSettingsByType)
PageDataUserEmailInfo client.find_users_by_query(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Find users by query (findUsersByQuery)
str client.get_activation_link(user_id: str)  # Get activation link (getActivationLink)
UserActivationLink client.get_activation_link_info(user_id: str)  # Get activation link info (getActivationLinkInfo)
PageDataUser client.get_all_customer_users(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Users (getCustomerUsers)
PageDataUserInfo client.get_all_user_infos(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All User Infos for current user (getAllUserInfos)
PageDataUserInfo client.get_customer_user_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer user Infos (getCustomerUserInfos)
PageDataUser client.get_customer_users(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Users (getCustomerUsers)
object client.get_general_user_settings()  # Get user settings (getGeneralUserSettings)
UserDashboardsInfo client.get_last_visited_dashboards()  # Get information about last visited and starred dashboards (getLastVisitedDashboards)
MobileSessionInfo client.get_mobile_session(x_mobile_token: str)  # getMobileSession
PageDataUser client.get_tenant_admins(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Users (getTenantAdmins)
User client.get_user_by_id(user_id: str)  # Get User (getUserById)
UserInfo client.get_user_info_by_id(user_id: str)  # Get User info (getUserInfoById)
object client.get_user_settings(type: str)  # Get user settings (getUserSettings)
JwtPair client.get_user_token(user_id: str)  # Get User Token (getUserToken)
PageDataUser client.get_user_users(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Users (getUsers)
PageDataUser client.get_users_by_entity_group_id(entity_group_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get users by Entity Group Id (getUsersByEntityGroupId)
List[User] client.get_users_by_ids(user_ids: List[str])  # Get Users By Ids (getUsersByIds)
PageDataUserEmailInfo client.get_users_for_assign(alarm_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get usersForAssign (getUsersForAssign)
bool client.is_user_token_access_enabled()  # Check Token Access Enabled (isUserTokenAccessEnabled)
None client.put_general_user_settings(body: object)  # Update user settings (putGeneralUserSettings)
None client.put_user_settings(type: str, body: object)  # Update user settings (putUserSettings)
None client.remove_mobile_session(x_mobile_token: str)  # removeMobileSession
UserDashboardsInfo client.report_user_dashboard_action(dashboard_id: str, action: str)  # Report action of User over the dashboard (reportUserDashboardAction)
None client.save_mobile_session(x_mobile_token: str, mobile_session_info: MobileSessionInfo)  # saveMobileSession
User client.save_user(user: User, send_activation_mail: Optional[str] = None, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)  # Save Or update User (saveUser)
object client.save_user_settings(body: object)  # Save user settings (saveUserSettings)
None client.send_activation_email(email: str)  # Send or re-send the activation email
None client.set_user_credentials_enabled(user_id: str, user_credentials_enabled: Optional[str] = None)  # Enable/Disable User credentials (setUserCredentialsEnabled)
```


## delete_general_user_settings

```python
None client.delete_general_user_settings(paths: str)
```

**DELETE** `/api/user/settings/{paths}`

Delete user settings (deleteGeneralUserSettings)

Delete user settings by specifying list of json element xpaths.   Example: to delete B and C element in { \"A\": {\"B\": 5}, \"C\": 15} send A.B,C in jsonPaths request parameter


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **paths** | **str** | paths | |

### Return type

None (empty response body)


## delete_user

```python
None client.delete_user(user_id: str)
```

**DELETE** `/api/user/{userId}`

Delete User (deleteUser)

Deletes the User, it's credentials and all the relations (from and to the User). Referencing non-existing User Id will cause an error.    Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## delete_user_settings_by_type

```python
None client.delete_user_settings_by_type(paths: str, type: str)
```

**DELETE** `/api/user/settings/{type}/{paths}`

Delete user settings by type (deleteUserSettingsByType)

Delete user settings by specifying list of json element xpaths.   Example: to delete B and C element in { \"A\": {\"B\": 5}, \"C\": 15} send A.B,C in jsonPaths request parameter


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **paths** | **str** | paths | |
| **type** | **str** | Settings type, case insensitive, one of: \"general\", \"quick_links\", \"doc_links\" or \"dashboards\". | |

### Return type

None (empty response body)


## find_users_by_query

```python
PageDataUserEmailInfo client.find_users_by_query(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/users/info`

Find users by query (findUsersByQuery)

Returns page of user data objects. Search is been executed by email, firstName and lastName fields. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUserEmailInfo**


## get_activation_link

```python
str client.get_activation_link(user_id: str)
```

**GET** `/api/user/{userId}/activationLink`

Get activation link (getActivationLink)

Get the activation link for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**


## get_activation_link_info

```python
UserActivationLink client.get_activation_link_info(user_id: str)
```

**GET** `/api/user/{userId}/activationLinkInfo`

Get activation link info (getActivationLinkInfo)

Get the activation link info for the user. The base url for activation link is configurable in the general settings of system administrator.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**UserActivationLink**


## get_all_customer_users

```python
PageDataUser client.get_all_customer_users(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/users`

Get Customer Users (getCustomerUsers)

Returns a page of users for the current tenant with authority 'CUSTOMER_USER'. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUser**


## get_all_user_infos

```python
PageDataUserInfo client.get_all_user_infos(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/userInfos/all`

Get All User Infos for current user (getAllUserInfos)

Returns a page of user info objects owned by the tenant or the customer of a current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUserInfo**


## get_customer_user_infos

```python
PageDataUserInfo client.get_customer_user_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/userInfos`

Get Customer user Infos (getCustomerUserInfos)

Returns a page of user info objects owned by the specified customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUserInfo**


## get_customer_users

```python
PageDataUser client.get_customer_users(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/users`

Get Customer Users (getCustomerUsers)

Returns a page of users owned by customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUser**


## get_general_user_settings

```python
object client.get_general_user_settings()
```

**GET** `/api/user/settings/general`

Get user settings (getGeneralUserSettings)

Fetch the User settings based on authorized user. 

### Return type

**object**


## get_last_visited_dashboards

```python
UserDashboardsInfo client.get_last_visited_dashboards()
```

**GET** `/api/user/lastVisitedDashboards`

Get information about last visited and starred dashboards (getLastVisitedDashboards)

Fetch the list of last visited and starred dashboards. Both lists are limited to 10 items.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**UserDashboardsInfo**


## get_mobile_session

```python
MobileSessionInfo client.get_mobile_session(x_mobile_token: str)
```

**GET** `/api/user/mobile/session`

getMobileSession


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **x_mobile_token** | **str** |  | |

### Return type

**MobileSessionInfo**


## get_tenant_admins

```python
PageDataUser client.get_tenant_admins(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/{tenantId}/users`

Get Tenant Users (getTenantAdmins)

Returns a page of users owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUser**


## get_user_by_id

```python
User client.get_user_by_id(user_id: str)
```

**GET** `/api/user/{userId}`

Get User (getUserById)

Fetch the User object based on the provided User Id. If the user has the authority of 'SYS_ADMIN', the server does not perform additional checks. If the user has the authority of 'TENANT_ADMIN', the server checks that the requested user is owned by the same tenant. If the user has the authority of 'CUSTOMER_USER', the server checks that the requested user is owned by the same customer.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**User**


## get_user_info_by_id

```python
UserInfo client.get_user_info_by_id(user_id: str)
```

**GET** `/api/user/info/{userId}`

Get User info (getUserInfoById)

Fetch the User info object based on the provided User Id. If the user has the authority of 'SYS_ADMIN', the server does not perform additional checks. If the user has the authority of 'TENANT_ADMIN', the server checks that the requested user is owned by the same tenant. If the user has the authority of 'CUSTOMER_USER', the server checks that the requested user is owned by the same customer.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**UserInfo**


## get_user_settings

```python
object client.get_user_settings(type: str)
```

**GET** `/api/user/settings/{type}`

Get user settings (getUserSettings)

Fetch the User settings based on authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Settings type, case insensitive, one of: \"general\", \"quick_links\", \"doc_links\" or \"dashboards\". | |

### Return type

**object**


## get_user_token

```python
JwtPair client.get_user_token(user_id: str)
```

**GET** `/api/user/{userId}/token`

Get User Token (getUserToken)

Returns the token of the User based on the provided User Id. If the user who performs the request has the authority of 'SYS_ADMIN', it is possible to get the token of any tenant administrator. If the user who performs the request has the authority of 'TENANT_ADMIN', it is possible to get the token of any customer user that belongs to the same tenant. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**JwtPair**


## get_user_users

```python
PageDataUser client.get_user_users(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/user/users`

Get Users (getUsers)

Returns a page of user objects available for the current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUser**


## get_users_by_entity_group_id

```python
PageDataUser client.get_users_by_entity_group_id(entity_group_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/users`

Get users by Entity Group Id (getUsersByEntityGroupId)

Returns a page of user objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUser**


## get_users_by_ids

```python
List[User] client.get_users_by_ids(user_ids: List[str])
```

**GET** `/api/users/list`

Get Users By Ids (getUsersByIds)

Requested users must be owned by tenant or assigned to customer which user is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_ids** | **List[str]** | A list of user ids, separated by comma ',' | |

### Return type

**List[User]**


## get_users_for_assign

```python
PageDataUserEmailInfo client.get_users_for_assign(alarm_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/users/assign/{alarmId}`

Get usersForAssign (getUsersForAssign)

Returns page of user data objects that can be assigned to provided alarmId. Search is been executed by email, firstName and lastName fields. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the user email. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, firstName, lastName, email] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataUserEmailInfo**


## is_user_token_access_enabled

```python
bool client.is_user_token_access_enabled()
```

**GET** `/api/user/tokenAccessEnabled`

Check Token Access Enabled (isUserTokenAccessEnabled)

Checks that the system is configured to allow administrators to impersonate themself as other users. If the user who performs the request has the authority of 'SYS_ADMIN', it is possible to login as any tenant administrator. If the user who performs the request has the authority of 'TENANT_ADMIN', it is possible to login as any customer user.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).

### Return type

**bool**


## put_general_user_settings

```python
None client.put_general_user_settings(body: object)
```

**PUT** `/api/user/settings/general`

Update user settings (putGeneralUserSettings)

Update user settings for authorized user. Only specified json elements will be updated.Example: you have such settings: {A:5, B:{C:10, D:20}}. Updating it with {B:{C:10, D:30}} will result in{A:5, B:{C:10, D:30}}. The same could be achieved by putting {B.D:30}


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

None (empty response body)


## put_user_settings

```python
None client.put_user_settings(type: str, body: object)
```

**PUT** `/api/user/settings/{type}`

Update user settings (putUserSettings)

Update user settings for authorized user. Only specified json elements will be updated.Example: you have such settings: {A:5, B:{C:10, D:20}}. Updating it with {B:{C:10, D:30}} will result in{A:5, B:{C:10, D:30}}. The same could be achieved by putting {B.D:30}


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | Settings type, case insensitive, one of: \"general\", \"quick_links\", \"doc_links\" or \"dashboards\". | |
| **body** | **object** |  | |

### Return type

None (empty response body)


## remove_mobile_session

```python
None client.remove_mobile_session(x_mobile_token: str)
```

**DELETE** `/api/user/mobile/session`

removeMobileSession


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **x_mobile_token** | **str** |  | |

### Return type

None (empty response body)


## report_user_dashboard_action

```python
UserDashboardsInfo client.report_user_dashboard_action(dashboard_id: str, action: str)
```

**GET** `/api/user/dashboards/{dashboardId}/{action}`

Report action of User over the dashboard (reportUserDashboardAction)

Report action of User over the dashboard.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **action** | **str** | Dashboard action, one of: \"visit\", \"star\" or \"unstar\". | |

### Return type

**UserDashboardsInfo**


## save_mobile_session

```python
None client.save_mobile_session(x_mobile_token: str, mobile_session_info: MobileSessionInfo)
```

**POST** `/api/user/mobile/session`

saveMobileSession


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **x_mobile_token** | **str** |  | |
| **mobile_session_info** | **MobileSessionInfo** |  | |

### Return type

None (empty response body)


## save_user

```python
User client.save_user(user: User, send_activation_mail: Optional[str] = None, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)
```

**POST** `/api/user`

Save Or update User (saveUser)

Create or update the User. When creating user, platform generates User Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created User Id will be present in the response. Specify existing User Id to update the device. Referencing non-existing User Id will cause 'Not Found' error.  Device email is unique for entire platform setup.  Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new User entity. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user** | **User** |  | |
| **send_activation_mail** | **str** | Send activation email (or use activation link) | [optional] |
| **entity_group_id** | **str** |  | [optional] |
| **entity_group_ids** | **List[str]** | A list of entity group ids, separated by comma ',' | [optional] |

### Return type

**User**


## save_user_settings

```python
object client.save_user_settings(body: object)
```

**POST** `/api/user/settings`

Save user settings (saveUserSettings)

Save user settings represented in json format for authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

**object**


## send_activation_email

```python
None client.send_activation_email(email: str)
```

**POST** `/api/user/sendActivationMail`

Send or re-send the activation email

Force send the activation email to the user. Useful to resend the email if user has accidentally deleted it.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **email** | **str** | Email of the user | |

### Return type

None (empty response body)


## set_user_credentials_enabled

```python
None client.set_user_credentials_enabled(user_id: str, user_credentials_enabled: Optional[str] = None)
```

**POST** `/api/user/{userId}/userCredentialsEnabled`

Enable/Disable User credentials (setUserCredentialsEnabled)

Enables or Disables user credentials. Useful when you would like to block user account without deleting it. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **user_credentials_enabled** | **str** | Enable (\"true\") or disable (\"false\") the credentials. | [optional] |

### Return type

None (empty response body)

