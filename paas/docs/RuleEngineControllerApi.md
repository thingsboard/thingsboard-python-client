# RuleEngineControllerApi

`ThingsboardClient` methods:

```python
str client.handle_rule_engine_request_for_entity(entity_type: str, entity_id: str, body: str)  # Push entity message to the rule engine (handleRuleEngineRequestForEntity)
str client.handle_rule_engine_request_for_entity_with_queue_and_timeout(entity_type: str, entity_id: str, queue_name: str, timeout: int, body: str)  # Push entity message with timeout and specified queue to the rule engine (handleRuleEngineRequestForEntityWithQueueAndTimeout)
str client.handle_rule_engine_request_for_entity_with_timeout(entity_type: str, entity_id: str, timeout: int, body: str)  # Push entity message with timeout to the rule engine (handleRuleEngineRequestForEntityWithTimeout)
str client.handle_rule_engine_request_for_user(body: str)  # Push user message to the rule engine (handleRuleEngineRequestForUser)
```


## handle_rule_engine_request_for_entity

```python
str client.handle_rule_engine_request_for_entity(entity_type: str, entity_id: str, body: str)
```

**POST** `/api/rule-engine/{entityType}/{entityId}`

Push entity message to the rule engine (handleRuleEngineRequestForEntity)

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **body** | **str** | A JSON object representing the message. | |

### Return type

**str**


## handle_rule_engine_request_for_entity_with_queue_and_timeout

```python
str client.handle_rule_engine_request_for_entity_with_queue_and_timeout(entity_type: str, entity_id: str, queue_name: str, timeout: int, body: str)
```

**POST** `/api/rule-engine/{entityType}/{entityId}/{queueName}/{timeout}`

Push entity message with timeout and specified queue to the rule engine (handleRuleEngineRequestForEntityWithQueueAndTimeout)

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. If request sent for Device/Device Profile or Asset/Asset Profile entity, specified queue will be used instead of the queue selected in the device or asset profile. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **queue_name** | **str** | Queue name to process the request in the rule engine | |
| **timeout** | **int** | Timeout to process the request in milliseconds | |
| **body** | **str** | A JSON object representing the message. | |

### Return type

**str**


## handle_rule_engine_request_for_entity_with_timeout

```python
str client.handle_rule_engine_request_for_entity_with_timeout(entity_type: str, entity_id: str, timeout: int, body: str)
```

**POST** `/api/rule-engine/{entityType}/{entityId}/{timeout}`

Push entity message with timeout to the rule engine (handleRuleEngineRequestForEntityWithTimeout)

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **timeout** | **int** | Timeout to process the request in milliseconds | |
| **body** | **str** | A JSON object representing the message. | |

### Return type

**str**


## handle_rule_engine_request_for_user

```python
str client.handle_rule_engine_request_for_user(body: str)
```

**POST** `/api/rule-engine/`

Push user message to the rule engine (handleRuleEngineRequestForUser)

Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses current User Id ( the one which credentials is used to perform the request) as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **str** | A JSON object representing the message. | |

### Return type

**str**

