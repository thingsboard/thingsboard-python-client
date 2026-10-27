
# ActionType

`tb_ce_client.models.ActionType`

## Enum Values


* `ADDED` (value: `'ADDED'`)

* `DELETED` (value: `'DELETED'`)

* `UPDATED` (value: `'UPDATED'`)

* `ATTRIBUTES_UPDATED` (value: `'ATTRIBUTES_UPDATED'`)

* `ATTRIBUTES_DELETED` (value: `'ATTRIBUTES_DELETED'`)

* `TIMESERIES_UPDATED` (value: `'TIMESERIES_UPDATED'`)

* `TIMESERIES_DELETED` (value: `'TIMESERIES_DELETED'`)

* `RPC_CALL` (value: `'RPC_CALL'`)

* `CREDENTIALS_UPDATED` (value: `'CREDENTIALS_UPDATED'`)

* `ASSIGNED_TO_CUSTOMER` (value: `'ASSIGNED_TO_CUSTOMER'`)

* `UNASSIGNED_FROM_CUSTOMER` (value: `'UNASSIGNED_FROM_CUSTOMER'`)

* `ACTIVATED` (value: `'ACTIVATED'`)

* `SUSPENDED` (value: `'SUSPENDED'`)

* `CREDENTIALS_READ` (value: `'CREDENTIALS_READ'`)

* `ATTRIBUTES_READ` (value: `'ATTRIBUTES_READ'`)

* `RELATION_ADD_OR_UPDATE` (value: `'RELATION_ADD_OR_UPDATE'`)

* `RELATION_DELETED` (value: `'RELATION_DELETED'`)

* `RELATIONS_DELETED` (value: `'RELATIONS_DELETED'`)

* `REST_API_RULE_ENGINE_CALL` (value: `'REST_API_RULE_ENGINE_CALL'`)

* `ALARM_ACK` (value: `'ALARM_ACK'`)

* `ALARM_CLEAR` (value: `'ALARM_CLEAR'`)

* `ALARM_DELETE` (value: `'ALARM_DELETE'`)

* `ALARM_ASSIGNED` (value: `'ALARM_ASSIGNED'`)

* `ALARM_UNASSIGNED` (value: `'ALARM_UNASSIGNED'`)

* `LOGIN` (value: `'LOGIN'`)

* `LOGOUT` (value: `'LOGOUT'`)

* `LOCKOUT` (value: `'LOCKOUT'`)

* `ASSIGNED_FROM_TENANT` (value: `'ASSIGNED_FROM_TENANT'`)

* `ASSIGNED_TO_TENANT` (value: `'ASSIGNED_TO_TENANT'`)

* `PROVISION_SUCCESS` (value: `'PROVISION_SUCCESS'`)

* `PROVISION_FAILURE` (value: `'PROVISION_FAILURE'`)

* `ASSIGNED_TO_EDGE` (value: `'ASSIGNED_TO_EDGE'`)

* `UNASSIGNED_FROM_EDGE` (value: `'UNASSIGNED_FROM_EDGE'`)

* `ADDED_COMMENT` (value: `'ADDED_COMMENT'`)

* `UPDATED_COMMENT` (value: `'UPDATED_COMMENT'`)

* `DELETED_COMMENT` (value: `'DELETED_COMMENT'`)

* `SMS_SENT` (value: `'SMS_SENT'`)

* `COMMUNITY_GRANT_OFFLINE_CHECKER_RUN` (value: `'COMMUNITY_GRANT_OFFLINE_CHECKER_RUN'`)

* `COMMUNITY_GRANT_REQUEST_ACCESS` (value: `'COMMUNITY_GRANT_REQUEST_ACCESS'`)

* `COMMUNITY_GRANT_ENROLLMENT` (value: `'COMMUNITY_GRANT_ENROLLMENT'`)



---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ActionType.model_validate(data)` or `ActionType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

