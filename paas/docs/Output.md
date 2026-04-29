
# Output

`tb_paas_client.models.Output`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **decimals_by_default** | **int** |  | [optional] |
| **name** | **str** |  | [optional] |
| **scope** | [**AttributeScope**](AttributeScope.md) |  | [optional] |
| **strategy** | **object** |  | [optional] |
| **type** | **str** |  | |



## Subtypes

#### AttributesOutput  *(type=`ATTRIBUTES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | AttributesOutputStrategy |  | [optional] |

#### TimeSeriesOutput  *(type=`TIME_SERIES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesOutputStrategy |  | [optional] |

## Referenced Types

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

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

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeSeriesImmediateOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ttl | int |  | [optional] |
| save_time_series | bool |  | [optional] |
| save_latest | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### TimeSeriesRuleChainOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`RULE_CHAIN`)*
*See TimeSeriesOutputStrategy for properties.*

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.decimals_by_default`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Output.model_validate(data)` or `Output.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

