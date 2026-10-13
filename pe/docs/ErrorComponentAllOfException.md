
# ErrorComponentAllOfException

`tb_pe_client.models.ErrorComponentAllOfException`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **cause** | [**ErrorComponentAllOfExceptionCause**](ErrorComponentAllOfExceptionCause.md) |  | [optional] |
| **stack_trace** | [**List[ErrorComponentAllOfExceptionCauseStackTrace]**](ErrorComponentAllOfExceptionCauseStackTrace.md) |  | [optional] |
| **message** | **str** |  | [optional] |
| **suppressed** | [**List[ErrorComponentAllOfExceptionCause]**](ErrorComponentAllOfExceptionCause.md) |  | [optional] |
| **localized_message** | **str** |  | [optional] |



## Referenced Types

#### ErrorComponentAllOfExceptionCause
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| stack_trace | List[ErrorComponentAllOfExceptionCauseStackTrace] |  | [optional] |
| message | str |  | [optional] |
| localized_message | str |  | [optional] |

#### ErrorComponentAllOfExceptionCauseStackTrace
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| class_loader_name | str |  | [optional] |
| module_name | str |  | [optional] |
| module_version | str |  | [optional] |
| method_name | str |  | [optional] |
| file_name | str |  | [optional] |
| line_number | int |  | [optional] |
| class_name | str |  | [optional] |
| native_method | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.cause`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ErrorComponentAllOfException.model_validate(data)` or `ErrorComponentAllOfException.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

