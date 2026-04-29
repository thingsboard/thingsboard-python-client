# AssetControllerApi

`ThingsboardClient` methods:

```python
Asset client.assign_asset_to_customer(customer_id: str, asset_id: str)  # Assign asset to customer (assignAssetToCustomer)
Asset client.assign_asset_to_edge(edge_id: str, asset_id: str)  # Assign asset to edge (assignAssetToEdge)
Asset client.assign_asset_to_public_customer(asset_id: str)  # Make asset publicly available (assignAssetToPublicCustomer)
None client.delete_asset(asset_id: str)  # Delete asset (deleteAsset)
List[Asset] client.find_assets_by_query(asset_search_query: AssetSearchQuery)  # Find related assets (findAssetsByQuery)
Asset client.get_asset_by_id(asset_id: str)  # Get Asset (getAssetById)
AssetInfo client.get_asset_info_by_id(asset_id: str)  # Get Asset Info (getAssetInfoById)
List[EntitySubtype] client.get_asset_types()  # Get Asset Types (getAssetTypes)
List[Asset] client.get_assets_by_ids(asset_ids: List[str])  # Get Assets By Ids (getAssetsByIds)
PageDataAssetInfo client.get_customer_asset_infos(customer_id: str, page_size: int, page: int, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Asset Infos (getCustomerAssetInfos)
PageDataAsset client.get_customer_assets(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Assets (getCustomerAssets)
PageDataAsset client.get_edge_assets(edge_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # Get assets assigned to edge (getEdgeAssets)
Asset client.get_tenant_asset_by_name(asset_name: str)  # Get Tenant Asset (getTenantAssetByName)
PageDataAssetInfo client.get_tenant_asset_infos(page_size: int, page: int, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Asset Infos (getTenantAssetInfos)
PageDataAsset client.get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Assets (getTenantAssets)
BulkImportResultAsset client.process_asset_bulk_import(bulk_import_request: BulkImportRequest)  # Import the bulk of assets (processAssetBulkImport)
Asset client.save_asset(asset: Asset, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)  # Create Or Update Asset (saveAsset)
Asset client.unassign_asset_from_customer(asset_id: str)  # Unassign asset from customer (unassignAssetFromCustomer)
Asset client.unassign_asset_from_edge(edge_id: str, asset_id: str)  # Unassign asset from edge (unassignAssetFromEdge)
```


## assign_asset_to_customer

```python
Asset client.assign_asset_to_customer(customer_id: str, asset_id: str)
```

**POST** `/api/customer/{customerId}/asset/{assetId}`

Assign asset to customer (assignAssetToCustomer)

Creates assignment of the asset to customer. Customer will be able to query asset afterwards.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**


## assign_asset_to_edge

```python
Asset client.assign_asset_to_edge(edge_id: str, asset_id: str)
```

**POST** `/api/edge/{edgeId}/asset/{assetId}`

Assign asset to edge (assignAssetToEdge)

