
# AgentBulkActionEventStats

`tb_paas_client.models.AgentBulkActionEventStats`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **counts_by_status** | **Dict[str, int]** | Number of events produced by the bulk action per processing status | [optional] |
| **total** | **int** | Total number of events produced by the bulk action | [optional] |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.counts_by_status`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentBulkActionEventStats.model_validate(data)` or `AgentBulkActionEventStats.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

