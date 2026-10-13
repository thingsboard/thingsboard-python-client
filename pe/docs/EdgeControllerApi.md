# EdgeControllerApi

`ThingsboardClient` methods:

```python
object client.activate_instance(license_secret: str, release_date: str)  # Activate edge instance (activateInstance)
object client.check_instance(body: object)  # Check edge license (checkInstance)
None client.delete_edge(edge_id: str)  # Delete edge (deleteEdge)
List[Edge] client.find_edges_by_query(edge_search_query: EdgeSearchQuery)  # Find related edges (findEdgesByQuery)
str client.find_missing_to_related_rule_chains(edge_id: str)  # Find missing rule chains (findMissingToRelatedRuleChains)
PageDataEdgeInfo client.get_all_edge_infos(page_size: int, page: int, include_customers: Optional[bool] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Edge Infos for current user (getAllEdgeInfos)
PageDataEdgeInfo client.get_customer_edge_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Edge Infos (getCustomerEdgeInfos)
PageDataEdge client.get_customer_edges(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Edges (getCustomerEdges)
Edge client.get_edge_by_id(edge_id: str)  # Get Edge (getEdgeById)
EdgeInfo client.get_edge_info_by_id(edge_id: str)  # Get Edge Info (getEdgeInfoById)
EdgeInstructions client.get_edge_install_instructions(edge_id: str, method: str)  # Get Edge Install Instructions (getEdgeInstallInstructions)
List[Edge] client.get_edge_list(edge_ids: List[str])  # Get Edges By Ids (getEdgeList)
List[EntitySubtype] client.get_edge_types()  # Get Edge Types (getEdgeTypes)
EdgeInstructions client.get_edge_upgrade_instructions(edge_version: str, method: str)  # Get Edge Upgrade Instructions (getEdgeUpgradeInstructions)
PageDataEdge client.get_edges(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Edges (getEdges)
PageDataEdge client.get_edges_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get edges by Entity Group Id (getEdgesByEntityGroupId)
Edge client.get_tenant_edge_by_name(edge_name: str)  # Get Tenant Edge by name (getTenantEdgeByName)
PageDataEdge client.get_tenant_edges(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Edges (getTenantEdges)
PageDataEdge client.get_user_edges(page_size: str, page: str, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edges (getUserEdges)
bool client.is_edge_upgrade_available(edge_id: str)  # Is edge upgrade enabled (isEdgeUpgradeAvailable)
bool client.is_edges_support_enabled()  # Is edges support enabled (isEdgesSupportEnabled)
BulkImportResultEdge client.process_edges_bulk_import(bulk_import_request: BulkImportRequest)  # Import the bulk of edges (processEdgesBulkImport)
Edge client.save_edge(edge: Edge, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)  # Create Or Update Edge (saveEdge)
Edge client.set_edge_root_rule_chain(edge_id: str, rule_chain_id: str)  # Set root rule chain for provided edge (setEdgeRootRuleChain)
str client.sync_edge(edge_id: str)  # Sync edge (syncEdge)
```


## activate_instance

```python
object client.activate_instance(license_secret: str, release_date: str)
```

**POST** `/api/license/activateInstance`

Activate edge instance (activateInstance)

Activates edge license on license portal.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **license_secret** | **str** |  | |
| **release_date** | **str** |  | |

### Return type

**object**


## check_instance

```python
object client.check_instance(body: object)
```

**POST** `/api/license/checkInstance`

Check edge license (checkInstance)

Checks license request from edge service by forwarding request to license portal.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** |  | |

### Return type

**object**


## delete_edge

```python
None client.delete_edge(edge_id: str)
```

**DELETE** `/api/edge/{edgeId}`

Delete edge (deleteEdge)

Deletes the edge. Referencing non-existing edge Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## find_edges_by_query

```python
List[Edge] client.find_edges_by_query(edge_search_query: EdgeSearchQuery)
```

**POST** `/api/edges`

Find related edges (findEdgesByQuery)

Returns all edges that are related to the specific entity. The entity id, relation type, edge types, depth of the search, and other query parameters defined using complex 'EdgeSearchQuery' object. See 'Model' tab of the Parameters for more info.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_search_query** | **EdgeSearchQuery** |  | |

### Return type

**List[Edge]**


## find_missing_to_related_rule_chains

```python
str client.find_missing_to_related_rule_chains(edge_id: str)
```

**GET** `/api/edge/missingToRelatedRuleChains/{edgeId}`

Find missing rule chains (findMissingToRelatedRuleChains)

Returns list of rule chains ids that are not assigned to particular edge, but these rule chains are present in the already assigned rule chains to edge.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**


## get_all_edge_infos

```python
PageDataEdgeInfo client.get_all_edge_infos(page_size: int, page: int, include_customers: Optional[bool] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edgeInfos/all`

Get All Edge Infos for current user (getAllEdgeInfos)

Returns a page of edge info objects owned by the tenant or the customer of a current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **type** | **str** | A string value representing the edge type. For example, 'default' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdgeInfo**


## get_customer_edge_infos

```python
PageDataEdgeInfo client.get_customer_edge_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/edgeInfos`

Get Customer Edge Infos (getCustomerEdgeInfos)

Returns a page of edge info objects owned by the specified customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **type** | **str** | A string value representing the edge type. For example, 'default' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdgeInfo**


## get_customer_edges

```python
PageDataEdge client.get_customer_edges(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/edges`

Get Customer Edges (getCustomerEdges)

Returns a page of edges objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | A string value representing the edge type. For example, 'default' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdge**


## get_edge_by_id

```python
Edge client.get_edge_by_id(edge_id: str)
```

**GET** `/api/edge/{edgeId}`

Get Edge (getEdgeById)

Get the Edge object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Edge**


