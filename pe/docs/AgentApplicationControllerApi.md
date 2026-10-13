# AgentApplicationControllerApi

`ThingsboardClient` methods:

```python
AgentApplication client.assign_related_entity_to_agent_app(agent_application_id: str, entity_type: str, entity_id: str)  # Assign Related Entity to Agent Application (assignRelatedEntityToAgentApp)
AgentApplication client.attach_to_profile(agent_application_id: str, profile_id: str)  # Attach Application to Profile (attachToProfile)
None client.cancel_agent_app_event(agent_application_id: str, agent_app_event_id: str)  # Cancel Agent Application Event (cancelAgentAppEvent)
AgentAppEvent client.create_agent_app_event(agent_application_id: str, agent_app_event_request: AgentAppEventRequest)  # Execute Agent Application Event (createAgentAppEvent)
AgentApplication client.detach_from_profile(agent_application_id: str)  # Detach Application from Profile (detachFromProfile)
AgentAppEvent client.get_agent_app_event_by_id(agent_app_event_id: str)  # Get Agent Application Event (getAgentAppEventById)
PageDataAgentAppEvent client.get_agent_app_events(agent_application_id: str, page_size: int, page: int, text_search: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Agent Application Events (getAgentAppEvents)
PageDataAgentAppUnit client.get_agent_app_units(agent_application_id: str, page_size: int, page: int, text_search: Optional[str] = None, type: Optional[AgentAppUnitType] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Agent Application Units (getAgentAppUnits)
AgentApplicationInfo client.get_agent_application_by_id(agent_application_id: str)  # Get Agent Application (getAgentApplicationById)
AgentApplication client.get_agent_application_by_related_entity(entity_type: str, entity_id: str)  # Get Agent Application by Related Entity (getAgentApplicationByRelatedEntity)
PageDataAgentApplicationInfo client.get_agent_applications_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Agent Applications by Agent Id (getAgentApplicationsByAgentId)
List[GetManagedRelatedEntityIds200ResponseInner] client.get_managed_related_entity_ids(entity_type: str)  # Get Managed Related Entity Ids (getManagedRelatedEntityIds)
PageDataEntityInfo client.get_related_entity_candidates(entity_type: str, page_size: int, page: int, text_search: Optional[str] = None, current_entity_id: Optional[str] = None)  # Get Related Entity Candidates (getRelatedEntityCandidates)
AgentAppInstallResponse client.install_agent_app(agent_app_event_request: AgentAppEventRequest)  # Install Agent Application (installAgentApp)
AgentApplication client.merge_agent_application_for_preview(template_version: str, app_type: Optional[AgentApplicationType] = None, compose_type: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, set_host_values: Optional[bool] = None, related_entity_type: Optional[str] = None, related_entity_id: Optional[str] = None, agent_application: Optional[AgentApplication] = None)  # Merge template into application for preview (mergeAgentApplicationForPreview)
AgentApplication client.unassign_related_entity_from_agent_app(agent_application_id: str)  # Unassign Related Entity from Agent Application (unassignRelatedEntityFromAgentApp)
AgentApplication client.update_agent_application(agent_application: AgentApplication)  # Update Agent Application (saveAgentApplication)
```


## assign_related_entity_to_agent_app

```python
AgentApplication client.assign_related_entity_to_agent_app(agent_application_id: str, entity_type: str, entity_id: str)
```

**POST** `/api/agent/app/{agentApplicationId}/relatedEntity/{entityType}/{entityId}`

Assign Related Entity to Agent Application (assignRelatedEntityToAgentApp)

Links an Edge or Gateway Device to the specified agent application and re-merges entity credentials into the compose.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **entity_type** | **str** | Related entity type (EDGE or DEVICE) | |
| **entity_id** | **str** | Related entity id | |

### Return type

**AgentApplication**


## attach_to_profile

```python
AgentApplication client.attach_to_profile(agent_application_id: str, profile_id: str)
```

**POST** `/api/agent/app/{agentApplicationId}/attach/{profileId}`

Attach Application to Profile (attachToProfile)

Re-attaches the application to a profile. The application adopts the profile's template version without running any upgrade or downgrade steps. After attachment the profile becomes the source of the config; the app's own credentials are carried over.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **profile_id** | **str** |  | |

### Return type

**AgentApplication**


## cancel_agent_app_event

```python
None client.cancel_agent_app_event(agent_application_id: str, agent_app_event_id: str)
```

**POST** `/api/agent/app/{agentApplicationId}/event/{agentAppEventId}/cancel`

Cancel Agent Application Event (cancelAgentAppEvent)

