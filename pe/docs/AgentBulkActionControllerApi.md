# AgentBulkActionControllerApi

`ThingsboardClient` methods:

```python
AgentBulkAction client.get_agent_bulk_action(bulk_action_id: str)  # Get Agent Bulk Action (getAgentBulkAction)
AgentBulkActionEventStats client.get_agent_bulk_action_event_stats(bulk_action_id: str)  # Get Agent Bulk Action Event Stats (getAgentBulkActionEventStats)
PageDataAgentAppEventInfo client.get_agent_bulk_action_events(bulk_action_id: str, page_size: int, page: int, text_search: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Agent Bulk Action Events (getAgentBulkActionEvents)
```


## get_agent_bulk_action

```python
AgentBulkAction client.get_agent_bulk_action(bulk_action_id: str)
```

**GET** `/api/agent/bulk/{bulkActionId}`

Get Agent Bulk Action (getAgentBulkAction)

Fetch the Agent Bulk Action object based on the provided Bulk Action Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_action_id** | **str** | Bulk Action Id | |

### Return type

**AgentBulkAction**


## get_agent_bulk_action_event_stats

```python
AgentBulkActionEventStats client.get_agent_bulk_action_event_stats(bulk_action_id: str)
```

**GET** `/api/agent/bulk/{bulkActionId}/eventStats`

Get Agent Bulk Action Event Stats (getAgentBulkActionEventStats)

Returns the number of agent application events produced by the given bulk action per processing status, together with their total.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_action_id** | **str** | Bulk Action Id | |

### Return type

**AgentBulkActionEventStats**


## get_agent_bulk_action_events

```python
PageDataAgentAppEventInfo client.get_agent_bulk_action_events(bulk_action_id: str, page_size: int, page: int, text_search: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/bulk/{bulkActionId}/events`

Get Agent Bulk Action Events (getAgentBulkActionEvents)

Returns a page of agent application events produced by the given bulk action, optionally filtered by action type and status. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulk_action_id** | **str** | Bulk Action Id | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive 'substring' filter based on the event fields | [optional] |
| **action_type** | **AgentAppEventActionType** | A string value representing the action type to filter by, e.g. 'UPDATE' | [optional] [enum: INSTALL, UPDATE, DELETE, RESTART, ROLLBACK, UPGRADE, AGENT_UPGRADE] |
| **processing_status** | **AgentProcessingStatus** | A string value representing the event status to filter by, e.g. 'FINISHED' | [optional] [enum: PENDING, QUEUED, PROCESSING, FINISHED, ERROR, START_FAILED] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataAgentAppEventInfo**

