# AlarmControllerApi

`ThingsboardClient` methods:

```python
AlarmInfo client.ack_alarm(alarm_id: str)  # Acknowledge Alarm (ackAlarm)
Alarm client.assign_alarm(alarm_id: str, assignee_id: str)  # Assign/Reassign Alarm (assignAlarm)
AlarmInfo client.clear_alarm(alarm_id: str)  # Clear Alarm (clearAlarm)
bool client.delete_alarm(alarm_id: str)  # Delete Alarm (deleteAlarm)
Alarm client.get_alarm_by_id(alarm_id: str)  # Get Alarm (getAlarmById)
AlarmInfo client.get_alarm_info_by_id(alarm_id: str)  # Get Alarm Info (getAlarmInfoById)
PageDataEntitySubtype client.get_alarm_types(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)  # Get Alarm Types (getAlarmTypes)
PageDataAlarmInfo client.get_alarms_by_entity(entity_type: str, entity_id: str, page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None)  # Get Alarms (getAlarmsByEntity)
PageDataAlarmInfo client.get_alarms_v2(entity_type: str, entity_id: str, page_size: int, page: int, status_list: Optional[List[str]] = None, severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # Get Alarms (getAlarmsV2)
PageDataAlarmInfo client.get_all_alarms(page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None)  # Get All Alarms (getAllAlarms)
PageDataAlarmInfo client.get_all_alarms_v2(page_size: int, page: int, status_list: Optional[List[str]] = None, severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)  # Get All Alarms (getAllAlarmsV2)
AlarmSeverity client.get_highest_alarm_severity(entity_type: str, entity_id: str, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None)  # Get Highest Alarm Severity (getHighestAlarmSeverity)
Alarm client.save_alarm(alarm: Alarm)  # Create or Update Alarm (saveAlarm)
Alarm client.unassign_alarm(alarm_id: str)  # Unassign Alarm (unassignAlarm)
```


## ack_alarm

```python
AlarmInfo client.ack_alarm(alarm_id: str)
```

**POST** `/api/alarm/{alarmId}/ack`

Acknowledge Alarm (ackAlarm)

Acknowledge the Alarm. Once acknowledged, the 'ack_ts' field will be set to current timestamp and special rule chain event 'ALARM_ACK' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AlarmInfo**


## assign_alarm

```python
Alarm client.assign_alarm(alarm_id: str, assignee_id: str)
```

**POST** `/api/alarm/{alarmId}/assign/{assigneeId}`

Assign/Reassign Alarm (assignAlarm)

Assign the Alarm. Once assigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_ASSIGNED' (or ALARM_REASSIGNED in case of assigning already assigned alarm) will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **assignee_id** | **str** | A string value representing the user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Alarm**


## clear_alarm

```python
AlarmInfo client.clear_alarm(alarm_id: str)
```

**POST** `/api/alarm/{alarmId}/clear`

Clear Alarm (clearAlarm)

Clear the Alarm. Once cleared, the 'clear_ts' field will be set to current timestamp and special rule chain event 'ALARM_CLEAR' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AlarmInfo**


## delete_alarm

```python
bool client.delete_alarm(alarm_id: str)
```

**DELETE** `/api/alarm/{alarmId}`

Delete Alarm (deleteAlarm)

Deletes the Alarm. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bool**


## get_alarm_by_id

```python
Alarm client.get_alarm_by_id(alarm_id: str)
```

**GET** `/api/alarm/{alarmId}`

Get Alarm (getAlarmById)

Fetch the Alarm object based on the provided Alarm Id.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Alarm**


## get_alarm_info_by_id

```python
AlarmInfo client.get_alarm_info_by_id(alarm_id: str)
```

**GET** `/api/alarm/info/{alarmId}`

Get Alarm Info (getAlarmInfoById)

Fetch the Alarm Info object based on the provided Alarm Id. Alarm Info is an extension of the default Alarm object that also contains name of the alarm originator.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AlarmInfo**


