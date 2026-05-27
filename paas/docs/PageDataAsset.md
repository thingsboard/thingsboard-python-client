
# PageDataAsset

`tb_paas_client.models.PageDataAsset`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[Asset]**](Asset.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### Asset
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AssetId | JSON object with the asset Id. Specify this field to update the asset. Referencing non-existing asset Id will cause error. Omit this field to create new asset. | [optional] |
| created_time | int | Timestamp of the asset creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the asset. May include: 'description' (string). | [optional] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| customer_id | CustomerId | JSON object with Customer Id. Optional on create: when omitted, defaults to the owner of the target Entity Group or to the current Customer user. Cannot be changed on update via this endpoint; use the Owner API (changeOwnerToCustomer) to re-assign an existing Asset. | [optional] |
| name | str | Unique Asset Name in scope of Tenant |  |
| type | str | Asset type | [optional] |
| label | str | Label that may be used in widgets | [optional] |
| asset_profile_id | AssetProfileId | JSON object with Asset Profile Id. | [optional] |
| version | int |  | [optional] |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAsset.model_validate(data)` or `PageDataAsset.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

