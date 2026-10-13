# AgentControllerApi

`ThingsboardClient` methods:

```python
None client.delete_agent(agent_id: str)  # Delete agent (deleteAgent)
PageDataAgentAppEventInfo client.get_agent_app_event_infos_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None)  # Get Agent App Event Infos by Agent Id (getAgentAppEventInfosByAgentId)
PageDataAgentAppEvent client.get_agent_app_events_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Agent App Events by Agent Id (getAgentAppEventsByAgentId)
Agent client.get_agent_by_id(agent_id: str)  # Get Agent (getAgentById)
AgentInfo client.get_agent_info_by_id(agent_id: str)  # Get Agent Info (getAgentInfoById)
List[AgentInfo] client.get_agent_infos_by_ids(agent_ids: List[str])  # Get Agent Infos By Ids (getAgentInfosByIds)
AgentInstructions client.get_agent_install_instructions(agent_id: str, method: str)  # Get Agent Install Instructions (getAgentInstallInstructions)
str client.get_agent_upgrade_target(agent_id: str)  # Get the agent upgrade target (getAgentUpgradeTarget)
PageDataAgentInfo client.get_customer_agent_infos(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Agent Infos (getCustomerAgentInfos)
PageDataAgent client.get_customer_agents(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Customer Agents (getCustomerAgents)
str client.get_latest_agent_image_ref()  # Get the newest published agent image (getLatestAgentImageRef)
PageDataAgentInfo client.get_tenant_agent_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Agent Infos (getTenantAgentInfos)
PageDataAgent client.get_tenant_agents(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Agents (getTenantAgents)
bool client.is_agent_upgrade_available(agent_id: str)  # Is agent upgrade available (isAgentUpgradeAvailable)
Agent client.save_agent(agent: Agent, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)  # Create Or Update Agent (saveAgent)
AgentAppEvent client.upgrade_agent(agent_id: str, agent_upgrade_request: AgentUpgradeRequest)  # Upgrade Agent (upgradeAgent)
```


## delete_agent

```python
None client.delete_agent(agent_id: str)
```

**DELETE** `/api/agent/{agentId}`

Delete agent (deleteAgent)

Deletes the agent and all the relations (from and to the agent). Referencing non-existing agent Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## get_agent_app_event_infos_by_agent_id

```python
PageDataAgentAppEventInfo client.get_agent_app_event_infos_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None)
```

**GET** `/api/agent/{agentId}/eventInfos`

Get Agent App Event Infos by Agent Id (getAgentAppEventInfosByAgentId)

Returns a page of agent application events for all applications belonging to the specified agent, enriched with the application name for each event. Supports optional filtering by action type and status, and text search over the application name. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional text value to match against the application name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, updatedTime, actionType, startStatus, processingStatus] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |
| **action_type** | **AgentAppEventActionType** | Optional filter by event action type | [optional] [enum: INSTALL, UPDATE, DELETE, RESTART, ROLLBACK, UPGRADE, AGENT_UPGRADE] |
| **processing_status** | **AgentProcessingStatus** | Optional filter by event status | [optional] [enum: PENDING, QUEUED, PROCESSING, FINISHED, ERROR, START_FAILED] |

### Return type

**PageDataAgentAppEventInfo**


## get_agent_app_events_by_agent_id

```python
PageDataAgentAppEvent client.get_agent_app_events_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/{agentId}/events`

Get Agent App Events by Agent Id (getAgentAppEventsByAgentId)

Returns a page of agent application events for all applications belonging to the specified agent. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value reserved for future event filtering | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, updatedTime] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentAppEvent**


## get_agent_by_id

```python
Agent client.get_agent_by_id(agent_id: str)
```

**GET** `/api/agent/{agentId}`

Get Agent (getAgentById)

Fetch the Agent object based on the provided Agent Id. The server checks that the agent is owned by the same tenant.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**Agent**


## get_agent_info_by_id

```python
AgentInfo client.get_agent_info_by_id(agent_id: str)
```

**GET** `/api/agent/info/{agentId}`

Get Agent Info (getAgentInfoById)

Fetch the Agent Info object based on the provided Agent Id. Agent Info extends the Agent object and adds customer title and 'is public' flag.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AgentInfo**


## get_agent_infos_by_ids

