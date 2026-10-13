
# PageDataAgentBulkAction

`tb_paas_client.models.PageDataAgentBulkAction`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[AgentBulkAction]**](AgentBulkAction.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentBulkAction
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AgentBulkActionId | JSON object with the Agent Bulk Action Id. | [optional] |
| created_time | int | Timestamp of the bulk action creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| agent_profile_id | UUID |  | [optional] |
| application_profile_id | UUID |  | [optional] |
| action_type | AgentAppEventActionType |  | [optional] |
| status | AgentBulkActionStatus |  | [optional] |
| error_msg | str |  | [optional] |
| processing_started_time | int |  | [optional] |
| total | int |  | [optional] |
| submitted | int |  | [optional] |
| skip_counts | Dict[str, int] |  | [optional] |

#### AgentAppEventActionType (enum)
`INSTALL` | `UPDATE` | `DELETE` | `RESTART` | `ROLLBACK` | `UPGRADE` | `AGENT_UPGRADE`

#### AgentBulkActionStatus (enum)
`QUEUED` | `IN_PROGRESS` | `STARTED` | `START_FAILED`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAgentBulkAction.model_validate(data)` or `PageDataAgentBulkAction.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

