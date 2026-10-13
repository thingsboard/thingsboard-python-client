# CustomerControllerApi

`ThingsboardClient` methods:

```python
None client.delete_customer(customer_id: str)  # Delete Customer (deleteCustomer)
PageDataCustomerInfo client.get_all_customer_infos(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Customer Infos for current user (getAllCustomerInfos)
Customer client.get_customer_by_id(customer_id: str)  # Get Customer (getCustomerById)
PageDataCustomerInfo client.get_customer_customer_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer sub-customers Infos (getCustomerCustomerInfos)
CustomerInfo client.get_customer_info_by_id(customer_id: str)  # Get Customer info (getCustomerInfoById)
str client.get_customer_title_by_id(customer_id: str)  # Get Customer Title (getCustomerTitleById)
PageDataCustomer client.get_customers(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Customers (getCustomers)
PageDataCustomer client.get_customers_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get customers by Entity Group Id (getCustomersByEntityGroupId)
List[Customer] client.get_customers_by_ids(customer_ids: List[str])  # Get customers by Customer Ids (getCustomersByIds)
object client.get_short_customer_info_by_id(customer_id: str)  # Get short Customer info (getShortCustomerInfoById)
Customer client.get_tenant_customer(customer_title: str)  # Get Tenant Customer by Customer title (getTenantCustomer)
PageDataCustomer client.get_user_customers(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customers (getUserCustomers)
Customer client.save_customer(customer: Customer, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)  # Create or update Customer (saveCustomer)
```


## delete_customer

```python
None client.delete_customer(customer_id: str)
```

**DELETE** `/api/customer/{customerId}`

Delete Customer (deleteCustomer)

Deletes the Customer and all customer Users. All assigned Dashboards, Assets, Devices, etc. will be unassigned but not deleted. Referencing non-existing Customer Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_all_customer_infos

```python
PageDataCustomerInfo client.get_all_customer_infos(page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customerInfos/all`

Get All Customer Infos for current user (getAllCustomerInfos)

Returns a page of customer info objects owned by the tenant or the customer of a current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, city] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomerInfo**


## get_customer_by_id

```python
Customer client.get_customer_by_id(customer_id: str)
```

**GET** `/api/customer/{customerId}`

Get Customer (getCustomerById)

Get the Customer object based on the provided Customer Id. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Customer**


## get_customer_customer_infos

```python
PageDataCustomerInfo client.get_customer_customer_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/customerInfos`

Get Customer sub-customers Infos (getCustomerCustomerInfos)

Returns a page of customer info objects owned by the specified customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, city] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomerInfo**


## get_customer_info_by_id

```python
CustomerInfo client.get_customer_info_by_id(customer_id: str)
```

**GET** `/api/customer/info/{customerId}`

Get Customer info (getCustomerInfoById)

Get the Customer info object based on the provided Customer Id. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**CustomerInfo**


## get_customer_title_by_id

```python
str client.get_customer_title_by_id(customer_id: str)
```

**GET** `/api/customer/{customerId}/title`

Get Customer Title (getCustomerTitleById)

Get the title of the customer. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**


## get_customers

```python
PageDataCustomer client.get_customers(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customers`

Get Tenant Customers (getCustomers)

Returns a page of customers owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, city] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomer**


## get_customers_by_entity_group_id

```python
PageDataCustomer client.get_customers_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/customers`

Get customers by Entity Group Id (getCustomersByEntityGroupId)

Returns a page of Customer objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, city] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomer**


## get_customers_by_ids

```python
List[Customer] client.get_customers_by_ids(customer_ids: List[str])
```

**GET** `/api/customers/list`

Get customers by Customer Ids (getCustomersByIds)

Returns a list of Customer objects based on the provided ids.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_ids** | **List[str]** | A list of customer ids, separated by comma ',' | |

### Return type

**List[Customer]**


## get_short_customer_info_by_id

```python
object client.get_short_customer_info_by_id(customer_id: str)
```

**GET** `/api/customer/{customerId}/shortInfo`

Get short Customer info (getShortCustomerInfoById)

Get the short customer object that contains only the title and 'isPublic' flag. If the user has the authority of 'Tenant Administrator', the server checks that the customer is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the user belongs to the customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**object**


## get_tenant_customer

```python
Customer client.get_tenant_customer(customer_title: str)
```

**GET** `/api/tenant/customers`

Get Tenant Customer by Customer title (getTenantCustomer)

Get the Customer using Customer Title.   Available for users with 'TENANT_ADMIN' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_title** | **str** | A string value representing the Customer title. | |

### Return type

**Customer**


## get_user_customers

```python
PageDataCustomer client.get_user_customers(page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/user/customers`

Get Customers (getUserCustomers)

Returns a page of customers available for the user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, email, country, city] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataCustomer**


## save_customer

```python
Customer client.save_customer(customer: Customer, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)
```

**POST** `/api/customer`

Create or update Customer (saveCustomer)

Creates or Updates the Customer. When creating customer, platform generates Customer Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Customer Id will be present in the response. Specify existing Customer Id to update the Customer. Referencing non-existing Customer Id will cause 'Not Found' error.Remove 'id', 'tenantId' from the request body example (below) to create new Customer entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer** | **Customer** | A JSON value representing the customer. | |
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'. If specified, the entity will be added to the corresponding entity group. | [optional] |
| **entity_group_ids** | **List[str]** | A list of string values, separated by comma ',' representing the Entity Group Ids. For example, '784f394c-42b6-435a-983c-b7beff2784f9','a84f394c-42b6-435a-083c-b7beff2784f9'. If specified, the entity will be added to the corresponding entity groups. | [optional] |
| **name_conflict_policy** | **NameConflictPolicy** | Optional value of name conflict policy. Possible values: FAIL or UNIQUIFY.  If omitted, FAIL policy is applied. FAIL policy implies exception will be thrown if an entity with the same name already exists.  UNIQUIFY policy appends a suffix to the entity name, if a name conflict occurs. | [optional] [enum: FAIL, UNIQUIFY] |
| **uniquify_separator** | **str** | Optional value of name suffix separator used by UNIQUIFY policy. By default, underscore separator is used. For example, strategy is UNIQUIFY, separator is '-'; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-7fsh4f'. | [optional] [default to &#39;_&#39;] |
| **uniquify_strategy** | **UniquifyStrategy** | Optional value of uniquify strategy used by UNIQUIFY policy. Possible values: RANDOM or INCREMENTAL. By default, RANDOM strategy is used, which means random alphanumeric string will be added as a suffix to entity name. INCREMENTAL implies the first possible number starting from 1 will be added as a name suffix. For example, strategy is UNIQUIFY, uniquify strategy is INCREMENTAL; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-1. | [optional] [enum: RANDOM, INCREMENTAL] |

### Return type

**Customer**

