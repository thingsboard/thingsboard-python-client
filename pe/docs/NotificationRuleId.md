
# NotificationRuleId

`tb_pe_client.models.NotificationRuleId`

**Extends:** **EntityId**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|



## Referenced Types

> **EntityId**: `{entity_type: EntityType, id: UUID}` — base type for all entity identifiers.

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `NotificationRuleId.model_validate(data)` or `NotificationRuleId.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

