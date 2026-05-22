
# PageDataSchedulerEventWithCustomerInfo

`tb_pe_client.models.PageDataSchedulerEventWithCustomerInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[SchedulerEventWithCustomerInfo]**](SchedulerEventWithCustomerInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### SchedulerEventWithCustomerInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | SchedulerEventId | JSON object with the scheduler event Id. Specify this field to update the scheduler event. Referencing non-existing scheduler event Id will cause error. Omit this field to create new scheduler event | [optional] |
| created_time | int | Timestamp of the scheduler event creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the scheduler event | [optional] |
| tenant_id | TenantId | JSON object with Tenant Id | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. Optional: when omitted the Scheduler Event is owned by the tenant. When the request is made by a Customer user, the value is forced to the user's own Customer Id. | [optional] |
| originator_id | EntityId | JSON object with Originator Id | [optional] [readonly] |
| name | str | scheduler event name | [optional] |
| type | str | scheduler event type | [optional] |
| schedule | object | a JSON value with schedule time configuration | [optional] |
| enabled | bool | Enable/disable scheduler | [optional] |
| version | int |  | [optional] |
| customer_title | str | Title of the customer | [optional] |
| customer_is_public | bool | Parameter that specifies if customer is public | [optional] [readonly] |
| timestamps | List[int] |  | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataSchedulerEventWithCustomerInfo.model_validate(data)` or `PageDataSchedulerEventWithCustomerInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

