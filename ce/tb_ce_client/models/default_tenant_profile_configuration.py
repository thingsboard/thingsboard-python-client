#
# Copyright © 2026-2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_ce_client.models.tenant_profile_configuration import TenantProfileConfiguration
from typing import Optional, Set
from typing_extensions import Self

class DefaultTenantProfileConfiguration(TenantProfileConfiguration):
    """
    DefaultTenantProfileConfiguration
    """ # noqa: E501
    type: StrictStr = "DEFAULT"  # post_process: discriminator default
    max_devices: Optional[StrictInt] = Field(default=None, serialization_alias="maxDevices")
    max_assets: Optional[StrictInt] = Field(default=None, serialization_alias="maxAssets")
    max_customers: Optional[StrictInt] = Field(default=None, serialization_alias="maxCustomers")
    max_users: Optional[StrictInt] = Field(default=None, serialization_alias="maxUsers")
    max_dashboards: Optional[StrictInt] = Field(default=None, serialization_alias="maxDashboards")
    max_rule_chains: Optional[StrictInt] = Field(default=None, serialization_alias="maxRuleChains")
    max_edges: Optional[StrictInt] = Field(default=None, serialization_alias="maxEdges")
    max_resources_in_bytes: Optional[StrictInt] = Field(default=None, serialization_alias="maxResourcesInBytes")
    max_ota_packages_in_bytes: Optional[StrictInt] = Field(default=None, serialization_alias="maxOtaPackagesInBytes")
    max_resource_size: Optional[StrictInt] = Field(default=None, serialization_alias="maxResourceSize")
    transport_tenant_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportTenantMsgRateLimit")
    transport_tenant_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportTenantTelemetryMsgRateLimit")
    transport_tenant_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportTenantTelemetryDataPointsRateLimit")
    transport_device_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportDeviceMsgRateLimit")
    transport_device_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportDeviceTelemetryMsgRateLimit")
    transport_device_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportDeviceTelemetryDataPointsRateLimit")
    transport_gateway_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayMsgRateLimit")
    transport_gateway_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayTelemetryMsgRateLimit")
    transport_gateway_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayTelemetryDataPointsRateLimit")
    transport_gateway_device_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayDeviceMsgRateLimit")
    transport_gateway_device_telemetry_msg_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayDeviceTelemetryMsgRateLimit")
    transport_gateway_device_telemetry_data_points_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="transportGatewayDeviceTelemetryDataPointsRateLimit")
    tenant_entity_export_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="tenantEntityExportRateLimit")
    tenant_entity_import_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="tenantEntityImportRateLimit")
    tenant_notification_requests_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="tenantNotificationRequestsRateLimit")
    tenant_notification_requests_per_rule_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="tenantNotificationRequestsPerRuleRateLimit")
    max_transport_messages: Optional[StrictInt] = Field(default=None, serialization_alias="maxTransportMessages")
    max_transport_data_points: Optional[StrictInt] = Field(default=None, serialization_alias="maxTransportDataPoints")
    max_re_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxREExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxJSExecutions")
    max_tbel_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxTbelExecutions")
    max_dp_storage_days: Optional[StrictInt] = Field(default=None, serialization_alias="maxDPStorageDays")
    max_rule_node_executions_per_message: Optional[StrictInt] = Field(default=None, serialization_alias="maxRuleNodeExecutionsPerMessage")
    max_debug_mode_duration_minutes: Optional[StrictInt] = Field(default=None, serialization_alias="maxDebugModeDurationMinutes")
    max_emails: Optional[StrictInt] = Field(default=None, serialization_alias="maxEmails")
    sms_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="smsEnabled")
    max_sms: Optional[StrictInt] = Field(default=None, serialization_alias="maxSms")
    max_created_alarms: Optional[StrictInt] = Field(default=None, serialization_alias="maxCreatedAlarms")
    tenant_server_rest_limits_configuration: Optional[StrictStr] = Field(default=None, serialization_alias="tenantServerRestLimitsConfiguration")
    customer_server_rest_limits_configuration: Optional[StrictStr] = Field(default=None, serialization_alias="customerServerRestLimitsConfiguration")
    max_ws_sessions_per_tenant: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSessionsPerTenant")
    max_ws_sessions_per_customer: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSessionsPerCustomer")
    max_ws_sessions_per_regular_user: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSessionsPerRegularUser")
    max_ws_sessions_per_public_user: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSessionsPerPublicUser")
    ws_msg_queue_limit_per_session: Optional[StrictInt] = Field(default=None, serialization_alias="wsMsgQueueLimitPerSession")
    max_ws_subscriptions_per_tenant: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSubscriptionsPerTenant")
    max_ws_subscriptions_per_customer: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSubscriptionsPerCustomer")
    max_ws_subscriptions_per_regular_user: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSubscriptionsPerRegularUser")
    max_ws_subscriptions_per_public_user: Optional[StrictInt] = Field(default=None, serialization_alias="maxWsSubscriptionsPerPublicUser")
    ws_updates_per_session_rate_limit: Optional[StrictStr] = Field(default=None, serialization_alias="wsUpdatesPerSessionRateLimit")
    cassandra_read_query_tenant_core_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="cassandraReadQueryTenantCoreRateLimits")
    cassandra_write_query_tenant_core_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="cassandraWriteQueryTenantCoreRateLimits")
    cassandra_read_query_tenant_rule_engine_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="cassandraReadQueryTenantRuleEngineRateLimits")
    cassandra_write_query_tenant_rule_engine_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="cassandraWriteQueryTenantRuleEngineRateLimits")
    edge_event_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="edgeEventRateLimits")
    edge_event_rate_limits_per_edge: Optional[StrictStr] = Field(default=None, serialization_alias="edgeEventRateLimitsPerEdge")
    edge_uplink_messages_rate_limits: Optional[StrictStr] = Field(default=None, serialization_alias="edgeUplinkMessagesRateLimits")
    edge_uplink_messages_rate_limits_per_edge: Optional[StrictStr] = Field(default=None, serialization_alias="edgeUplinkMessagesRateLimitsPerEdge")
    default_storage_ttl_days: Optional[StrictInt] = Field(default=None, serialization_alias="defaultStorageTtlDays")
    alarms_ttl_days: Optional[StrictInt] = Field(default=None, serialization_alias="alarmsTtlDays")
    rpc_ttl_days: Optional[StrictInt] = Field(default=None, serialization_alias="rpcTtlDays")
    queue_stats_ttl_days: Optional[StrictInt] = Field(default=None, serialization_alias="queueStatsTtlDays")
    rule_engine_exceptions_ttl_days: Optional[StrictInt] = Field(default=None, serialization_alias="ruleEngineExceptionsTtlDays")
    warn_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="warnThreshold")
    max_calculated_fields_per_entity: Optional[StrictInt] = Field(default=None, serialization_alias="maxCalculatedFieldsPerEntity")
    max_arguments_per_cf: Optional[StrictInt] = Field(default=None, serialization_alias="maxArgumentsPerCF")
    min_allowed_scheduled_update_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, serialization_alias="minAllowedScheduledUpdateIntervalInSecForCF")
    max_relation_level_per_cf_argument: Optional[StrictInt] = Field(default=None, serialization_alias="maxRelationLevelPerCfArgument")
    max_related_entities_to_return_per_cf_argument: Optional[StrictInt] = Field(default=None, serialization_alias="maxRelatedEntitiesToReturnPerCfArgument")
    max_data_points_per_rolling_arg: Optional[StrictInt] = Field(default=None, serialization_alias="maxDataPointsPerRollingArg")
    max_state_size_in_k_bytes: Optional[StrictInt] = Field(default=None, serialization_alias="maxStateSizeInKBytes")
    max_single_value_argument_size_in_k_bytes: Optional[StrictInt] = Field(default=None, serialization_alias="maxSingleValueArgumentSizeInKBytes")
    min_allowed_deduplication_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, serialization_alias="minAllowedDeduplicationIntervalInSecForCF")
    min_allowed_aggregation_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, serialization_alias="minAllowedAggregationIntervalInSecForCF")
    intermediate_aggregation_interval_in_sec_for_cf: Optional[StrictInt] = Field(default=None, serialization_alias="intermediateAggregationIntervalInSecForCF")
    cf_reevaluation_check_interval: Optional[StrictInt] = Field(default=None, serialization_alias="cfReevaluationCheckInterval")
    alarms_reevaluation_interval: Optional[StrictInt] = Field(default=None, serialization_alias="alarmsReevaluationInterval")
    __properties: ClassVar[List[str]] = ["type", "maxDevices", "maxAssets", "maxCustomers", "maxUsers", "maxDashboards", "maxRuleChains", "maxEdges", "maxResourcesInBytes", "maxOtaPackagesInBytes", "maxResourceSize", "transportTenantMsgRateLimit", "transportTenantTelemetryMsgRateLimit", "transportTenantTelemetryDataPointsRateLimit", "transportDeviceMsgRateLimit", "transportDeviceTelemetryMsgRateLimit", "transportDeviceTelemetryDataPointsRateLimit", "transportGatewayMsgRateLimit", "transportGatewayTelemetryMsgRateLimit", "transportGatewayTelemetryDataPointsRateLimit", "transportGatewayDeviceMsgRateLimit", "transportGatewayDeviceTelemetryMsgRateLimit", "transportGatewayDeviceTelemetryDataPointsRateLimit", "tenantEntityExportRateLimit", "tenantEntityImportRateLimit", "tenantNotificationRequestsRateLimit", "tenantNotificationRequestsPerRuleRateLimit", "maxTransportMessages", "maxTransportDataPoints", "maxREExecutions", "maxJSExecutions", "maxTbelExecutions", "maxDPStorageDays", "maxRuleNodeExecutionsPerMessage", "maxDebugModeDurationMinutes", "maxEmails", "smsEnabled", "maxSms", "maxCreatedAlarms", "tenantServerRestLimitsConfiguration", "customerServerRestLimitsConfiguration", "maxWsSessionsPerTenant", "maxWsSessionsPerCustomer", "maxWsSessionsPerRegularUser", "maxWsSessionsPerPublicUser", "wsMsgQueueLimitPerSession", "maxWsSubscriptionsPerTenant", "maxWsSubscriptionsPerCustomer", "maxWsSubscriptionsPerRegularUser", "maxWsSubscriptionsPerPublicUser", "wsUpdatesPerSessionRateLimit", "cassandraReadQueryTenantCoreRateLimits", "cassandraWriteQueryTenantCoreRateLimits", "cassandraReadQueryTenantRuleEngineRateLimits", "cassandraWriteQueryTenantRuleEngineRateLimits", "edgeEventRateLimits", "edgeEventRateLimitsPerEdge", "edgeUplinkMessagesRateLimits", "edgeUplinkMessagesRateLimitsPerEdge", "defaultStorageTtlDays", "alarmsTtlDays", "rpcTtlDays", "queueStatsTtlDays", "ruleEngineExceptionsTtlDays", "warnThreshold", "maxCalculatedFieldsPerEntity", "maxArgumentsPerCF", "minAllowedScheduledUpdateIntervalInSecForCF", "maxRelationLevelPerCfArgument", "maxRelatedEntitiesToReturnPerCfArgument", "maxDataPointsPerRollingArg", "maxStateSizeInKBytes", "maxSingleValueArgumentSizeInKBytes", "minAllowedDeduplicationIntervalInSecForCF", "minAllowedAggregationIntervalInSecForCF", "intermediateAggregationIntervalInSecForCF", "cfReevaluationCheckInterval", "alarmsReevaluationInterval"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DefaultTenantProfileConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DefaultTenantProfileConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "max_devices": obj.get("maxDevices"),
            "max_assets": obj.get("maxAssets"),
            "max_customers": obj.get("maxCustomers"),
            "max_users": obj.get("maxUsers"),
            "max_dashboards": obj.get("maxDashboards"),
            "max_rule_chains": obj.get("maxRuleChains"),
            "max_edges": obj.get("maxEdges"),
            "max_resources_in_bytes": obj.get("maxResourcesInBytes"),
            "max_ota_packages_in_bytes": obj.get("maxOtaPackagesInBytes"),
            "max_resource_size": obj.get("maxResourceSize"),
            "transport_tenant_msg_rate_limit": obj.get("transportTenantMsgRateLimit"),
            "transport_tenant_telemetry_msg_rate_limit": obj.get("transportTenantTelemetryMsgRateLimit"),
            "transport_tenant_telemetry_data_points_rate_limit": obj.get("transportTenantTelemetryDataPointsRateLimit"),
            "transport_device_msg_rate_limit": obj.get("transportDeviceMsgRateLimit"),
            "transport_device_telemetry_msg_rate_limit": obj.get("transportDeviceTelemetryMsgRateLimit"),
            "transport_device_telemetry_data_points_rate_limit": obj.get("transportDeviceTelemetryDataPointsRateLimit"),
            "transport_gateway_msg_rate_limit": obj.get("transportGatewayMsgRateLimit"),
            "transport_gateway_telemetry_msg_rate_limit": obj.get("transportGatewayTelemetryMsgRateLimit"),
            "transport_gateway_telemetry_data_points_rate_limit": obj.get("transportGatewayTelemetryDataPointsRateLimit"),
            "transport_gateway_device_msg_rate_limit": obj.get("transportGatewayDeviceMsgRateLimit"),
            "transport_gateway_device_telemetry_msg_rate_limit": obj.get("transportGatewayDeviceTelemetryMsgRateLimit"),
            "transport_gateway_device_telemetry_data_points_rate_limit": obj.get("transportGatewayDeviceTelemetryDataPointsRateLimit"),
            "tenant_entity_export_rate_limit": obj.get("tenantEntityExportRateLimit"),
            "tenant_entity_import_rate_limit": obj.get("tenantEntityImportRateLimit"),
            "tenant_notification_requests_rate_limit": obj.get("tenantNotificationRequestsRateLimit"),
            "tenant_notification_requests_per_rule_rate_limit": obj.get("tenantNotificationRequestsPerRuleRateLimit"),
            "max_transport_messages": obj.get("maxTransportMessages"),
            "max_transport_data_points": obj.get("maxTransportDataPoints"),
            "max_re_executions": obj.get("maxREExecutions"),
            "max_js_executions": obj.get("maxJSExecutions"),
            "max_tbel_executions": obj.get("maxTbelExecutions"),
            "max_dp_storage_days": obj.get("maxDPStorageDays"),
            "max_rule_node_executions_per_message": obj.get("maxRuleNodeExecutionsPerMessage"),
            "max_debug_mode_duration_minutes": obj.get("maxDebugModeDurationMinutes"),
            "max_emails": obj.get("maxEmails"),
            "sms_enabled": obj.get("smsEnabled"),
            "max_sms": obj.get("maxSms"),
            "max_created_alarms": obj.get("maxCreatedAlarms"),
            "tenant_server_rest_limits_configuration": obj.get("tenantServerRestLimitsConfiguration"),
            "customer_server_rest_limits_configuration": obj.get("customerServerRestLimitsConfiguration"),
            "max_ws_sessions_per_tenant": obj.get("maxWsSessionsPerTenant"),
            "max_ws_sessions_per_customer": obj.get("maxWsSessionsPerCustomer"),
            "max_ws_sessions_per_regular_user": obj.get("maxWsSessionsPerRegularUser"),
            "max_ws_sessions_per_public_user": obj.get("maxWsSessionsPerPublicUser"),
            "ws_msg_queue_limit_per_session": obj.get("wsMsgQueueLimitPerSession"),
            "max_ws_subscriptions_per_tenant": obj.get("maxWsSubscriptionsPerTenant"),
            "max_ws_subscriptions_per_customer": obj.get("maxWsSubscriptionsPerCustomer"),
            "max_ws_subscriptions_per_regular_user": obj.get("maxWsSubscriptionsPerRegularUser"),
            "max_ws_subscriptions_per_public_user": obj.get("maxWsSubscriptionsPerPublicUser"),
            "ws_updates_per_session_rate_limit": obj.get("wsUpdatesPerSessionRateLimit"),
            "cassandra_read_query_tenant_core_rate_limits": obj.get("cassandraReadQueryTenantCoreRateLimits"),
            "cassandra_write_query_tenant_core_rate_limits": obj.get("cassandraWriteQueryTenantCoreRateLimits"),
            "cassandra_read_query_tenant_rule_engine_rate_limits": obj.get("cassandraReadQueryTenantRuleEngineRateLimits"),
            "cassandra_write_query_tenant_rule_engine_rate_limits": obj.get("cassandraWriteQueryTenantRuleEngineRateLimits"),
            "edge_event_rate_limits": obj.get("edgeEventRateLimits"),
            "edge_event_rate_limits_per_edge": obj.get("edgeEventRateLimitsPerEdge"),
            "edge_uplink_messages_rate_limits": obj.get("edgeUplinkMessagesRateLimits"),
            "edge_uplink_messages_rate_limits_per_edge": obj.get("edgeUplinkMessagesRateLimitsPerEdge"),
            "default_storage_ttl_days": obj.get("defaultStorageTtlDays"),
            "alarms_ttl_days": obj.get("alarmsTtlDays"),
            "rpc_ttl_days": obj.get("rpcTtlDays"),
            "queue_stats_ttl_days": obj.get("queueStatsTtlDays"),
            "rule_engine_exceptions_ttl_days": obj.get("ruleEngineExceptionsTtlDays"),
            "warn_threshold": obj.get("warnThreshold"),
            "max_calculated_fields_per_entity": obj.get("maxCalculatedFieldsPerEntity"),
            "max_arguments_per_cf": obj.get("maxArgumentsPerCF"),
            "min_allowed_scheduled_update_interval_in_sec_for_cf": obj.get("minAllowedScheduledUpdateIntervalInSecForCF"),
            "max_relation_level_per_cf_argument": obj.get("maxRelationLevelPerCfArgument"),
            "max_related_entities_to_return_per_cf_argument": obj.get("maxRelatedEntitiesToReturnPerCfArgument"),
            "max_data_points_per_rolling_arg": obj.get("maxDataPointsPerRollingArg"),
            "max_state_size_in_k_bytes": obj.get("maxStateSizeInKBytes"),
            "max_single_value_argument_size_in_k_bytes": obj.get("maxSingleValueArgumentSizeInKBytes"),
            "min_allowed_deduplication_interval_in_sec_for_cf": obj.get("minAllowedDeduplicationIntervalInSecForCF"),
            "min_allowed_aggregation_interval_in_sec_for_cf": obj.get("minAllowedAggregationIntervalInSecForCF"),
            "intermediate_aggregation_interval_in_sec_for_cf": obj.get("intermediateAggregationIntervalInSecForCF"),
            "cf_reevaluation_check_interval": obj.get("cfReevaluationCheckInterval"),
            "alarms_reevaluation_interval": obj.get("alarmsReevaluationInterval")
        })
        return _obj


