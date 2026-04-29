# RpcV2ControllerApi

`ThingsboardClient` methods:

```python
None client.delete_rpc(rpc_id: str)  # Delete persistent RPC
Rpc client.get_persisted_rpc(rpc_id: str)  # Get persistent RPC request
str client.get_persisted_rpc_by_device(device_id: str, page_size: int, page: int, rpc_status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get persistent RPC requests
str client.handle_one_way_device_rpc_request_v2(device_id: str, body: str)  # Send one-way RPC request (handleOneWayDeviceRPCRequestV2)
str client.handle_two_way_device_rpc_request_v2(device_id: str, body: str)  # Send two-way RPC request (handleTwoWayDeviceRPCRequestV2)
```


## delete_rpc

```python
None client.delete_rpc(rpc_id: str)
```

**DELETE** `/api/rpc/persistent/{rpcId}`

Delete persistent RPC

Deletes the persistent RPC request.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rpc_id** | **str** | A string value representing the rpc id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_persisted_rpc

```python
Rpc client.get_persisted_rpc(rpc_id: str)
```

**GET** `/api/rpc/persistent/{rpcId}`

Get persistent RPC request

Get information about the status of the RPC call.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rpc_id** | **str** | A string value representing the rpc id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Rpc**


## get_persisted_rpc_by_device

```python
str client.get_persisted_rpc_by_device(device_id: str, page_size: int, page: int, rpc_status: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/rpc/persistent/device/{deviceId}`

Get persistent RPC requests

Allows to query RPC calls for specific device using pagination.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **rpc_status** | **str** | Status of the RPC | [optional] [enum: QUEUED, SENT, DELIVERED, SUCCESSFUL, TIMEOUT, EXPIRED, FAILED] |
| **text_search** | **str** | Not implemented. Leave empty. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, expirationTime, request, response] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**str**


## handle_one_way_device_rpc_request_v2

```python
str client.handle_one_way_device_rpc_request_v2(device_id: str, body: str)
```

**POST** `/api/rpc/oneway/{deviceId}`

Send one-way RPC request (handleOneWayDeviceRPCRequestV2)

Sends the one-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   \"method\": \"setGpio\",   \"params\": {     \"pin\": 7,     \"value\": 1   },   \"persistent\": false,   \"timeout\": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, \"getCurrentTime\" or \"getWeatherForecast\". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON \"{}\" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is \"false\". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is either 200 OK if the message was sent to device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** | A JSON object representing the RPC request. | |

### Return type

**str**


## handle_two_way_device_rpc_request_v2

```python
str client.handle_two_way_device_rpc_request_v2(device_id: str, body: str)
```

**POST** `/api/rpc/twoway/{deviceId}`

Send two-way RPC request (handleTwoWayDeviceRPCRequestV2)

Sends the two-way remote-procedure call (RPC) request to device. Sends the one-way remote-procedure call (RPC) request to device. The RPC call is A JSON that contains the method name ('method'), parameters ('params') and multiple optional fields. See example below. We will review the properties of the RPC call one-by-one below.   ```json {   \"method\": \"setGpio\",   \"params\": {     \"pin\": 7,     \"value\": 1   },   \"persistent\": false,   \"timeout\": 5000 } ```  ### Server-side RPC structure  The body of server-side RPC request consists of multiple fields:  * **method** - mandatory, name of the method to distinct the RPC calls.   For example, \"getCurrentTime\" or \"getWeatherForecast\". The value of the parameter is a string. * **params** - mandatory, parameters used for processing of the request. The value is a JSON. Leave empty JSON \"{}\" if no parameters needed. * **timeout** - optional, value of the processing timeout in milliseconds. The default value is 10000 (10 seconds). The minimum value is 5000 (5 seconds). * **expirationTime** - optional, value of the epoch time (in milliseconds, UTC timezone). Overrides **timeout** if present. * **persistent** - optional, indicates persistent RPC. The default value is \"false\". * **retries** - optional, defines how many times persistent RPC will be re-sent in case of failures on the network and/or device side. * **additionalInfo** - optional, defines metadata for the persistent RPC that will be added to the persistent RPC events.  ### RPC Result In case of persistent RPC, the result of this call is 'rpcId' UUID. In case of lightweight RPC, the result of this call is the response from device, or 504 Gateway Timeout if device is offline.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** | A JSON object representing the RPC request. | |

### Return type

**str**

