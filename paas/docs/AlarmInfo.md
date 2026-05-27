
# AlarmInfo

`tb_paas_client.models.AlarmInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AlarmId**](AlarmId.md) | JSON object with the alarm Id. Specify this field to update the alarm. Referencing non-existing alarm Id will cause error. Omit this field to create new alarm. | [optional] |
| **created_time** | **int** | Timestamp of the alarm creation, in milliseconds | [optional] [readonly] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. Derived from the originator entity owner and cannot be set independently; any value supplied in the request body must match the originator's customer or the request is rejected. | [optional] [readonly] |
| **type** | **str** | representing type of the Alarm | |
| **originator** | [**EntityId**](EntityId.md) | JSON object with alarm originator id | |
| **severity** | [**AlarmSeverity**](AlarmSeverity.md) | Alarm severity | |
| **acknowledged** | **bool** | Acknowledged | |
| **cleared** | **bool** | Cleared | |
| **assignee_id** | [**UserId**](UserId.md) | Alarm assignee user id | [optional] |
| **start_ts** | **int** | Timestamp of the alarm start time, in milliseconds | [optional] |
| **end_ts** | **int** | Timestamp of the alarm end time(last time update), in milliseconds | [optional] |
| **ack_ts** | **int** | Timestamp of the alarm acknowledgement, in milliseconds | [optional] |
| **clear_ts** | **int** | Timestamp of the alarm clearing, in milliseconds | [optional] |
| **assign_ts** | **int** | Timestamp of the alarm assignment, in milliseconds | [optional] |
| **details** | **object** | JSON object with alarm details | [optional] |
| **propagate** | **bool** | Propagation flag to specify if alarm should be propagated to parent entities of alarm originator | [optional] |
| **propagate_to_owner** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator | [optional] |
| **propagate_to_owner_hierarchy** | **bool** | Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy | [optional] |
| **propagate_to_tenant** | **bool** | Propagation flag to specify if alarm should be propagated to the tenant entity | [optional] |
| **propagate_relation_types** | **List[str]** | JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored. | [optional] |
| **originator_name** | **str** | Alarm originator name | [optional] |
| **originator_label** | **str** | Alarm originator label | [optional] |
| **originator_display_name** | **str** | Originator display name | [optional] |
| **assignee** | [**AlarmAssignee**](AlarmAssignee.md) | Alarm assignee | [optional] |
| **name** | **str** | representing type of the Alarm | [readonly] |
| **status** | [**AlarmStatus**](AlarmStatus.md) | status of the Alarm | [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AlarmSeverity (enum)
`CRITICAL` | `MAJOR` | `MINOR` | `WARNING` | `INDETERMINATE`

#### AlarmAssignee
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | UserId |  | [optional] |
| first_name | str |  | [optional] |
| last_name | str |  | [optional] |
| email | str |  | [optional] |

#### AlarmStatus (enum)
`ACTIVE_UNACK` | `ACTIVE_ACK` | `CLEARED_UNACK` | `CLEARED_ACK`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AlarmInfo.model_validate(data)` or `AlarmInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

