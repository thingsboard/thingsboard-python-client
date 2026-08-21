
# DeviceProfileTransportConfiguration

`tb_paas_client.models.DeviceProfileTransportConfiguration`

Configuration for device profile transport

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### CoapDeviceProfileTransportConfiguration  *(type=`COAP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coap_device_type_configuration | CoapDeviceTypeConfiguration |  | [optional] |
| client_settings | PowerSavingConfiguration |  | [optional] |

#### DefaultDeviceProfileTransportConfiguration  *(type=`DEFAULT`)*
*(no additional properties)*

#### Lwm2mDeviceProfileTransportConfiguration  *(type=`LWM2M`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| observe_attr | TelemetryMappingConfiguration | Configuration for mapping LwM2M resources to telemetry and attributes | [optional] |
| bootstrap_server_update_enable | bool | Flag indicating whether LwM2M bootstrap server update is enabled | [optional] |
| bootstrap | List[LwM2MBootstrapServerCredential] |  | [optional] |
| client_lw_m2m_settings | OtherConfiguration | Other LwM2M client settings | [optional] |

#### MqttDeviceProfileTransportConfiguration  *(type=`MQTT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_telemetry_topic | str |  | [optional] |
| device_attributes_topic | str |  | [optional] |
| device_attributes_subscribe_topic | str |  | [optional] |
| transport_payload_type_configuration | TransportPayloadTypeConfiguration |  | [optional] |
| sparkplug | bool |  | [optional] |
| sparkplug_attributes_metric_names | List[str] |  | [optional] |
| send_ack_on_validation_exception | bool |  | [optional] |

#### SnmpDeviceProfileTransportConfiguration  *(type=`SNMP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timeout_ms | int |  | [optional] |
| retries | int |  | [optional] |
| communication_configs | List[SnmpCommunicationConfig] |  | [optional] |

## Referenced Types

#### CoapDeviceTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coap_device_type | str |  |  |

#### DefaultCoapDeviceTypeConfiguration  *(extends CoapDeviceTypeConfiguration, coap_device_type=`DEFAULT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| transport_payload_type_configuration | TransportPayloadTypeConfiguration |  | [optional] |

#### EfentoCoapDeviceTypeConfiguration  *(extends CoapDeviceTypeConfiguration, coap_device_type=`EFENTO`)*
*See CoapDeviceTypeConfiguration for properties.*

#### PowerSavingConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

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

#### NoSecLwM2MBootstrapServerCredential  *(extends LwM2MBootstrapServerCredential, security_mode=`NO_SEC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| short_server_id | int | Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server. | [optional] [readonly] |
| bootstrap_server_is | bool | Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified. | [optional] [readonly] |
| host | str | Host for 'No Security' mode | [optional] [readonly] |
| port | int | Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server | [optional] [readonly] |
| client_hold_off_time | int | Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.) | [optional] [readonly] |
| server_public_key | str | Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded | [optional] [readonly] |
| server_certificate | str | Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded | [optional] [readonly] |
| bootstrap_server_account_timeout | int | Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.) | [optional] [readonly] |
| lifetime | int | Specify the lifetime of the registration in seconds. | [optional] [readonly] |
| default_min_period | int | The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0. | [optional] [readonly] |
| notif_if_disabled | bool | If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true. | [optional] [readonly] |
| binding | str | This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode. | [optional] [readonly] |

#### PSKLwM2MBootstrapServerCredential  *(extends LwM2MBootstrapServerCredential, security_mode=`PSK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| short_server_id | int | Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server. | [optional] [readonly] |
| bootstrap_server_is | bool | Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified. | [optional] [readonly] |
| host | str | Host for 'No Security' mode | [optional] [readonly] |
| port | int | Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server | [optional] [readonly] |
| client_hold_off_time | int | Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.) | [optional] [readonly] |
| server_public_key | str | Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded | [optional] [readonly] |
| server_certificate | str | Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded | [optional] [readonly] |
| bootstrap_server_account_timeout | int | Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.) | [optional] [readonly] |
| lifetime | int | Specify the lifetime of the registration in seconds. | [optional] [readonly] |
| default_min_period | int | The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0. | [optional] [readonly] |
| notif_if_disabled | bool | If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true. | [optional] [readonly] |
| binding | str | This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode. | [optional] [readonly] |

