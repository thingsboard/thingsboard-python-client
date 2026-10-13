
# EntityExportSettings

`tb_paas_client.models.EntityExportSettings`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **export_relations** | **bool** |  | [optional] |
| **export_attributes** | **bool** |  | [optional] |
| **export_credentials** | **bool** |  | [optional] |
| **export_calculated_fields** | **bool** |  | [optional] |
| **export_permissions** | **bool** |  | [optional] |
| **export_group_entities** | **bool** |  | [optional] |
| **embed_group_members** | **bool** |  | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.export_relations`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityExportSettings.model_validate(data)` or `EntityExportSettings.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

