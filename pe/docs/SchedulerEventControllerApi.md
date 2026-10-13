# SchedulerEventControllerApi

`ThingsboardClient` methods:

```python
SchedulerEventInfo client.assign_scheduler_event_to_edge(edge_id: str, scheduler_event_id: str)  # Assign scheduler event to edge (assignSchedulerEventToEdge)
None client.delete_scheduler_event(scheduler_event_id: str)  # Delete Scheduler Event (deleteSchedulerEvent)
SchedulerEvent client.enable_scheduler_event(scheduler_event_id: str, enabled_value: bool)  # Enable or disable Scheduler Event (enableSchedulerEvent)
List[SchedulerEventInfo] client.get_all_edge_scheduler_events(edge_id: str)  # Get All Edge Scheduler Events (getAllEdgeSchedulerEvents)
List[SchedulerEventWithCustomerInfo] client.get_all_scheduler_events(type: Optional[str] = None)  # Get all scheduler events (getAllSchedulerEvents)
PageDataSchedulerEventInfo client.get_edge_scheduler_events(edge_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Edge Scheduler Events (getEdgeSchedulerEvents)
PageDataScheduledReportInfo client.get_scheduled_report_events(page_size: str, page: str, report_template_id: Optional[UUID] = None, user_id: Optional[UUID] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Scheduled Report Events (getScheduledReportEvents)
SchedulerEvent client.get_scheduler_event_by_id(scheduler_event_id: str)  # Get Scheduler Event (getSchedulerEventById)
SchedulerEventWithCustomerInfo client.get_scheduler_event_info_by_id(scheduler_event_id: str)  # Get Scheduler Event With Customer Info (getSchedulerEventInfoById)
PageDataSchedulerEventWithCustomerInfo client.get_scheduler_events(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, type: Optional[str] = None, edge_id: Optional[UUID] = None)  # Get scheduler events (getSchedulerEvents)
List[SchedulerEventInfo] client.get_scheduler_events_by_ids(scheduler_event_ids: List[str])  # Get Scheduler Events By Ids (getSchedulerEventsByIds)
List[SchedulerEventWithCustomerInfo] client.get_scheduler_events_by_range(start_time: int, end_time: int, type: Optional[str] = None, edge_id: Optional[UUID] = None, text_search: Optional[str] = None)  # Get scheduler events (getSchedulerEventsByRange)
SchedulerEvent client.save_scheduler_event(scheduler_event: SchedulerEvent)  # Save Scheduler Event (saveSchedulerEvent)
SchedulerEventInfo client.unassign_scheduler_event_from_edge(edge_id: str, scheduler_event_id: str)  # Unassign scheduler event from edge (unassignSchedulerEventFromEdge)
```


## assign_scheduler_event_to_edge

```python
SchedulerEventInfo client.assign_scheduler_event_to_edge(edge_id: str, scheduler_event_id: str)
```

**POST** `/api/edge/{edgeId}/schedulerEvent/{schedulerEventId}`

Assign scheduler event to edge (assignSchedulerEventToEdge)

