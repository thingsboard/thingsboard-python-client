
# PageDataTenantProfile

`tb_pe_client.models.PageDataTenantProfile`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **data** | [**List[TenantProfile]**](TenantProfile.md) | Array of the entities | [optional] |
| **total_pages** | **int** | Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria | [optional] [readonly] |
| **total_elements** | **int** | Total number of elements in all available pages | [optional] [readonly] |
| **has_next** | **bool** | 'false' value indicates the end of the result set | [optional] [readonly] |



## Referenced Types

> **EntityId types** (`AdminSettingsId`, `AiModelId`, `AlarmId`, `ApiKeyId`, `ApiUsageStateId`, `AssetId`, `AssetProfileId`, `BlobEntityId`, `CalculatedFieldId`, `ConverterId`, `CustomerId`, `DashboardId`, `DeviceId`, `DeviceProfileId`, `DomainId`, `EdgeId`, `EntityGroupId`, `EntityViewId`, `GroupPermissionId`, `IntegrationId`, `JobId`, `MobileAppBundleId`, `MobileAppId`, `NotificationId`, `NotificationRequestId`, `NotificationRuleId`, `NotificationTargetId`, `NotificationTemplateId`, `OAuth2ClientId`, `OtaPackageId`, `QueueId`, `QueueStatsId`, `ReportId`, `ReportTemplateId`, `RoleId`, `RpcId`, `RuleChainId`, `RuleNodeId`, `SchedulerEventId`, `SecretId`, `TbResourceId`, `TenantId`, `TenantProfileId`, `UserId`, `WidgetTypeId`, `WidgetsBundleId`, etc.): `{entity_type: EntityType, id: UUID}` — all EntityId subtypes share this structure.

#### TenantProfile
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| id | TenantProfileId | JSON object with the tenant profile Id. Specify this field to update the tenant profile. Referencing non-existing tenant profile Id will cause error. Omit this field to create new tenant profile. | [optional] |
| created_time | int | Timestamp of the tenant profile creation, in milliseconds | [optional] [readonly] |
| name | str | Name of the tenant profile | [optional] |
| description | str | Description of the tenant profile | [optional] |
| default | bool | Default Tenant profile to be used. | [optional] |
| isolated_tb_rule_engine | bool | If enabled, will push all messages related to this tenant and processed by the rule engine into separate queue. Useful for complex microservices deployments, to isolate processing of the data for specific tenants | [optional] |
| profile_data | TenantProfileData |  | [optional] |

#### TenantProfileData
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| configuration | TenantProfileConfiguration | Complex JSON object that contains profile settings: max devices, max assets, rate limits, etc. | [optional] |
| queue_configuration | List[TenantProfileQueueConfiguration] | JSON array of queue configuration per tenant profile | [optional] |

#### TenantProfileConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | str |  |  |

