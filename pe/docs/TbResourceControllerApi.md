# TbResourceControllerApi

`ThingsboardClient` methods:

```python
TbResourceDeleteResult client.delete_resource(resource_id: str, force: Optional[bool] = None)  # Delete Resource (deleteResource)
bytearray client.download_jks_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)  # Download JKS Resource (downloadJksResourceIfChanged)
bytearray client.download_js_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)  # Download JS Resource (downloadJsResourceIfChanged)
bytearray client.download_lwm2m_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)  # Download LWM2M Resource (downloadLwm2mResourceIfChanged)
bytearray client.download_pkcs12_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)  # Download PKCS_12 Resource (downloadPkcs12ResourceIfChanged)
bytearray client.download_resource(resource_id: str)  # Download Resource (downloadResource)
bytearray client.download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: Optional[str] = None)  # Download resource (downloadResourceIfChanged)
List[LwM2mObject] client.get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids: List[str])  # Get LwM2M Objects (getLwm2mListObjects)
List[LwM2mObject] client.get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get LwM2M Objects (getLwm2mListObjectsPage)
TbResource client.get_resource_by_id(resource_id: str)  # Get Resource (getResourceById)
TbResourceInfo client.get_resource_info(resource_type: str, scope: str, key: str)  # Get resource info (getResourceInfo)
TbResourceInfo client.get_resource_info_by_id(resource_id: str)  # Get Resource Info (getResourceInfoById)
PageDataTbResourceInfo client.get_resources(page_size: int, page: int, resource_type: Optional[List[ResourceType]] = None, resource_sub_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Resource Infos (getResources)
List[TbResourceInfo] client.get_system_or_tenant_resources_by_ids(resource_ids: List[str])  # Get Resource Infos by ids (getSystemOrTenantResourcesByIds)
PageDataTbResourceInfo client.get_tenant_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get All Resource Infos (getTenantResources)
TbResourceInfo client.save_resource(tb_resource: TbResource)  # Create Or Update Resource (saveResource)
TbResourceInfo client.update_resource_data(id: UUID, file: bytearray)  # updateResourceData
TbResourceInfo client.update_resource_info(id: UUID, tb_resource_info: TbResourceInfo)  # updateResourceInfo
TbResourceInfo client.upload_resource(resource_type: str, file: bytearray, title: Optional[str] = None, descriptor: Optional[str] = None, resource_sub_type: Optional[str] = None)  # Upload Resource via Multipart File (uploadResource)
```


## delete_resource

```python
TbResourceDeleteResult client.delete_resource(resource_id: str, force: Optional[bool] = None)
```

**DELETE** `/api/resource/{resourceId}`

Delete Resource (deleteResource)

Deletes the Resource. Referencing non-existing Resource Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **force** | **bool** |  | [optional] |

### Return type

**TbResourceDeleteResult**


## download_jks_resource_if_changed

```python
bytearray client.download_jks_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)
```

**GET** `/api/resource/jks/{resourceId}/download`

Download JKS Resource (downloadJksResourceIfChanged)

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **if_none_match** | **str** |  | [optional] |

### Return type

**bytearray**


## download_js_resource_if_changed

```python
bytearray client.download_js_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)
```

**GET** `/api/resource/js/{resourceId}/download`

Download JS Resource (downloadJsResourceIfChanged)

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **if_none_match** | **str** |  | [optional] |

### Return type

**bytearray**


## download_lwm2m_resource_if_changed

```python
bytearray client.download_lwm2m_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)
```

**GET** `/api/resource/lwm2m/{resourceId}/download`

Download LWM2M Resource (downloadLwm2mResourceIfChanged)

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **if_none_match** | **str** |  | [optional] |

### Return type

**bytearray**


## download_pkcs12_resource_if_changed

```python
bytearray client.download_pkcs12_resource_if_changed(resource_id: str, if_none_match: Optional[str] = None)
```

**GET** `/api/resource/pkcs12/{resourceId}/download`

Download PKCS_12 Resource (downloadPkcs12ResourceIfChanged)

Download Resource based on the provided Resource Id or return 304 status code if resource was not changed.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **if_none_match** | **str** |  | [optional] |

### Return type

**bytearray**


## download_resource

```python
bytearray client.download_resource(resource_id: str)
```

**GET** `/api/resource/{resourceId}/download`

Download Resource (downloadResource)

Download Resource based on the provided Resource Id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bytearray**


## download_resource_if_changed

```python
bytearray client.download_resource_if_changed(resource_type: str, scope: str, key: str, if_none_match: Optional[str] = None)
```

**GET** `/api/resource/{resourceType}/{scope}/{key}`

Download resource (downloadResourceIfChanged)

Download resource with a given type and key for the given scope  Available for any authorized user. 


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str** | Type of the resource | [enum: lwm2m_model, jks, pkcs_12, js_module, dashboard] |
| **scope** | **str** | Scope of the resource | [enum: system, tenant] |
| **key** | **str** | Key of the resource, e.g. 'extension.js' | |
| **if_none_match** | **str** |  | [optional] |

### Return type

**bytearray**


## get_lwm2m_list_objects

```python
List[LwM2mObject] client.get_lwm2m_list_objects(sort_order: str, sort_property: str, object_ids: List[str])
```

**GET** `/api/resource/lwm2m`

