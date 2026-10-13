
# SubscriptionDetails

`tb_paas_client.models.SubscriptionDetails`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**SubscriptionId**](SubscriptionId.md) |  | [optional] |
| **created_time** | **int** | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **external_id** | **str** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) |  | [optional] |
| **billing_customer_id** | [**BillingCustomerId**](BillingCustomerId.md) |  | [optional] |
| **subscription_plan_id** | [**SubscriptionPlanId**](SubscriptionPlanId.md) |  | [optional] |
| **current_period_start_ts** | **int** |  | [optional] |
| **current_period_end_ts** | **int** |  | [optional] |
| **active** | **bool** |  | [optional] |
| **trial** | **bool** |  | [optional] |
| **trial_end_ts** | **int** |  | [optional] |
| **status** | **str** |  | [optional] |
| **last_paid** | **bool** |  | [optional] |
| **upcoming_invoice_date** | **int** |  | [optional] |
| **upcoming_invoice_amount_due** | **int** |  | [optional] |
| **coupon_id** | [**CouponId**](CouponId.md) |  | [optional] |
| **discount_end_date** | **int** |  | [optional] |
| **subscription_plan_name** | **str** |  | [optional] |
| **plan_has_addons** | **bool** |  | [optional] |
| **plan_ui_type** | **str** |  | [optional] |
| **plan_is_free** | **bool** |  | [optional] |
| **plan_is_active** | **bool** |  | [optional] |
| **edge_count_included** | **int** |  | [optional] |
| **items** | [**SubscriptionItems**](SubscriptionItems.md) |  | [optional] |
| **discount** | [**Discount**](Discount.md) |  | [optional] |
| **name** | **str** |  | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### SubscriptionItems
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| extra_device_pack_count | int |  | [optional] |
| extra_customer_pack_count | int |  | [optional] |
| extra_integration_pack_count | int |  | [optional] |
| extra_calculated_field_count | int |  | [optional] |
| traffic_pack_count | int |  | [optional] |
| compute_pack_count | int |  | [optional] |
| storage_pack_count | int |  | [optional] |
| alarm_pack_count | int |  | [optional] |
| email_pack_count | int |  | [optional] |
| sms_pack_count | int |  | [optional] |
| ai_credits_pack_count | int |  | [optional] |
| edge_enabled | bool |  | [optional] |
| extra_edge_count | int |  | [optional] |
| trendz_enabled | bool |  | [optional] |
| white_labeling_addon_enabled | bool |  | [optional] |

#### Discount
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| coupon_code | str |  | [optional] |
| coupon_valid | bool |  | [optional] |
| amount_off | int |  | [optional] |
| percent_off | float |  | [optional] |
| coupon_id | CouponId |  | [optional] |
| duration | CouponDuration |  | [optional] |
| duration_in_months | int |  | [optional] |
| end_date | int |  | [optional] |
| package | bool |  | [optional] |

#### CouponDuration (enum)
`FOREVER` | `ONCE` | `REPEATING`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SubscriptionDetails.model_validate(data)` or `SubscriptionDetails.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

