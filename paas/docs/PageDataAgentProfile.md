
# PageDataAgentProfile

`tb_paas_client.models.PageDataAgentProfile`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[AgentProfile]**](AgentProfile.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentProfile
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AgentProfileId | JSON object with the Agent Profile Id. | [optional] |
| created_time | int | Timestamp of the profile creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| name | str | Unique profile name within tenant |  |
| description | str | Profile description | [optional] |
| provision_key | str | Provision key for future auto-provisioning | [optional] |
| provision_secret | str | Provision secret for future auto-provisioning | [optional] |
| provision_type | AgentProvisionType | Provisioning strategy. DISABLED by default. | [optional] |
| version | int |  | [optional] |
| default | bool | Used to mark the default profile that will be assigned to agents when no profile is specified. | [optional] |

#### AgentProvisionType (enum)
`DISABLED` | `NO_AUTO_INSTALL` | `AUTO_INSTALL_PER_APP_TYPE` | `AUTO_INSTALL_PER_APP_PROFILE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAgentProfile.model_validate(data)` or `PageDataAgentProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

