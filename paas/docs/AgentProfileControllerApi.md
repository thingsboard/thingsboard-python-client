# AgentProfileControllerApi

`ThingsboardClient` methods:

```python
None client.assign_app_profile_to_agent_profile(agent_profile_id: str, application_profile_id: str)  # Assign App Profile to Agent Profile (assignAppProfileToAgentProfile)
None client.assign_app_profiles_to_agent_profile(agent_profile_id: str, app_profile_ids: Optional[List[str]] = None)  # Assign Multiple App Profiles to Agent Profile (assignAppProfilesToAgentProfile)
AgentBulkAction client.bulk_operation(agent_profile_id: str, application_profile_id: str, bulk_operation_request: BulkOperationRequest)  # Bulk Operation (bulkOperation)
None client.delete_agent_profile(agent_profile_id: str)  # Delete Agent Profile (deleteAgentProfile)
PageDataAgentBulkAction client.get_agent_profile_app_profile_bulk_actions(agent_profile_id: str, application_profile_id: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Bulk Actions for Agent Profile and Application Profile (getAgentProfileAppProfileBulkActions)
List[AgentAppProfileRelationInfo] client.get_agent_profile_app_profile_infos(agent_profile_id: str)  # Get Agent Profile App Profile Infos (getAgentProfileAppProfileInfos)
PageDataAgentBulkAction client.get_agent_profile_bulk_actions(agent_profile_id: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Bulk Actions for Agent Profile (getAgentProfileBulkActions)
AgentProfile client.get_agent_profile_by_id(agent_profile_id: str)  # Get Agent Profile (getAgentProfileById)
AgentProfileInfo client.get_agent_profile_info_by_id(agent_profile_id: str)  # Get Agent Profile Info (getAgentProfileInfoById)
AgentInstructions client.get_agent_provision_instructions(agent_profile_id: str, method: str)  # Get Agent Provision Instructions (getAgentProvisionInstructions)
AgentProfileInfo client.get_default_agent_profile_info()  # Get Default Agent Profile (getDefaultAgentProfileInfo)
PageDataAgentProfileInfo client.get_tenant_agent_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Agent Profile Infos (getTenantAgentProfileInfos)
PageDataAgentProfile client.get_tenant_agent_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Agent Profiles (getTenantAgentProfiles)
BulkOperationPreview client.preview_bulk_operation(agent_profile_id: str, application_profile_id: str, bulk_operation_request: BulkOperationRequest)  # Preview Bulk Operation (previewBulkOperation)
AgentProfile client.save_agent_profile(agent_profile: AgentProfile, app_profile_ids: Optional[List[str]] = None)  # Create or Update Agent Profile (saveAgentProfile)
None client.set_app_profile_relates_on_auto_discovery(agent_profile_id: str, application_profile_id: str, relate: bool)  # Set App Profile Relates On Auto-Discovery (setAppProfileRelatesOnAutoDiscovery)
AgentProfile client.set_default_agent_profile(agent_profile_id: str)  # Make Agent Profile Default (setDefaultAgentProfile)
None client.unassign_app_profile_from_agent_profile(agent_profile_id: str, application_profile_id: str)  # Unassign App Profile from Agent Profile (unassignAppProfileFromAgentProfile)
```


## assign_app_profile_to_agent_profile

```python
None client.assign_app_profile_to_agent_profile(agent_profile_id: str, application_profile_id: str)
```

**POST** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}`

Assign App Profile to Agent Profile (assignAppProfileToAgentProfile)

Assigns the given agent application profile to the agent profile, making it available to applications managed by that agent profile.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |

### Return type

None (empty response body)


## assign_app_profiles_to_agent_profile

```python
None client.assign_app_profiles_to_agent_profile(agent_profile_id: str, app_profile_ids: Optional[List[str]] = None)
```

**POST** `/api/agent/profile/{agentProfileId}/appProfiles/assign`

Assign Multiple App Profiles to Agent Profile (assignAppProfilesToAgentProfile)

Assigns the given set of agent application profiles to the agent profile in a single request, replacing the previous assignment set. An explicitly empty 'appProfileIds' value (e.g. 'appProfileIds=') removes all assignments.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **app_profile_ids** | **List[str]** | Agent application profile ids that replace the current assignment set. An explicitly empty value removes all assignments. | [optional] |

### Return type

None (empty response body)


## bulk_operation

```python
AgentBulkAction client.bulk_operation(agent_profile_id: str, application_profile_id: str, bulk_operation_request: BulkOperationRequest)
```

**POST** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}/bulk`