Creates assignment of an existing scheduler event to an instance of The Edge. Assignment works in async way - first, notification event pushed to edge service queue on platform. Second, remote edge service will receive a copy of assignment scheduler event (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once scheduler event will be delivered to edge service, it is going to be available for usage on remote edge instance.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**SchedulerEventInfo**


## delete_scheduler_event

```python
None client.delete_scheduler_event(scheduler_event_id: str)
```

**DELETE** `/api/schedulerEvent/{schedulerEventId}`

Delete Scheduler Event (deleteSchedulerEvent)

Deletes the scheduler event. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## enable_scheduler_event

```python
SchedulerEvent client.enable_scheduler_event(scheduler_event_id: str, enabled_value: bool)
```

**PUT** `/api/schedulerEvent/{schedulerEventId}/enabled/{enabledValue}`

Enable or disable Scheduler Event (enableSchedulerEvent)

Updates scheduler event with enabled = true/false. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **enabled_value** | **bool** | Enabled or disabled scheduler | |

### Return type

**SchedulerEvent**


## get_all_edge_scheduler_events

```python
List[SchedulerEventInfo] client.get_all_edge_scheduler_events(edge_id: str)
```

**GET** `/api/edge/{edgeId}/allSchedulerEvents`

Get All Edge Scheduler Events (getAllEdgeSchedulerEvents)

Fetch the list of Scheduler Event Info objects based on the provided Edge entity. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**List[SchedulerEventInfo]**


## get_all_scheduler_events

```python
List[SchedulerEventWithCustomerInfo] client.get_all_scheduler_events(type: Optional[str] = None)
```

**GET** `/api/schedulerEvents/all`

Get all scheduler events (getAllSchedulerEvents)

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **str** | A string value representing the scheduler type. For example, 'generateReport' | [optional] |

### Return type

**List[SchedulerEventWithCustomerInfo]**


## get_edge_scheduler_events

```python
PageDataSchedulerEventInfo client.get_edge_scheduler_events(edge_id: str, page_size: str, page: str, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/edge/{edgeId}/schedulerEvents`

Get Edge Scheduler Events (getEdgeSchedulerEvents)

Returns a page of  Scheduler Events Info objects based on the provided Edge entity. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'startsWith' filter based on the scheduler event name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataSchedulerEventInfo**


## get_scheduled_report_events

```python
PageDataScheduledReportInfo client.get_scheduled_report_events(page_size: str, page: str, report_template_id: Optional[UUID] = None, user_id: Optional[UUID] = None, include_customers: Optional[bool] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/scheduledReports`

Get Scheduled Report Events (getScheduledReportEvents)

  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **str** | Maximum amount of entities in a one page | |
| **page** | **str** | Sequence number of page starting from 0 | |
| **report_template_id** | **UUID** | Report template id | [optional] |
| **user_id** | **UUID** | The user used for report generation. | [optional] |
| **include_customers** | **bool** | Include customer or sub-customer entities. For tenant administrator: when true, includes entities for all customers; when false (default), only own entities are returned. For customer user: when true, includes entities for all sub-customers. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the scheduler event name or customer title. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataScheduledReportInfo**


## get_scheduler_event_by_id

```python
SchedulerEvent client.get_scheduler_event_by_id(scheduler_event_id: str)
```

**GET** `/api/schedulerEvent/{schedulerEventId}`

Get Scheduler Event (getSchedulerEventById)

Fetch the SchedulerEvent object based on the provided scheduler event Id. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**SchedulerEvent**


## get_scheduler_event_info_by_id

```python
SchedulerEventWithCustomerInfo client.get_scheduler_event_info_by_id(scheduler_event_id: str)
```

**GET** `/api/schedulerEvent/info/{schedulerEventId}`

Get Scheduler Event With Customer Info (getSchedulerEventInfoById)

Fetch the SchedulerEventWithCustomerInfo object based on the provided scheduler event Id. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details. Referencing non-existing Scheduler Event Id will cause 'Not Found' error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**SchedulerEventWithCustomerInfo**


## get_scheduler_events

```python
PageDataSchedulerEventWithCustomerInfo client.get_scheduler_events(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, type: Optional[str] = None, edge_id: Optional[UUID] = None)
```

**GET** `/api/schedulerEvents`

Get scheduler events (getSchedulerEvents)

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details.   You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.     Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on event's name, type, or customer's name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |
| **type** | **str** | A string value representing the scheduler type. For example, 'generateReport' | [optional] |
| **edge_id** | **UUID** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |

### Return type

**PageDataSchedulerEventWithCustomerInfo**


## get_scheduler_events_by_ids

```python
List[SchedulerEventInfo] client.get_scheduler_events_by_ids(scheduler_event_ids: List[str])
```

**GET** `/api/schedulerEvents/list`

Get Scheduler Events By Ids (getSchedulerEventsByIds)

Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Events allows you to schedule various types of events with flexible schedule configuration. Scheduler fires configured scheduler events according to their schedule. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event_ids** | **List[str]** | A list of scheduler event ids, separated by comma ',' | |

### Return type

**List[SchedulerEventInfo]**


## get_scheduler_events_by_range

```python
List[SchedulerEventWithCustomerInfo] client.get_scheduler_events_by_range(start_time: int, end_time: int, type: Optional[str] = None, edge_id: Optional[UUID] = None, text_search: Optional[str] = None)
```

**GET** `/api/schedulerEvents/startTime/{startTime}/endTime/{endTime}`

Get scheduler events (getSchedulerEventsByRange)

Retrieves scheduler events filtering by event run time. Requested scheduler events must be owned by tenant or assigned to customer which user is performing the request. Scheduler Event With Customer Info extends Scheduler Event Info object and adds 'customerTitle' - a String value representing the title of the customer which user created a Scheduler Event and 'customerIsPublic' - a boolean parameter that specifies if customer is public. See the 'Model' tab of the Response Class for more details.   You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.     Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **start_time** | **int** | Start time filter in milliseconds for scheduler event run time | |
| **end_time** | **int** | End time filter in milliseconds for scheduler event run time | |
| **type** | **str** | A string value representing the scheduler type. For example, 'generateReport' | [optional] |
| **edge_id** | **UUID** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | [optional] |
| **text_search** | **str** | Case-insensitive 'substring' filter based on event's name, type, or customer's name | [optional] |

### Return type

**List[SchedulerEventWithCustomerInfo]**


## save_scheduler_event

```python
SchedulerEvent client.save_scheduler_event(scheduler_event: SchedulerEvent)
```

**POST** `/api/schedulerEvent`

Save Scheduler Event (saveSchedulerEvent)

Creates or Updates scheduler event. Scheduler Event extends Scheduler Event Info object and adds 'configuration' - a JSON structure of scheduler event configuration. See the 'Model' tab of the Response Class for more details. When creating scheduler event, platform generates scheduler event Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created scheduler event id will be present in the response. Specify existing scheduler event id to update the scheduler event. Referencing non-existing scheduler event Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Scheduler Event entity.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scheduler_event** | **SchedulerEvent** |  | |

### Return type

**SchedulerEvent**


## unassign_scheduler_event_from_edge

```python
SchedulerEventInfo client.unassign_scheduler_event_from_edge(edge_id: str, scheduler_event_id: str)
```

**DELETE** `/api/edge/{edgeId}/schedulerEvent/{schedulerEventId}`

Unassign scheduler event from edge (unassignSchedulerEventFromEdge)

Clears assignment of the scheduler event to the edge. Unassignment works in async way - first, 'unassign' notification event pushed to edge queue on platform. Second, remote edge service will receive an 'unassign' command to remove entity group (Edge will receive this instantly, if it's currently connected, or once it's going to be connected to platform). Third, once 'unassign' command will be delivered to edge service, it's going to remove entity group and entities inside this group locally.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **edge_id** | **str** | A string value representing the edge id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **scheduler_event_id** | **str** | A string value representing the scheduler id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**SchedulerEventInfo**

