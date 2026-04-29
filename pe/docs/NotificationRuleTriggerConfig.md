
# NotificationRuleTriggerConfig

`tb_pe_client.models.NotificationRuleTriggerConfig`

Configuration for notification rule trigger

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **trigger_type** | [**NotificationRuleTriggerType**](NotificationRuleTriggerType.md) |  | |



## Subtypes

#### AlarmNotificationRuleTriggerConfig  *(trigger_type=`ALARM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| notify_on | List[AlarmAction] |  |  |
| clear_rule | ClearRule |  | [optional] |

#### AlarmAssignmentNotificationRuleTriggerConfig  *(trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| notify_on | List[Action] |  |  |

#### AlarmCommentNotificationRuleTriggerConfig  *(trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| only_user_comments | bool |  | [optional] |
| notify_on_comment_update | bool |  | [optional] |

#### ApiUsageLimitNotificationRuleTriggerConfig  *(trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_features | List[ApiFeature] |  | [optional] |
| notify_on | List[ApiUsageStateValue] |  | [optional] |

#### DeviceActivityNotificationRuleTriggerConfig  *(trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| devices | List[UUID] |  | [optional] |
| device_profiles | List[UUID] |  | [optional] |
| notify_on | List[DeviceEvent] |  |  |

#### EdgeCommunicationFailureNotificationRuleTriggerConfig  *(trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |

#### EdgeConnectionNotificationRuleTriggerConfig  *(trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |
| notify_on | List[EdgeConnectivityEvent] |  | [optional] |

#### EntitiesLimitNotificationRuleTriggerConfig  *(trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| threshold | float |  | [optional] |

#### EntityActionNotificationRuleTriggerConfig  *(trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| created | bool |  | [optional] |
| updated | bool |  | [optional] |
| deleted | bool |  | [optional] |

#### IntegrationLifecycleEventNotificationRuleTriggerConfig  *(trigger_type=`INTEGRATION_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| integration_types | List[IntegrationType] |  | [optional] |
| integrations | List[UUID] |  | [optional] |
| notify_on | List[ComponentLifecycleEvent] |  | [optional] |
| only_on_error | bool |  | [optional] |

#### NewPlatformVersionNotificationRuleTriggerConfig  *(trigger_type=`NEW_PLATFORM_VERSION`)*
*(no additional properties)*

#### RateLimitsNotificationRuleTriggerConfig  *(trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| apis | List[LimitedApi] |  | [optional] |

#### ResourcesShortageNotificationRuleTriggerConfig  *(trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cpu_threshold | float |  | [optional] |
| ram_threshold | float |  | [optional] |
| storage_threshold | float |  | [optional] |

#### RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig  *(trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| rule_chains | List[UUID] |  | [optional] |
| rule_chain_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_chain_lifecycle_failures | bool |  | [optional] |
| track_rule_node_events | bool |  | [optional] |
| rule_node_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_node_lifecycle_failures | bool |  | [optional] |

#### TaskProcessingFailureNotificationRuleTriggerConfig  *(trigger_type=`TASK_PROCESSING_FAILURE`)*
*(no additional properties)*

## Referenced Types

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `INTEGRATION_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | … (15 values total)

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### AlarmAction (enum)
`CREATED` | `SEVERITY_CHANGED` | `ACKNOWLEDGED` | `CLEARED`

#### ClearRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### Action (enum)
`ASSIGNED` | `UNASSIGNED`

#### ApiFeature (enum)
`TRANSPORT` | `DB` | `RE` | `JS` | `TBEL` | `EMAIL` | `SMS` | `ALARM` | `REPORT` | `AI`

#### ApiUsageStateValue (enum)
`ENABLED` | `WARNING` | `DISABLED`

#### DeviceEvent (enum)
`ACTIVE` | `INACTIVE`

#### EdgeConnectivityEvent (enum)
`CONNECTED` | `DISCONNECTED`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

#### IntegrationType (enum)
`OCEANCONNECT` | `SIGFOX` | `THINGPARK` | `TPE` | `CHIRPSTACK` | `PARTICLE` | `TMOBILE_IOT_CDP` | `HTTP` | `MQTT` | `PUB_SUB` | … (29 values total)

#### ComponentLifecycleEvent (enum)
`CREATED` | `STARTED` | `ACTIVATED` | `SUSPENDED` | `UPDATED` | `STOPPED` | `DELETED` | `FAILED` | `DEACTIVATED` | `RELATION_UPDATED` | … (11 values total)

#### LimitedApi (enum)
`ENTITY_EXPORT` | `ENTITY_IMPORT` | `NOTIFICATION_REQUESTS` | `NOTIFICATION_REQUESTS_PER_RULE` | `REST_REQUESTS_PER_TENANT` | `REST_REQUESTS_PER_CUSTOMER` | `WS_UPDATES_PER_SESSION` | `CASSANDRA_WRITE_QUERIES_CORE` | `CASSANDRA_READ_QUERIES_CORE` | `CASSANDRA_WRITE_QUERIES_RULE_ENGINE` | … (36 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.trigger_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleTriggerConfig.model_validate(data)` or `NotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