Bulk Operation (bulkOperation)

Enqueues a bulk operation over the applications of the given agent profile and application profile and returns the created bulk action to track its progress.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |
| **bulk_operation_request** | **BulkOperationRequest** |  | |

### Return type

**AgentBulkAction**


## delete_agent_profile

```python
None client.delete_agent_profile(agent_profile_id: str)
```

**DELETE** `/api/agent/profile/{agentProfileId}`

Delete Agent Profile (deleteAgentProfile)

Deletes the Agent Profile. Referencing a non-existing Agent Profile Id will cause an error. The default Agent Profile can not be deleted.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |

### Return type

None (empty response body)


## get_agent_profile_app_profile_bulk_actions

```python
PageDataAgentBulkAction client.get_agent_profile_app_profile_bulk_actions(agent_profile_id: str, application_profile_id: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}/bulk`

Get Bulk Actions for Agent Profile and Application Profile (getAgentProfileAppProfileBulkActions)

Returns a page of bulk actions previously submitted for the given agent profile and application profile pair. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataAgentBulkAction**


## get_agent_profile_app_profile_infos

```python
List[AgentAppProfileRelationInfo] client.get_agent_profile_app_profile_infos(agent_profile_id: str)
```

**GET** `/api/agent/profile/{agentProfileId}/appProfilesInfo`

Get Agent Profile App Profile Infos (getAgentProfileAppProfileInfos)

Returns app profiles assigned to the given agent profile, enriched with template version, the count of AgentApplications using each app profile within this agent profile and the additional info of the assignment relation.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |

### Return type

**List[AgentAppProfileRelationInfo]**


## get_agent_profile_bulk_actions

```python
PageDataAgentBulkAction client.get_agent_profile_bulk_actions(agent_profile_id: str, page_size: int, page: int, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/agent/profile/{agentProfileId}/bulk`

Get Bulk Actions for Agent Profile (getAgentProfileBulkActions)

Returns a page of bulk actions previously submitted for the given agent profile. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataAgentBulkAction**


## get_agent_profile_by_id

```python
AgentProfile client.get_agent_profile_by_id(agent_profile_id: str)
```

**GET** `/api/agent/profile/{agentProfileId}`

Get Agent Profile (getAgentProfileById)

Fetch the Agent Profile object based on the provided Agent Profile Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |

### Return type

**AgentProfile**


## get_agent_profile_info_by_id

```python
AgentProfileInfo client.get_agent_profile_info_by_id(agent_profile_id: str)
```

**GET** `/api/agent/profile/info/{agentProfileId}`

Get Agent Profile Info (getAgentProfileInfoById)

Fetch the Agent Profile Info object based on the provided Agent Profile Id. Agent Profile Info is a lightweight object that omits the auto-provision key and secret; it is readable by any tenant admin so agent screens can resolve the linked profile.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |

### Return type

**AgentProfileInfo**


## get_agent_provision_instructions

```python
AgentInstructions client.get_agent_provision_instructions(agent_profile_id: str, method: str)
```

**GET** `/api/agent/profile/instructions/provision/{agentProfileId}/{method}`

Get Agent Provision Instructions (getAgentProvisionInstructions)

Returns the auto-provision docker command for the specified agent profile with the server address and gRPC port resolved server-side.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **method** | **str** | Installation method ('docker') | [enum: docker] |

### Return type

**AgentInstructions**


## get_default_agent_profile_info

```python
AgentProfileInfo client.get_default_agent_profile_info()
```