#### DefaultTenantProfileConfiguration  *(extends TenantProfileConfiguration, type=`DEFAULT`)*
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| max_devices | int |  | [optional] |
| max_assets | int |  | [optional] |
| max_customers | int |  | [optional] |
| max_users | int |  | [optional] |
| max_dashboards | int |  | [optional] |
| max_rule_chains | int |  | [optional] |
| max_edges | int |  | [optional] |
| max_resources_in_bytes | int |  | [optional] |
| max_ota_packages_in_bytes | int |  | [optional] |
| max_resource_size | int |  | [optional] |
| max_report_size_in_bytes | int |  | [optional] |
| max_integrations | int |  | [optional] |
| max_converters | int |  | [optional] |
| max_scheduler_events | int |  | [optional] |
| transport_tenant_msg_rate_limit | str |  | [optional] |
| transport_tenant_telemetry_msg_rate_limit | str |  | [optional] |
| transport_tenant_telemetry_data_points_rate_limit | str |  | [optional] |
| transport_device_msg_rate_limit | str |  | [optional] |
| transport_device_telemetry_msg_rate_limit | str |  | [optional] |
| transport_device_telemetry_data_points_rate_limit | str |  | [optional] |
| transport_gateway_msg_rate_limit | str |  | [optional] |
| transport_gateway_telemetry_msg_rate_limit | str |  | [optional] |
| transport_gateway_telemetry_data_points_rate_limit | str |  | [optional] |
| transport_gateway_device_msg_rate_limit | str |  | [optional] |
| transport_gateway_device_telemetry_msg_rate_limit | str |  | [optional] |
| transport_gateway_device_telemetry_data_points_rate_limit | str |  | [optional] |
| integration_msgs_per_tenant_rate_limit | str |  | [optional] |
| integration_msgs_per_device_rate_limit | str |  | [optional] |
| integration_msgs_per_asset_rate_limit | str |  | [optional] |
| tenant_entity_export_rate_limit | str |  | [optional] |
| tenant_entity_import_rate_limit | str |  | [optional] |
| tenant_notification_requests_rate_limit | str |  | [optional] |
| tenant_notification_requests_per_rule_rate_limit | str |  | [optional] |
| max_transport_messages | int |  | [optional] |
| max_transport_data_points | int |  | [optional] |
| max_re_executions | int |  | [optional] |
| max_js_executions | int |  | [optional] |
| max_tbel_executions | int |  | [optional] |
| max_dp_storage_days | int |  | [optional] |
| max_rule_node_executions_per_message | int |  | [optional] |
| max_debug_mode_duration_minutes | int |  | [optional] |
| max_emails | int |  | [optional] |
| sms_enabled | bool |  | [optional] |
| max_sms | int |  | [optional] |
| max_created_alarms | int |  | [optional] |
| max_generated_reports | int |  | [optional] |
| max_ai_credits | int |  | [optional] |
| tenant_server_rest_limits_configuration | str |  | [optional] |
| customer_server_rest_limits_configuration | str |  | [optional] |
| max_ws_sessions_per_tenant | int |  | [optional] |
| max_ws_sessions_per_customer | int |  | [optional] |
| max_ws_sessions_per_regular_user | int |  | [optional] |
| max_ws_sessions_per_public_user | int |  | [optional] |
| ws_msg_queue_limit_per_session | int |  | [optional] |
| max_ws_subscriptions_per_tenant | int |  | [optional] |
| max_ws_subscriptions_per_customer | int |  | [optional] |
| max_ws_subscriptions_per_regular_user | int |  | [optional] |
| max_ws_subscriptions_per_public_user | int |  | [optional] |
| ws_updates_per_session_rate_limit | str |  | [optional] |
| cassandra_read_query_tenant_core_rate_limits | str |  | [optional] |
| cassandra_write_query_tenant_core_rate_limits | str |  | [optional] |
| cassandra_read_query_tenant_rule_engine_rate_limits | str |  | [optional] |
| cassandra_write_query_tenant_rule_engine_rate_limits | str |  | [optional] |
| edge_event_rate_limits | str |  | [optional] |
| edge_event_rate_limits_per_edge | str |  | [optional] |
| edge_uplink_messages_rate_limits | str |  | [optional] |
| edge_uplink_messages_rate_limits_per_edge | str |  | [optional] |
| default_storage_ttl_days | int |  | [optional] |
| alarms_ttl_days | int |  | [optional] |
| rpc_ttl_days | int |  | [optional] |
| queue_stats_ttl_days | int |  | [optional] |
| rule_engine_exceptions_ttl_days | int |  | [optional] |
| blob_entity_ttl_days | int |  | [optional] |
| report_ttl_days | int |  | [optional] |
| warn_threshold | float |  | [optional] |
| max_calculated_fields_per_entity | int |  | [optional] |
| max_arguments_per_cf | int |  | [optional] |
| min_allowed_scheduled_update_interval_in_sec_for_cf | int |  | [optional] |
| max_relation_level_per_cf_argument | int |  | [optional] |
| max_related_entities_to_return_per_cf_argument | int |  | [optional] |
| max_data_points_per_rolling_arg | int |  | [optional] |
| max_state_size_in_k_bytes | int |  | [optional] |
| max_single_value_argument_size_in_k_bytes | int |  | [optional] |
| min_allowed_deduplication_interval_in_sec_for_cf | int |  | [optional] |
| min_allowed_aggregation_interval_in_sec_for_cf | int |  | [optional] |
| intermediate_aggregation_interval_in_sec_for_cf | int |  | [optional] |
| cf_reevaluation_check_interval | int |  | [optional] |
| alarms_reevaluation_interval | int |  | [optional] |
| ai_chat_requests_per_tenant_rate_limit | str |  | [optional] |

#### TenantProfileQueueConfiguration
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| name | str |  | [optional] |
| topic | str |  | [optional] |
| poll_interval | int |  | [optional] |
| partitions | int |  | [optional] |
| consumer_per_partition | bool |  | [optional] |
| pack_processing_timeout | int |  | [optional] |
| submit_strategy | SubmitStrategy |  | [optional] |
| processing_strategy | ProcessingStrategy |  | [optional] |
| additional_info | object |  | [optional] |

#### EntityType (enum)
`TENANT` | `CUSTOMER` | `USER` | `DASHBOARD` | `ASSET` | `DEVICE` | `ALARM` | `ENTITY_GROUP` | `CONVERTER` | `INTEGRATION` | … (46 values total)

#### SubmitStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | SubmitStrategyType |  | [optional] |
| batch_size | int |  | [optional] |

#### ProcessingStrategy
| Name | Type | Description | Notes |
|------|------|-------------|-------|
| type | ProcessingStrategyType |  | [optional] |
| retries | int |  | [optional] |
| failure_percentage | float |  | [optional] |
| pause_between_retries | int |  | [optional] |
| max_pause_between_retries | int |  | [optional] |

#### SubmitStrategyType (enum)
`BURST` | `BATCH` | `SEQUENTIAL_BY_ORIGINATOR` | `SEQUENTIAL_BY_TENANT` | `SEQUENTIAL`

#### ProcessingStrategyType (enum)
`SKIP_ALL_FAILURES` | `SKIP_ALL_FAILURES_AND_TIMED_OUT` | `RETRY_ALL` | `RETRY_FAILED` | `RETRY_TIMED_OUT` | `RETRY_FAILED_AND_TIMED_OUT`

---

### Conventions

- **Package:** `tb_pe_client.models`
- **Attribute access:** `obj.data`, `obj.name`, etc.
- **Serialize:** `obj.model_dump()` or `obj.model_dump(by_alias=True)` for camelCase JSON
- **Deserialize:** `PageDataTenantProfile.model_validate(data)` or `PageDataTenantProfile.model_validate_json(json_str)`
- **None fields:** Optional attributes default to `None`; accessing them never raises exceptions

