
# PageDataReportTemplateInfo

`tb_pe_client.models.PageDataReportTemplateInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[ReportTemplateInfo]**](ReportTemplateInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### ReportTemplateInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | ReportTemplateId | JSON object with the report template Id. Specify this field to update the report. Referencing non-existing report template Id will cause error. Omit this field to create new report template | [optional] |
| created_time | int | Timestamp of the report template creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id. Tenant Id of the report template can't be changed. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. Optional: when omitted the Report Template is owned by the tenant. When the request is made by a Customer user, the value is forced to the user's own Customer Id. | [optional] |
| name | str | Report name |  |
| format | TbReportFormat | Report format |  |
| type | ReportTemplateType | Report template type |  |
| description | str | Description | [optional] |
| version | int |  | [optional] |
| owner_name | str | Owner name | [optional] [readonly] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### TbReportFormat (enum)
`PDF` | `CSV`

#### ReportTemplateType (enum)
`REPORT` | `SUB_REPORT`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataReportTemplateInfo.model_validate(data)` or `PageDataReportTemplateInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

