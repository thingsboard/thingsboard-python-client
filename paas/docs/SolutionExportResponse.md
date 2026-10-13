
# SolutionExportResponse

`tb_paas_client.models.SolutionExportResponse`

Solution export response containing the exported solution data and any dependency warnings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **solution** | [**SolutionData**](SolutionData.md) | The exported solution data containing all requested entities grouped by type. | [optional] |
| **warnings** | **List[str]** | List of dependency warnings. Generated when exported entities reference other entities that are not included in the export (e.g. a device profile references a rule chain that was not selected for export). | [optional] |



## Referenced Types

#### SolutionData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entities | Dict[str, List[EntityExportData]] | Exported entities grouped by entity type. Each key is an entity type (e.g. DEVICE_PROFILE, RULE_CHAIN) and the value is a list of entity export data objects. |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.solution`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SolutionExportResponse.model_validate(data)` or `SolutionExportResponse.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

