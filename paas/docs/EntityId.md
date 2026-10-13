
# EntityId

`tb_paas_client.models.EntityId`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_type** | [**EntityType**](EntityType.md) |  | |
| **id** | **UUID** | ID of the entity, time-based UUID v1 | |



## Subtypes

#### AdminSettingsId  *(entity_type=`ADMIN_SETTINGS`)*
*(no additional properties)*

#### AgentId  *(entity_type=`AGENT`)*
*(no additional properties)*

#### AgentApplicationId  *(entity_type=`AGENT_APPLICATION`)*
*(no additional properties)*

#### AgentAppEventId  *(entity_type=`AGENT_APP_EVENT`)*
*(no additional properties)*

#### AgentAppProfileId  *(entity_type=`AGENT_APP_PROFILE`)*
*(no additional properties)*

#### AgentAppUnitId  *(entity_type=`AGENT_APP_UNIT`)*
*(no additional properties)*

#### AgentBulkActionId  *(entity_type=`AGENT_BULK_ACTION`)*
*(no additional properties)*

#### AgentProfileId  *(entity_type=`AGENT_PROFILE`)*
*(no additional properties)*

#### AiModelId  *(entity_type=`AI_MODEL`)*
*(no additional properties)*

#### AlarmId  *(entity_type=`ALARM`)*
*(no additional properties)*

#### ApiKeyId  *(entity_type=`API_KEY`)*
*(no additional properties)*

#### ApiUsageStateId  *(entity_type=`API_USAGE_STATE`)*
*(no additional properties)*

#### AssetId  *(entity_type=`ASSET`)*
*(no additional properties)*

#### AssetProfileId  *(entity_type=`ASSET_PROFILE`)*
*(no additional properties)*

#### BillingCustomerId  *(entity_type=`BILLING_CUSTOMER`)*
*(no additional properties)*

#### BlobEntityId  *(entity_type=`BLOB_ENTITY`)*
*(no additional properties)*

#### CalculatedFieldId  *(entity_type=`CALCULATED_FIELD`)*
*(no additional properties)*

#### ConverterId  *(entity_type=`CONVERTER`)*
*(no additional properties)*

#### CouponId  *(entity_type=`COUPON`)*
*(no additional properties)*

#### CustomerId  *(entity_type=`CUSTOMER`)*
*(no additional properties)*

#### DashboardId  *(entity_type=`DASHBOARD`)*
*(no additional properties)*

#### DeviceId  *(entity_type=`DEVICE`)*
*(no additional properties)*

#### DeviceProfileId  *(entity_type=`DEVICE_PROFILE`)*
*(no additional properties)*

#### DomainId  *(entity_type=`DOMAIN`)*
*(no additional properties)*

#### EdgeId  *(entity_type=`EDGE`)*
*(no additional properties)*

#### EntityGroupId  *(entity_type=`ENTITY_GROUP`)*
*(no additional properties)*

#### EntityViewId  *(entity_type=`ENTITY_VIEW`)*
*(no additional properties)*

#### GroupPermissionId  *(entity_type=`GROUP_PERMISSION`)*
*(no additional properties)*

#### IntegrationId  *(entity_type=`INTEGRATION`)*
*(no additional properties)*

#### JobId  *(entity_type=`JOB`)*
*(no additional properties)*

#### MobileAppId  *(entity_type=`MOBILE_APP`)*
*(no additional properties)*

#### MobileAppBundleId  *(entity_type=`MOBILE_APP_BUNDLE`)*
*(no additional properties)*

#### NotificationId  *(entity_type=`NOTIFICATION`)*
*(no additional properties)*

#### NotificationRequestId  *(entity_type=`NOTIFICATION_REQUEST`)*
*(no additional properties)*

#### NotificationRuleId  *(entity_type=`NOTIFICATION_RULE`)*
*(no additional properties)*

#### NotificationTargetId  *(entity_type=`NOTIFICATION_TARGET`)*
*(no additional properties)*

#### NotificationTemplateId  *(entity_type=`NOTIFICATION_TEMPLATE`)*
*(no additional properties)*

#### OAuth2ClientId  *(entity_type=`OAUTH2_CLIENT`)*
*(no additional properties)*

#### OtaPackageId  *(entity_type=`OTA_PACKAGE`)*
*(no additional properties)*

#### ProductId  *(entity_type=`PRODUCT`)*
*(no additional properties)*

#### QueueId  *(entity_type=`QUEUE`)*
*(no additional properties)*

#### QueueStatsId  *(entity_type=`QUEUE_STATS`)*
*(no additional properties)*

#### ReportId  *(entity_type=`REPORT`)*
*(no additional properties)*

#### ReportTemplateId  *(entity_type=`REPORT_TEMPLATE`)*
*(no additional properties)*

#### RoleId  *(entity_type=`ROLE`)*
*(no additional properties)*

#### RpcId  *(entity_type=`RPC`)*
*(no additional properties)*

#### RuleChainId  *(entity_type=`RULE_CHAIN`)*
*(no additional properties)*

#### RuleNodeId  *(entity_type=`RULE_NODE`)*
*(no additional properties)*

#### SchedulerEventId  *(entity_type=`SCHEDULER_EVENT`)*
*(no additional properties)*

#### SecretId  *(entity_type=`SECRET`)*
*(no additional properties)*

#### SubscriptionId  *(entity_type=`SUBSCRIPTION`)*
*(no additional properties)*

#### SubscriptionAddonId  *(entity_type=`SUBSCRIPTION_ADDON`)*
*(no additional properties)*

#### SubscriptionPlanId  *(entity_type=`SUBSCRIPTION_PLAN`)*
*(no additional properties)*

#### TbResourceId  *(entity_type=`TB_RESOURCE`)*
*(no additional properties)*

#### TenantId  *(entity_type=`TENANT`)*
*(no additional properties)*

#### TenantProfileId  *(entity_type=`TENANT_PROFILE`)*
*(no additional properties)*

#### UserId  *(entity_type=`USER`)*
*(no additional properties)*

#### WidgetsBundleId  *(entity_type=`WIDGETS_BUNDLE`)*
*(no additional properties)*

#### WidgetTypeId  *(entity_type=`WIDGET_TYPE`)*
*(no additional properties)*

## Referenced Types

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityId.model_validate(data)` or `EntityId.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