## get_alarm_types

```python
PageDataEntitySubtype client.get_alarm_types(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/alarm/types`

Get Alarm Types (getAlarmTypes)

Returns a set of unique alarm types based on alarms that are either owned by the tenant or assigned to the customer which user is performing the request.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on of next alarm fields: type, severity or status | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataEntitySubtype**


## get_alarms_by_entity

```python
PageDataAlarmInfo client.get_alarms_by_entity(entity_type: str, entity_id: str, page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None)
```

**GET** `/api/alarm/{entityType}/{entityId}`

Get Alarms (getAlarmsByEntity)

Returns a page of alarms for the selected entity. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **search_status** | **str** | A string value representing one of the AlarmSearchStatus enumeration value | [optional] [enum: ANY, ACTIVE, CLEARED, ACK, UNACK] |
| **status** | **str** | A string value representing one of the AlarmStatus enumeration value | [optional] [enum: ACTIVE_UNACK, ACTIVE_ACK, CLEARED_UNACK, CLEARED_ACK] |
| **assignee_id** | **str** | A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on of next alarm fields: type, severity or status | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, startTs, endTs, type, ackTs, clearTs, severity, status] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **fetch_originator** | **bool** | A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null. | [optional] |

### Return type

**PageDataAlarmInfo**


## get_alarms_v2

```python
PageDataAlarmInfo client.get_alarms_v2(entity_type: str, entity_id: str, page_size: int, page: int, status_list: Optional[List[str]] = None, severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/v2/alarm/{entityType}/{entityId}`

Get Alarms (getAlarmsV2)

Returns a page of alarms for the selected entity. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **status_list** | **List[str]** | A list of string values separated by comma ',' representing one of the AlarmSearchStatus enumeration value | [optional] [enum: ANY, ACTIVE, CLEARED, ACK, UNACK] |
| **severity_list** | **List[str]** | A list of string values separated by comma ',' representing one of the AlarmSeverity enumeration value | [optional] [enum: CRITICAL, MAJOR, MINOR, WARNING, INDETERMINATE] |
| **type_list** | **List[str]** | A list of string values separated by comma ',' representing alarm types | [optional] |
| **assignee_id** | **str** | A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on of next alarm fields: type, severity or status | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, startTs, endTs, type, ackTs, clearTs, severity, status] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |

### Return type

**PageDataAlarmInfo**


## get_all_alarms

```python
PageDataAlarmInfo client.get_all_alarms(page_size: int, page: int, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None, fetch_originator: Optional[bool] = None)
```

**GET** `/api/alarms`

Get All Alarms (getAllAlarms)

Returns a page of alarms that belongs to the current user owner. If the user has the authority of 'Tenant Administrator', the server returns alarms that belongs to the tenant of current user. If the user has the authority of 'Customer User', the server returns alarms that belongs to the customer of current user. Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **search_status** | **str** | A string value representing one of the AlarmSearchStatus enumeration value | [optional] [enum: ANY, ACTIVE, CLEARED, ACK, UNACK] |
| **status** | **str** | A string value representing one of the AlarmStatus enumeration value | [optional] [enum: ACTIVE_UNACK, ACTIVE_ACK, CLEARED_UNACK, CLEARED_ACK] |
| **assignee_id** | **str** | A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on of next alarm fields: type, severity or status | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, startTs, endTs, type, ackTs, clearTs, severity, status] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **fetch_originator** | **bool** | A boolean value to specify if the alarm originator name will be filled in the AlarmInfo object  field: 'originatorName' or will returns as null. | [optional] |

### Return type

**PageDataAlarmInfo**


## get_all_alarms_v2

```python
PageDataAlarmInfo client.get_all_alarms_v2(page_size: int, page: int, status_list: Optional[List[str]] = None, severity_list: Optional[List[str]] = None, type_list: Optional[List[str]] = None, assignee_id: Optional[str] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, start_time: Optional[int] = None, end_time: Optional[int] = None)
```