```python
List[AgentInfo] client.get_agent_infos_by_ids(agent_ids: List[str])
```

**GET** `/api/agentInfos`

Get Agent Infos By Ids (getAgentInfosByIds)

Requested agents must be owned by tenant or assigned to customer which user is performing the request.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_ids** | **List[str]** | A list of agent ids, separated by comma ',' | |

### Return type

**List[AgentInfo]**


## get_agent_install_instructions

```python
AgentInstructions client.get_agent_install_instructions(agent_id: str, method: str)
```

**GET** `/api/agent/instructions/install/{agentId}/{method}`

Get Agent Install Instructions (getAgentInstallInstructions)

Returns the docker install command for the specified agent with the server address and gRPC port resolved server-side.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **method** | **str** | Installation method ('docker') | [enum: docker] |

### Return type

**AgentInstructions**


## get_agent_upgrade_target

```python
str client.get_agent_upgrade_target(agent_id: str)
```

**GET** `/api/agent/{agentId}/upgrade/target`

Get the agent upgrade target (getAgentUpgradeTarget)

Returns the image reference the agent should be upgraded to, or an empty string when it already runs the newest published image or cannot be placed in the version graph.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**str**


## get_customer_agent_infos

```python
PageDataAgentInfo client.get_customer_agent_infos(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/agentInfos`

Get Customer Agent Infos (getCustomerAgentInfos)

Returns a page of agent info objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing agent name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentInfo**


## get_customer_agents

```python
PageDataAgent client.get_customer_agents(customer_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/customer/{customerId}/agents`

Get Customer Agents (getCustomerAgents)

Returns a page of agent objects assigned to customer. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customer_id** | **str** | A string value representing the customer id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing agent name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgent**


## get_latest_agent_image_ref

```python
str client.get_latest_agent_image_ref()
```

**GET** `/api/agent/upgrade/latest`

Get the newest published agent image (getLatestAgentImageRef)

Returns the newest agent image reference known from the version graph, or the floating tag while no version has been published. Lets a list of agents decide locally which rows are upgradable without asking per row.  Available for users with 'TENANT_ADMIN' authority.

### Return type

**str**


## get_tenant_agent_infos

```python
PageDataAgentInfo client.get_tenant_agent_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/agentInfos`

Get Tenant Agent Infos (getTenantAgentInfos)

Returns a page of agent info objects owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing agent name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentInfo**


## get_tenant_agents

```python
PageDataAgent client.get_tenant_agents(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/agents`

Get Tenant Agents (getTenantAgents)

Returns a page of agents owned by tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing agent name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgent**


## is_agent_upgrade_available

```python
bool client.is_agent_upgrade_available(agent_id: str)
```

**GET** `/api/agent/{agentId}/upgrade/available`

Is agent upgrade available (isAgentUpgradeAvailable)

Returns 'true' when the agent reports an image older than the newest published one, 'false' otherwise — including when the agent runs a floating tag such as 'latest', whose current content cannot be told from the tag.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**bool**


## save_agent

```python
Agent client.save_agent(agent: Agent, entity_group_id: Optional[str] = None, entity_group_ids: Optional[List[str]] = None)
```

**POST** `/api/agent`

Create Or Update Agent (saveAgent)

Creates or Updates the Agent. When creating agent, platform generates Agent Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Agent id will be present in the response. Specify existing Agent id to update the agent. Referencing non-existing Agent Id will cause 'Not Found' error. Remove 'id', 'tenantId' and optionally 'customerId' from the request body example (below) to create new Agent entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent** | **Agent** | A JSON value representing the agent. | |
| **entity_group_id** | **str** |  | [optional] |
| **entity_group_ids** | **List[str]** | A list of entity group ids, separated by comma ',' | [optional] |

### Return type

**Agent**


## upgrade_agent

```python
AgentAppEvent client.upgrade_agent(agent_id: str, agent_upgrade_request: AgentUpgradeRequest)
```

**POST** `/api/agent/{agentId}/upgrade`

Upgrade Agent (upgradeAgent)

Creates an agent-scoped upgrade event that makes the agent replace its own container with the given image. At most one agent upgrade can be active per agent, and it blocks all application events for that agent until it completes.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **agent_upgrade_request** | **AgentUpgradeRequest** |  | |

### Return type

**AgentAppEvent**