#### RPKLwM2MBootstrapServerCredential  *(extends LwM2MBootstrapServerCredential, security_mode=`RPK`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| short_server_id | int | Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server. | [optional] [readonly] |
| bootstrap_server_is | bool | Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified. | [optional] [readonly] |
| host | str | Host for 'No Security' mode | [optional] [readonly] |
| port | int | Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server | [optional] [readonly] |
| client_hold_off_time | int | Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.) | [optional] [readonly] |
| server_public_key | str | Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded | [optional] [readonly] |
| server_certificate | str | Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded | [optional] [readonly] |
| bootstrap_server_account_timeout | int | Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.) | [optional] [readonly] |
| lifetime | int | Specify the lifetime of the registration in seconds. | [optional] [readonly] |
| default_min_period | int | The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0. | [optional] [readonly] |
| notif_if_disabled | bool | If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true. | [optional] [readonly] |
| binding | str | This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode. | [optional] [readonly] |

#### X509LwM2MBootstrapServerCredential  *(extends LwM2MBootstrapServerCredential, security_mode=`X509`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| short_server_id | int | Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server. | [optional] [readonly] |
| bootstrap_server_is | bool | Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified. | [optional] [readonly] |
| host | str | Host for 'No Security' mode | [optional] [readonly] |
| port | int | Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server | [optional] [readonly] |
| client_hold_off_time | int | Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.) | [optional] [readonly] |
| server_public_key | str | Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded | [optional] [readonly] |
| server_certificate | str | Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded | [optional] [readonly] |
| bootstrap_server_account_timeout | int | Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.) | [optional] [readonly] |
| lifetime | int | Specify the lifetime of the registration in seconds. | [optional] [readonly] |
| default_min_period | int | The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0. | [optional] [readonly] |
| notif_if_disabled | bool | If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true. | [optional] [readonly] |
| binding | str | This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode. | [optional] [readonly] |

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

#### TransportPayloadTypeConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| transport_payload_type | str |  |  |

#### JsonTransportPayloadConfiguration  *(extends TransportPayloadTypeConfiguration, transport_payload_type=`JSON`)*
*See TransportPayloadTypeConfiguration for properties.*

#### ProtoTransportPayloadConfiguration  *(extends TransportPayloadTypeConfiguration, transport_payload_type=`PROTOBUF`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_telemetry_proto_schema | str |  | [optional] |
| device_attributes_proto_schema | str |  | [optional] |
| device_rpc_request_proto_schema | str |  | [optional] |
| device_rpc_response_proto_schema | str |  | [optional] |
| enable_compatibility_with_json_payload_format | bool |  | [optional] |
| use_json_payload_format_for_default_downlink_topics | bool |  | [optional] |

#### SnmpCommunicationConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| spec | SnmpCommunicationSpec | Specification of the SNMP communication |  |

#### ClientAttributesQueryingSnmpCommunicationConfig  *(extends SnmpCommunicationConfig, spec=`CLIENT_ATTRIBUTES_QUERYING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| mappings | List[SnmpMapping] |  | [optional] |
| querying_frequency_ms | int |  | [optional] |

#### SharedAttributesSettingSnmpCommunicationConfig  *(extends SnmpCommunicationConfig, spec=`SHARED_ATTRIBUTES_SETTING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| mappings | List[SnmpMapping] |  | [optional] |

#### TelemetryQueryingSnmpCommunicationConfig  *(extends SnmpCommunicationConfig, spec=`TELEMETRY_QUERYING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| mappings | List[SnmpMapping] |  | [optional] |
| querying_frequency_ms | int |  | [optional] |

#### ToDeviceRpcRequestSnmpCommunicationConfig  *(extends SnmpCommunicationConfig, spec=`TO_DEVICE_RPC_REQUEST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| mappings | List[SnmpMapping] |  | [optional] |

#### ToServerRpcRequestSnmpCommunicationConfig  *(extends SnmpCommunicationConfig, spec=`TO_SERVER_RPC_REQUEST`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| mappings | List[SnmpMapping] |  | [optional] |

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

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

#### SnmpCommunicationSpec (enum)
`TELEMETRY_QUERYING` | `CLIENT_ATTRIBUTES_QUERYING` | `SHARED_ATTRIBUTES_SETTING` | `TO_DEVICE_RPC_REQUEST` | `TO_SERVER_RPC_REQUEST`

#### LwM2mVersion
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| supported | bool |  | [optional] |

#### SnmpMapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| oid | str |  | [optional] |
| key | str |  | [optional] |
| data_type | DataType |  | [optional] |

#### DataType (enum)
`BOOLEAN` | `LONG` | `DOUBLE` | `STRING` | `JSON`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfileTransportConfiguration.model_validate(data)` or `DeviceProfileTransportConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

