# DomainControllerApi

`ThingsboardClient` methods:

```python
None client.delete_domain(id: UUID)  # Delete Domain by ID (deleteDomain)
CloudDomainInfo client.get_cloud_domain_info_by_id(id: UUID)  # Get Domain info by Id (getCloudDomainInfoById)
DomainInfo client.get_domain_info_by_id(id: UUID)  # Get Domain info by Id (getDomainInfoById)
PageDataDomainInfo client.get_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Domain infos (getDomainInfos)
Domain client.save_domain(domain: Domain, oauth2_client_ids: Optional[List[str]] = None)  # Save or Update Domain (saveDomain)
None client.update_domain_oauth2_clients(id: UUID, request_body: List[UUID])  # Update oauth2 clients (updateDomainOauth2Clients)
```


## delete_domain

```python
None client.delete_domain(id: UUID)
```

**DELETE** `/api/domain/{id}`

Delete Domain by ID (deleteDomain)

Deletes Domain by ID. Referencing non-existing domain Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## get_cloud_domain_info_by_id

```python
CloudDomainInfo client.get_cloud_domain_info_by_id(id: UUID)
```

**GET** `/api/domain/cloud/info/{id}`

Get Domain info by Id (getCloudDomainInfoById)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**CloudDomainInfo**


## get_domain_info_by_id

```python
DomainInfo client.get_domain_info_by_id(id: UUID)
```

**GET** `/api/domain/info/{id}`

Get Domain info by Id (getDomainInfoById)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**DomainInfo**


## get_domain_infos

```python
PageDataDomainInfo client.get_domain_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/domain/infos`

Get Domain infos (getDomainInfos)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on domain's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataDomainInfo**


## save_domain

```python
Domain client.save_domain(domain: Domain, oauth2_client_ids: Optional[List[str]] = None)
```

**POST** `/api/domain`

Save or Update Domain (saveDomain)

Create or update the Domain. When creating domain, platform generates Domain Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Domain Id will be present in the response. Specify existing Domain Id to update the domain. Referencing non-existing Domain Id will cause 'Not Found' error.  Domain name is unique for entire platform setup.    Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **domain** | **Domain** |  | |
| **oauth2_client_ids** | **List[str]** | A list of oauth2 client registration ids, separated by comma ',' | [optional] |

### Return type

**Domain**


## update_domain_oauth2_clients

```python
None client.update_domain_oauth2_clients(id: UUID, request_body: List[UUID])
```

**PUT** `/api/domain/{id}/oauth2Clients`

Update oauth2 clients (updateDomainOauth2Clients)

Update oauth2 clients for the specified domain.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |
| **request_body** | **List[UUID]** |  | |

### Return type

None (empty response body)

