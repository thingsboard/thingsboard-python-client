
# DummyJobConfiguration

`tb_paas_client.models.DummyJobConfiguration`

Dummy job configuration

**Extends:** **JobConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **task_processing_time_ms** | **int** |  | [optional] |
| **successful_tasks_count** | **int** |  | [optional] |
| **failed_tasks_count** | **int** |  | [optional] |
| **permanently_failed_tasks_count** | **int** |  | [optional] |
| **errors** | **List[str]** |  | [optional] |
| **retries** | **int** |  | [optional] |
| **task_processing_timeout_ms** | **int** |  | [optional] |
| **general_error** | **str** |  | [optional] |
| **submitted_tasks_before_general_error** | **int** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### JobConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tasks_key | str |  |  |
| to_reprocess | List[TaskResult] |  | [optional] |
| type | str |  |  |

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| error | str |  | [optional] |
| job_type | str |  |  |

#### CfReprocessingTaskResult  *(extends TaskResult, job_type=`CF_REPROCESSING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failure | CfReprocessingTaskFailure |  | [optional] |

#### DummyTaskResult  *(extends TaskResult, job_type=`DUMMY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failure | DummyTaskFailure |  | [optional] |

#### ReportTaskResult  *(extends TaskResult, job_type=`REPORT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| report | Report |  | [optional] |

#### CfReprocessingTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| entity_info | EntityInfo |  | [optional] |

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

#### DummyTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| number | int |  | [optional] |
| fail_always | bool |  | [optional] |

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### TbReportFormat (enum)
`PDF` | `CSV`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.task_processing_time_ms`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DummyJobConfiguration.model_validate(data)` or `DummyJobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

