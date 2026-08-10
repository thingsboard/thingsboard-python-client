
# DummyJobConfiguration

`tb_ce_client.models.DummyJobConfiguration`

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
- **Attribute access:** `obj.task_processing_time_ms`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DummyJobConfiguration.model_validate(data)` or `DummyJobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

