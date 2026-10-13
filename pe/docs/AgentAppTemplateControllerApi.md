# AgentAppTemplateControllerApi

`ThingsboardClient` methods:

```python
AgentAppTemplate client.get_agent_app_template_by_current_version(app_type: AgentApplicationType, config_type: AgentAppConfigType, current_version: str)  # Get Agent App Template by current version (getAgentAppTemplateByCurrentVersion)
List[AgentAppTemplate] client.get_agent_app_templates()  # Get all Agent App Templates (getAgentAppTemplates)
List[AgentAppTemplate] client.get_agent_app_templates_by_app_type(app_type: AgentApplicationType, config_type: AgentAppConfigType)  # Get Agent App Templates by type (getAgentAppTemplatesByAppType)
AgentAppTemplate client.get_latest_agent_app_template_by_app_type_and_config_type(app_type: AgentApplicationType, config_type: AgentAppConfigType)  # Get Agent App Template (getLatestAgentAppTemplateByType)
```


## get_agent_app_template_by_current_version

```python
AgentAppTemplate client.get_agent_app_template_by_current_version(app_type: AgentApplicationType, config_type: AgentAppConfigType, current_version: str)
```

**GET** `/api/agent/app/template/{appType}/{configType}/version/{currentVersion}`

Get Agent App Template by current version (getAgentAppTemplateByCurrentVersion)

Fetch the Agent App Template object based on the provided app type, config type, and current version. Matches the version exactly, including a floating tag used as a version such as the gateway 'latest' tag.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **app_type** | **AgentApplicationType** | A string value representing the agent application type, e.g. 'EDGE', 'GATEWAY' | [enum: GENERIC, EDGE, GATEWAY] |
| **config_type** | **AgentAppConfigType** | A string value representing the agent configuration type, e.g. 'DOCKER_COMPOSE' | [enum: DOCKER_COMPOSE] |
| **current_version** | **str** | A string value representing the current version of the template, e.g. '1.0.0' | |

### Return type

**AgentAppTemplate**


## get_agent_app_templates

```python
List[AgentAppTemplate] client.get_agent_app_templates()
```

**GET** `/api/agent/app/templates`

Get all Agent App Templates (getAgentAppTemplates)

Returns a list of all agent app templates available for the current tenant.  Available for users with 'TENANT_ADMIN' authority.

### Return type

**List[AgentAppTemplate]**


## get_agent_app_templates_by_app_type

```python
List[AgentAppTemplate] client.get_agent_app_templates_by_app_type(app_type: AgentApplicationType, config_type: AgentAppConfigType)
```

**GET** `/api/agent/app/templates/{appType}/{configType}`

Get Agent App Templates by type (getAgentAppTemplatesByAppType)

Returns a list of agent app templates filtered by application type and config type.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **app_type** | **AgentApplicationType** | A string value representing the agent application type, e.g. 'EDGE', 'GATEWAY' | [enum: GENERIC, EDGE, GATEWAY] |
| **config_type** | **AgentAppConfigType** | A string value representing the agent configuration type, e.g. 'DOCKER_COMPOSE' | [enum: DOCKER_COMPOSE] |

### Return type

**List[AgentAppTemplate]**


## get_latest_agent_app_template_by_app_type_and_config_type

```python
AgentAppTemplate client.get_latest_agent_app_template_by_app_type_and_config_type(app_type: AgentApplicationType, config_type: AgentAppConfigType)
```

**GET** `/api/agent/app/template/{appType}/{configType}/latest`

Get Agent App Template (getLatestAgentAppTemplateByType)

Fetch the latest Agent App Template object for the given app type and config type.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **app_type** | **AgentApplicationType** | A string value representing the agent application type, e.g. 'EDGE', 'GATEWAY' | [enum: GENERIC, EDGE, GATEWAY] |
| **config_type** | **AgentAppConfigType** | A string value representing the agent configuration type, e.g. 'DOCKER_COMPOSE' | [enum: DOCKER_COMPOSE] |

### Return type

**AgentAppTemplate**

