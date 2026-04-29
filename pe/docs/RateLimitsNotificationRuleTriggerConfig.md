
# RateLimitsNotificationRuleTriggerConfig

`tb_pe_client.models.RateLimitsNotificationRuleTriggerConfig`

**Extends:** **NotificationRuleTriggerConfig**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **apis** | [**List[LimitedApi]**](LimitedApi.md) |  | [optional] |



## Referenced Types

#### NotificationRuleTriggerConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| trigger_type | NotificationRuleTriggerType |  |  |

#### LimitedApi (enum)
`ENTITY_EXPORT` | `ENTITY_IMPORT` | `NOTIFICATION_REQUESTS` | `NOTIFICATION_REQUESTS_PER_RULE` | `REST_REQUESTS_PER_TENANT` | `REST_REQUESTS_PER_CUSTOMER` | `WS_UPDATES_PER_SESSION` | `CASSANDRA_WRITE_QUERIES_CORE` | `CASSANDRA_READ_QUERIES_CORE` | `CASSANDRA_WRITE_QUERIES_RULE_ENGINE` | … (36 values total)

#### NotificationRuleTriggerType (enum)
`ENTITY_ACTION` | `ALARM` | `ALARM_COMMENT` | `ALARM_ASSIGNMENT` | `DEVICE_ACTIVITY` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `INTEGRATION_LIFECYCLE_EVENT` | `EDGE_CONNECTION` | `EDGE_COMMUNICATION_FAILURE` | `NEW_PLATFORM_VERSION` | … (15 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.apis`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `RateLimitsNotificationRuleTriggerConfig.model_validate(data)` or `RateLimitsNotificationRuleTriggerConfig.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

