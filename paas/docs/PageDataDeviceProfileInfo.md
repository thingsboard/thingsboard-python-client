
# PageDataDeviceProfileInfo

`tb_paas_client.models.PageDataDeviceProfileInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[DeviceProfileInfo]**](DeviceProfileInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### DeviceProfileInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | DeviceProfileId | JSON object with the Device Profile Id. | [optional] |
| name | str | Entity Name | [optional] |
| image | str | Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view. | [optional] |
| default_dashboard_id | DashboardId | Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to device details. | [optional] |
| type | DeviceProfileType | Type of the profile. Always 'DEFAULT' for now. Reserved for future use. | [optional] |
| transport_type | DeviceTransportType | Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT. | [optional] |
| tenant_id | TenantId | Tenant id. | [optional] |

#### DeviceProfileType (enum)
`DEFAULT`

#### DeviceTransportType (enum)
`DEFAULT` | `MQTT` | `COAP` | `LWM2M` | `SNMP`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataDeviceProfileInfo.model_validate(data)` or `PageDataDeviceProfileInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