Get LwM2M Objects (getLwm2mListObjects)

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [enum: ASC, DESC] |
| **sort_property** | **str** | Property of entity to sort by | [enum: id, name] |
| **object_ids** | **List[str]** | LwM2M Object ids. | |

### Return type

**List[LwM2mObject]**


## get_lwm2m_list_objects_page

```python
List[LwM2mObject] client.get_lwm2m_list_objects_page(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/resource/lwm2m/page`

Get LwM2M Objects (getLwm2mListObjectsPage)

Returns a page of LwM2M objects parsed from Resources with type 'LWM2M_MODEL' owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. LwM2M Object is a object that includes information about the LwM2M model which can be used in transport configuration for the LwM2M device profile.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the resource title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: id, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**List[LwM2mObject]**


## get_resource_by_id

```python
TbResource client.get_resource_by_id(resource_id: str)
```

**GET** `/api/resource/{resourceId}`

Get Resource (getResourceById)

Fetch the Resource object based on the provided Resource Id. Resource is a heavyweight object that includes main information about the Resource and also data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TbResource**


## get_resource_info

```python
TbResourceInfo client.get_resource_info(resource_type: str, scope: str, key: str)
```

**GET** `/api/resource/{resourceType}/{scope}/{key}/info`

Get resource info (getResourceInfo)

Get info for the resource with the given type, scope and key. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str** | Type of the resource | [enum: lwm2m_model, jks, pkcs_12, js_module, dashboard] |
| **scope** | **str** | Scope of the resource | [enum: system, tenant] |
| **key** | **str** | Key of the resource, e.g. 'extension.js' | |

### Return type

**TbResourceInfo**


## get_resource_info_by_id

```python
TbResourceInfo client.get_resource_info_by_id(resource_id: str)
```

**GET** `/api/resource/info/{resourceId}`

Get Resource Info (getResourceInfoById)

Fetch the Resource Info object based on the provided Resource Id. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_id** | **str** | A string value representing the resource id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**TbResourceInfo**


## get_resources

```python
PageDataTbResourceInfo client.get_resources(page_size: int, page: int, resource_type: Optional[List[ResourceType]] = None, resource_sub_type: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/resource`

Get Resource Infos (getResources)

Returns a page of Resource Info objects owned by tenant or sysadmin. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **resource_type** | **List[ResourceType]** | A list of resource types, separated by comma ','. | [optional] |
| **resource_sub_type** | **str** | A string value representing the resource sub-type. | [optional] [enum: EXTENSION, MODULE] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the resource title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, resourceType, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTbResourceInfo**


## get_system_or_tenant_resources_by_ids

```python
List[TbResourceInfo] client.get_system_or_tenant_resources_by_ids(resource_ids: List[str])
```

**GET** `/api/resource/list`

Get Resource Infos by ids (getSystemOrTenantResourcesByIds)


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_ids** | **List[str]** | A list of resource ids, separated by comma ',' | |

### Return type

**List[TbResourceInfo]**


## get_tenant_resources

```python
PageDataTbResourceInfo client.get_tenant_resources(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/resource/tenant`

Get All Resource Infos (getTenantResources)

Returns a page of Resource Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. Resource Info is a lightweight object that includes main information about the Resource excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the resource title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, title, resourceType, tenantId] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataTbResourceInfo**


## save_resource

```python
TbResourceInfo client.save_resource(tb_resource: TbResource)
```

**POST** `/api/resource`

Create Or Update Resource (saveResource)

Create or update the Resource. When creating the Resource, platform generates Resource id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Resource id will be present in the response. Specify existing Resource id to update the Resource. Referencing non-existing Resource Id will cause 'Not Found' error.   Resource combination of the title with the key is unique in the scope of tenant. Remove 'id', 'tenantId' from the request body example (below) to create new Resource entity.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **tb_resource** | **TbResource** |  | |

### Return type

**TbResourceInfo**


## update_resource_data

```python
TbResourceInfo client.update_resource_data(id: UUID, file: bytearray)
```

**PUT** `/api/resource/{id}/data`

updateResourceData


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | Unique identifier of the Resource to update | |
| **file** | **bytearray** | Resource file. | |

### Return type

**TbResourceInfo**


## update_resource_info

```python
TbResourceInfo client.update_resource_info(id: UUID, tb_resource_info: TbResourceInfo)
```

**PUT** `/api/resource/{id}/info`

updateResourceInfo


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** | Unique identifier of the Resource to update | |
| **tb_resource_info** | **TbResourceInfo** |  | |

### Return type

**TbResourceInfo**


## upload_resource

```python
TbResourceInfo client.upload_resource(resource_type: str, file: bytearray, title: Optional[str] = None, descriptor: Optional[str] = None, resource_sub_type: Optional[str] = None)
```

**POST** `/api/resource/upload`

Upload Resource via Multipart File (uploadResource)

Create the Resource using multipart file upload.   Resource combination of the title with the key is unique in the scope of tenant.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resource_type** | **str** | Resource type. | |
| **file** | **bytearray** | Resource file. | |
| **title** | **str** | Resource title. | [optional] |
| **descriptor** | **str** | Resource descriptor (JSON). | [optional] |
| **resource_sub_type** | **str** | Resource sub type. | [optional] |

### Return type

**TbResourceInfo**