Force-cancels an in-flight or pending agent application event, marking it as ERROR. Cannot cancel events that are already in a terminal state (FINISHED or ERROR).  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **agent_app_event_id** | **str** | A string value representing the agent app event id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

None (empty response body)


## create_agent_app_event

```python
AgentAppEvent client.create_agent_app_event(agent_application_id: str, agent_app_event_request: AgentAppEventRequest)
```

**POST** `/api/agent/app/{agentApplicationId}/event`

Execute Agent Application Event (createAgentAppEvent)

Creates an event for the specified agent application. The action type determines the operation (UPDATE, DELETE, RESTART, UPGRADE, ROLLBACK). Step inputs can be provided for actions that require them. Returns the created event so the caller can open a progress view.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **agent_app_event_request** | **AgentAppEventRequest** | A JSON value representing the event request. | |

### Return type

**AgentAppEvent**


## detach_from_profile

```python
AgentApplication client.detach_from_profile(agent_application_id: str)
```

**POST** `/api/agent/app/{agentApplicationId}/detach`

Detach Application from Profile (detachFromProfile)

Detaches the application from its profile. The application keeps the effective config it already carries (profile config with its own credentials merged in) and becomes standalone and editable.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AgentApplication**


## get_agent_app_event_by_id

```python
AgentAppEvent client.get_agent_app_event_by_id(agent_app_event_id: str)
```

**GET** `/api/agent/app/event/{agentAppEventId}`

Get Agent Application Event (getAgentAppEventById)

Fetches a single agent application event by id. Works for orphan events whose application has been deleted (application_id is nullable).  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_app_event_id** | **str** | A string value representing the agent app event id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AgentAppEvent**


## get_agent_app_events

```python
PageDataAgentAppEvent client.get_agent_app_events(agent_application_id: str, page_size: int, page: int, text_search: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, processing_status: Optional[AgentProcessingStatus] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/app/{agentApplicationId}/events`

Get Agent Application Events (getAgentAppEvents)

Returns a page of events for the specified agent application. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional case-insensitive substring matched against the event action type and processing status | [optional] |
| **action_type** | **AgentAppEventActionType** | Optional action type filter | [optional] [enum: INSTALL, UPDATE, DELETE, RESTART, ROLLBACK, UPGRADE, AGENT_UPGRADE] |
| **processing_status** | **AgentProcessingStatus** | Optional processing status filter | [optional] [enum: PENDING, QUEUED, PROCESSING, FINISHED, ERROR, START_FAILED] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, updatedTime] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentAppEvent**


## get_agent_app_units

```python
PageDataAgentAppUnit client.get_agent_app_units(agent_application_id: str, page_size: int, page: int, text_search: Optional[str] = None, type: Optional[AgentAppUnitType] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/app/{agentApplicationId}/units`

Get Agent Application Units (getAgentAppUnits)

Returns a page of units (containers, volumes, networks) for the specified agent application. Live per-unit data such as `image` and `state` lives in server-scope attributes on each unit and should be fetched separately via the standard telemetry/attributes API.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Case-insensitive substring match against the unit identifier | [optional] |
| **type** | **AgentAppUnitType** | Optional unit type filter (CONTAINER, VOLUME, NETWORK) | [optional] [enum: CONTAINER, VOLUME, NETWORK] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, identifier, type] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentAppUnit**


## get_agent_application_by_id

```python
AgentApplicationInfo client.get_agent_application_by_id(agent_application_id: str)
```

**GET** `/api/agent/app/{agentApplicationId}`

Get Agent Application (getAgentApplicationById)

Fetch the Agent Application object based on the provided Agent Application Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AgentApplicationInfo**


## get_agent_application_by_related_entity

```python
AgentApplication client.get_agent_application_by_related_entity(entity_type: str, entity_id: str)
```

**GET** `/api/agent/apps/{entityType}/{entityId}`

Get Agent Application by Related Entity (getAgentApplicationByRelatedEntity)

Returns the agent application linked to the specified entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | Entity type | |
| **entity_id** | **str** | Entity id | |

### Return type

**AgentApplication**


## get_agent_applications_by_agent_id

```python
PageDataAgentApplicationInfo client.get_agent_applications_by_agent_id(agent_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/{agentId}/apps`

Get Agent Applications by Agent Id (getAgentApplicationsByAgentId)

Returns a page of agent applications that belong to the specified agent. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str** | A string value representing the agent id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing application name | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentApplicationInfo**


## get_managed_related_entity_ids

```python
List[GetManagedRelatedEntityIds200ResponseInner] client.get_managed_related_entity_ids(entity_type: str)
```

