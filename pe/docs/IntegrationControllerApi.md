# IntegrationControllerApi

`ThingsboardClient` methods:

```python
Integration client.assign_integration_to_edge(edge_id: str, integration_id: str)  # Assign integration to edge (assignIntegrationToEdge)
None client.check_integration_connection(integration: Integration)  # Check integration connectivity (checkIntegrationConnection)
None client.delete_integration(integration_id: str)  # Delete integration (deleteIntegration)
bytearray client.export_integration_package(integration_id: str)  # Export integration as IoT Hub package
str client.find_all_related_edges_missing_attributes(integration_id: str)  # Find missing attributes for all related edges (findAllRelatedEdgesMissingAttributes)
str client.find_edge_missing_attributes(edge_id: str, integration_ids: List[str])  # Find edge missing attributes for assigned integrations (findEdgeMissingAttributes)
PageDataIntegrationInfo client.get_edge_integration_infos(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Integrations (getEdgeIntegrationInfos)
PageDataIntegration client.get_edge_integrations(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Integrations (getEdgeIntegrations)
Integration client.get_integration_by_id(integration_id: str)  # Get Integration (getIntegrationById)
Integration client.get_integration_by_routing_key(routing_key: str)  # Get Integration by Routing Key (getIntegrationByRoutingKey)
PageDataIntegrationInfo client.get_integration_infos(page_size: str, page: str, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Integration Infos (getIntegrationInfos)
PageDataIntegration client.get_integrations(page_size: str, page: str, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Integrations (getIntegrations)
List[Integration] client.get_integrations_by_ids(integration_ids: List[str])  # Get Integrations By Ids (getIntegrationsByIds)
Dict[str, IntegrationConvertersInfo] client.get_integrations_converters_info()  # Get Integrations Converters info (getIntegrationsConvertersInfo)
Integration client.save_integration(integration: Integration)  # Create Or Update Integration (saveIntegration)
Integration client.unassign_integration_from_edge(edge_id: str, integration_id: str)  # Unassign integration from edge (unassignIntegrationFromEdge)
```


## assign_integration_to_edge

```python
Integration client.assign_integration_to_edge(edge_id: str, integration_id: str)
```

**POST** `/api/edge/{edgeId}/integration/{integrationId}`

Assign integration to edge (assignIntegrationToEdge)

Creates assignment of an existing integration edge template to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment integration (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once integration will be delivered to edge service, it's going to start locally.   Only integration edge template can be assigned to edge.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **integration_id** | **str** |  | |

### Return type

**Integration**


## check_integration_connection

```python
None client.check_integration_connection(integration: Integration)
```

**POST** `/api/integration/check`

Check integration connectivity (checkIntegrationConnection)

Checks if the connection to the integration is established. Throws an error if the connection is not established. Example: Failed to connect to MQTT broker at host:port.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration** | **Integration** |  | |

### Return type

None (empty response body)


## delete_integration

```python
None client.delete_integration(integration_id: str)
```

**DELETE** `/api/integration/{integrationId}`

Delete integration (deleteIntegration)

Deletes the integration and all the relations (from and to the integration). Referencing non-existing integration Id will cause an error.    Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str** | A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## export_integration_package

```python
bytearray client.export_integration_package(integration_id: str)
```

**GET** `/api/integration/{integrationId}/export-package`

Export integration as IoT Hub package

Returns a ZIP containing integration.json, uplink.json, optional downlink.json, and form.json. Sensitive fields are tokenized via @TemplateField annotations on the integration's runtime POJO.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str** |  | |

### Return type

**bytearray**


## find_all_related_edges_missing_attributes

```python
str client.find_all_related_edges_missing_attributes(integration_id: str)
```

**GET** `/api/edge/integration/{integrationId}/allMissingAttributes`

Find missing attributes for all related edges (findAllRelatedEdgesMissingAttributes)

Returns list of attribute names of all related edges that are missing in the integration configuration.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str** | A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**


## find_edge_missing_attributes

```python
str client.find_edge_missing_attributes(edge_id: str, integration_ids: List[str])
```

**GET** `/api/edge/integration/{edgeId}/missingAttributes`

Find edge missing attributes for assigned integrations (findEdgeMissingAttributes)

Returns list of edge attribute names that are missing in assigned integrations.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **integration_ids** | **List[str]** | A list of assigned integration ids, separated by comma ',' | |

### Return type

**str**


## get_edge_integration_infos

```python
PageDataIntegrationInfo client.get_edge_integration_infos(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edge/{edgeId}/integrationInfos`

Get Edge Integrations (getEdgeIntegrationInfos)

Returns a page of Integrations assigned to the specified edge. The integration object contains information about the Integration, including the heavyweight configuration object. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the integration name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, debugMode, allowCreateDevicesOrAssets, enabled, remote, routingKey, secret] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataIntegrationInfo**


