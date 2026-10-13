
# BulkImportRequest

`tb_paas_client.models.BulkImportRequest`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **file** | **str** |  | [optional] |
| **mapping** | [**Mapping**](Mapping.md) |  | [optional] |
| **customer_id** | [**CustomerId**](CustomerId.md) |  | [optional] |
| **entity_group_id** | **str** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### Mapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| columns | List[ColumnMapping] |  | [optional] |
| delimiter | str |  | [optional] |
| update | bool |  | [optional] |
| header | bool |  | [optional] |

#### ColumnMapping
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | BulkImportColumnType |  | [optional] |
| key | str |  | [optional] |

#### BulkImportColumnType (enum)
`NAME` | `TYPE` | `LABEL` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIMESERIES` | `ACCESS_TOKEN` | `X509` | `MQTT_CLIENT_ID` | `MQTT_USER_NAME` | … (32 values total)

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.file`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BulkImportRequest.model_validate(data)` or `BulkImportRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

