
# SingleEntityVersionCreateRequest

`tb_pe_client.models.SingleEntityVersionCreateRequest`

**Extends:** **VersionCreateRequest**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_id** | [**EntityId**](EntityId.md) |  | [optional] |
| **config** | [**VersionCreateConfig**](VersionCreateConfig.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### VersionCreateRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| version_name | str |  | [optional] |
| branch | str |  | [optional] |
| type | VersionCreateRequestType | Type of the version to create |  |

#### VersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| save_permissions | bool |  | [optional] |
| save_group_entities | bool |  | [optional] |

#### VersionCreateRequestType (enum)
`SINGLE_ENTITY` | `COMPLEX`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `SingleEntityVersionCreateRequest.model_validate(data)` or `SingleEntityVersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

