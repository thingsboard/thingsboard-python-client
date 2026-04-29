
# Device

`tb_paas_client.models.Device`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**DeviceId**](DeviceId.md) | JSON object with the Device Id. Specify this field to update the Device. Referencing non-existing Device Id will cause error. Omit this field to create new Device. | [optional] |
| **created_time** | **int** | Timestamp of the device creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the device. May include: 'gateway' (boolean, whether the device is a gateway), 'description' (string), 'lastConnectedGateway' (string, UUID of the last gateway that connected this device). | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Use 'assignDeviceToTenant' to change the Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Use 'assignDeviceToCustomer' to change the Customer Id. | [optional] [readonly] |
| **name** | **str** | Unique Device Name in scope of Tenant | [optional] |
| **type** | **str** | Device Profile Name | [optional] |
| **label** | **str** | Label that may be used in widgets | [optional] |
| **device_profile_id** | [**DeviceProfileId**](DeviceProfileId.md) | JSON object with Device Profile Id. If not provided, the type will be used to determine the profile. If neither deviceProfileId nor type is specified, the default device profile will be used. | [optional] |
| **device_data** | [**DeviceData**](DeviceData.md) | JSON object with content specific to type of transport in the device profile. | [optional] |
| **firmware_id** | [**OtaPackageId**](OtaPackageId.md) | JSON object with Ota Package Id. | [optional] |
| **software_id** | [**OtaPackageId**](OtaPackageId.md) | JSON object with Ota Package Id. | [optional] |
| **version** | **int** |  | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DeviceData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | DeviceConfiguration | Device configuration for device profile type. DEFAULT is only supported value for now | [optional] |
| transport_configuration | DeviceTransportConfiguration | Device transport configuration used to connect the device | [optional] |

#### DeviceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | DeviceProfileType | Device profile type |  |

#### DefaultDeviceConfiguration  *(extends DeviceConfiguration, type=`DEFAULT`)*
*See DeviceConfiguration for properties.*

#### DeviceTransportConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CoapDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`COAP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

#### DefaultDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`DEFAULT`)*
*See DeviceTransportConfiguration for properties.*

#### Lwm2mDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`LWM2M`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| power_mode | PowerMode |  | [optional] |
| psm_activity_timer | int |  | [optional] |
| edrx_cycle | int |  | [optional] |
| paging_transmission_window | int |  | [optional] |

#### MqttDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`MQTT`)*
*See DeviceTransportConfiguration for properties.*

#### SnmpDeviceTransportConfiguration  *(extends DeviceTransportConfiguration, type=`SNMP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| host | str |  | [optional] |
| port | int |  | [optional] |
| protocol_version | SnmpProtocolVersion |  | [optional] |
| community | str |  | [optional] |
| username | str |  | [optional] |
| security_name | str |  | [optional] |
| context_name | str |  | [optional] |
| authentication_protocol | AuthenticationProtocol |  | [optional] |
| authentication_passphrase | str |  | [optional] |
| privacy_protocol | PrivacyProtocol |  | [optional] |
| privacy_passphrase | str |  | [optional] |
| engine_id | str |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### DeviceProfileType (enum)
`DEFAULT`

#### PowerMode (enum)
`PSM` | `DRX` | `E_DRX`

#### SnmpProtocolVersion (enum)
`V1` | `V2C` | `V3`

#### AuthenticationProtocol (enum)
`SHA_1` | `SHA_224` | `SHA_256` | `SHA_384` | `SHA_512` | `MD5`

#### PrivacyProtocol (enum)
`DES` | `AES_128` | `AES_192` | `AES_256`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `Device.model_validate(data)` or `Device.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

