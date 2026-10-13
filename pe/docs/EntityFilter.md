
# EntityFilter

`tb_pe_client.models.EntityFilter`

Filter for selecting entities

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **str** |  | |



## Subtypes

#### ApiUsageStateFilter  *(type=`apiUsageState`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | CustomerId |  | [optional] |

#### AssetSearchQueryFilter  *(type=`assetSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| asset_types | List[str] |  | [optional] |

#### AssetTypeFilter  *(type=`assetType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| asset_types | List[str] |  | [optional] |
| asset_name_filter | str |  | [optional] |
| asset_type | str |  | [optional] |

#### DeviceSearchQueryFilter  *(type=`deviceSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| device_types | List[str] |  | [optional] |

#### DeviceTypeFilter  *(type=`deviceType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_types | List[str] |  | [optional] |
| device_name_filter | str |  | [optional] |
| device_type | str |  | [optional] |

#### EdgeSearchQueryFilter  *(type=`edgeSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| edge_types | List[str] |  | [optional] |

#### EdgeTypeFilter  *(type=`edgeType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edge_types | List[str] |  | [optional] |
| edge_name_filter | str |  | [optional] |
| edge_type | str |  | [optional] |

#### EntitiesByGroupNameFilter  *(type=`entitiesByGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| owner_id | EntityId |  | [optional] |
| entity_group_name_filter | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| state_entity_param_name | str |  | [optional] |

#### EntityGroupFilter  *(type=`entityGroup`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| default_state_group_type | EntityType |  | [optional] |
| default_state_entity_group | str |  | [optional] |

#### EntityGroupListFilter  *(type=`entityGroupList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_list | List[str] |  | [optional] |

#### EntityGroupNameFilter  *(type=`entityGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_name_filter | str |  | [optional] |

#### EntityListFilter  *(type=`entityList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_list | List[str] |  | [optional] |

#### EntityNameFilter  *(type=`entityName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_name_filter | str |  | [optional] |

#### EntityTypeFilter  *(type=`entityType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |

#### EntityViewSearchQueryFilter  *(type=`entityViewSearchQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |
| entity_view_types | List[str] |  | [optional] |

#### EntityViewTypeFilter  *(type=`entityViewType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_view_types | List[str] |  | [optional] |
| entity_view_name_filter | str |  | [optional] |
| entity_view_type | str |  | [optional] |

#### RelationsQueryFilter  *(type=`relationsQuery`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| root_entity | AliasEntityId |  | [optional] |
| multi_root | bool |  | [optional] |
| multi_root_entities_type | EntityType |  | [optional] |
| multi_root_entity_ids | List[str] |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |
| filters | List[RelationEntityTypeFilter] |  | [optional] |
| max_level | int |  | [optional] |
| fetch_last_level_only | bool |  | [optional] |
| negate | bool |  | [optional] |
| root_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### SchedulerEventFilter  *(type=`schedulerEvent`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| originator | AliasEntityId |  | [optional] |
| event_type | str |  | [optional] |
| originator_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### SingleEntityFilter  *(type=`singleEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |

#### StateEntityFilter  *(type=`stateEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_state_entity | AliasEntityId |  | [optional] |

#### StateEntityOwnerFilter  *(type=`stateEntityOwner`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AliasEntityId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alias_entity_type | AliasEntityType |  | [optional] |
| entity_type | EntityType |  |  |
| id | UUID | ID of the entity, time-based UUID v1 |  |

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### RelationEntityTypeFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relation_type | str | Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages'). | [optional] |
| entity_types | List[EntityType] | Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET'). | [optional] |
| negate | bool | Negate relation type between root entity and other entity. | [optional] |

#### AliasEntityType (enum)
`CURRENT_CUSTOMER` | `CURRENT_TENANT` | `CURRENT_USER` | `CURRENT_USER_OWNER`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.type`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityFilter.model_validate(data)` or `EntityFilter.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

