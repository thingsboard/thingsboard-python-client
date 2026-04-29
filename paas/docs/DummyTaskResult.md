
# DummyTaskResult

`tb_paas_client.models.DummyTaskResult`

**Extends:** **TaskResult**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **failure** | [**DummyTaskFailure**](DummyTaskFailure.md) |  | [optional] |



## Referenced Types

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| error | str |  | [optional] |
| job_type | str |  |  |

#### DummyTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| number | int |  | [optional] |
| fail_always | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.failure`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DummyTaskResult.model_validate(data)` or `DummyTaskResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