## get_edge_info_by_id

```python
EdgeInfo client.get_edge_info_by_id(edge_id: str)
```

**GET** `/api/edge/info/{edgeId}`

Get Edge Info (getEdgeInfoById)

Get the Edge info object based on the provided Edge Id. If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**EdgeInfo**


## get_edge_install_instructions

```python
EdgeInstructions client.get_edge_install_instructions(edge_id: str, method: str)
```

**GET** `/api/edge/instructions/install/{edgeId}/{method}`

Get Edge Install Instructions (getEdgeInstallInstructions)

Get an install instructions for provided edge id.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **method** | **str** | Installation method ('docker', 'ubuntu' or 'centos') | [enum: docker, ubuntu, centos] |

### Return type

**EdgeInstructions**


## get_edge_list

```python
List[Edge] client.get_edge_list(edge_ids: List[str])
```

**GET** `/api/edges/list`

Get Edges By Ids (getEdgeList)

Requested edges must be owned by tenant or assigned to customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_ids** | **List[str]** | A list of edges ids, separated by comma ',' | |

### Return type

**List[Edge]**


## get_edge_types

```python
List[EntitySubtype] client.get_edge_types()
```

**GET** `/api/edge/types`

Get Edge Types (getEdgeTypes)

Returns a set of unique edge types based on edges that are either owned by the tenant or assigned to the customer which user is performing the request.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**List[EntitySubtype]**


## get_edge_upgrade_instructions

```python
EdgeInstructions client.get_edge_upgrade_instructions(edge_version: str, method: str)
```

**GET** `/api/edge/instructions/upgrade/{edgeVersion}/{method}`

Get Edge Upgrade Instructions (getEdgeUpgradeInstructions)

Get an upgrade instructions for provided edge version.If the user has the authority of 'Tenant Administrator', the server checks that the edge is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the edge is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_version** | **str** | Edge version | |
| **method** | **str** | Upgrade method ('docker', 'ubuntu' or 'centos') | [enum: docker, ubuntu, centos] |

### Return type

**EdgeInstructions**


## get_edges

```python
PageDataEdge client.get_edges(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edges`

Get Tenant Edges (getEdges)

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdge**


## get_edges_by_entity_group_id

```python
PageDataEdge client.get_edges_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/edges`

Get edges by Entity Group Id (getEdgesByEntityGroupId)

Returns a page of Edge objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdge**


## get_tenant_edge_by_name

```python
Edge client.get_tenant_edge_by_name(edge_name: str)
```

**GET** `/api/tenant/edge`

Get Tenant Edge by name (getTenantEdgeByName)

Requested edge must be owned by tenant or customer that the user belongs to. Edge name is an unique property of edge. So it can be used to identify the edge.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_name** | **str** | Unique name of the edge | |

### Return type

**Edge**


## get_tenant_edges

```python
PageDataEdge client.get_tenant_edges(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/edges`

Get Tenant Edges (getTenantEdges)

Returns a page of edges owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | A string value representing the edge type. For example, 'default' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdge**


## get_user_edges

```python
PageDataEdge client.get_user_edges(page_size: str, page: str, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/user/edges`

Get Edges (getUserEdges)

Returns a page of edges available for current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **type** | **str** | A string value representing the edge type. For example, 'default' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the edge name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEdge**


## is_edge_upgrade_available

```python
bool client.is_edge_upgrade_available(edge_id: str)
```

**GET** `/api/edge/{edgeId}/upgrade/available`

Is edge upgrade enabled (isEdgeUpgradeAvailable)

Returns 'true' if upgrade available for connected edge, 'false' - otherwise.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bool**


## is_edges_support_enabled

```python
bool client.is_edges_support_enabled()
```

**GET** `/api/edges/enabled`

Is edges support enabled (isEdgesSupportEnabled)

Returns 'true' if edges support enabled on server, 'false' - otherwise.

### Return type

**bool**


## process_edges_bulk_import

```python
BulkImportResultEdge client.process_edges_bulk_import(bulk_import_request: BulkImportRequest)
```

**POST** `/api/edge/bulk_import`

Import the bulk of edges (processEdgesBulkImport)

There's an ability to import the bulk of edges using the only .csv file.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_import_request** | **BulkImportRequest** |  | |

### Return type

**BulkImportResultEdge**


## save_edge

```python
Edge client.save_edge(edge: Edge, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)
```

**POST** `/api/edge`

Create Or Update Edge (saveEdge)

Create or update the Edge. When creating edge, platform generates Edge Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created edge id will be present in the response. Specify existing Edge id to update the edge. Referencing non-existing Edge Id will cause 'Not Found' error.  Edge name is unique in the scope of tenant. Use unique identifiers like MAC or IMEI for the edge names and non-unique 'label' field for user-friendly visualization purposes.Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Edge entity. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge** | **Edge** |  | |
| **entity_group_id** | **str** |  | [optional] |
| **entity_group_ids** | **List[str]** | A list of entity group ids, separated by comma ',' | [optional] |

### Return type

**Edge**


## set_edge_root_rule_chain

```python
Edge client.set_edge_root_rule_chain(edge_id: str, rule_chain_id: str)
```

**POST** `/api/edge/{edgeId}/{ruleChainId}/root`

Set root rule chain for provided edge (setEdgeRootRuleChain)

Change root rule chain of the edge to the new provided rule chain.  This operation will send a notification to update root rule chain on remote edge service.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **rule_chain_id** | **str** | A string value representing the rule chain id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Edge**


## sync_edge

```python
str client.sync_edge(edge_id: str)
```

**POST** `/api/edge/sync/{edgeId}`

Sync edge (syncEdge)

Starts synchronization process between edge and cloud.  All entities that are assigned to particular edge are going to be send to remote edge service.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**

