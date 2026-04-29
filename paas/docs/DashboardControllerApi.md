# DashboardControllerApi

`ThingsboardClient` methods:

```python
None client.delete_dashboard(dashboard_id: str)  # Delete the Dashboard (deleteDashboard)
List[Dashboard] client.export_group_dashboards(entity_group_id: str, limit: int, accept_encoding: Optional[str] = None)  # Export Dashboards (exportGroupDashboards)
PageDataDashboardInfo client.get_all_dashboards(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Dashboards for current user (getAllDashboards)
PageDataDashboardInfo client.get_customer_dashboards(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Dashboards (getCustomerDashboards)
HomeDashboardInfo client.get_customer_home_dashboard_info()  # Get Customer Home Dashboard Info (getCustomerHomeDashboardInfo)
Dashboard client.get_dashboard_by_id(dashboard_id: str, include_resources: Optional[bool] = None, accept_encoding: Optional[str] = None)  # Get Dashboard (getDashboardById)
DashboardInfo client.get_dashboard_info_by_id(dashboard_id: str)  # Get Dashboard Info (getDashboardInfoById)
PageDataDashboardInfo client.get_dashboards_by_entity_group_id(entity_group_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get dashboards by Entity Group Id (getDashboardsByEntityGroupId)
List[DashboardInfo] client.get_dashboards_by_ids(dashboard_ids: List[str])  # Get dashboards by Dashboard Ids (getDashboardsByIds)
HomeDashboard client.get_home_dashboard(accept_encoding: Optional[str] = None)  # Get Home Dashboard (getHomeDashboard)
HomeDashboardInfo client.get_home_dashboard_info()  # Get Home Dashboard Info (getHomeDashboardInfo)
int client.get_max_datapoints_limit()  # Get max data points limit (getMaxDatapointsLimit)
int client.get_server_time()  # Get server time (getServerTime)
PageDataDashboardInfo client.get_tenant_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Dashboards (getTenantDashboards)
PageDataDashboardInfo client.get_tenant_dashboards_by_tenant_id(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Dashboards by System Administrator (getTenantDashboardsByTenantId)
HomeDashboardInfo client.get_tenant_home_dashboard_info()  # Get Tenant Home Dashboard Info (getTenantHomeDashboardInfo)
PageDataDashboardInfo client.get_user_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, operation: Optional[str] = None, user_id: Optional[str] = None)  # Get Dashboards (getUserDashboards)
None client.import_group_dashboards(entity_group_id: str, dashboard: List[Dashboard], overwrite: Optional[bool] = None)  # Import Dashboards (importGroupDashboards)
Dashboard client.save_dashboard(dashboard: Dashboard, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, accept_encoding: Optional[str] = None)  # Create Or Update Dashboard (saveDashboard)
None client.set_customer_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)  # Update Customer Home Dashboard Info (setCustomerHomeDashboardInfo)
None client.set_tenant_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)  # Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)
```


## delete_dashboard

```python
None client.delete_dashboard(dashboard_id: str)
```

**DELETE** `/api/dashboard/{dashboardId}`

Delete the Dashboard (deleteDashboard)

Delete the Dashboard. Only users with 'TENANT_ADMIN') authority may delete the dashboards.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## export_group_dashboards

```python
List[Dashboard] client.export_group_dashboards(entity_group_id: str, limit: int, accept_encoding: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/dashboards/export`

Export Dashboards (exportGroupDashboards)

Export the dashboards that belong to specified group id.The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **limit** | **int** | Limit of the entities to export | |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**List[Dashboard]**


## get_all_dashboards

```python
PageDataDashboardInfo client.get_all_dashboards(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/dashboards/all`

Get All Dashboards for current user (getAllDashboards)

Returns a page of dashboard info objects owned by the tenant or the customer of a current user. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_customer_dashboards

```python
PageDataDashboardInfo client.get_customer_dashboards(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/dashboards`

Get Customer Dashboards (getCustomerDashboards)

Returns a page of dashboard info objects owned by the specified customer. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_customer_home_dashboard_info

