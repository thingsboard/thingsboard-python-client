# AgentAppProfileControllerApi

`ThingsboardClient` methods:

```python
None client.delete_agent_app_profile(profile_id: str)  # Delete Agent Application Profile (deleteAgentAppProfile)
AgentAppProfile client.get_agent_app_profile_by_id(profile_id: str)  # Get Agent Application Profile (getAgentAppProfileById)
AgentAppProfileInfo client.get_agent_app_profile_info_by_id(profile_id: str)  # Get Agent Application Profile Info (getAgentAppProfileInfoById)
List[AgentAppProfileInfo] client.get_agent_app_profiles_by_app_type(app_type: AgentApplicationType)  # Get Agent Application Profiles by app type (getAgentAppProfilesByAppType)
List[AgentAppProfile] client.get_agent_app_profiles_by_ids(agent_app_profile_ids: List[str])  # Get Agent Application Profiles By Ids (getAgentAppProfilesByIds)
PageDataAgentAppProfile client.get_tenant_agent_app_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Tenant Agent Application Profiles (getTenantAgentAppProfiles)
AgentAppProfile client.materialize_agent_app_profile(app_type: AgentApplicationType, template_version: str, compose_type: Optional[str] = None)  # Create Agent Application Profile from template (materializeAgentAppProfile)
AgentAppProfile client.merge_agent_app_profile_for_preview(template_version: str, agent_app_profile: AgentAppProfile, compose_type: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, set_host_values: Optional[bool] = None)  # Merge template into application profile for preview (mergeAgentAppProfileForPreview)
AgentAppProfile client.save_agent_app_profile(agent_app_profile: AgentAppProfile)  # Create or Update Agent Application Profile (saveAgentAppProfile)
```


## delete_agent_app_profile

```python
None client.delete_agent_app_profile(profile_id: str)
```

**DELETE** `/api/agent/app/profile/{profileId}`

Delete Agent Application Profile (deleteAgentAppProfile)

Deletes the agent application profile. Cannot delete if referenced by applications.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str** | Profile Id | |

### Return type

None (empty response body)


## get_agent_app_profile_by_id

```python
AgentAppProfile client.get_agent_app_profile_by_id(profile_id: str)
```

**GET** `/api/agent/app/profile/{profileId}`

Get Agent Application Profile (getAgentAppProfileById)

Fetch the Agent Application Profile by Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str** | Profile Id | |

### Return type

**AgentAppProfile**


## get_agent_app_profile_info_by_id

```python
AgentAppProfileInfo client.get_agent_app_profile_info_by_id(profile_id: str)
```

**GET** `/api/agent/app/profile/info/{profileId}`

Get Agent Application Profile Info (getAgentAppProfileInfoById)

Fetch the Agent Application Profile Info by Id. Readable by any tenant admin without AGENT_APP_PROFILE permission, so agent/application screens can resolve the linked profile. Returns the full profile, config and arguments included - an application profile carries deployment configuration rather than credentials, so it is not gated like other profiles.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **profile_id** | **str** | Profile Id | |

### Return type

**AgentAppProfileInfo**


## get_agent_app_profiles_by_app_type

```python
List[AgentAppProfileInfo] client.get_agent_app_profiles_by_app_type(app_type: AgentApplicationType)
```

**GET** `/api/agent/app/profiles/{appType}`

Get Agent Application Profiles by app type (getAgentAppProfilesByAppType)

Returns a list of agent application profiles filtered by application type.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **app_type** | **AgentApplicationType** | Application type, e.g. 'EDGE', 'GATEWAY', 'GENERIC' | [enum: GENERIC, EDGE, GATEWAY] |

### Return type

**List[AgentAppProfileInfo]**


## get_agent_app_profiles_by_ids

```python
List[AgentAppProfile] client.get_agent_app_profiles_by_ids(agent_app_profile_ids: List[str])
```

**GET** `/api/agent/app/profiles`

Get Agent Application Profiles By Ids (getAgentAppProfilesByIds)

Requested agent application profiles must be owned by tenant which is performing the request.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_app_profile_ids** | **List[str]** | A list of agent application profile ids, separated by comma ',' | |

### Return type

**List[AgentAppProfile]**


## get_tenant_agent_app_profiles

```python
PageDataAgentAppProfile client.get_tenant_agent_app_profiles(page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/tenant/agent/app/profiles`

Get Tenant Agent Application Profiles (getTenantAgentAppProfiles)

Returns a page of agent application profiles owned by tenant.You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See response schema for more details.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | Optional search text | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAgentAppProfile**


## materialize_agent_app_profile

```python
AgentAppProfile client.materialize_agent_app_profile(app_type: AgentApplicationType, template_version: str, compose_type: Optional[str] = None)
```

**POST** `/api/agent/app/profile/materialize/{appType}/{templateVersion}`

Create Agent Application Profile from template (materializeAgentAppProfile)

Creates an agent application profile from the default configuration of the template with the given app type and version. Used to materialize a predefined (virtual) profile shown in the UI into a real profile on first use. If a profile with the given app type and template version already exists, the existing profile is returned (the oldest one by created time) instead of creating a new one.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **app_type** | **AgentApplicationType** | Application type, e.g. 'EDGE', 'GATEWAY', 'GENERIC' | [enum: GENERIC, EDGE, GATEWAY] |
| **template_version** | **str** | The template version to materialize (e.g. '4.3.1.2EDGEPE') | |
| **compose_type** | **str** | The compose type to select from the template (e.g. 'in_memory', 'kafka'). Defaults to the template's first compose type. | [optional] |

### Return type

**AgentAppProfile**


## merge_agent_app_profile_for_preview

```python
AgentAppProfile client.merge_agent_app_profile_for_preview(template_version: str, agent_app_profile: AgentAppProfile, compose_type: Optional[str] = None, action_type: Optional[AgentAppEventActionType] = None, set_host_values: Optional[bool] = None)
```

**POST** `/api/agent/app/profiles/merge/{templateVersion}/preview`

Merge template into application profile for preview (mergeAgentAppProfileForPreview)

Merges the specified template into an agent application profile for preview purposes. The compose type determines which compose configuration variant from the template is used.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **template_version** | **str** | The template version to merge (e.g. '4.3.1.2EDGEPE') | |
| **agent_app_profile** | **AgentAppProfile** | Agent application profile to merge template with | |
| **compose_type** | **str** | The compose type to select from the template (e.g. 'monolith', 'microservices') | [optional] |
| **action_type** | **AgentAppEventActionType** | The event action this merge previews (e.g. UPGRADE). Drives action-specific merge rules. | [optional] [enum: INSTALL, UPDATE, DELETE, RESTART, ROLLBACK, UPGRADE, AGENT_UPGRADE] |
| **set_host_values** | **bool** | Whether to auto-fill host values (e.g. CLOUD_RPC_HOST) from the platform base URL. Should be true only for the install preview; keep false when previewing the saved compose of an existing profile to preserve user-configured host values. | [optional] [default to False] |

### Return type

**AgentAppProfile**


## save_agent_app_profile

```python
AgentAppProfile client.save_agent_app_profile(agent_app_profile: AgentAppProfile)
```

**POST** `/api/agent/app/profile`

Create or Update Agent Application Profile (saveAgentAppProfile)

Creates or updates an agent application profile.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **agent_app_profile** | **AgentAppProfile** |  | |

### Return type

**AgentAppProfile**

