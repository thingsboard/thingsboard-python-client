
# PageDataEntityView

`tb_paas_client.models.PageDataEntityView`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[EntityView]**](EntityView.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityView
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityViewId | JSON object with the Entity View Id. Specify this field to update the Entity View. Referencing non-existing Entity View Id will cause error. Omit this field to create new Entity View. | [optional] |
| created_time | int | Timestamp of the Entity View creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the entity view. May include: 'description' (string). | [optional] |
| entity_id | EntityId | JSON object with the referenced Entity Id (Device or Asset). |  |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. Optional on create: when omitted, defaults to the owner of the target Entity Group or to the current Customer user. Cannot be changed on update via this endpoint; use the Owner API (changeOwnerToCustomer) to re-assign an existing Entity View. | [optional] |
| name | str | Entity View name |  |
| type | str | Device Profile Name |  |
| keys | TelemetryEntityView | Set of telemetry and attribute keys to expose via Entity View. | [optional] |
| start_time_ms | int | Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval; | [optional] |
| end_time_ms | int | Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval; | [optional] |
| version | int |  | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### TelemetryEntityView
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| timeseries | List[str] | List of time-series data keys to expose |  |
| attributes | AttributesEntityView | JSON object with attributes to expose |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### AttributesEntityView
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| cs | List[str] | List of client-side attribute keys to expose |  |
| ss | List[str] | List of server-side attribute keys to expose |  |
| sh | List[str] | List of shared attribute keys to expose |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataEntityView.model_validate(data)` or `PageDataEntityView.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