**GET** `/api/v2/alarms`

Get All Alarms (getAllAlarmsV2)

Returns a page of alarms that belongs to the current user owner. If the user has the authority of 'Tenant Administrator', the server returns alarms that belongs to the tenant of current user. If the user has the authority of 'Customer User', the server returns alarms that belongs to the customer of current user. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **status_list** | **List[str]** | A list of string values separated by comma ',' representing one of the AlarmSearchStatus enumeration value | [optional] [enum: ANY, ACTIVE, CLEARED, ACK, UNACK] |
| **severity_list** | **List[str]** | A list of string values separated by comma ',' representing one of the AlarmSeverity enumeration value | [optional] [enum: CRITICAL, MAJOR, MINOR, WARNING, INDETERMINATE] |
| **type_list** | **List[str]** | A list of string values separated by comma ',' representing alarm types | [optional] |
| **assignee_id** | **str** | A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on of next alarm fields: type, severity or status | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, startTs, endTs, type, ackTs, clearTs, severity, status] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **start_time** | **int** | The start timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |
| **end_time** | **int** | The end timestamp in milliseconds of the search time range over the Alarm class field: 'createdTime'. | [optional] |

### Return type

**PageDataAlarmInfo**


## get_highest_alarm_severity

```python
AlarmSeverity client.get_highest_alarm_severity(entity_type: str, entity_id: str, search_status: Optional[str] = None, status: Optional[str] = None, assignee_id: Optional[str] = None)
```

**GET** `/api/alarm/highestSeverity/{entityType}/{entityId}`

Get Highest Alarm Severity (getHighestAlarmSeverity)

Search the alarms by originator ('entityType' and entityId') and optional 'status' or 'searchStatus' filters and returns the highest AlarmSeverity(CRITICAL, MAJOR, MINOR, WARNING or INDETERMINATE). Specifying both parameters 'searchStatus' and 'status' at the same time will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **search_status** | **str** | A string value representing one of the AlarmSearchStatus enumeration value | [optional] [enum: ANY, ACTIVE, CLEARED, ACK, UNACK] |
| **status** | **str** | A string value representing one of the AlarmStatus enumeration value | [optional] [enum: ACTIVE_UNACK, ACTIVE_ACK, CLEARED_UNACK, CLEARED_ACK] |
| **assignee_id** | **str** | A string value representing the assignee user id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**AlarmSeverity**


## save_alarm

```python
Alarm client.save_alarm(alarm: Alarm)
```

**POST** `/api/alarm`

Create or Update Alarm (saveAlarm)

Creates or Updates the Alarm. When creating alarm, platform generates Alarm Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm id will be present in the response. Specify existing Alarm id to update the alarm. Referencing non-existing Alarm Id will cause 'Not Found' error.   Platform also deduplicate the alarms based on the entity id of originator and alarm 'type'. For example, if the user or system component create the alarm with the type 'HighTemperature' for device 'Device A' the new active alarm is created. If the user tries to create 'HighTemperature' alarm for the same device again, the previous alarm will be updated (the 'end_ts' will be set to current timestamp). If the user clears the alarm (see 'Clear Alarm(clearAlarm)'), than new alarm with the same type and same device may be created. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Alarm entity.   The alarm originator is an immutable routing key: when updating an existing alarm, the 'originator' in the request body must match the stored alarm's originator. A request that references an existing alarm id but carries a different originator is treated as a lookup miss and causes a 'Not Found' error.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm** | **Alarm** | A JSON value representing the alarm. | |

### Return type

**Alarm**


## unassign_alarm

```python
Alarm client.unassign_alarm(alarm_id: str)
```

**DELETE** `/api/alarm/{alarmId}/assign`

Unassign Alarm (unassignAlarm)

Unassign the Alarm. Once unassigned, the 'assign_ts' field will be set to current timestamp and special rule chain event 'ALARM_UNASSIGNED' will be generated. Referencing non-existing Alarm Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_id** | **str** | A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Alarm**

