# AssetControllerApi

`ThingsboardClient` methods:

```python
None client.delete_asset(asset_id: str)  # Delete asset (deleteAsset)
List[Asset] client.find_assets_by_query(asset_search_query: AssetSearchQuery)  # Find related assets (findAssetsByQuery)
PageDataAssetInfo client.get_all_asset_infos(page_size: int, page: int, include_customers: Optional[bool] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Asset Infos for current user (getAllAssetInfos)
Asset client.get_asset_by_id(asset_id: str)  # Get Asset (getAssetById)
AssetInfo client.get_asset_info_by_id(asset_id: str)  # Get Asset Info (getAssetInfoById)
List[EntitySubtype] client.get_asset_types()  # Get Asset Types (getAssetTypes)
PageDataAsset client.get_assets_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get assets by Entity Group Id (getAssetsByEntityGroupId)
List[Asset] client.get_assets_by_ids(asset_ids: List[str])  # Get Assets By Ids (getAssetsByIds)
PageDataAssetInfo client.get_customer_asset_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Asset Infos (getCustomerAssetInfos)
PageDataAsset client.get_customer_assets(customer_id: str, page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Assets (getCustomerAssets)
Asset client.get_tenant_asset_by_name(asset_name: str)  # Get Tenant Asset (getTenantAssetByName)
PageDataAsset client.get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Assets (getTenantAssets)
PageDataAsset client.get_user_assets(page_size: str, page: str, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Assets (getUserAssets)
BulkImportResultAsset client.process_asset_bulk_import(bulk_import_request: BulkImportRequest)  # Import the bulk of assets (processAssetsBulkImport)
Asset client.save_asset(asset: Asset, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)  # Create Or Update Asset (saveAsset)
```


## delete_asset

```python
None client.delete_asset(asset_id: str)
```

**DELETE** `/api/asset/{assetId}`

Delete asset (deleteAsset)

Deletes the asset and all the relations (from and to the asset). Referencing non-existing asset Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


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

Returns all assets that are related to the specific entity. The entity id, relation type, asset types, depth of the search, and other query parameters defined using complex 'AssetSearchQuery' object. See 'Model' tab of the Parameters for more info.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_search_query** | **AssetSearchQuery** |  | |

### Return type

**List[Asset]**


## get_all_asset_infos

```python
PageDataAssetInfo client.get_all_asset_infos(page_size: int, page: int, include_customers: Optional[bool] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/assetInfos/all`

Get All Asset Infos for current user (getAllAssetInfos)

Returns a page of asset info objects owned by the tenant or the customer of a current user. Asset Info is an extension of the default Asset object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAssetInfo**


## get_asset_by_id

```python
Asset client.get_asset_by_id(asset_id: str)
```

**GET** `/api/asset/{assetId}`

Get Asset (getAssetById)

Fetch the Asset object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


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

Fetch the Asset Info object based on the provided Asset Id. If the user has the authority of 'Tenant Administrator', the server checks that the asset is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the asset is assigned to the same customer.Asset Info is an extension of the default Asset object that contains information about the owner name.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


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


## get_assets_by_entity_group_id

```python
PageDataAsset client.get_assets_by_entity_group_id(entity_group_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/entityGroup/{entityGroupId}/assets`

Get assets by Entity Group Id (getAssetsByEntityGroupId)

Returns a page of asset objects that belongs to specified Entity Group Id. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for specified group.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the asset name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, label, customerTitle] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAsset**


## get_assets_by_ids

```python
List[Asset] client.get_assets_by_ids(asset_ids: List[str])
```

**GET** `/api/assets`

Get Assets By Ids (getAssetsByIds)

Requested assets must be owned by tenant or assigned to customer which user is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_ids** | **List[str]** | A list of asset ids, separated by comma ',' | |

### Return type

**List[Asset]**


## get_customer_asset_infos

```python
PageDataAssetInfo client.get_customer_asset_infos(customer_id: str, page_size: int, page: int, include_customers: Optional[bool] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/assetInfos`

Get Customer Asset Infos (getCustomerAssetInfos)

Returns a page of asset info objects owned by the specified customer. Asset Info is an extension of the default Asset object that contains information about the owner name.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
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

Returns a page of assets objects owned by customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


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


## get_tenant_asset_by_name

```python
Asset client.get_tenant_asset_by_name(asset_name: str)
```

**GET** `/api/tenant/asset`

Get Tenant Asset (getTenantAssetByName)

Requested asset must be owned by tenant that the user belongs to. Asset name is an unique property of asset. So it can be used to identify the asset.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset_name** | **str** | A string value representing the Asset name. | |

### Return type

**Asset**


## get_tenant_assets

```python
PageDataAsset client.get_tenant_assets(page_size: int, page: int, type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/assets`

Get Tenant Assets (getTenantAssets)

Returns a page of assets owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


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


## get_user_assets

```python
PageDataAsset client.get_user_assets(page_size: str, page: str, type: Optional[str] = None, asset_profile_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/user/assets`

Get Assets (getUserAssets)

Returns a page of assets objects available for the current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Asset Info is an extension of the default Asset object that contains information about the owner name.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **type** | **str** | Asset type | [optional] |
| **asset_profile_id** | **str** | A string value representing the asset profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
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

Import the bulk of assets (processAssetsBulkImport)

There's an ability to import the bulk of assets using the only .csv file.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_import_request** | **BulkImportRequest** |  | |

### Return type

**BulkImportResultAsset**


## save_asset

```python
Asset client.save_asset(asset: Asset, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None, name_conflict_policy: Optional[NameConflictPolicy] = None, uniquify_separator: Optional[str] = None, uniquify_strategy: Optional[UniquifyStrategy] = None)
```

**POST** `/api/asset`

Create Or Update Asset (saveAsset)

Creates or Updates the Asset. When creating asset, platform generates Asset Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Asset id will be present in the response. Specify existing Asset id to update the asset. Referencing non-existing Asset Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Asset entity.    Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **asset** | **Asset** | A JSON value representing the asset. | |
| **entity_group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9'. If specified, the entity will be added to the corresponding entity group. | [optional] |
| **entity_group_ids** | **List[str]** | A list of string values, separated by comma ',' representing the Entity Group Ids. For example, '784f394c-42b6-435a-983c-b7beff2784f9','a84f394c-42b6-435a-083c-b7beff2784f9'. If specified, the entity will be added to the corresponding entity groups. | [optional] |
| **name_conflict_policy** | **NameConflictPolicy** | Optional value of name conflict policy. Possible values: FAIL or UNIQUIFY.  If omitted, FAIL policy is applied. FAIL policy implies exception will be thrown if an entity with the same name already exists.  UNIQUIFY policy appends a suffix to the entity name, if a name conflict occurs. | [optional] [enum: FAIL, UNIQUIFY] |
| **uniquify_separator** | **str** | Optional value of name suffix separator used by UNIQUIFY policy. By default, underscore separator is used. For example, strategy is UNIQUIFY, separator is '-'; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-7fsh4f'. | [optional] [default to &#39;_&#39;] |
| **uniquify_strategy** | **UniquifyStrategy** | Optional value of uniquify strategy used by UNIQUIFY policy. Possible values: RANDOM or INCREMENTAL. By default, RANDOM strategy is used, which means random alphanumeric string will be added as a suffix to entity name. INCREMENTAL implies the first possible number starting from 1 will be added as a name suffix. For example, strategy is UNIQUIFY, uniquify strategy is INCREMENTAL; if a name conflict occurs for entity name 'test-name', created entity will have name like 'test-name-1. | [optional] [enum: RANDOM, INCREMENTAL] |

### Return type

**Asset**

