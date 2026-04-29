# OtaPackageControllerApi

`ThingsboardClient` methods:

```python
None client.delete_ota_package(ota_package_id: str)  # Delete OTA Package (deleteOtaPackage)
bytearray client.download_ota_package(ota_package_id: str)  # Download OTA Package (downloadOtaPackage)
PageDataOtaPackageInfo client.get_group_ota_packages(group_id: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get group OTA Package Infos (getGroupOtaPackages)
OtaPackage client.get_ota_package_by_id(ota_package_id: str)  # Get OTA Package (getOtaPackageById)
OtaPackageInfo client.get_ota_package_info_by_id(ota_package_id: str)  # Get OTA Package Info (getOtaPackageInfoById)
PageDataOtaPackageInfo client.get_ota_packages(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get OTA Package Infos (getOtaPackages)
PageDataOtaPackageInfo client.get_ota_packages_by_device_profile_and_type(device_profile_id: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get OTA Package Infos by Device Profile and Type (getOtaPackagesByDeviceProfileAndType)
OtaPackageInfo client.save_ota_package_data(ota_package_id: str, checksum_algorithm: str, file: bytearray, checksum: Optional[str] = None)  # Save OTA Package data (saveOtaPackageData)
OtaPackageInfo client.save_ota_package_info(save_ota_package_info_request: SaveOtaPackageInfoRequest)  # Create Or Update OTA Package Info (saveOtaPackageInfo)
```


## delete_ota_package

```python
None client.delete_ota_package(ota_package_id: str)
```

**DELETE** `/api/otaPackage/{otaPackageId}`

Delete OTA Package (deleteOtaPackage)

Deletes the OTA Package. Referencing non-existing OTA Package Id will cause an error. Can't delete the OTA Package if it is referenced by existing devices or device profile.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ota_package_id** | **str** | A string value representing the ota package id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## download_ota_package

```python
bytearray client.download_ota_package(ota_package_id: str)
```

**GET** `/api/otaPackage/{otaPackageId}/download`

Download OTA Package (downloadOtaPackage)

Download OTA Package based on the provided OTA Package Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ota_package_id** | **str** | A string value representing the ota package id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bytearray**


## get_group_ota_packages

```python
PageDataOtaPackageInfo client.get_group_ota_packages(group_id: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/otaPackages/group/{groupId}/{type}`

Get group OTA Package Infos (getGroupOtaPackages)

Returns a page of OTA Package Info objects owned by tenant, and by entity group. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **group_id** | **str** | A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **type** | **str** | OTA Package type. | [enum: FIRMWARE, SOFTWARE] |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the ota package title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, type, title, version, tag, url, fileName, dataSize, checksum] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataOtaPackageInfo**


## get_ota_package_by_id

```python
OtaPackage client.get_ota_package_by_id(ota_package_id: str)
```

**GET** `/api/otaPackage/{otaPackageId}`

Get OTA Package (getOtaPackageById)

Fetch the OTA Package object based on the provided OTA Package Id. The server checks that the OTA Package is owned by the same tenant. OTA Package is a heavyweight object that includes main information about the OTA Package and also data.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ota_package_id** | **str** | A string value representing the ota package id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**OtaPackage**


## get_ota_package_info_by_id

```python
OtaPackageInfo client.get_ota_package_info_by_id(ota_package_id: str)
```

**GET** `/api/otaPackage/info/{otaPackageId}`

Get OTA Package Info (getOtaPackageInfoById)

Fetch the OTA Package Info object based on the provided OTA Package Id. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ota_package_id** | **str** | A string value representing the ota package id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**OtaPackageInfo**


## get_ota_packages

```python
PageDataOtaPackageInfo client.get_ota_packages(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/otaPackages`

Get OTA Package Infos (getOtaPackages)

Returns a page of OTA Package Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the ota package title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, type, title, version, tag, url, fileName, dataSize, checksum] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataOtaPackageInfo**


## get_ota_packages_by_device_profile_and_type

```python
PageDataOtaPackageInfo client.get_ota_packages_by_device_profile_and_type(device_profile_id: str, type: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/otaPackages/{deviceProfileId}/{type}`

Get OTA Package Infos by Device Profile and Type (getOtaPackagesByDeviceProfileAndType)

Returns a page of OTA Package Info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details. OTA Package Info is a lightweight object that includes main information about the OTA Package excluding the heavyweight data.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_profile_id** | **str** | A string value representing the device profile id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **type** | **str** | OTA Package type. | [enum: FIRMWARE, SOFTWARE] |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the ota package title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, type, title, version, tag, url, fileName, dataSize, checksum] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataOtaPackageInfo**


## save_ota_package_data

```python
OtaPackageInfo client.save_ota_package_data(ota_package_id: str, checksum_algorithm: str, file: bytearray, checksum: Optional[str] = None)
```

**POST** `/api/otaPackage/{otaPackageId}`

Save OTA Package data (saveOtaPackageData)

Update the OTA Package. Adds the date to the existing OTA Package Info  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ota_package_id** | **str** | A string value representing the ota package id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **checksum_algorithm** | **str** | OTA Package checksum algorithm. | [enum: MD5, SHA256, SHA384, SHA512, CRC32, MURMUR3_32, MURMUR3_128] |
| **file** | **bytearray** | OTA Package data. | |
| **checksum** | **str** | OTA Package checksum. For example, '0xd87f7e0c' | [optional] |

### Return type

**OtaPackageInfo**


## save_ota_package_info

```python
OtaPackageInfo client.save_ota_package_info(save_ota_package_info_request: SaveOtaPackageInfoRequest)
```

**POST** `/api/otaPackage`

Create Or Update OTA Package Info (saveOtaPackageInfo)

Create or update the OTA Package Info. When creating OTA Package Info, platform generates OTA Package id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created OTA Package id will be present in the response. Specify existing OTA Package id to update the OTA Package Info. Referencing non-existing OTA Package Id will cause 'Not Found' error.   OTA Package combination of the title with the version is unique in the scope of tenant.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **save_ota_package_info_request** | **SaveOtaPackageInfoRequest** |  | |

### Return type

**OtaPackageInfo**

