
# AgentUpgradeRequest

`tb_paas_client.models.AgentUpgradeRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **image_ref** | **str** | Target agent image reference — a digest-pinned reference in production, or a tag. | |



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.image_ref`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentUpgradeRequest.model_validate(data)` or `AgentUpgradeRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

