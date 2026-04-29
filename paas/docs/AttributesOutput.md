
# AttributesOutput

`tb_paas_client.models.AttributesOutput`

**Extends:** **Output**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **strategy** | [**AttributesOutputStrategy**](AttributesOutputStrategy.md) |  | [optional] |



## Referenced Types

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| decimals_by_default | int |  | [optional] |
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

#### AttributesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributesImmediateOutputStrategy  *(extends AttributesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| send_attributes_updated_notification | bool |  | [optional] |
| update_attributes_only_on_value_change | bool |  | [optional] |
| save_attribute | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### AttributesRuleChainOutputStrategy  *(extends AttributesOutputStrategy, type=`RULE_CHAIN`)*
*See AttributesOutputStrategy for properties.*

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.strategy`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AttributesOutput.model_validate(data)` or `AttributesOutput.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

