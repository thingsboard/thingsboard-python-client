
# EdgeInfo

`tb_paas_client.models.EdgeInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**EdgeId**](EdgeId.md) | JSON object with the Edge Id. Specify this field to update the Edge. Referencing non-existing Edge Id will cause error. Omit this field to create new Edge. | [optional] |
| **created_time** | **int** | Timestamp of the edge creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** | Additional parameters of the edge. May include: 'description' (string). | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Always set to the tenant of the current user on save; cannot be changed after creation. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. | [optional] |
| **root_rule_chain_id** | [**RuleChainId**](RuleChainId.md) | JSON object with Root Rule Chain Id. Use 'setEdgeRootRuleChain' to change the Root Rule Chain Id. | [optional] [readonly] |
| **name** | **str** | Unique Edge Name in scope of Tenant | |
| **type** | **str** | Edge type | |
| **label** | **str** | Label that may be used in widgets | [optional] |
| **routing_key** | **str** | Edge routing key ('username') to authorize on cloud | |
| **secret** | **str** | Edge secret ('password') to authorize on cloud | |
| **edge_license_key** | **str** | Edge license key obtained from license portal | |
| **cloud_endpoint** | **str** | Edge uses this cloud URL to activate and periodically check it's license | |
| **edge_license_type** | [**EdgeLicenseType**](EdgeLicenseType.md) |  | [optional] |
| **version** | **int** |  | [optional] |
| **owner_name** | **str** | Owner name | [optional] [readonly] |
| **groups** | [**List[EntityInfo]**](EntityInfo.md) | Groups | [optional] |
| **owner_id** | [**EntityId**](EntityId.md) |  | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EdgeLicenseType (enum)
`LICENSE` | `ADD_ON`

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EdgeInfo.model_validate(data)` or `EdgeInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

