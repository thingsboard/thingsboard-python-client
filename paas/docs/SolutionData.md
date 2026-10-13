
# SolutionData

`tb_paas_client.models.SolutionData`

Portable solution package containing exported entities grouped by type. Represents a self-contained snapshot that can be imported into another tenant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entities** | **Dict[str, List[EntityExportData]]** | Exported entities grouped by entity type. Each key is an entity type (e.g. DEVICE_PROFILE, RULE_CHAIN) and the value is a list of entity export data objects. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entities`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SolutionData.model_validate(data)` or `SolutionData.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

