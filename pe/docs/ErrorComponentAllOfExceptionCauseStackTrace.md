
# ErrorComponentAllOfExceptionCauseStackTrace

`tb_pe_client.models.ErrorComponentAllOfExceptionCauseStackTrace`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **class_loader_name** | **str** |  | [optional] |
| **module_name** | **str** |  | [optional] |
| **module_version** | **str** |  | [optional] |
| **method_name** | **str** |  | [optional] |
| **file_name** | **str** |  | [optional] |
| **line_number** | **int** |  | [optional] |
| **class_name** | **str** |  | [optional] |
| **native_method** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.class_loader_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ErrorComponentAllOfExceptionCauseStackTrace.model_validate(data)` or `ErrorComponentAllOfExceptionCauseStackTrace.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