```python
HomeDashboardInfo client.get_customer_home_dashboard_info()
```

**GET** `/api/customer/dashboard/home/info`

Get Customer Home Dashboard Info (getCustomerHomeDashboardInfo)

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the corresponding customer.   Available for users with 'CUSTOMER_USER' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.

### Return type

**HomeDashboardInfo**


## get_dashboard_by_id

```python
Dashboard client.get_dashboard_by_id(dashboard_id: str, include_resources: Optional[bool] = None, accept_encoding: Optional[str] = None)
```

**GET** `/api/dashboard/{dashboardId}`

Get Dashboard (getDashboardById)

Get the dashboard based on 'dashboardId' parameter. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **include_resources** | **bool** | Export used resources and replace resource links with resource metadata | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**Dashboard**


## get_dashboard_info_by_id

```python
DashboardInfo client.get_dashboard_info_by_id(dashboard_id: str)
```

**GET** `/api/dashboard/info/{dashboardId}`

Get Dashboard Info (getDashboardInfoById)

Get the information about the dashboard based on 'dashboardId' parameter. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_id** | **str** | A string value representing the dashboard id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**DashboardInfo**


## get_dashboards_by_entity_group_id

```python
PageDataDashboardInfo client.get_dashboards_by_entity_group_id(entity_group_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/dashboards`

Get dashboards by Entity Group Id (getDashboardsByEntityGroupId)

Returns a page of Dashboard objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_dashboards_by_ids

```python
List[DashboardInfo] client.get_dashboards_by_ids(dashboard_ids: List[str])
```

**GET** `/api/dashboards`

Get dashboards by Dashboard Ids (getDashboardsByIds)

Returns a list of DashboardInfo objects based on the provided ids. Filters the list based on the user permissions.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard_ids** | **List[str]** | A list of dashboard ids, separated by comma ',' | |

### Return type

**List[DashboardInfo]**


## get_home_dashboard

```python
HomeDashboard client.get_home_dashboard(accept_encoding: Optional[str] = None)
```

**GET** `/api/dashboard/home`

Get Home Dashboard (getHomeDashboard)

Returns the home dashboard object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user. The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accept_encoding** | **str** |  | [optional] |

### Return type

**HomeDashboard**


## get_home_dashboard_info

```python
HomeDashboardInfo client.get_home_dashboard_info()
```

**GET** `/api/dashboard/home/info`

Get Home Dashboard Info (getHomeDashboardInfo)

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the User. If 'homeDashboardId' parameter is not set on the User level and the User has authority 'CUSTOMER_USER', check the same parameter for the corresponding Customer. If 'homeDashboardId' parameter is not set on the User and Customer levels then checks the same parameter for the Tenant that owns the user.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**HomeDashboardInfo**


## get_max_datapoints_limit

```python
int client.get_max_datapoints_limit()
```

**GET** `/api/dashboard/maxDatapointsLimit`

Get max data points limit (getMaxDatapointsLimit)

Get the maximum number of data points that dashboard may request from the server per in a single subscription command. This value impacts the time window behavior. It impacts 'Max values' parameter in case user selects 'None' as 'Data aggregation function'. It also impacts the 'Grouping interval' in case of any other 'Data aggregation function' is selected. The actual value of the limit is configurable in the system configuration file.

### Return type

**int**


## get_server_time

```python
int client.get_server_time()
```

**GET** `/api/dashboard/serverTime`

Get server time (getServerTime)

Get the server time (milliseconds since January 1, 1970 UTC). Used to adjust view of the dashboards according to the difference between browser and server time.

### Return type

**int**


## get_tenant_dashboards

```python
PageDataDashboardInfo client.get_tenant_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/dashboards`

Get Tenant Dashboards (getTenantDashboards)

Returns a page of dashboard info objects owned by the tenant of a current user. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **mobile** | **bool** | Exclude dashboards that are hidden for mobile | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_tenant_dashboards_by_tenant_id