## get_edge_integrations

```python
PageDataIntegration client.get_edge_integrations(edge_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edge/{edgeId}/integrations`

Get Edge Integrations (getEdgeIntegrations)

Returns a page of Integrations assigned to the specified edge. The integration object contains information about the Integration, including the heavyweight configuration object. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the integration name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, debugMode, allowCreateDevicesOrAssets, enabled, remote, routingKey, secret] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataIntegration**


## get_integration_by_id

```python
Integration client.get_integration_by_id(integration_id: str)
```

**GET** `/api/integration/{integrationId}`

Get Integration (getIntegrationById)

Fetch the Integration object based on the provided Integration Id. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_id** | **str** | A string value representing the integration id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Integration**


## get_integration_by_routing_key

```python
Integration client.get_integration_by_routing_key(routing_key: str)
```

**GET** `/api/integration/routingKey/{routingKey}`

Get Integration by Routing Key (getIntegrationByRoutingKey)

Fetch the Integration object based on the provided routing key. The server checks that the integration is owned by the same tenant.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **routing_key** | **str** | A string value representing the integration routing key. For example, '542047e6-c1b2-112e-a87e-e49247c09d4b' | |

### Return type

**Integration**


## get_integration_infos

```python
PageDataIntegrationInfo client.get_integration_infos(page_size: str, page: str, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/integrationInfos`

Get Integration Infos (getIntegrationInfos)

Returns a page of integration infos owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **is_edge_template** | **bool** | Fetch edge template integrations | [optional] [default to False] |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the integration name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, debugMode, allowCreateDevicesOrAssets, enabled, remote, routingKey, secret] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataIntegrationInfo**


## get_integrations

```python
PageDataIntegration client.get_integrations(page_size: str, page: str, is_edge_template: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/integrations`

Get Integrations (getIntegrations)

Returns a page of integrations owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **is_edge_template** | **bool** | Fetch edge template integrations | [optional] [default to False] |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the integration name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name, type, debugMode, allowCreateDevicesOrAssets, enabled, remote, routingKey, secret] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataIntegration**


## get_integrations_by_ids

```python
List[Integration] client.get_integrations_by_ids(integration_ids: List[str])
```

**GET** `/api/integrations/list`

Get Integrations By Ids (getIntegrationsByIds)

Requested integrations must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration_ids** | **List[str]** | A list of integration ids, separated by comma ',' | |

### Return type

**List[Integration]**


## get_integrations_converters_info

```python
Dict[str, IntegrationConvertersInfo] client.get_integrations_converters_info()
```

**GET** `/api/integrations/converters/info`

Get Integrations Converters info (getIntegrationsConvertersInfo)

Returns a JSON object containing information about existing tenant converters and converters available in library.   Available for users with 'TENANT_ADMIN' authority.

### Return type

**Dict[str, IntegrationConvertersInfo]**


## save_integration

```python
Integration client.save_integration(integration: Integration)
```

**POST** `/api/integration`

Create Or Update Integration (saveIntegration)

Create or update the Integration. When creating integration, platform generates Integration Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created integration id will be present in the response. Specify existing Integration id to update the integration. Referencing non-existing integration Id will cause 'Not Found' error. Integration configuration is validated for each type of the integration before it can be created.   # Integration Configuration  Integration configuration (**'configuration'** field) is the JSON object representing the special configuration per integration type with the connectivity fields and other important parameters dependent on the specific integration type. Let's review the configuration object for the MQTT Integration type below.   ```json {    \"clientConfiguration\":{       \"host\":\"broker.hivemq.com\",       \"port\":1883,       \"cleanSession\":false,       \"ssl\":false,       \"connectTimeoutSec\":10,       \"clientId\":\"\",       \"maxBytesInMessage\":32368,       \"credentials\":{          \"type\":\"anonymous\"       }    },    \"downlinkTopicPattern\":\"${topic}\",    \"topicFilters\":[       {          \"filter\":\"tb/mqtt-integration-tutorial/sensors/+/temperature\",          \"qos\":0       }    ],    \"metadata\":{    } } ```  Remove 'id', 'tenantId' from the request body example (below) to create new Integration entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **integration** | **Integration** |  | |

### Return type

**Integration**


## unassign_integration_from_edge

```python
Integration client.unassign_integration_from_edge(edge_id: str, integration_id: str)
```

**DELETE** `/api/edge/{edgeId}/integration/{integrationId}`

Unassign integration from edge (unassignIntegrationFromEdge)

Clears assignment of the integration to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove integration (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove integration locally.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** |  | |
| **integration_id** | **str** |  | |

### Return type

**Integration**

