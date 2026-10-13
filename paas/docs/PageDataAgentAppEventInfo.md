
# PageDataAgentAppEventInfo

`tb_paas_client.models.PageDataAgentAppEventInfo`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[AgentAppEventInfo]**](AgentAppEventInfo.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentAppEventInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AgentAppEventId | JSON object with the Agent App Event Id. | [optional] |
| created_time | int | Timestamp of the event creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| application_id | AgentApplicationId |  | [optional] |
| agent_id | AgentId |  | [optional] |
| application_name | str |  | [optional] |
| action_type | AgentAppEventActionType |  | [optional] |
| start_status | ProcessingStartStatus |  | [optional] |
| processing_status | AgentProcessingStatus |  | [optional] |
| current_step_id | UUID |  | [optional] |
| current_activity | str |  | [optional] |
| error_message | str |  | [optional] |
| updated_time | int |  | [optional] |
| step_states | Dict[str, AgentAppEventStepStatesValue] |  | [optional] |
| bulk_action_id | UUID |  | [optional] |
| resolved_arguments | Dict[str, str] |  | [optional] |
| winner_container_id | str |  | [optional] |
| finalize_deadline_ts | int |  | [optional] |
| context_metadata | Dict[str, str] |  | [optional] |
| agent_name | str | Name of the Agent that owns the Application. | [optional] [readonly] |

#### AgentAppEventActionType (enum)
`INSTALL` | `UPDATE` | `DELETE` | `RESTART` | `ROLLBACK` | `UPGRADE` | `AGENT_UPGRADE`

#### ProcessingStartStatus (enum)
`DELIVERY_FAIL` | `PENDING` | `DELIVERED`

#### AgentProcessingStatus (enum)
`PENDING` | `QUEUED` | `PROCESSING` | `FINISHED` | `ERROR` | `START_FAILED`

#### AgentAppEventStepStatesValue
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | AgentAppStepType |  | [optional] |
| backup_volumes | StepFieldListString |  | [optional] |
| service_image_regex_patterns | StepFieldListString |  | [optional] |
| remove_volumes | StepFieldBoolean |  | [optional] |
| pull_images | StepFieldBoolean |  | [optional] |
| failed_event_id | StepFieldAgentAppEventId |  | [optional] |
| image | StepFieldString |  | [optional] |
| entrypoint | StepFieldListString |  | [optional] |
| cmd | StepFieldListString |  | [optional] |
| env | StepFieldListString |  | [optional] |
| binds | StepFieldListString |  | [optional] |
| networks | StepFieldListString |  | [optional] |
| retries | StepFieldInteger |  | [optional] |
| network_from_service_image_regex_pattern | StepFieldString |  | [optional] |

#### AgentAppStepType (enum)
`COMPOSE_TEMPLATE` | `COMPOSE` | `COMPOSE_START` | `COMPOSE_DOWN` | `ROLLBACK` | `BACKUP_VOLUME` | `BACKUP_VOLUME_REMOVE` | `COMPOSE_RESTART` | `RUN_JOB` | `AGENT_PREPARE` | … (11 values total)

#### StepFieldListString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| user_choice | bool |  | [optional] |
| value | List[str] |  | [optional] |

#### StepFieldBoolean
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | bool |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldAgentAppEventId
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | AgentAppEventId |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldString
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | str |  | [optional] |
| user_choice | bool |  | [optional] |

#### StepFieldInteger
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| value | int |  | [optional] |
| user_choice | bool |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (59 values total)

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataAgentAppEventInfo.model_validate(data)` or `PageDataAgentAppEventInfo.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