**GET** `/api/agent/app/managedRelatedEntities/{entityType}`

Get Managed Related Entity Ids (getManagedRelatedEntityIds)

Returns the ids of entities of the given type that are already linked to an agent application.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | Related entity type (EDGE or DEVICE) | |

### Return type

**List[GetManagedRelatedEntityIds200ResponseInner]**


## get_related_entity_candidates

```python
PageDataEntityInfo client.get_related_entity_candidates(entity_type: str, page_size: int, page: int, text_search: Optional[str] = None, current_entity_id: Optional[str] = None)
```

**GET** `/api/agent/app/relatedEntityCandidates`

Get Related Entity Candidates (getRelatedEntityCandidates)

Returns a page of Edges or Gateway Devices (devices with 'gateway' set in additional info) that can be linked to an agent application. Entities already linked to another application are excluded unless passed as 'currentEntityId'. Results are sorted by name. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | Related entity type (EDGE or DEVICE) | [enum: EDGE, DEVICE] |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional String value representing entity name | [optional] |
| **current_entity_id** | **str** | Optional id of the entity currently linked to the edited application; it is kept in the result even though it is managed | [optional] |

### Return type

**PageDataEntityInfo**


## install_agent_app

```python
AgentAppInstallResponse client.install_agent_app(agent_app_event_request: AgentAppEventRequest)
```

**POST** `/api/agent/app/event`

Install Agent Application (installAgentApp)

Creates a new agent application and an INSTALL event in a single operation. Returns both the created application and the INSTALL event so the caller can open a progress view without a second round-trip. The request body must include the application object.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_app_event_request** | **AgentAppEventRequest** | A JSON value representing the install event request with the application. | |

### Return type

**AgentAppInstallResponse**


## merge_agent_application_for_preview

```python
AgentApplication client.merge_agent_application_for_preview(template_version: str, app_type: Optional[AgentApplicationType] = None, compose_type: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, set_host_values: Optional[bool] = None, related_entity_type: Optional[str] = None, related_entity_id: Optional[str] = None, agent_application: Optional[AgentApplication] = None)
```

**POST** `/api/agent/app/merge/{templateVersion}/preview`

Merge template into application for preview (mergeAgentApplicationForPreview)

Merges the specified template into an agent application for preview purposes. If no application is provided in the body, a new one is created from the template. The compose type determines which compose configuration variant from the template is used. Optionally provide relatedEntityType and relatedEntityId to auto-fill entity credentials (Edge routing key/secret or Gateway access token) into the compose.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **template_version** | **str** | The template version to merge (e.g. '4.3.1.2EDGEPE') | |
| **app_type** | **AgentApplicationType** | Application type (EDGE, GATEWAY, GENERIC). Required when no application body is supplied. | [optional] [enum: GENERIC, EDGE, GATEWAY] |
| **compose_type** | **str** | The compose type to select from the template (e.g. 'monolith', 'microservices') | [optional] |
| **action_type** | **AgentAppEventActionType** | The event action this merge previews (e.g. UPGRADE). Drives action-specific merge rules. | [optional] [enum: INSTALL, UPDATE, DELETE, RESTART, ROLLBACK, UPGRADE, AGENT_UPGRADE] |
| **set_host_values** | **bool** | Whether to auto-fill host values (e.g. CLOUD_RPC_HOST) from the platform base URL. Should be true only for the install preview; keep false when previewing the saved compose of an existing application to preserve user-configured host values. | [optional] [default to False] |
| **related_entity_type** | **str** | Related entity type (EDGE or DEVICE) | [optional] |
| **related_entity_id** | **str** | Related entity id | [optional] |
| **agent_application** | **AgentApplication** | Optional agent application to merge with. If null, a new application is created from the template. | [optional] |

### Return type

**AgentApplication**


## unassign_related_entity_from_agent_app

```python
AgentApplication client.unassign_related_entity_from_agent_app(agent_application_id: str)
```

**DELETE** `/api/agent/app/{agentApplicationId}/relatedEntity`

Unassign Related Entity from Agent Application (unassignRelatedEntityFromAgentApp)

Removes the link between an agent application and its related Edge or Gateway Device.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application_id** | **str** | A string value representing the agent application id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |

### Return type

**AgentApplication**


## update_agent_application

```python
AgentApplication client.update_agent_application(agent_application: AgentApplication)
```

**PUT** `/api/agent/app`

Update Agent Application (saveAgentApplication)

Updates the Agent Application.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_application** | **AgentApplication** | A JSON value representing the agent application. | |

### Return type

**AgentApplication**

