# OAuth2ControllerApi

`ThingsboardClient` methods:

```python
None client.delete_oauth2_client(id: UUID)  # Delete oauth2 client (deleteOauth2Client)
PageDataOAuth2ClientInfo client.find_o_auth2_client_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get OAuth2 Client infos (findOAuth2ClientInfos)
List[OAuth2ClientInfo] client.find_tenant_o_auth2_client_infos_by_ids(client_ids: List[str])  # Get OAuth2 Client infos By Ids (findTenantOAuth2ClientInfosByIds)
str client.get_login_processing_url()  # Get OAuth2 log in processing URL (getLoginProcessingUrl)
OAuth2Client client.get_o_auth2_client_by_id(id: UUID)  # Get OAuth2 Client by id (getOAuth2ClientById)
List[OAuth2ClientLoginInfo] client.get_o_auth2_clients(pkg_name: Optional[str] = None, platform: Optional[str] = None)  # Get OAuth2 clients (getOAuth2Clients)
OAuth2Client client.save_o_auth2_client(o_auth2_client: OAuth2Client)  # Save OAuth2 Client (saveOAuth2Client)
```


## delete_oauth2_client

```python
None client.delete_oauth2_client(id: UUID)
```

**DELETE** `/api/oauth2/client/{id}`

Delete oauth2 client (deleteOauth2Client)

Deletes the oauth2 client. Referencing non-existing oauth2 client Id will cause an error.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

None (empty response body)


## find_o_auth2_client_infos

```python
PageDataOAuth2ClientInfo client.find_o_auth2_client_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/oauth2/client/infos`

Get OAuth2 Client infos (findOAuth2ClientInfos)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on client's title | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataOAuth2ClientInfo**


## find_tenant_o_auth2_client_infos_by_ids

```python
List[OAuth2ClientInfo] client.find_tenant_o_auth2_client_infos_by_ids(client_ids: List[str])
```

**GET** `/api/oauth2/client/list`

Get OAuth2 Client infos By Ids (findTenantOAuth2ClientInfosByIds)

Fetch OAuth2 Client info objects based on the provided ids.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **client_ids** | **List[str]** | A list of oauth2 ids, separated by comma ',' | |

### Return type

**List[OAuth2ClientInfo]**


## get_login_processing_url

```python
str client.get_login_processing_url()
```

**GET** `/api/oauth2/loginProcessingUrl`

Get OAuth2 log in processing URL (getLoginProcessingUrl)

Returns the URL enclosed in double quotes. After successful authentication with OAuth2 provider, it makes a redirect to this path so that the platform can do further log in processing. This URL may be configured as 'security.oauth2.loginProcessingUrl' property in yml configuration file, or as 'SECURITY_OAUTH2_LOGIN_PROCESSING_URL' env variable. By default it is '/login/oauth2/code/'  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.

### Return type

**str**


## get_o_auth2_client_by_id

```python
OAuth2Client client.get_o_auth2_client_by_id(id: UUID)
```

**GET** `/api/oauth2/client/{id}`

Get OAuth2 Client by id (getOAuth2ClientById)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **UUID** |  | |

### Return type

**OAuth2Client**


## get_o_auth2_clients

```python
List[OAuth2ClientLoginInfo] client.get_o_auth2_clients(pkg_name: Optional[str] = None, platform: Optional[str] = None)
```

**POST** `/api/noauth/oauth2Clients`

Get OAuth2 clients (getOAuth2Clients)

Get the list of OAuth2 clients to log in with, available for such domain scheme (HTTP or HTTPS) (if x-forwarded-proto request header is present - the scheme is known from it) and domain name and port (port may be known from x-forwarded-port header)


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pkg_name** | **str** | Mobile application package name, to find OAuth2 clients where there is configured mobile application with such package name | [optional] |
| **platform** | **str** | Platform type to search OAuth2 clients for which the usage with this platform type is allowed in the settings. If platform type is not one of allowable values - it will just be ignored | [optional] [enum: WEB, ANDROID, IOS] |

### Return type

**List[OAuth2ClientLoginInfo]**


## save_o_auth2_client

```python
OAuth2Client client.save_o_auth2_client(o_auth2_client: OAuth2Client)
```

**POST** `/api/oauth2/client`

Save OAuth2 Client (saveOAuth2Client)

  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **o_auth2_client** | **OAuth2Client** |  | |

### Return type

**OAuth2Client**

