
# AgentInfo

`tb_paas_client.models.AgentInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | [**AgentId**](AgentId.md) | JSON object with the Agent Id. Specify this field to update the Agent. Referencing non-existing Agent Id will cause error. Omit this field to create new Agent. | [optional] |
| **created_time** | **int** | Timestamp of the agent creation, in milliseconds | [optional] [readonly] |
| **additional_info** | **object** |  | [optional] |
| **tenant_id** | [**TenantId**](TenantId.md) | JSON object with Tenant Id. Use 'assignAgentToTenant' to change the Tenant Id. | [optional] [readonly] |
| **customer_id** | [**CustomerId**](CustomerId.md) | JSON object with Customer Id. | [optional] [readonly] |
| **name** | **str** | Unique Agent Name in scope of Tenant | |
| **description** | **str** | Agent description | [optional] |
| **routing_key** | **str** | Agent routing key used for authentication | |
| **secret** | **str** | Agent secret used for authentication | |
| **agent_profile_id** | [**AgentProfileId**](AgentProfileId.md) | JSON object with Agent Profile Id. Nullable. | [optional] |
| **version** | **int** |  | [optional] |
| **customer_title** | **str** | Title of the Customer that owns the agent. | [optional] [readonly] |
| **customer_is_public** | **bool** | Indicates special 'Public' Customer that is auto-generated to use the agents on public dashboards. | [optional] [readonly] |
| **agent_profile_name** | **str** | Name of the Agent Profile the agent belongs to. | [optional] [readonly] |
| **owner_name** | **str** | Owner name — tenant title if the agent is owned by a tenant, or customer title otherwise. | [optional] [readonly] |
| **groups** | [**List[EntityInfo]**](EntityInfo.md) | Entity groups that contain this agent (excluding the implicit 'All' group). | [optional] |
| **active** | **bool** | Whether the agent currently has an active connection (derived from server-scope 'active' attribute). | [optional] [readonly] |
| **agent_version** | **str** | Agent software version reported on the last connect (derived from server-scope 'agentVersion' attribute). | [optional] [readonly] |
| **upgrade_target_image_ref** | **str** | Image reference this agent should be upgraded to, or null when no upgrade applies. Resolved from the published version graph. | [optional] [readonly] |
| **owner_id** | [**EntityId**](EntityId.md) | JSON object with Customer or Tenant Id | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentInfo.model_validate(data)` or `AgentInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

