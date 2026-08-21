
# DeviceProfile

`tb_paas_client.models.DeviceProfile`

A JSON value representing the device profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with the device profile Id. Specify this field to update the device profile. Referencing non-existing device profile Id will cause error. Omit this field to create new device profile. | [optional] |
| **created_time** | **int** | Timestamp of the profile creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id that owns the profile. | [optional] [readonly] |
| **name** | **str** | Unique Device Profile Name in scope of Tenant. | [optional] |
| **description** | **str** | Device Profile description.  | [optional] |
| **image** | **str** | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.  | [optional] |
| **type** | [**DeviceProfileType**](DeviceProfileType.md) | Type of the profile. Always 'DEFAULT' for now. Reserved for future use. | [optional] |
| **transport_type** | [**DeviceTransportType**](DeviceTransportType.md) | Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT. | [optional] |
| **provision_type** | [**DeviceProfileProvisionType**](DeviceProfileProvisionType.md) | Provisioning strategy. | [optional] |
| **default_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the rule chain. If present, the specified rule chain will be used to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the root rule chain will be used to process those messages. | [optional] |
| **default_dashboard_id** | [**DashboardId**](DashboardId.md) | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details. | [optional] |
| **default_queue_name** | **str** | Rule engine queue name. If present, the specified queue will be used to store all unprocessed messages related to device, including telemetry, attribute updates, etc. Otherwise, the 'Main' queue will be used to store those messages. | [optional] |
| **profile_data** | [**DeviceProfileData**](DeviceProfileData.md) | Complex JSON object that includes addition device profile configuration (transport, alarm rules, etc). | [optional] |
| **provision_device_key** | **str** | Unique provisioning key used by 'Device Provisioning' feature. | [optional] |
| **firmware_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the firmware OTA package. If present, the specified package will be used as default device firmware.  | [optional] |
| **software_id** | [**OtaPackageId**](OtaPackageId.md) | Reference to the software OTA package. If present, the specified package will be used as default device software.  | [optional] |
| **default_edge_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | Reference to the edge rule chain. If present, the specified edge rule chain will be used on the edge to process all messages related to device, including telemetry, attribute updates, etc. Otherwise, the edge root rule chain will be used to process those messages. | [optional] |
| **version** | **int** |  | [optional] |
| **default** | **bool** | Used to mark the default profile. Default profile is used when the device profile is not specified during device creation. | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DeviceProfileType (enum)
`DEFAULT`

#### DeviceTransportType (enum)
`DEFAULT` | `MQTT` | `COAP` | `LWM2M` | `SNMP`

#### DeviceProfileProvisionType (enum)
`DISABLED` | `ALLOW_CREATE_NEW_DEVICES` | `CHECK_PRE_PROVISIONED_DEVICES` | `X509_CERTIFICATE_CHAIN`

#### DeviceProfileData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | DeviceProfileConfiguration | JSON object of device profile configuration | [optional] |
| transport_configuration | DeviceProfileTransportConfiguration | JSON object of device profile transport configuration | [optional] |
| provision_configuration | DeviceProfileProvisionConfiguration | JSON object of provisioning strategy type per device profile | [optional] |

#### DeviceProfileConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DefaultDeviceProfileConfiguration  *(extends DeviceProfileConfiguration, type=`DEFAULT`)*
*See DeviceProfileConfiguration for properties.*

#### DeviceProfileTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CoapDeviceProfileTransportConfiguration  *(extends DeviceProfileTransportConfiguration, type=`COAP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coap_device_type_configuration | CoapDeviceTypeConfiguration |  | [optional] |
| client_settings | PowerSavingConfiguration |  | [optional] |

#### DefaultDeviceProfileTransportConfiguration  *(extends DeviceProfileTransportConfiguration, type=`DEFAULT`)*
*See DeviceProfileTransportConfiguration for properties.*

#### Lwm2mDeviceProfileTransportConfiguration  *(extends DeviceProfileTransportConfiguration, type=`LWM2M`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| observe_attr | TelemetryMappingConfiguration | Configuration for mapping LwM2M resources to telemetry and attributes | [optional] |
| bootstrap_server_update_enable | bool | Flag indicating whether LwM2M bootstrap server update is enabled | [optional] |
| bootstrap | List[LwM2MBootstrapServerCredential] |  | [optional] |
| client_lw_m2m_settings | OtherConfiguration | Other LwM2M client settings | [optional] |

#### MqttDeviceProfileTransportConfiguration  *(extends DeviceProfileTransportConfiguration, type=`MQTT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_telemetry_topic | str |  | [optional] |
| device_attributes_topic | str |  | [optional] |
| device_attributes_subscribe_topic | str |  | [optional] |
| transport_payload_type_configuration | TransportPayloadTypeConfiguration |  | [optional] |
| sparkplug | bool |  | [optional] |
| sparkplug_attributes_metric_names | List[str] |  | [optional] |
| send_ack_on_validation_exception | bool |  | [optional] |

#### SnmpDeviceProfileTransportConfiguration  *(extends DeviceProfileTransportConfiguration, type=`SNMP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timeout_ms | int |  | [optional] |
| retries | int |  | [optional] |
| communication_configs | List[SnmpCommunicationConfig] |  | [optional] |

#### DeviceProfileProvisionConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| provision_device_secret | str | Provision device secret | [optional] |
| type | str |  |  |

#### AllowCreateNewDevicesDeviceProfileProvisionConfiguration  *(extends DeviceProfileProvisionConfiguration, type=`ALLOW_CREATE_NEW_DEVICES`)*
*See DeviceProfileProvisionConfiguration for properties.*

#### CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration  *(extends DeviceProfileProvisionConfiguration, type=`CHECK_PRE_PROVISIONED_DEVICES`)*
*See DeviceProfileProvisionConfiguration for properties.*

#### DisabledDeviceProfileProvisionConfiguration  *(extends DeviceProfileProvisionConfiguration, type=`DISABLED`)*
*See DeviceProfileProvisionConfiguration for properties.*

#### X509CertificateChainProvisionConfiguration  *(extends DeviceProfileProvisionConfiguration, type=`X509_CERTIFICATE_CHAIN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| certificate_reg_ex_pattern | str |  | [optional] |
| allow_create_new_devices_by_x509_certificate | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

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
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `DeviceProfile.model_validate(data)` or `DeviceProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

