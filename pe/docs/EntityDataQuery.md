
# EntityDataQuery

`tb_pe_client.models.EntityDataQuery`

Entity data query to find entities. Page size is capped at 100.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_filter** | [**EntityFilter**](EntityFilter.md) |  | [optional] |
| **key_filters** | [**List[KeyFilter]**](KeyFilter.md) |  | [optional] |
| **key_filters_operation** | [**AlarmRuleComplexOperation**](AlarmRuleComplexOperation.md) |  | [optional] |
| **page_link** | [**EntityDataPageLink**](EntityDataPageLink.md) |  | [optional] |
| **entity_fields** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **latest_values** | [**List[EntityKey]**](EntityKey.md) |  | [optional] |
| **key_filters_operation_or_default** | [**AlarmRuleComplexOperation**](AlarmRuleComplexOperation.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### EntityFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### ApiUsageStateFilter  *(extends EntityFilter, type=`apiUsageState`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| customer_id | CustomerId |  | [optional] |

#### AssetSearchQueryFilter  *(extends EntityFilter, type=`assetSearchQuery`)*
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

#### AssetTypeFilter  *(extends EntityFilter, type=`assetType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| asset_types | List[str] |  | [optional] |
| asset_name_filter | str |  | [optional] |
| asset_type | str |  | [optional] |

#### DeviceSearchQueryFilter  *(extends EntityFilter, type=`deviceSearchQuery`)*
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

#### DeviceTypeFilter  *(extends EntityFilter, type=`deviceType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| device_types | List[str] |  | [optional] |
| device_name_filter | str |  | [optional] |
| device_type | str |  | [optional] |

#### EdgeSearchQueryFilter  *(extends EntityFilter, type=`edgeSearchQuery`)*
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

#### EdgeTypeFilter  *(extends EntityFilter, type=`edgeType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| edge_types | List[str] |  | [optional] |
| edge_name_filter | str |  | [optional] |
| edge_type | str |  | [optional] |

#### EntitiesByGroupNameFilter  *(extends EntityFilter, type=`entitiesByGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| owner_id | EntityId |  | [optional] |
| entity_group_name_filter | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| state_entity_param_name | str |  | [optional] |

#### EntityGroupFilter  *(extends EntityFilter, type=`entityGroup`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group | str |  | [optional] |
| group_state_entity | bool |  | [optional] |
| default_state_group_type | EntityType |  | [optional] |
| default_state_entity_group | str |  | [optional] |

#### EntityGroupListFilter  *(extends EntityFilter, type=`entityGroupList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_list | List[str] |  | [optional] |

#### EntityGroupNameFilter  *(extends EntityFilter, type=`entityGroupName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| group_type | EntityType |  | [optional] |
| entity_group_name_filter | str |  | [optional] |

#### EntityListFilter  *(extends EntityFilter, type=`entityList`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_list | List[str] |  | [optional] |

#### EntityNameFilter  *(extends EntityFilter, type=`entityName`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |
| entity_name_filter | str |  | [optional] |

#### EntityTypeFilter  *(extends EntityFilter, type=`entityType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_type | EntityType |  | [optional] |

#### EntityViewSearchQueryFilter  *(extends EntityFilter, type=`entityViewSearchQuery`)*
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

#### EntityViewTypeFilter  *(extends EntityFilter, type=`entityViewType`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| entity_view_types | List[str] |  | [optional] |
| entity_view_name_filter | str |  | [optional] |
| entity_view_type | str |  | [optional] |

#### RelationsQueryFilter  *(extends EntityFilter, type=`relationsQuery`)*
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

#### SchedulerEventFilter  *(extends EntityFilter, type=`schedulerEvent`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| originator | AliasEntityId |  | [optional] |
| event_type | str |  | [optional] |
| originator_state_entity | bool |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### SingleEntityFilter  *(extends EntityFilter, type=`singleEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |

#### StateEntityFilter  *(extends EntityFilter, type=`stateEntity`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_state_entity | AliasEntityId |  | [optional] |

#### StateEntityOwnerFilter  *(extends EntityFilter, type=`stateEntityOwner`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| single_entity | AliasEntityId |  | [optional] |
| default_state_entity | AliasEntityId |  | [optional] |

#### KeyFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| value_type | EntityKeyValueType |  | [optional] |
| predicate | KeyFilterPredicate |  | [optional] |

#### AlarmRuleComplexOperation (enum)
`AND` | `OR`

#### EntityDataPageLink
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| page_size | int |  | [optional] |
| page | int |  | [optional] |
| text_search | str |  | [optional] |
| sort_order | EntityDataSortOrder |  | [optional] |
| dynamic | bool |  | [optional] |

#### EntityKey
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | EntityKeyType |  | [optional] |
| key | str |  | [optional] |

#### EntityKeyValueType (enum)
`STRING` | `NUMERIC` | `BOOLEAN` | `DATE_TIME`

#### KeyFilterPredicate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### BooleanFilterPredicate  *(extends KeyFilterPredicate, type=`BOOLEAN`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | BooleanOperation |  | [optional] |
| value | FilterPredicateValueBoolean | The value associated with the filter predicate | [optional] |

#### ComplexFilterPredicate  *(extends KeyFilterPredicate, type=`COMPLEX`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | AlarmRuleComplexOperation |  | [optional] |
| predicates | List[KeyFilterPredicate] |  | [optional] |

#### NumericFilterPredicate  *(extends KeyFilterPredicate, type=`NUMERIC`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | NumericOperation |  | [optional] |
| value | FilterPredicateValueDouble | The value associated with the filter predicate | [optional] |

#### StringFilterPredicate  *(extends KeyFilterPredicate, type=`STRING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| operation | StringOperation |  | [optional] |
| value | FilterPredicateValueString | The value associated with the filter predicate | [optional] |
| ignore_case | bool |  | [optional] |

#### EntityDataSortOrder
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | EntityKey |  | [optional] |
| direction | Direction |  | [optional] |

#### EntityKeyType (enum)
`ATTRIBUTE` | `CLIENT_ATTRIBUTE` | `SHARED_ATTRIBUTE` | `SERVER_ATTRIBUTE` | `TIME_SERIES` | `ENTITY_FIELD` | `ALARM_FIELD`

#### AliasEntityId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| alias_entity_type | AliasEntityType |  | [optional] |
| entity_type | EntityType |  |  |
| id | UUID | ID of the entity, time-based UUID v1 |  |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### RelationEntityTypeFilter
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| relation_type | str | Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages'). | [optional] |
| entity_types | List[EntityType] | Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET'). | [optional] |
| negate | bool | Negate relation type between root entity and other entity. | [optional] |

#### Direction (enum)
`ASC` | `DESC`

#### AliasEntityType (enum)
`CURRENT_CUSTOMER` | `CURRENT_TENANT` | `CURRENT_USER` | `CURRENT_USER_OWNER`

#### StringOperation (enum)
`EQUAL` | `NOT_EQUAL` | `STARTS_WITH` | `ENDS_WITH` | `CONTAINS` | `NOT_CONTAINS` | `IN` | `NOT_IN`

#### FilterPredicateValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | str |  | [optional] |
| user_value | str |  | [optional] |
| dynamic_value | DynamicValueString |  | [optional] |

#### NumericOperation (enum)
`EQUAL` | `NOT_EQUAL` | `GREATER` | `LESS` | `GREATER_OR_EQUAL` | `LESS_OR_EQUAL`

#### FilterPredicateValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | float |  | [optional] |
| user_value | float |  | [optional] |
| dynamic_value | DynamicValueDouble |  | [optional] |

#### BooleanOperation (enum)
`EQUAL` | `NOT_EQUAL`

#### FilterPredicateValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| default_value | bool |  | [optional] |
| user_value | bool |  | [optional] |
| dynamic_value | DynamicValueBoolean |  | [optional] |

#### DynamicValueString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | str |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueDouble
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | float |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| resolved_value | bool |  | [optional] |
| source_type | DynamicValueSourceType |  | [optional] |
| source_attribute | str |  | [optional] |
| inherit | bool |  | [optional] |

#### DynamicValueSourceType (enum)
`CURRENT_TENANT` | `CURRENT_CUSTOMER` | `CURRENT_USER` | `CURRENT_DEVICE`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.entity_filter`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `EntityDataQuery.model_validate(data)` or `EntityDataQuery.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

