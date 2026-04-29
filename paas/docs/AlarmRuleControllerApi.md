# AlarmRuleControllerApi

`ThingsboardClient` methods:

```python
None client.delete_alarm_rule(alarm_rule_id: str)  # Delete Alarm Rule (deleteAlarmRule)
AlarmRuleDefinition client.get_alarm_rule_by_id(alarm_rule_id: str)  # Get Alarm Rule (getAlarmRuleById)
PageDataString client.get_alarm_rule_names(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)  # Get alarm rule names (getAlarmRuleNames)
PageDataAlarmRuleDefinitionInfo client.get_alarm_rules(page_size: int, page: int, entity_type: Optional[EntityType] = None, entities: Optional[List[UUID]] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get alarm rules (getAlarmRules)
PageDataAlarmRuleDefinition client.get_alarm_rules_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)  # Get Alarm Rules by Entity Id (getAlarmRulesByEntityId)
object client.get_latest_alarm_rule_debug_event(alarm_rule_id: str)  # Get latest alarm rule debug event (getLatestAlarmRuleDebugEvent)
AlarmRuleDefinition client.save_alarm_rule(alarm_rule_definition: AlarmRuleDefinition)  # Create Or Update Alarm Rule (saveAlarmRule)
object client.test_alarm_rule_script(body: object)  # Test alarm rule TBEL expression (testAlarmRuleScript)
```


## delete_alarm_rule

```python
None client.delete_alarm_rule(alarm_rule_id: str)
```

**DELETE** `/api/alarm/rule/{alarmRuleId}`

Delete Alarm Rule (deleteAlarmRule)

Deletes the alarm rule. Referencing non-existing Alarm Rule Id will cause an error.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_rule_id** | **str** |  | |

### Return type

None (empty response body)


## get_alarm_rule_by_id

```python
AlarmRuleDefinition client.get_alarm_rule_by_id(alarm_rule_id: str)
```

**GET** `/api/alarm/rule/{alarmRuleId}`

Get Alarm Rule (getAlarmRuleById)

Fetch the Alarm Rule object based on the provided Alarm Rule Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_rule_id** | **str** |  | |

### Return type

**AlarmRuleDefinition**


## get_alarm_rule_names

```python
PageDataString client.get_alarm_rule_names(page_size: int, page: int, text_search: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/alarm/rules/names`

Get alarm rule names (getAlarmRuleNames)

Fetch the list of alarm rule names.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataString**


## get_alarm_rules

```python
PageDataAlarmRuleDefinitionInfo client.get_alarm_rules(page_size: int, page: int, entity_type: Optional[EntityType] = None, entities: Optional[List[UUID]] = None, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/alarm/rules`

Get alarm rules (getAlarmRules)

Fetch tenant alarm rules based on the filter.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **entity_type** | **EntityType** | Entity type filter. If not specified, alarm rules for all supported entity types will be returned. | [optional] [enum: TENANT, CUSTOMER, USER, DASHBOARD, ASSET, DEVICE, ALARM, ENTITY_GROUP, CONVERTER, INTEGRATION, RULE_CHAIN, RULE_NODE, SCHEDULER_EVENT, BLOB_ENTITY, REPORT_TEMPLATE, REPORT, ENTITY_VIEW, WIDGETS_BUNDLE, WIDGET_TYPE, ROLE, GROUP_PERMISSION, TENANT_PROFILE, DEVICE_PROFILE, ASSET_PROFILE, API_USAGE_STATE, TB_RESOURCE, OTA_PACKAGE, EDGE, RPC, QUEUE, NOTIFICATION_TARGET, NOTIFICATION_TEMPLATE, NOTIFICATION_REQUEST, NOTIFICATION, NOTIFICATION_RULE, QUEUE_STATS, OAUTH2_CLIENT, DOMAIN, MOBILE_APP, MOBILE_APP_BUNDLE, CALCULATED_FIELD, JOB, SECRET, ADMIN_SETTINGS, AI_MODEL, API_KEY, BILLING_CUSTOMER, SUBSCRIPTION_PLAN, SUBSCRIPTION, COUPON, PRODUCT, SUBSCRIPTION_ADDON] |
| **entities** | **List[UUID]** | Entities filter. If not specified, alarm rules for entity type filter will be returned. | [optional] |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAlarmRuleDefinitionInfo**


## get_alarm_rules_by_entity_id

```python
PageDataAlarmRuleDefinition client.get_alarm_rules_by_entity_id(entity_type: str, entity_id: str, page_size: int, page: int, text_search: Optional[str] = None, sort_property: Optional[str] = None, sort_order: Optional[str] = None)
```

**GET** `/api/alarm/rules/{entityType}/{entityId}`

Get Alarm Rules by Entity Id (getAlarmRulesByEntityId)

Fetch the Alarm Rules based on the provided Entity Id.  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **entity_type** | **str** | A string value representing the entity type. For example, 'DEVICE' | |
| **entity_id** | **str** | A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' | |
| **page_size** | **int** | Maximum amount of entities in a one page | |
| **page** | **int** | Sequence number of page starting from 0 | |
| **text_search** | **str** | The case insensitive 'substring' filter based on the calculated field name. | [optional] |
| **sort_property** | **str** | Property of entity to sort by | [optional] [enum: createdTime, name] |
| **sort_order** | **str** | Sort order. ASC (ASCENDING) or DESC (DESCENDING) | [optional] [enum: ASC, DESC] |

### Return type

**PageDataAlarmRuleDefinition**


## get_latest_alarm_rule_debug_event

```python
object client.get_latest_alarm_rule_debug_event(alarm_rule_id: str)
```

**GET** `/api/alarm/rule/{alarmRuleId}/debug`

Get latest alarm rule debug event (getLatestAlarmRuleDebugEvent)

Gets latest alarm rule debug event for specified alarm rule id. Referencing non-existing alarm rule id will cause an error.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_rule_id** | **str** |  | |

### Return type

**object**


## save_alarm_rule

```python
AlarmRuleDefinition client.save_alarm_rule(alarm_rule_definition: AlarmRuleDefinition)
```

**POST** `/api/alarm/rule`

Create Or Update Alarm Rule (saveAlarmRule)

Creates or Updates the Alarm Rule. When creating alarm rule, platform generates Alarm Rule Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm Rule Id will be present in the response. Specify existing Alarm Rule Id to update the alarm rule. Referencing non-existing Alarm Rule Id will cause 'Not Found' error. Remove 'id', 'tenantId' from the request body example (below) to create new Alarm Rule entity.   Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alarm_rule_definition** | **AlarmRuleDefinition** | A JSON value representing the alarm rule. | |

### Return type

**AlarmRuleDefinition**


## test_alarm_rule_script

```python
object client.test_alarm_rule_script(body: object)
```

**POST** `/api/alarm/rule/testScript`

Test alarm rule TBEL expression (testAlarmRuleScript)

Execute the alarm rule TBEL condition expression and return the result. Alarm rule expressions must return a boolean value. The format of request:   ```json {   \"expression\": \"return temperature > 50;\",   \"arguments\": {     \"temperature\": { \"type\": \"SINGLE_VALUE\", \"ts\": 1739776478057, \"value\": 55 }   } } ```   Expected result JSON contains \"output\" and \"error\".  Available for users with 'TENANT_ADMIN' authority.


### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **object** | Test alarm rule TBEL condition expression. The expression must return a boolean value. | |

### Return type

**object**

