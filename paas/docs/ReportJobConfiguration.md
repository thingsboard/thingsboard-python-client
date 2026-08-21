
# ReportJobConfiguration

`tb_paas_client.models.ReportJobConfiguration`

**Extends:** **JobConfiguration**

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **report_template_id** | [**ReportTemplateId**](ReportTemplateId.md) |  | [optional] |
| **user_id** | [**UserId**](UserId.md) |  | [optional] |
| **timezone** | **str** |  | [optional] |
| **targets** | **List[UUID]** |  | [optional] |
| **notification_template_id** | [**NotificationTemplateId**](NotificationTemplateId.md) |  | [optional] |
| **notification_requests** | [**List[NotificationRequest]**](NotificationRequest.md) |  | [optional] |
| **originator** | [**EntityId**](EntityId.md) |  | [optional] |
| **rule_node** | [**RuleNode**](RuleNode.md) |  | [optional] |
| **output_tb_msg_proto** | **str** |  | [optional] |
| **queue_name** | **str** |  | [optional] |
| **scheduler_event_info** | [**EntityInfo**](EntityInfo.md) |  | [optional] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BillingCustomerId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CouponId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `ProductId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `SubscriptionAddonId`, `SubscriptionId`, `SubscriptionPlanId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### JobConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| tasks_key | str |  |  |
| to_reprocess | List[TaskResult] |  | [optional] |
| type | str |  |  |

#### NotificationRequest
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | NotificationRequestId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| targets | List[UUID] |  |  |
| template_id | NotificationTemplateId |  | [optional] |
| template | NotificationTemplate |  | [optional] |
| info | NotificationInfo |  | [optional] |
| additional_config | NotificationRequestConfig |  | [optional] |
| originator_entity_id | EntityId |  | [optional] |
| rule_id | NotificationRuleId |  | [optional] |
| status | NotificationRequestStatus |  | [optional] |
| stats | NotificationRequestStats |  | [optional] |

#### RuleNode
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | RuleNodeId | JSON object with the Rule Node Id. Specify this field to update the Rule Node. Referencing non-existing Rule Node Id will cause error. Omit this field to create new rule node. | [optional] |
| created_time | int | Timestamp of the rule node creation, in milliseconds | [optional] [readonly] |
| additional_info | object | Additional parameters of the rule node. May include: 'layoutX' (number, X coordinate for visualization), 'layoutY' (number, Y coordinate for visualization), 'description' (string). | [optional] |
| rule_chain_id | RuleChainId | JSON object with the Rule Chain Id. | [optional] [readonly] |
| type | str | Full Java Class Name of the rule node implementation. | [optional] |
| name | str | User defined name of the rule node. Used on UI and for logging. | [optional] |
| debug_settings | DebugSettings | Debug settings object. | [optional] |
| singleton_mode | bool | Enable/disable singleton mode. | [optional] |
| queue_name | str | Queue name. | [optional] |
| configuration_version | int | Version of rule node configuration. | [optional] |
| configuration | object | JSON with the rule node configuration. Structure depends on the rule node implementation. | [optional] |
| external_id | RuleNodeId |  | [optional] |
| debug_mode | bool |  | [optional] |

#### EntityInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | EntityId | JSON object with the entity Id. | [optional] |
| name | str | Entity Name | [optional] |

#### TaskResult
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| key | str |  | [optional] |
| success | bool |  | [optional] |
| discarded | bool |  | [optional] |
| finish_ts | int |  | [optional] |
| error | str |  | [optional] |
| job_type | str |  |  |

#### CfReprocessingTaskResult  *(extends TaskResult, job_type=`CF_REPROCESSING`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failure | CfReprocessingTaskFailure |  | [optional] |

#### DummyTaskResult  *(extends TaskResult, job_type=`DUMMY`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failure | DummyTaskFailure |  | [optional] |

#### ReportTaskResult  *(extends TaskResult, job_type=`REPORT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| report | Report |  | [optional] |

#### NotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | NotificationTemplateId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  | [optional] |
| name | str |  |  |
| notification_type | NotificationType |  |  |
| configuration | NotificationTemplateConfig |  |  |

