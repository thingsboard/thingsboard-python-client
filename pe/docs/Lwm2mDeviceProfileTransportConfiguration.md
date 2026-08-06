
# Lwm2mDeviceProfileTransportConfiguration

`tb_pe_client.models.Lwm2mDeviceProfileTransportConfiguration`

**Extends:** **DeviceProfileTransportConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **observe_attr** | [**TelemetryMappingConfiguration**](TelemetryMappingConfiguration.md) | Configuration for mapping LwM2M resources to telemetry and attributes | [optional] |
| **bootstrap_server_update_enable** | **bool** | Flag indicating whether LwM2M bootstrap server update is enabled | [optional] |
| **bootstrap** | [**List[LwM2MBootstrapServerCredential]**](LwM2MBootstrapServerCredential.md) |  | [optional] |
| **client_lw_m2m_settings** | [**OtherConfiguration**](OtherConfiguration.md) | Other LwM2M client settings | [optional] |



## Referenced Types

#### DeviceProfileTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TelemetryMappingConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key_name | Dict[str, str] | Map of LwM2M resource paths to telemetry key names | [optional] |
| observe | List[str] | Set of resources to observe | [optional] |
| attribute | List[str] | Set of attribute keys | [optional] |
| telemetry | List[str] | Set of telemetry keys | [optional] |
| attribute_lwm2m | Dict[str, ObjectAttributes] | Map of resource paths to specific LwM2M object attributes | [optional] |
| init_attr_tel_as_obs_strategy | bool |  | [optional] |
| observe_strategy | TelemetryObserveStrategy | Observation strategy for telemetry | [optional] |

#### LwM2MBootstrapServerCredential
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| security_mode | str |  |  |

#### OtherConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |
| use_object19_for_ota_info | bool |  | [optional] |
| fw_update_strategy | int |  | [optional] |
| sw_update_strategy | int |  | [optional] |
| client_only_observe_after_connect | int |  | [optional] |
| fw_update_resource | str |  | [optional] |
| sw_update_resource | str |  | [optional] |
| default_object_id_ver | str |  | [optional] |

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

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

#### LwM2mVersion
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| supported | bool |  | [optional] |

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.observe_attr`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Lwm2mDeviceProfileTransportConfiguration.model_validate(data)` or `Lwm2mDeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