**GET** `/api/agent/profile/info/default`

Get Default Agent Profile (getDefaultAgentProfileInfo)

Fetch the Agent Profile Info object that is marked as default within the current tenant scope.  Available for users with 'TENANT_ADMIN' authority.

### Return type

**AgentProfileInfo**


## get_tenant_agent_profile_infos

```python
PageDataAgentProfileInfo client.get_tenant_agent_profile_infos(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/agent/profileInfos`

Get Tenant Agent Profile Infos (getTenantAgentProfileInfos)

Returns a page of Agent Profile Info objects owned by the current tenant. Agent Profile Info is a lightweight object that contains only id and name of the profile. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** |  | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataAgentProfileInfo**


## get_tenant_agent_profiles

```python
PageDataAgentProfile client.get_tenant_agent_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/agent/profiles`

Get Tenant Agent Profiles (getTenantAgentProfiles)

Returns a page of Agent Profile objects owned by the current tenant. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** |  | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] |

### Return type

**PageDataAgentProfile**


## preview_bulk_operation

```python
BulkOperationPreview client.preview_bulk_operation(agent_profile_id: str, application_profile_id: str, bulk_operation_request: BulkOperationRequest)
```

**POST** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}/bulk/preview`

Preview Bulk Operation (previewBulkOperation)

Previews the effect of a bulk operation over the applications of the given agent profile and application profile without enqueuing it, returning the set of affected applications and the resulting actions.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |
| **bulk_operation_request** | **BulkOperationRequest** |  | |

### Return type

**BulkOperationPreview**


## save_agent_profile

```python
AgentProfile client.save_agent_profile(agent_profile: AgentProfile, app_profile_ids: Optional[List[str]] = None)
```

**POST** `/api/agent/profile`

Create or Update Agent Profile (saveAgentProfile)

Creates or updates the Agent Profile. When an id is not present in the request, a new Agent Profile is created, otherwise the existing one is updated. Optionally synchronizes the agent application profile assignments in the same request: when the 'appProfileIds' parameter is absent, existing assignments are left untouched; when it is present, the assignment set is replaced with the given ids — including an explicitly empty value (e.g. 'appProfileIds='), which removes all assignments.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile** | **AgentProfile** |  | |
| **app_profile_ids** | **List[str]** | Agent application profile ids to assign to this agent profile. Absent: assignments are not modified. Present: assignments are replaced with the given ids; an explicitly empty value removes all assignments. | [optional] |

### Return type

**AgentProfile**


## set_app_profile_relates_on_auto_discovery

```python
None client.set_app_profile_relates_on_auto_discovery(agent_profile_id: str, application_profile_id: str, relate: bool)
```

**POST** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}/autoDiscovery`

Set App Profile Relates On Auto-Discovery (setAppProfileRelatesOnAutoDiscovery)

Enables or disables automatic assignment of the app profile to new auto-discovered applications with a matching template. Only one app profile per agent profile and template pair may relate on auto-discovery.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |
| **relate** | **bool** | Whether the app profile should be auto-assigned to new auto-discovered applications with a matching template | |

### Return type

None (empty response body)


## set_default_agent_profile

```python
AgentProfile client.set_default_agent_profile(agent_profile_id: str)
```

**POST** `/api/agent/profile/{agentProfileId}/default`

Make Agent Profile Default (setDefaultAgentProfile)

Marks agent profile as default within a tenant scope.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |

### Return type

**AgentProfile**


## unassign_app_profile_from_agent_profile

```python
None client.unassign_app_profile_from_agent_profile(agent_profile_id: str, application_profile_id: str)
```

**DELETE** `/api/agent/profile/{agentProfileId}/appProfile/{applicationProfileId}`

Unassign App Profile from Agent Profile (unassignAppProfileFromAgentProfile)

Removes the assignment of the given agent application profile from the agent profile.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_profile_id** | **str** | Agent Profile Id | |
| **application_profile_id** | **str** | Agent Application Profile Id | |

### Return type

None (empty response body)

