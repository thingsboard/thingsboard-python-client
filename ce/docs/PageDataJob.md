
# PageDataJob

`tb_ce_client.models.PageDataJob`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[Job]**](Job.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `CalculatedFieldId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityViewId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### Job
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | JobId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  |  |
| type | JobType |  |  |
| key | str |  |  |
| entity_id | EntityId |  |  |
| entity_name | str |  | [optional] |
| status | JobStatus |  |  |
| configuration | JobConfiguration |  |  |
| result | JobResult |  |  |

#### JobType (enum)
`DUMMY`

#### JobStatus (enum)
`QUEUED` | `PENDING` | `RUNNING` | `COMPLETED` | `FAILED` | `CANCELLED`

#### JobConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tasks_key | str |  |  |
| to_reprocess | List[TaskResult] |  | [optional] |
| type | str |  |  |

#### DummyJobConfiguration  *(extends JobConfiguration, type=`DUMMY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| task_processing_time_ms | int |  | [optional] |
| successful_tasks_count | int |  | [optional] |
| failed_tasks_count | int |  | [optional] |
| permanently_failed_tasks_count | int |  | [optional] |
| errors | List[str] |  | [optional] |
| retries | int |  | [optional] |
| task_processing_timeout_ms | int |  | [optional] |
| general_error | str |  | [optional] |
| submitted_tasks_before_general_error | int |  | [optional] |

#### JobResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| successful_count | int | Count of successfully completed tasks | [optional] |
| failed_count | int | Count of failed tasks | [optional] |
| discarded_count | int | Count of discarded tasks | [optional] |
| total_count | int | Total number of tasks, set when all tasks are submitted | [optional] |
| results | List[TaskResult] |  | [optional] |
| general_error | str | General error message if the job failed | [optional] |
| start_ts | int | Timestamp of the job start, in milliseconds | [optional] |
| finish_ts | int | Timestamp of the job finish, in milliseconds | [optional] |
| cancellation_ts | int | Timestamp of the job cancellation, in milliseconds | [optional] |
| job_type | str |  |  |

#### DummyJobResult  *(extends JobResult, job_type=`DUMMY`)*
*See JobResult for properties.*

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `RULE_CHAIN` | `RULE_NODE` | `ENTITY_VIEW` | … (36 values total)

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| error | str |  | [optional] |
| job_type | str |  |  |

#### DummyTaskResult  *(extends TaskResult, job_type=`DUMMY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failure | DummyTaskFailure |  | [optional] |

#### DummyTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| number | int |  | [optional] |
| fail_always | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_ce_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataJob.model_validate(data)` or `PageDataJob.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

