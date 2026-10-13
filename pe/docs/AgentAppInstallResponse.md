
# AgentAppInstallResponse

`tb_pe_client.models.AgentAppInstallResponse`

Response payload for the install-agent-application endpoint. Carries both the created application and the INSTALL event so the caller can open a progress dialog without a second round-trip.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **application** | [**AgentApplication**](AgentApplication.md) | The newly created agent application. | [optional] |
| **event** | [**AgentAppEvent**](AgentAppEvent.md) | The INSTALL event created alongside the application. | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AgentAppEventId`, `AgentAppProfileId`, `AgentAppUnitId`, `AgentApplicationId`, `AgentBulkActionId`, `AgentId`, `AgentProfileId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### AgentApplication
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | AgentApplicationId | JSON object with the Agent Application Id. | [optional] |
| created_time | int | Timestamp of the agent application creation, in milliseconds | [optional] [readonly] |
| tenant_id | TenantId | JSON object with Tenant Id. | [optional] [readonly] |
| agent_id | AgentId | Agent this application belongs to |  |
| name | str | Application name (not unique across tenant) | [optional] |
| template_version | str | Template version this application is based on |  |
| desired_template_version | str |  | [optional] |
| app_type | AgentApplicationType | Application type |  |
| config | DockerComposeConfig |  | [optional] |
| version | int |  | [optional] |
| project_name | str |  | [optional] |
| pending_deletion | bool |  | [optional] |
| origin | AgentApplicationOrigin | Origin of the application (INSTALLED or DISCOVERED) | [optional] |
| application_profile_id | AgentAppProfileId | Application Profile Id. When set, config is read-only and inherited from the profile. | [optional] |
| profile_config_version | int |  | [optional] |

#### AgentAppEvent
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

#### AgentApplicationType (enum)
`GENERIC` | `EDGE` | `GATEWAY`

#### DockerComposeConfig  *(extends AgentAppConfig)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| compose | object |  | [optional] |
| compose_type | str |  | [optional] |

#### AgentApplicationOrigin (enum)
`INSTALLED` | `DISCOVERED` | `AUTO_PROVISIONED`

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

#### AgentAppConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| arguments | List[AgentAppArgument] |  | [optional] |
| edge_routing_key | str |  | [optional] |
| type | AgentAppConfigType |  | [optional] |

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
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (53 values total)

#### AgentAppArgument
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str | Argument name, referenced in the compose as ${tb.<name>}. | [optional] |
| source_type | AgentAppArgumentSource | Source entity the value is resolved from. | [optional] |
| source_entity_id | EntityId | Concrete source entity id. Required when sourceType references a specific entity (DEVICE, ASSET, CUSTOMER, EDGE); ignored for the context-derived sources. | [optional] |
| value_type | AgentAppArgumentValueType | Whether the value is read from an attribute or the latest telemetry. | [optional] |
| scope | AttributeScope | Attribute scope. Applicable only when valueType is ATTRIBUTE. Defaults to SERVER_SCOPE. | [optional] |
| key | str | Attribute or latest telemetry key to read. | [optional] |
| default_value | str | Optional fallback value used when the source has no value for the key. | [optional] |
| format | AgentAppArgumentFormat | How the resolved value is injected into the compose: STRING (quoted) or JSON (raw, for arrays/objects/numbers when the placeholder is the whole value). Defaults to STRING. | [optional] |

#### AgentAppConfigType (enum)
`DOCKER_COMPOSE`

#### AgentAppArgumentSource (enum)
`AGENT` | `OWNER` | `RELATED_ENTITY` | `TENANT` | `DEVICE` | `ASSET` | `CUSTOMER` | `EDGE`

#### AgentAppArgumentValueType (enum)
`ATTRIBUTE` | `LATEST_TELEMETRY`

#### AttributeScope (enum)
`CLIENT_SCOPE` | `SERVER_SCOPE` | `SHARED_SCOPE`

#### AgentAppArgumentFormat (enum)
`STRING` | `JSON`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.application`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `AgentAppInstallResponse.model_validate(data)` or `AgentAppInstallResponse.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