#### NotificationInfo
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| dashboard_id | DashboardId |  | [optional] |
| state_entity_id | EntityId |  | [optional] |
| type | str |  |  |

#### NotificationRequestConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sending_delay_in_sec | int |  | [optional] |
| reports | List[ReportId] |  | [optional] |

#### NotificationRequestStatus (enum)
`PROCESSING` | `SENT` | `SCHEDULED`

#### NotificationRequestStats
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| sent | Dict[str, int] |  | [optional] |
| errors | Dict[str, Dict[str, str]] |  | [optional] |
| total_errors | int |  | [optional] |
| error | str |  | [optional] |
| total_sent | int |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (52 values total)

#### DebugSettings
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| failures_enabled | bool | Debug failures. | [optional] |
| all_enabled | bool | Debug All. Used as a trigger for updating debugAllUntil. | [optional] |
| all_enabled_until | int | Timestamp of the end time for the processing debug events. | [optional] |

#### NotificationType (enum)
`GENERAL` | `ALARM` | `DEVICE_ACTIVITY` | `ENTITY_ACTION` | `ALARM_COMMENT` | `RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT` | `ALARM_ASSIGNMENT` | `NEW_PLATFORM_VERSION` | `ENTITIES_LIMIT` | `ENTITIES_LIMIT_INCREASE_REQUEST` | … (24 values total)

#### NotificationTemplateConfig
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| delivery_methods_templates | Dict[str, DeliveryMethodNotificationTemplate] |  |  |
| attach_report | bool |  | [optional] |
| report_template_id | ReportTemplateId |  | [optional] |
| user_id | UserId |  | [optional] |
| timezone | str |  | [optional] |

#### CfReprocessingTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| entity_info | EntityInfo |  | [optional] |

#### Report
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | ReportId |  | [optional] |
| created_time | int | Entity creation timestamp in milliseconds since Unix epoch | [optional] [readonly] |
| tenant_id | TenantId |  |  |
| customer_id | CustomerId |  | [optional] |
| template_id | ReportTemplateId |  |  |
| format | TbReportFormat |  |  |
| name | str |  |  |
| user_id | UserId |  |  |
| owner_id | EntityId | JSON object with Customer or Tenant Id | [optional] [readonly] |

#### DummyTaskFailure
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| error | str |  | [optional] |
| number | int |  | [optional] |
| fail_always | bool |  | [optional] |

#### DeliveryMethodNotificationTemplate
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| body | str |  |  |
| method | str |  |  |

#### EmailDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`EMAIL`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str |  |  |

#### MicrosoftTeamsDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`MICROSOFT_TEAMS`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str |  | [optional] |
| theme_color | str |  | [optional] |
| button | Button |  | [optional] |

#### MobileAppDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`MOBILE_APP`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str | Subject line for the mobile notification |  |
| additional_config | object | Additional JSON configuration for web buttons/actions | [optional] |

#### SlackDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`SLACK`)*
*See DeliveryMethodNotificationTemplate for properties.*

#### SmsDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`SMS`)*
*See DeliveryMethodNotificationTemplate for properties.*

#### WebDeliveryMethodNotificationTemplate  *(extends DeliveryMethodNotificationTemplate, method=`WEB`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| subject | str | Subject line for the web notification |  |
| additional_config | object | Additional JSON configuration for web buttons/actions | [optional] |

#### TbReportFormat (enum)
`PDF` | `CSV`

#### Button
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| enabled | bool |  | [optional] |
| text | str |  | [optional] |
| link_type | LinkType |  | [optional] |
| link | str |  | [optional] |
| dashboard_id | UUID |  | [optional] |
| dashboard_state | str |  | [optional] |
| set_entity_id_in_state | bool |  | [optional] |

#### LinkType (enum)
`LINK` | `DASHBOARD`

---

### Conventions

- **Package:** `tb_paas_client.models`
- **Attribute access:** `obj.report_template_id`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `ReportJobConfiguration.model_validate(data)` or `ReportJobConfiguration.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

