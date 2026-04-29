# RpcV1ControllerApi

`ThingsboardClient` methods:

```python
str client.handle_one_way_device_rpc_request_v1(device_id: str, body: str)  # Send one-way RPC request (handleOneWayDeviceRPCRequestV1)
str client.handle_two_way_device_rpc_request_v1(device_id: str, body: str)  # Send two-way RPC request (handleTwoWayDeviceRPCRequestV1)
```


## handle_one_way_device_rpc_request_v1

```python
str client.handle_one_way_device_rpc_request_v1(device_id: str, body: str)
```

**POST** `/api/plugins/rpc/oneway/{deviceId}`

Send one-way RPC request (handleOneWayDeviceRPCRequestV1)

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** | A JSON object representing the RPC request. | |

### Return type

**str**


## handle_two_way_device_rpc_request_v1

```python
str client.handle_two_way_device_rpc_request_v1(device_id: str, body: str)
```

**POST** `/api/plugins/rpc/twoway/{deviceId}`

Send two-way RPC request (handleTwoWayDeviceRPCRequestV1)

Deprecated. See 'Rpc V 2 Controller' instead.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **device_id** | **str** | A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** | A JSON object representing the RPC request. | |

### Return type

**str**

