
# JobResult

`tb_paas_client.models.JobResult`

Job execution result

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **successful_count** | **int** | Count of successfully completed tasks | [optional] |
| **failed_count** | **int** | Count of failed tasks | [optional] |
| **discarded_count** | **int** | Count of discarded tasks | [optional] |
| **total_count** | **int** | Total number of tasks, set when all tasks are submitted | [optional] |
| **results** | [**List[TaskResult]**](TaskResult.md) |  | [optional] |
| **general_error** | **str** | General error message if the job failed | [optional] |
| **start_ts** | **int** | Timestamp of the job start, in milliseconds | [optional] |
| **finish_ts** | **int** | Timestamp of the job finish, in milliseconds | [optional] |
| **cancellation_ts** | **int** | Timestamp of the job cancellation, in milliseconds | [optional] |
| **job_type** | **str** |  | |



## Subtypes

#### CfReprocessingJobResult  *(job_type=`CF_REPROCESSING`)*
*(no additional properties)*

#### DummyJobResult  *(job_type=`DUMMY`)*
*(no additional properties)*

#### ReportJobResult  *(job_type=`REPORT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| report | Report |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| error | str |  | [optional] |
| job_type | str |  |  |

#### Report
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | ReportId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  |  |
| customer_id | CustomerId |  | [optional] |
| template_id | ReportTemplateId |  |  |
| format | TbReportFormat |  |  |
| name | str |  |  |
| user_id | UserId |  |  |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### TbReportFormat (enum)
`PDF` | `CSV`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.successful_count`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `JobResult.model_validate(data)` or `JobResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

