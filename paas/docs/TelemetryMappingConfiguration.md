
# TelemetryMappingConfiguration

`tb_paas_client.models.TelemetryMappingConfiguration`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **key_name** | **Dict[str, str]** | Map of LwM2M resource paths to telemetry key names | [optional] |
| **observe** | **List[str]** | Set of resources to observe | [optional] |
| **attribute** | **List[str]** | Set of attribute keys | [optional] |
| **telemetry** | **List[str]** | Set of telemetry keys | [optional] |
| **attribute_lwm2m** | [**Dict[str, ObjectAttributes]**](ObjectAttributes.md) | Map of resource paths to specific LwM2M object attributes | [optional] |
| **init_attr_tel_as_obs_strategy** | **bool** |  | [optional] |
| **observe_strategy** | [**TelemetryObserveStrategy**](TelemetryObserveStrategy.md) | Observation strategy for telemetry | [optional] |



## Referenced Types

#### ObjectAttributes
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dim | int |  | [optional] |
| ssid | int |  | [optional] |
| uri | str |  | [optional] |
| ver | object |  | [optional] |
| lwm2m | LwM2mVersion |  | [optional] |
| pmin | int |  | [optional] |
| pmax | int |  | [optional] |
| gt | float |  | [optional] |
| lt | float |  | [optional] |
| st | float |  | [optional] |
| epmin | int |  | [optional] |
| epmax | int |  | [optional] |

#### TelemetryObserveStrategy (enum)
`SINGLE` | `COMPOSITE_ALL` | `COMPOSITE_BY_OBJECT`

#### LwM2mVersion
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| supported | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.key_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `TelemetryMappingConfiguration.model_validate(data)` or `TelemetryMappingConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

