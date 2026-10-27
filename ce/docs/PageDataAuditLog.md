
# PageDataAuditLog

`tb_ce_client.models.PageDataAuditLog`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[AuditLog]**](AuditLog.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `CalculatedFieldId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityViewId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AuditLog
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AuditLogId | JSON object with the auditLog Id | [optional] |
| created_time | int | Timestamp of the auditLog creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id | [optional] [readonly] |
| entity_id | EntityId | JSON object with Entity id | [optional] [readonly] |
| entity_name | str | Name of the logged entity | [optional] [readonly] |
| user_id | UserId | JSON object with User id. | [optional] [readonly] |
| user_name | str | Unique user name(email) of the user that performed some action on logged entity | [optional] [readonly] |
| action_type | ActionType | String represented Action type | [optional] [readonly] |
| action_data | object | JsonNode represented action data | [optional] [readonly] |
| action_status | ActionStatus | String represented Action status | [optional] [readonly] |
| action_failure_details | str | Failure action details info. An empty string in case of action status type 'SUCCESS', otherwise includes stack trace of the caused exception. | [optional] [readonly] |

#### AuditLogId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UUID | string |  |

#### ActionType (enum)
`ADDED` | `DELETED` | `UPDATED` | `ATTRIBUTES_UPDATED` | `ATTRIBUTES_DELETED` | `TIMESERIES_UPDATED` | `TIMESERIES_DELETED` | `RPC_CALL` | `CREDENTIALS_UPDATED` | `ASSIGNED_TO_CUSTOMER` | … (40 values total)

#### ActionStatus (enum)
`SUCCESS` | `FAILURE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAuditLog.model_validate(data)` or `PageDataAuditLog.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

