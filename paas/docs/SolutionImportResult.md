
# SolutionImportResult

`tb_paas_client.models.SolutionImportResult`

Result of a solution import operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **success** | **bool** | 'true' if all entities were imported successfully. | [optional] |
| **created** | **Dict[str, int]** | Number of newly created entities per entity type. Entity types with zero created entities are omitted. | [optional] |
| **id_mapping** | **Dict[str, UUID]** | Mapping from external entity IDs (as they appear in the solution file) to the internal entity IDs assigned during import. | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.success`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SolutionImportResult.model_validate(data)` or `SolutionImportResult.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

