
# GeofencingCalculatedFieldConfiguration

`tb_paas_client.models.GeofencingCalculatedFieldConfiguration`

**Extends:** **CalculatedFieldConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **entity_coordinates** | [**EntityCoordinates**](EntityCoordinates.md) |  | |
| **zone_groups** | [**Dict[str, ZoneGroupConfiguration]**](ZoneGroupConfiguration.md) |  | |
| **scheduled_update_enabled** | **bool** |  | [optional] |
| **scheduled_update_interval** | **int** |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### CalculatedFieldConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| output | Output |  | [optional] |
| type | str |  |  |

#### EntityCoordinates
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| latitude_key_name | str |  |  |
| longitude_key_name | str |  |  |

#### ZoneGroupConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ref_entity_id | EntityId |  | [optional] |
| ref_dynamic_source_configuration | CfArgumentDynamicSourceConfiguration |  | [optional] |
| perimeter_key_name | str |  |  |
| report_strategy | GeofencingReportStrategy |  |  |
| create_relations_with_matched_zones | bool |  | [optional] |
| relation_type | str |  | [optional] |
| direction | EntitySearchDirection |  | [optional] |

#### Output
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| decimals_by_default | int |  | [optional] |
| name | str |  | [optional] |
| scope | AttributeScope |  | [optional] |
| strategy | object |  | [optional] |
| type | str |  |  |

#### AttributesOutput  *(extends Output, type=`ATTRIBUTES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | AttributesOutputStrategy |  | [optional] |

#### TimeSeriesOutput  *(extends Output, type=`TIME_SERIES`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| strategy | TimeSeriesOutputStrategy |  | [optional] |

#### CfArgumentDynamicSourceConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### CurrentOwnerDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`CURRENT_OWNER`)*
*See CfArgumentDynamicSourceConfiguration for properties.*

#### RelationPathQueryDynamicSourceConfiguration  *(extends CfArgumentDynamicSourceConfiguration, type=`RELATION_PATH_QUERY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| levels | List[RelationPathLevel] |  | [optional] |

#### GeofencingReportStrategy (enum)
`REPORT_TRANSITION_EVENTS_ONLY` | `REPORT_PRESENCE_STATUS_ONLY` | `REPORT_TRANSITION_EVENTS_AND_PRESENCE_STATUS`

#### EntitySearchDirection (enum)
`FROM` | `TO`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### TimeSeriesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### TimeSeriesImmediateOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| ttl | int |  | [optional] |
| save_time_series | bool |  | [optional] |
| save_latest | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### TimeSeriesRuleChainOutputStrategy  *(extends TimeSeriesOutputStrategy, type=`RULE_CHAIN`)*
*See TimeSeriesOutputStrategy for properties.*

#### AttributesOutputStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### AttributesImmediateOutputStrategy  *(extends AttributesOutputStrategy, type=`IMMEDIATE`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| send_attributes_updated_notification | bool |  | [optional] |
| update_attributes_only_on_value_change | bool |  | [optional] |
| save_attribute | bool |  | [optional] |
| send_ws_update | bool |  | [optional] |
| process_cfs | bool |  | [optional] |

#### AttributesRuleChainOutputStrategy  *(extends AttributesOutputStrategy, type=`RULE_CHAIN`)*
*See AttributesOutputStrategy for properties.*

#### RelationPathLevel
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| direction | EntitySearchDirection |  |  |
| relation_type | str |  |  |

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.entity_coordinates`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `GeofencingCalculatedFieldConfiguration.model_validate(data)` or `GeofencingCalculatedFieldConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

