
# NotificationRuleInfo

`tb_pe_client.models.NotificationRuleInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**NotificationRuleId**](NotificationRuleId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **name** | **str** |  | |
| **enabled** | **bool** |  | [optional] |
| **template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | |
| **trigger_type** | [**NotificationRuleTriggerType**](NotificationRuleTriggerType.md) |  | |
| **trigger_config** | [**NotificationRuleTriggerConfig**](NotificationRuleTriggerConfig.md) |  | |
| **recipients_config** | [**NotificationRuleRecipientsConfig**](NotificationRuleRecipientsConfig.md) |  | |
| **additional_config** | [**NotificationRuleConfig**](NotificationRuleConfig.md) |  | [optional] |
| **template_name** | **str** |  | [optional] |
| **delivery_methods** | [**List[NotificationDeliveryMethod]**](NotificationDeliveryMethod.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `INTEGRATION_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | … (15 values total)

#### NotificationRuleTriggerConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  |  |

#### AlarmNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ALARM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| notify_on | List[AlarmAction] |  |  |
| clear_rule | ClearRule |  | [optional] |

#### AlarmAssignmentNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| notify_on | List[Action] |  |  |

#### AlarmCommentNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_types | List[str] |  | [optional] |
| alarm_severities | List[AlarmSeverity] |  | [optional] |
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |
| only_user_comments | bool |  | [optional] |
| notify_on_comment_update | bool |  | [optional] |

#### ApiUsageLimitNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| api_features | List[ApiFeature] |  | [optional] |
| notify_on | List[ApiUsageStateValue] |  | [optional] |

#### DeviceActivityNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| devices | List[UUID] |  | [optional] |
| device_profiles | List[UUID] |  | [optional] |
| notify_on | List[DeviceEvent] |  |  |

#### EdgeCommunicationFailureNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |

#### EdgeConnectionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edges | List[UUID] |  | [optional] |
| notify_on | List[EdgeConnectivityEvent] |  | [optional] |

#### EntitiesLimitNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| threshold | float |  | [optional] |

#### EntityActionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_types | List[EntityType] |  | [optional] |
| created | bool |  | [optional] |
| updated | bool |  | [optional] |
| deleted | bool |  | [optional] |

#### IntegrationLifecycleEventNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`INTEGRATION_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| integration_types | List[IntegrationType] |  | [optional] |
| integrations | List[UUID] |  | [optional] |
| notify_on | List[ComponentLifecycleEvent] |  | [optional] |
| only_on_error | bool |  | [optional] |

#### NewPlatformVersionNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`NEW_PLATFORM_VERSION`)*
*See NotificationRuleTriggerConfig for properties.*

#### RateLimitsNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| apis | List[LimitedApi] |  | [optional] |

#### ResourcesShortageNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cpu_threshold | float |  | [optional] |
| ram_threshold | float |  | [optional] |
| storage_threshold | float |  | [optional] |

#### RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| rule_chains | List[UUID] |  | [optional] |
| rule_chain_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_chain_lifecycle_failures | bool |  | [optional] |
| track_rule_node_events | bool |  | [optional] |
| rule_node_events | List[ComponentLifecycleEvent] |  | [optional] |
| only_rule_node_lifecycle_failures | bool |  | [optional] |

#### TaskProcessingFailureNotificationRuleTriggerConfig  *(extends NotificationRuleTriggerConfig, trigger_type=`TASK_PROCESSING_FAILURE`)*
*See NotificationRuleTriggerConfig for properties.*

#### NotificationRuleRecipientsConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  | [optional] |

#### EscalatedNotificationRuleRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ALARM`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| escalation_table | Dict[str, List[UUID]] |  |  |

#### AlarmAssignmentRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ALARM_ASSIGNMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### AlarmCommentRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ALARM_COMMENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ApiUsageLimitRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`API_USAGE_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### DeviceActivityRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`DEVICE_ACTIVITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeCommunicationFailureRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`EDGE_COMMUNICATION_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EdgeConnectionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`EDGE_CONNECTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntitiesLimitRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ENTITIES_LIMIT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### EntityActionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`ENTITY_ACTION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### IntegrationLifecycleEventRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`INTEGRATION_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### NewPlatformVersionRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`NEW_PLATFORM_VERSION`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RateLimitsRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RATE_LIMITS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### ResourceShortageRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RESOURCES_SHORTAGE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### RuleEngineComponentLifecycleEventRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### TaskProcessingFailureRecipientsConfig  *(extends NotificationRuleRecipientsConfig, trigger_type=`TASK_PROCESSING_FAILURE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| targets | List[UUID] |  |  |

#### NotificationRuleConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| description | str |  | [optional] |

#### NotificationDeliveryMethod (enum)
`WEB` | `EMAIL` | `SMS` | `SLACK` | `MICROSOFT_TEAMS` | `MOBILE_APP`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### AlarmAction (enum)
`CREATED` | `SEVERITY_CHANGED` | `ACKNOWLEDGED` | `CLEARED`

#### ClearRule
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alarm_statuses | List[AlarmSearchStatus] |  | [optional] |

#### DeviceEvent (enum)
`ACTIVE` | `INACTIVE`

#### AlarmSearchStatus (enum)
`ANY` | `ACTIVE` | `CLEARED` | `ACK` | `UNACK`

#### ComponentLifecycleEvent (enum)
`CREATED` | `STARTED` | `ACTIVATED` | `SUSPENDED` | `UPDATED` | `STOPPED` | `DELETED` | `FAILED` | `DEACTIVATED` | `RELATION_UPDATED` | … (11 values total)

#### Action (enum)
`ASSIGNED` | `UNASSIGNED`

#### ApiFeature (enum)
`TRANSPORT` | `DB` | `RE` | `JS` | `TBEL` | `EMAIL` | `SMS` | `ALARM` | `REPORT` | `AI`

#### ApiUsageStateValue (enum)
`ENABLED` | `WARNING` | `DISABLED`

#### LimitedApi (enum)
`ENTITY_EXPORT` | `ENTITY_IMPORT` | `NOTIFICATION_REQUESTS` | `NOTIFICATION_REQUESTS_PER_RULE` | `REST_REQUESTS_PER_TENANT` | `REST_REQUESTS_PER_CUSTOMER` | `WS_UPDATES_PER_SESSION` | `CASSANDRA_WRITE_QUERIES_CORE` | `CASSANDRA_READ_QUERIES_CORE` | `CASSANDRA_WRITE_QUERIES_RULE_ENGINE` | … (36 values total)

#### EdgeConnectivityEvent (enum)
`CONNECTED` | `DISCONNECTED`

#### IntegrationType (enum)
`OCEANCONNECT` | `SIGFOX` | `THINGPARK` | `TPE` | `CHIRPSTACK` | `PARTICLE` | `TMOBILE_IOT_CDP` | `HTTP` | `MQTT` | `PUB_SUB` | … (29 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleInfo.model_validate(data)` or `NotificationRuleInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