```python
PageDataDashboardInfo client.get_tenant_dashboards_by_tenant_id(tenant_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/{tenantId}/dashboards`

Get Tenant Dashboards by System Administrator (getTenantDashboardsByTenantId)

Returns a page of dashboard info objects owned by tenant. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'SYS_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tenant_id** | **str** | A string value representing the tenant id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataDashboardInfo**


## get_tenant_home_dashboard_info

```python
HomeDashboardInfo client.get_tenant_home_dashboard_info()
```

**GET** `/api/tenant/dashboard/home/info`

Get Tenant Home Dashboard Info (getTenantHomeDashboardInfo)

Returns the home dashboard info object that is configured as 'homeDashboardId' parameter in the 'additionalInfo' of the corresponding tenant.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'READ' permission for the white labeling resource.

### Return type

**HomeDashboardInfo**


## get_user_dashboards

```python
PageDataDashboardInfo client.get_user_dashboards(page_size: int, page: int, mobile: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, operation: Optional[str] = None, user_id: Optional[str] = None)
```

**GET** `/api/user/dashboards`

Get Dashboards (getUserDashboards)

Returns a page of Dashboard Info objects available for specified or current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. The Dashboard Info object contains lightweight information about the dashboard (e.g. title, image, assigned customers) but does not contain the heavyweight configuration JSON.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **mobile** | **bool** | Exclude dashboards that are hidden for mobile | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the dashboard title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **operation** | **str** | Filter by allowed operations for the current user | [optional] |
| **user_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**PageDataDashboardInfo**


## import_group_dashboards

```python
None client.import_group_dashboards(entity_group_id: str, dashboard: List[Dashboard], overwrite: Optional[bool] = None)
```

**POST** `/api/entityGroup/{entityGroupId}/dashboards/import`

Import Dashboards (importGroupDashboards)

Import the dashboards to specified group.The Dashboard object is a heavyweight object that contains information about the dashboard (e.g. title, image, assigned customers) and also configuration JSON (e.g. layouts, widgets, entity aliases).  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **dashboard** | **List[Dashboard]** |  | |
| **overwrite** | **bool** | Overwrite dashboards with the same name | [optional] [default to False] |

### Return type

None (empty response body)


## save_dashboard

```python
Dashboard client.save_dashboard(dashboard: Dashboard, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, accept_encoding: Optional[str] = None)
```

**POST** `/api/dashboard`

Create Or Update Dashboard (saveDashboard)

Create or update the Dashboard. When creating dashboard, platform generates Dashboard Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Dashboard id will be present in the response. Specify existing Dashboard id to update the dashboard. Referencing non-existing dashboard Id will cause 'Not Found' error. Only users with 'TENANT_ADMIN') authority may create the dashboards.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Dashboard entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dashboard** | **Dashboard** | A JSON value representing the dashboard. | |
| **entity_group_id** | **str** |  | [optional] |
| **entity_group_ids** | **List[str]** | A list of entity group ids, separated by comma ',' | [optional] |
| **accept_encoding** | **str** |  | [optional] |

### Return type

**Dashboard**


## set_customer_home_dashboard_info

```python
None client.set_customer_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)
```

**POST** `/api/customer/dashboard/home/info`

Update Customer Home Dashboard Info (setCustomerHomeDashboardInfo)

Update the home dashboard assignment for the current customer.   Available for users with 'CUSTOMER_USER' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **home_dashboard_info** | **HomeDashboardInfo** |  | |

### Return type

None (empty response body)


## set_tenant_home_dashboard_info

```python
None client.set_tenant_home_dashboard_info(home_dashboard_info: HomeDashboardInfo)
```

**POST** `/api/tenant/dashboard/home/info`

Update Tenant Home Dashboard Info (getTenantHomeDashboardInfo)

Update the home dashboard assignment for the current tenant.   Available for users with 'TENANT_ADMIN' authority.  Security check is performed to verify that the user has 'WRITE' permission for the white labeling resource.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **home_dashboard_info** | **HomeDashboardInfo** |  | |

### Return type

None (empty response body)

