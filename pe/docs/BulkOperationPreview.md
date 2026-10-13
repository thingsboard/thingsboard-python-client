
# BulkOperationPreview

`tb_pe_client.models.BulkOperationPreview`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **total** | **int** | Total number of apps targeted by the bulk operation | [optional] |
| **eligible** | **int** | Number of apps that would be submitted (total minus skipped) | [optional] |
| **skipped_counts_by_reason** | **Dict[str, int]** | Skip count per reason for the targeted apps | [optional] |
| **skipped_sample** | [**List[SkippedApp]**](SkippedApp.md) | Sample of skipped apps, capped per reason. Use the run history to inspect the full list. | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### SkippedApp
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| agent_id | AgentId | Agent Id owning the application | [optional] |
| agent_name | str | Agent name | [optional] |
| application_id | AgentApplicationId | Application Id | [optional] |
| application_name | str | Application name | [optional] |
| reason | SkipReason | Reason for skipping | [optional] |
| msg | str | Optional message in case of a failure | [optional] |

#### SkipReason (enum)
`VERSION_MISMATCH` | `ACTIVE_EVENT` | `RATE_LIMIT_EXCEEDED` | `ERROR`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.total`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `BulkOperationPreview.model_validate(data)` or `BulkOperationPreview.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