Creates assignment of an existing asset to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment asset (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once asset will be delivered to edge service, it's going to be available for usage on remote edge instance.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**


## assign_asset_to_public_customer

```python
Asset client.assign_asset_to_public_customer(asset_id: str)
```

**POST** `/api/customer/public/asset/{assetId}`

Make asset publicly available (assignAssetToPublicCustomer)

Asset will be available for non-authorized (not logged-in) users. This is useful to create dashboards that you plan to share/embed on a publicly available website. However, users that are logged-in and belong to different tenant will not be able to access the asset.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**


## delete_asset

```python
None client.delete_asset(asset_id: str)
```

**DELETE** `/api/asset/{assetId}`

Delete asset (deleteAsset)

Deletes the asset and all the relations (from and to the asset). Referencing non-existing asset Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## find_assets_by_query

```python
List[Asset] client.find_assets_by_query(asset_search_query: AssetSearchQuery)
```

**POST** `/api/assets`

Find related assets (findAssetsByQuery)

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_search_query** | **AssetSearchQuery** |  | |

### Return type

**List[Asset]**


## get_asset_by_id

```python
Asset client.get_asset_by_id(asset_id: str)
```

**GET** `/api/asset/{assetId}`

Get Asset (getAssetById)

Fetch the Asset object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**


## get_asset_info_by_id

```python
AssetInfo client.get_asset_info_by_id(asset_id: str)
```

**GET** `/api/asset/info/{assetId}`

Get Asset Info (getAssetInfoById)

Fetch the Asset Info object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer. Asset Info is an extension of the default Asset object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AssetInfo**


## get_asset_types

```python
List[EntitySubtype] client.get_asset_types()
```

**GET** `/api/asset/types`

Get Asset Types (getAssetTypes)

Deprecated. See 'getAssetProfileNames' API from Asset Profile Controller instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.

### Return type

**List[EntitySubtype]**


## get_assets_by_ids

```python
List[Asset] client.get_assets_by_ids(asset_ids: List[str])
```

**GET** `/api/assets`

Get Assets By Ids (getAssetsByIds)

Requested assets must be owned by tenant or assigned to customer which user is performing the request. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_ids** | **List[str]** | A list of assets ids, separated by comma ',' | |

### Return type

**List[Asset]**


## get_customer_asset_infos

```python
PageDataAssetInfo client.get_customer_asset_infos(customer_id: str, page_size: int, page: int, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/assetInfos`

Get Customer Asset Infos (getCustomerAssetInfos)

Returns a page of assets info objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Asset Info is an extension of the default Asset object that contains information about the assigned customer name. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAssetInfo**


## get_customer_assets

```python
PageDataAsset client.get_customer_assets(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/assets`

Get Customer Assets (getCustomerAssets)

Returns a page of assets objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAsset**


## get_edge_assets

```python
PageDataAsset client.get_edge_assets(edge_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/edge/{edgeId}/assets`

Get assets assigned to edge (getEdgeAssets)

Returns a page of assets assigned to edge. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | Timestamp. Assets with creation time before it won't be queried | [optional] |
| **end_time** | **int** | Timestamp. Assets with creation time after it won't be queried | [optional] |

### Return type

**PageDataAsset**


## get_tenant_asset_by_name

```python
Asset client.get_tenant_asset_by_name(asset_name: str)
```

**GET** `/api/tenant/asset`

Get Tenant Asset (getTenantAssetByName)

Requested asset must be owned by tenant that the user belongs to. Asset name is an unique property of asset. So it can be used to identify the asset.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_name** | **str** | A string value representing the Asset name. | |

### Return type

**Asset**


## get_tenant_asset_infos

```python
PageDataAssetInfo client.get_tenant_asset_infos(page_size: int, page: int, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/assetInfos`

Get Tenant Asset Infos (getTenantAssetInfos)

Returns a page of assets info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Asset Info is an extension of the default Asset object that contains information about the assigned customer name.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAssetInfo**


## get_tenant_assets

```python
PageDataAsset client.get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/assets`

Get Tenant Assets (getTenantAssets)

Returns a page of assets owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAsset**


## process_asset_bulk_import

```python
BulkImportResultAsset client.process_asset_bulk_import(bulk_import_request: BulkImportRequest)
```

**POST** `/api/asset/bulk_import`

Import the bulk of assets (processAssetBulkImport)

There's an ability to import the bulk of assets using the only .csv file.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_import_request** | **BulkImportRequest** |  | |

### Return type

**BulkImportResultAsset**


## save_asset

```python
Asset client.save_asset(asset: Asset, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)
```

**POST** `/api/asset`

Create Or Update Asset (saveAsset)

Creates or Updates the Asset. When creating asset, platform generates Asset Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Asset id will be present in the response. Specify existing Asset id to update the asset. Referencing non-existing Asset Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Asset entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset** | **Asset** | A JSON value representing the asset. | |
| **name_conflict_policy** | **NameConflictPolicy** | Optional value of name conflict policy. Possible values: FAIL or UNIQUIFY.  If omitted, FAIL policy is applied. FAIL policy implies exception will be thrown if an entity with the same name already exists.  UNIQUIFY policy appends a suffix to the entity name, if a name conflict occurs. | [optional] [enum: FAIL, UNIQUIFY] |
| **uniquify_separator** | **str** | Optional value of name suffix separator used by UNIQUIFY policy. By default, underscore separator is used. For example, strategy is UNIQUIFY, separator is '-'; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-7fsh4f'. | [optional] [default to &#39;_&#39;] |
| **uniquify_strategy** | **UniquifyStrategy** | Optional value of uniquify strategy used by UNIQUIFY policy. Possible values: RANDOM or INCREMENTAL. By default, RANDOM strategy is used, which means random alphanumeric string will be added as a suffix to entity name. INCREMENTAL implies the first possible number starting from 1 will be added as a name suffix. For example, strategy is UNIQUIFY, uniquify strategy is INCREMENTAL; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-1. | [optional] [enum: RANDOM, INCREMENTAL] |

### Return type

**Asset**


## unassign_asset_from_customer

```python
Asset client.unassign_asset_from_customer(asset_id: str)
```

**DELETE** `/api/customer/asset/{assetId}`

Unassign asset from customer (unassignAssetFromCustomer)

Clears assignment of the asset to customer. Customer will not be able to query asset afterwards.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**


## unassign_asset_from_edge

```python
Asset client.unassign_asset_from_edge(edge_id: str, asset_id: str)
```

**DELETE** `/api/edge/{edgeId}/asset/{assetId}`

Unassign asset from edge (unassignAssetFromEdge)

Clears assignment of the asset to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove asset (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove asset locally.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **asset_id** | **str** | A string value representing the asset id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Asset**

