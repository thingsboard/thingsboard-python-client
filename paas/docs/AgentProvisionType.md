
# AgentProvisionType

`tb_paas_client.models.AgentProvisionType`

## Enum Values


* `DISABLED` (value: `'DISABLED'`)

* `NO_AUTO_INSTALL` (value: `'NO_AUTO_INSTALL'`)

* `AUTO_INSTALL_PER_APP_TYPE` (value: `'AUTO_INSTALL_PER_APP_TYPE'`)

* `AUTO_INSTALL_PER_APP_PROFILE` (value: `'AUTO_INSTALL_PER_APP_PROFILE'`)



---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentProvisionType.model_validate(data)` or `AgentProvisionType.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

