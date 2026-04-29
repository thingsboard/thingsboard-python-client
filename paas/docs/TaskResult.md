
# TaskResult

`tb_paas_client.models.TaskResult`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key** | **str** |  | [optional] |
| **success** | **bool** |  | [optional] |
| **discarded** | **bool** |  | [optional] |
| **finish_ts** | **int** |  | [optional] |
| **error** | **str** |  | [optional] |
| **job_type** | **str** |  | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.key`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TaskResult.model_validate(data)` or `TaskResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

