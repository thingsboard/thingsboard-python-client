
# SolutionValidationResult

`tb_paas_client.models.SolutionValidationResult`

Result of a solution validation (dry-run). Checks structural validity and dependency references without modifying any data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **valid** | **bool** | 'true' if the solution can be imported without errors. 'false' if there are structural issues (empty entities, unsupported types, malformed data). | [optional] |
| **entity_summary** | **Dict[str, int]** | Number of entities per type found in the solution file. | [optional] |
| **conflicts** | **List[str]** | List of blocking issues that would prevent import (e.g. unsupported entity types, missing or malformed entity data). | [optional] |
| **warnings** | **List[str]** | List of non-blocking warnings (e.g. missing dependency references). | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.valid`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SolutionValidationResult.model_validate(data)` or `SolutionValidationResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

