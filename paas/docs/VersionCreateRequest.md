
# VersionCreateRequest

`tb_paas_client.models.VersionCreateRequest`

Request for creating a version

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **version_name** | **str** |  | [optional] |
| **branch** | **str** |  | [optional] |
| **type** | [**VersionCreateRequestType**](VersionCreateRequestType.md) | Type of the version to create | |



## Subtypes

#### ComplexVersionCreateRequest  *(type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sync_strategy | SyncStrategy |  | [optional] |
| entity_types | Dict[str, EntityTypeVersionCreateConfig] |  | [optional] |

#### SingleEntityVersionCreateRequest  *(type=`SINGLE_ENTITY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_id | EntityId |  | [optional] |
| config | VersionCreateConfig |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### VersionCreateRequestType (enum)
`SINGLE_ENTITY` | `COMPLEX`

#### SyncStrategy (enum)
`MERGE` | `OVERWRITE`

#### EntityTypeVersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| save_permissions | bool |  | [optional] |
| save_group_entities | bool |  | [optional] |
| sync_strategy | SyncStrategy |  | [optional] |
| entity_ids | List[UUID] |  | [optional] |
| all_entities | bool |  | [optional] |

#### VersionCreateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| save_relations | bool |  | [optional] |
| save_attributes | bool |  | [optional] |
| save_credentials | bool |  | [optional] |
| save_calculated_fields | bool |  | [optional] |
| save_permissions | bool |  | [optional] |
| save_group_entities | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.version_name`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `VersionCreateRequest.model_validate(data)` or `VersionCreateRequest.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

