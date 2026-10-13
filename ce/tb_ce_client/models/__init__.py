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
import importlib
from typing import TYPE_CHECKING

__all__ = [
    "AccountTwoFaSettings",
    "Action",
    "ActionStatus",
    "ActionType",
    "ActivateUserRequest",
    "AdminSettings",
    "AdminSettingsId",
    "AffectedTenantAdministratorsFilter",
    "AffectedUserFilter",
    "AggFunction",
    "AggFunctionInput",
    "AggInput",
    "AggInterval",
    "AggKeyInput",
    "AggMetric",
    "AiChatModelConfig",
    "AiModel",
    "AiModelConfig",
    "AiModelExportData",
    "AiModelId",
    "AiModelType",
    "Alarm",
    "AlarmAction",
    "AlarmAssignee",
    "AlarmAssignmentNotificationRuleTriggerConfig",
    "AlarmAssignmentRecipientsConfig",
    "AlarmCalculatedFieldConfiguration",
    "AlarmComment",
    "AlarmCommentId",
    "AlarmCommentInfo",
    "AlarmCommentNotificationRuleTriggerConfig",
    "AlarmCommentRecipientsConfig",
    "AlarmCommentType",
    "AlarmCondition",
    "AlarmConditionExpression",
    "AlarmConditionFilter",
    "AlarmConditionValueAlarmSchedule",
    "AlarmConditionValueBoolean",
    "AlarmConditionValueDouble",
    "AlarmConditionValueInteger",
    "AlarmConditionValueLong",
    "AlarmConditionValueString",
    "AlarmCountQuery",
    "AlarmData",
    "AlarmDataPageLink",
    "AlarmDataQuery",
    "AlarmId",
    "AlarmInfo",
    "AlarmNotificationRuleTriggerConfig",
    "AlarmRule",
    "AlarmRuleBooleanFilterPredicate",
    "AlarmRuleBooleanOperation",
    "AlarmRuleComplexFilterPredicate",
    "AlarmRuleComplexOperation",
    "AlarmRuleDefinition",
    "AlarmRuleDefinitionInfo",
    "AlarmRuleKeyFilterPredicate",
    "AlarmRuleNumericFilterPredicate",
    "AlarmRuleNumericOperation",
    "AlarmRuleStringFilterPredicate",
    "AlarmRuleStringOperation",
    "AlarmSchedule",
    "AlarmSearchStatus",
    "AlarmSeverity",
    "AlarmStatus",
    "AliasEntityId",
    "AliasEntityType",
    "AllUsersFilter",
    "AllowCreateNewDevicesDeviceProfileProvisionConfiguration",
    "AmazonBedrockChatModelConfig",
    "AmazonBedrockProviderConfig",
    "AnthropicChatModelConfig",
    "AnthropicProviderConfig",
    "AnyTimeSchedule",
    "ApiFeature",
    "ApiKey",
    "ApiKeyId",
    "ApiKeyInfo",
    "ApiUsageLimitNotificationRuleTriggerConfig",
    "ApiUsageLimitRecipientsConfig",
    "ApiUsageStateFilter",
    "ApiUsageStateId",
    "ApiUsageStateValue",
    "Argument",
    "ArgumentType",
    "Asset",
    "AssetExportData",
    "AssetId",
    "AssetInfo",
    "AssetProfile",
    "AssetProfileExportData",
    "AssetProfileId",
    "AssetProfileInfo",
    "AssetSearchQuery",
    "AssetSearchQueryFilter",
    "AssetTypeFilter",
    "AttributeData",
    "AttributeExportData",
    "AttributeScope",
    "AttributesEntityView",
    "AttributesImmediateOutputStrategy",
    "AttributesOutput",
    "AttributesOutputStrategy",
    "AttributesRuleChainOutputStrategy",
    "AuditLog",
    "AuditLogId",
    "AuthenticationProtocol",
    "Authority",
    "AutoVersionCreateConfig",
    "AvailableEntityKeys",
    "AvailableEntityKeysV2",
    "AwsSnsSmsProviderConfiguration",
    "AzureOpenAiChatModelConfig",
    "AzureOpenAiProviderConfig",
    "BackupCodeTwoFaAccountConfig",
    "BackupCodeTwoFaProviderConfig",
    "BadgePosition",
    "Basic",
    "BooleanFilterPredicate",
    "BooleanOperation",
    "BranchInfo",
    "BulkImportColumnType",
    "BulkImportRequest",
    "BulkImportResultAsset",
    "BulkImportResultDevice",
    "BulkImportResultEdge",
    "Button",
    "CalculatedField",
    "CalculatedFieldConfiguration",
    "CalculatedFieldDebugEventFilter",
    "CalculatedFieldId",
    "CalculatedFieldInfo",
    "CalculatedFieldType",
    "CfArgumentDynamicSourceConfiguration",
    "ChangePasswordRequest",
    "CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration",
    "ChecksumAlgorithm",
    "ClaimRequest",
    "ClearRule",
    "ClientAttributesQueryingSnmpCommunicationConfig",
    "CoapDeviceProfileTransportConfiguration",
    "CoapDeviceTransportConfiguration",
    "CoapDeviceTypeConfiguration",
    "ColumnMapping",
    "ComparisonTsValue",
    "ComplexFilterPredicate",
    "ComplexVersionCreateRequest",
    "ComponentClusteringMode",
    "ComponentDescriptor",
    "ComponentDescriptorId",
    "ComponentLifecycleEvent",
    "ComponentScope",
    "ComponentType",
    "CurrentOwnerDynamicSourceConfiguration",
    "CustomInterval",
    "CustomMobilePage",
    "CustomTimeSchedule",
    "CustomTimeScheduleItem",
    "Customer",
    "CustomerExportData",
    "CustomerId",
    "CustomerUsersFilter",
    "Dashboard",
    "DashboardExportData",
    "DashboardId",
    "DashboardInfo",
    "DashboardPage",
    "DataType",
    "DayInterval",
    "DebugSettings",
    "DefaultCoapDeviceTypeConfiguration",
    "DefaultDeviceConfiguration",
    "DefaultDeviceProfileConfiguration",
    "DefaultDeviceProfileTransportConfiguration",
    "DefaultDeviceTransportConfiguration",
    "DefaultMobilePage",
    "DefaultPageId",
    "DefaultRuleChainCreateRequest",
    "DefaultTenantProfileConfiguration",
    "DeliveryMethodNotificationTemplate",
    "Device",
    "DeviceActivityNotificationRuleTriggerConfig",
    "DeviceActivityRecipientsConfig",
    "DeviceConfiguration",
    "DeviceCredentials",
    "DeviceCredentialsId",
    "DeviceCredentialsType",
    "DeviceData",
    "DeviceEvent",
    "DeviceExportData",
    "DeviceId",
    "DeviceInfo",
    "DeviceProfile",
    "DeviceProfileConfiguration",
    "DeviceProfileData",
    "DeviceProfileExportData",
    "DeviceProfileId",
    "DeviceProfileInfo",
    "DeviceProfileProvisionConfiguration",
    "DeviceProfileProvisionType",
    "DeviceProfileTransportConfiguration",
    "DeviceProfileType",
    "DeviceSearchQuery",
    "DeviceSearchQueryFilter",
    "DeviceTransportConfiguration",
    "DeviceTransportType",
    "DeviceTypeFilter",
    "Direction",
    "DisabledDeviceProfileProvisionConfiguration",
    "Domain",
    "DomainId",
    "DomainInfo",
    "DummyJobConfiguration",
    "DummyJobResult",
    "DummyTaskFailure",
    "DummyTaskResult",
    "DurationAlarmCondition",
    "DynamicValueBoolean",
    "DynamicValueDouble",
    "DynamicValueSourceType",
    "DynamicValueString",
    "Edge",
    "EdgeCommunicationFailureNotificationRuleTriggerConfig",
    "EdgeCommunicationFailureRecipientsConfig",
    "EdgeConnectionNotificationRuleTriggerConfig",
    "EdgeConnectionRecipientsConfig",
    "EdgeConnectivityEvent",
    "EdgeEvent",
    "EdgeEventActionType",
    "EdgeEventId",
    "EdgeEventType",
    "EdgeId",
    "EdgeInfo",
    "EdgeInstructions",
    "EdgeSearchQuery",
    "EdgeSearchQueryFilter",
    "EdgeTypeFilter",
    "EdqsApiMode",
    "EdqsState",
    "EdqsSyncRequest",
    "EdqsSyncStatus",
    "EfentoCoapDeviceTypeConfiguration",
    "EmailDeliveryMethodNotificationTemplate",
    "EmailTwoFaAccountConfig",
    "EmailTwoFaProviderConfig",
    "EntitiesLimitNotificationRuleTriggerConfig",
    "EntitiesLimitRecipientsConfig",
    "EntityActionNotificationRuleTriggerConfig",
    "EntityActionRecipientsConfig",
    "EntityAggregationCalculatedFieldConfiguration",
    "EntityCoordinates",
    "EntityCountQuery",
    "EntityData",
    "EntityDataDiff",
    "EntityDataInfo",
    "EntityDataPageLink",
    "EntityDataQuery",
    "EntityDataSortOrder",
    "EntityExportData",
    "EntityFilter",
    "EntityId",
    "EntityInfo",
    "EntityKey",
    "EntityKeyType",
    "EntityKeyValueType",
    "EntityListFilter",
    "EntityLoadError",
    "EntityNameFilter",
    "EntityRelation",
    "EntityRelationInfo",
    "EntityRelationsQuery",
    "EntitySearchDirection",
    "EntitySubtype",
    "EntityType",
    "EntityTypeFilter",
    "EntityTypeLoadResult",
    "EntityTypeVersionCreateConfig",
    "EntityTypeVersionLoadConfig",
    "EntityTypeVersionLoadRequest",
    "EntityVersion",
    "EntityView",
    "EntityViewExportData",
    "EntityViewId",
    "EntityViewInfo",
    "EntityViewSearchQuery",
    "EntityViewSearchQueryFilter",
    "EntityViewTypeFilter",
    "ErrorEventFilter",
    "EscalatedNotificationRuleRecipientsConfig",
    "EventFilter",
    "EventId",
    "EventInfo",
    "EventType",
    "ExportableEntity",
    "Failure",
    "FeaturesInfo",
    "FilterPredicateValueBoolean",
    "FilterPredicateValueDouble",
    "FilterPredicateValueString",
    "GeofencingCalculatedFieldConfiguration",
    "GeofencingReportStrategy",
    "GitHubModelsChatModelConfig",
    "GitHubModelsProviderConfig",
    "GoogleAiGeminiChatModelConfig",
    "GoogleAiGeminiProviderConfig",
    "GoogleVertexAiGeminiChatModelConfig",
    "GoogleVertexAiGeminiProviderConfig",
    "HasIdObject",
    "HomeDashboard",
    "HomeDashboardInfo",
    "HourInterval",
    "Job",
    "JobConfiguration",
    "JobId",
    "JobResult",
    "JobStatus",
    "JobType",
    "JsonTransportPayloadConfiguration",
    "JwtPair",
    "JwtSettings",
    "KeyFilter",
    "KeyFilterPredicate",
    "KeyInfo",
    "KeySample",
    "LastVisitedDashboardInfo",
    "LifeCycleEventFilter",
    "LimitedApi",
    "LinkType",
    "Login401Response",
    "LoginMobileInfo",
    "LoginRequest",
    "LoginResponse",
    "LwM2MBootstrapServerCredential",
    "LwM2MServerSecurityConfigDefault",
    "LwM2mInstance",
    "LwM2mObject",
    "LwM2mResourceObserve",
    "LwM2mVersion",
    "Lwm2mDeviceProfileTransportConfiguration",
    "Lwm2mDeviceTransportConfiguration",
    "MapperType",
    "Mapping",
    "MicrosoftTeamsDeliveryMethodNotificationTemplate",
    "MicrosoftTeamsNotificationTargetConfig",
    "MistralAiChatModelConfig",
    "MistralAiProviderConfig",
    "MobileApp",
    "MobileAppBundle",
    "MobileAppBundleId",
    "MobileAppBundleInfo",
    "MobileAppDeliveryMethodNotificationTemplate",
    "MobileAppId",
    "MobileAppNotificationDeliveryMethodConfig",
    "MobileAppStatus",
    "MobileAppVersionInfo",
    "MobileLayoutConfig",
    "MobilePage",
    "MobilePageType",
    "MobileSessionInfo",
    "ModelNone",
    "MonthInterval",
    "MqttDeviceProfileTransportConfiguration",
    "MqttDeviceTransportConfiguration",
    "NameConflictPolicy",
    "NewPlatformVersionNotificationRuleTriggerConfig",
    "NewPlatformVersionRecipientsConfig",
    "NoDataFilterPredicate",
    "NoSecLwM2MBootstrapServerCredential",
    "NodeConnectionInfo",
    "Notification",
    "NotificationDeliveryMethod",
    "NotificationDeliveryMethodConfig",
    "NotificationId",
    "NotificationInfo",
    "NotificationPref",
    "NotificationRequest",
    "NotificationRequestConfig",
    "NotificationRequestId",
    "NotificationRequestInfo",
    "NotificationRequestPreview",
    "NotificationRequestStats",
    "NotificationRequestStatus",
    "NotificationRule",
    "NotificationRuleConfig",
    "NotificationRuleExportData",
    "NotificationRuleId",
    "NotificationRuleInfo",
    "NotificationRuleRecipientsConfig",
    "NotificationRuleTriggerConfig",
    "NotificationRuleTriggerType",
    "NotificationSettings",
    "NotificationStatus",
    "NotificationTarget",
    "NotificationTargetConfig",
    "NotificationTargetExportData",
    "NotificationTargetId",
    "NotificationTemplate",
    "NotificationTemplateConfig",
    "NotificationTemplateExportData",
    "NotificationTemplateId",
    "NotificationType",
    "NumericFilterPredicate",
    "NumericOperation",
    "OAuth2BasicMapperConfig",
    "OAuth2Client",
    "OAuth2ClientId",
    "OAuth2ClientInfo",
    "OAuth2ClientLoginInfo",
    "OAuth2ClientRegistrationTemplate",
    "OAuth2ClientRegistrationTemplateId",
    "OAuth2CustomMapperConfig",
    "OAuth2MapperConfig",
    "ObjectAttributes",
    "ObjectType",
    "OllamaAuth",
    "OllamaChatModelConfig",
    "OllamaProviderConfig",
    "OpenAiChatModelConfig",
    "OpenAiProviderConfig",
    "OriginatorEntityOwnerUsersFilter",
    "OtaPackage",
    "OtaPackageExportData",
    "OtaPackageId",
    "OtaPackageInfo",
    "OtaPackageType",
    "OtherConfiguration",
    "Output",
    "PSKLwM2MBootstrapServerCredential",
    "PageDataAiModel",
    "PageDataAlarmCommentInfo",
    "PageDataAlarmData",
    "PageDataAlarmInfo",
    "PageDataAlarmRuleDefinition",
    "PageDataAlarmRuleDefinitionInfo",
    "PageDataApiKeyInfo",
    "PageDataAsset",
    "PageDataAssetInfo",
    "PageDataAssetProfile",
    "PageDataAssetProfileInfo",
    "PageDataAuditLog",
    "PageDataCalculatedField",
    "PageDataCalculatedFieldInfo",
    "PageDataCustomer",
    "PageDataDashboardInfo",
    "PageDataDevice",
    "PageDataDeviceInfo",
    "PageDataDeviceProfile",
    "PageDataDeviceProfileInfo",
    "PageDataDomainInfo",
    "PageDataEdge",
    "PageDataEdgeEvent",
    "PageDataEdgeInfo",
    "PageDataEntityData",
    "PageDataEntityInfo",
    "PageDataEntitySubtype",
    "PageDataEntityVersion",
    "PageDataEntityView",
    "PageDataEntityViewInfo",
    "PageDataEventInfo",
    "PageDataJob",
    "PageDataMobileApp",
    "PageDataMobileAppBundleInfo",
    "PageDataNotification",
    "PageDataNotificationRequestInfo",
    "PageDataNotificationRuleInfo",
    "PageDataNotificationTarget",
    "PageDataNotificationTemplate",
    "PageDataOAuth2ClientInfo",
    "PageDataOtaPackageInfo",
    "PageDataQueue",
    "PageDataQueueStats",
    "PageDataRuleChain",
    "PageDataString",
    "PageDataTbResourceInfo",
    "PageDataTenant",
    "PageDataTenantInfo",
    "PageDataTenantProfile",
    "PageDataUser",
    "PageDataUserEmailInfo",
    "PageDataWidgetTypeInfo",
    "PageDataWidgetsBundle",
    "PlatformTwoFaSettings",
    "PlatformType",
    "PlatformUsersNotificationTargetConfig",
    "PowerMode",
    "PowerSavingConfiguration",
    "PrivacyProtocol",
    "ProcessingStrategy",
    "ProcessingStrategyType",
    "PropagationCalculatedFieldConfiguration",
    "ProtoTransportPayloadConfiguration",
    "QRCodeConfig",
    "QrCodeSettings",
    "QrCodeSettingsId",
    "QuarterInterval",
    "Queue",
    "QueueId",
    "QueueStats",
    "QueueStatsId",
    "RPKLwM2MBootstrapServerCredential",
    "RateLimitsNotificationRuleTriggerConfig",
    "RateLimitsRecipientsConfig",
    "ReferencedEntityKey",
    "RefreshTokenRequest",
    "RelatedEntitiesAggregationCalculatedFieldConfiguration",
    "RelationEntityTypeFilter",
    "RelationPathLevel",
    "RelationPathQueryDynamicSourceConfiguration",
    "RelationTypeGroup",
    "RelationsQueryFilter",
    "RelationsSearchParameters",
    "RepeatingAlarmCondition",
    "RepositoryAuthMethod",
    "RepositorySettings",
    "RepositorySettingsInfo",
    "ResetPasswordEmailRequest",
    "ResetPasswordRequest",
    "ResourceExportData",
    "ResourceShortageRecipientsConfig",
    "ResourceSubType",
    "ResourceType",
    "ResourcesShortageNotificationRuleTriggerConfig",
    "Rpc",
    "RpcId",
    "RpcStatus",
    "RuleChain",
    "RuleChainConnectionInfo",
    "RuleChainData",
    "RuleChainDebugEventFilter",
    "RuleChainExportData",
    "RuleChainId",
    "RuleChainImportResult",
    "RuleChainMetaData",
    "RuleChainNote",
    "RuleChainOutputLabelsUsage",
    "RuleChainType",
    "RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig",
    "RuleEngineComponentLifecycleEventRecipientsConfig",
    "RuleNode",
    "RuleNodeDebugEventFilter",
    "RuleNodeId",
    "SaveDeviceWithCredentialsRequest",
    "SaveOtaPackageInfoRequest",
    "ScriptCalculatedFieldConfiguration",
    "ScriptLanguage",
    "SecuritySettings",
    "SharedAttributesSettingSnmpCommunicationConfig",
    "ShortCustomerInfo",
    "SimpleAlarmCondition",
    "SimpleAlarmConditionExpression",
    "SimpleCalculatedFieldConfiguration",
    "SingleEntityFilter",
    "SingleEntityVersionCreateRequest",
    "SingleEntityVersionLoadRequest",
    "SlackConversation",
    "SlackConversationType",
    "SlackDeliveryMethodNotificationTemplate",
    "SlackNotificationDeliveryMethodConfig",
    "SlackNotificationTargetConfig",
    "SmppBindType",
    "SmppSmsProviderConfiguration",
    "SmsDeliveryMethodNotificationTemplate",
    "SmsProviderConfiguration",
    "SmsTwoFaAccountConfig",
    "SmsTwoFaProviderConfig",
    "SnmpCommunicationConfig",
    "SnmpCommunicationSpec",
    "SnmpDeviceProfileTransportConfiguration",
    "SnmpDeviceTransportConfiguration",
    "SnmpMapping",
    "SnmpProtocolVersion",
    "SpecificTimeSchedule",
    "StarredDashboardInfo",
    "StatisticsEventFilter",
    "StoreInfo",
    "StringFilterPredicate",
    "StringOperation",
    "SubmitStrategy",
    "SubmitStrategyType",
    "Success",
    "SyncStrategy",
    "SystemAdministratorsFilter",
    "SystemInfo",
    "SystemInfoData",
    "TaskProcessingFailureNotificationRuleTriggerConfig",
    "TaskProcessingFailureRecipientsConfig",
    "TaskResult",
    "TbChatRequest",
    "TbChatResponse",
    "TbContent",
    "TbImageDeleteResult",
    "TbResource",
    "TbResourceDeleteResult",
    "TbResourceExportData",
    "TbResourceId",
    "TbResourceInfo",
    "TbTextContent",
    "TbUserMessage",
    "TbelAlarmConditionExpression",
    "TelemetryEntityView",
    "TelemetryMappingConfiguration",
    "TelemetryObserveStrategy",
    "TelemetryQueryingSnmpCommunicationConfig",
    "Tenant",
    "TenantAdministratorsFilter",
    "TenantId",
    "TenantInfo",
    "TenantNameStrategyType",
    "TenantProfile",
    "TenantProfileConfiguration",
    "TenantProfileData",
    "TenantProfileId",
    "TenantProfileQueueConfiguration",
    "TestSmsRequest",
    "ThingsboardCredentialsExpiredResponse",
    "ThingsboardErrorCode",
    "ThingsboardErrorResponse",
    "TimeSeriesImmediateOutputStrategy",
    "TimeSeriesOutput",
    "TimeSeriesOutputStrategy",
    "TimeSeriesRuleChainOutputStrategy",
    "TimeUnit",
    "ToCoreEdqsRequest",
    "ToDeviceRpcRequestSnmpCommunicationConfig",
    "ToServerRpcRequestSnmpCommunicationConfig",
    "Token",
    "TotpTwoFaAccountConfig",
    "TotpTwoFaProviderConfig",
    "TransportPayloadTypeConfiguration",
    "TrendzSettings",
    "TsData",
    "TsValue",
    "TwilioSmsProviderConfiguration",
    "TwoFaAccountConfig",
    "TwoFaAccountConfigUpdateRequest",
    "TwoFaProviderConfig",
    "TwoFaProviderInfo",
    "TwoFaProviderType",
    "UniquifyStrategy",
    "UpdateMessage",
    "UsageInfo",
    "User",
    "UserActivationLink",
    "UserDashboardsInfo",
    "UserEmailInfo",
    "UserId",
    "UserListFilter",
    "UserMobileInfo",
    "UserNotificationSettings",
    "UserPasswordPolicy",
    "UsersFilter",
    "VersionCreateConfig",
    "VersionCreateRequest",
    "VersionCreateRequestType",
    "VersionCreationResult",
    "VersionLoadConfig",
    "VersionLoadRequest",
    "VersionLoadRequestType",
    "VersionLoadResult",
    "VersionedEntityInfo",
    "Watermark",
    "WebDeliveryMethodNotificationTemplate",
    "WebViewPage",
    "WeekInterval",
    "WeekSunSatInterval",
    "WidgetBundleInfo",
    "WidgetType",
    "WidgetTypeDetails",
    "WidgetTypeExportData",
    "WidgetTypeId",
    "WidgetTypeInfo",
    "WidgetsBundle",
    "WidgetsBundleExportData",
    "WidgetsBundleId",
    "X509CertificateChainProvisionConfiguration",
    "X509LwM2MBootstrapServerCredential",
    "YearInterval",
    "ZoneGroupConfiguration",
]

if TYPE_CHECKING:
    from tb_ce_client.models.account_two_fa_settings import AccountTwoFaSettings
    from tb_ce_client.models.action import Action
    from tb_ce_client.models.action_status import ActionStatus
    from tb_ce_client.models.action_type import ActionType
    from tb_ce_client.models.activate_user_request import ActivateUserRequest
    from tb_ce_client.models.admin_settings import AdminSettings
    from tb_ce_client.models.admin_settings_id import AdminSettingsId
    from tb_ce_client.models.affected_tenant_administrators_filter import AffectedTenantAdministratorsFilter
    from tb_ce_client.models.affected_user_filter import AffectedUserFilter
    from tb_ce_client.models.agg_function import AggFunction
    from tb_ce_client.models.agg_function_input import AggFunctionInput
    from tb_ce_client.models.agg_input import AggInput
    from tb_ce_client.models.agg_interval import AggInterval
    from tb_ce_client.models.agg_key_input import AggKeyInput
    from tb_ce_client.models.agg_metric import AggMetric
    from tb_ce_client.models.ai_chat_model_config import AiChatModelConfig
    from tb_ce_client.models.ai_model import AiModel
    from tb_ce_client.models.ai_model_config import AiModelConfig
    from tb_ce_client.models.ai_model_export_data import AiModelExportData
    from tb_ce_client.models.ai_model_id import AiModelId
    from tb_ce_client.models.ai_model_type import AiModelType
    from tb_ce_client.models.alarm import Alarm
    from tb_ce_client.models.alarm_action import AlarmAction
    from tb_ce_client.models.alarm_assignee import AlarmAssignee
    from tb_ce_client.models.alarm_assignment_notification_rule_trigger_config import AlarmAssignmentNotificationRuleTriggerConfig
    from tb_ce_client.models.alarm_assignment_recipients_config import AlarmAssignmentRecipientsConfig
    from tb_ce_client.models.alarm_calculated_field_configuration import AlarmCalculatedFieldConfiguration
    from tb_ce_client.models.alarm_comment import AlarmComment
    from tb_ce_client.models.alarm_comment_id import AlarmCommentId
    from tb_ce_client.models.alarm_comment_info import AlarmCommentInfo
    from tb_ce_client.models.alarm_comment_notification_rule_trigger_config import AlarmCommentNotificationRuleTriggerConfig
    from tb_ce_client.models.alarm_comment_recipients_config import AlarmCommentRecipientsConfig
    from tb_ce_client.models.alarm_comment_type import AlarmCommentType
    from tb_ce_client.models.alarm_condition import AlarmCondition
    from tb_ce_client.models.alarm_condition_expression import AlarmConditionExpression
    from tb_ce_client.models.alarm_condition_filter import AlarmConditionFilter
    from tb_ce_client.models.alarm_condition_value_alarm_schedule import AlarmConditionValueAlarmSchedule
    from tb_ce_client.models.alarm_condition_value_boolean import AlarmConditionValueBoolean
    from tb_ce_client.models.alarm_condition_value_double import AlarmConditionValueDouble
    from tb_ce_client.models.alarm_condition_value_integer import AlarmConditionValueInteger
    from tb_ce_client.models.alarm_condition_value_long import AlarmConditionValueLong
    from tb_ce_client.models.alarm_condition_value_string import AlarmConditionValueString
    from tb_ce_client.models.alarm_count_query import AlarmCountQuery
    from tb_ce_client.models.alarm_data import AlarmData
    from tb_ce_client.models.alarm_data_page_link import AlarmDataPageLink
    from tb_ce_client.models.alarm_data_query import AlarmDataQuery
    from tb_ce_client.models.alarm_id import AlarmId
    from tb_ce_client.models.alarm_info import AlarmInfo
    from tb_ce_client.models.alarm_notification_rule_trigger_config import AlarmNotificationRuleTriggerConfig
    from tb_ce_client.models.alarm_rule import AlarmRule
    from tb_ce_client.models.alarm_rule_boolean_filter_predicate import AlarmRuleBooleanFilterPredicate
    from tb_ce_client.models.alarm_rule_boolean_operation import AlarmRuleBooleanOperation
    from tb_ce_client.models.alarm_rule_complex_filter_predicate import AlarmRuleComplexFilterPredicate
    from tb_ce_client.models.alarm_rule_complex_operation import AlarmRuleComplexOperation
    from tb_ce_client.models.alarm_rule_definition import AlarmRuleDefinition
    from tb_ce_client.models.alarm_rule_definition_info import AlarmRuleDefinitionInfo
    from tb_ce_client.models.alarm_rule_key_filter_predicate import AlarmRuleKeyFilterPredicate
    from tb_ce_client.models.alarm_rule_numeric_filter_predicate import AlarmRuleNumericFilterPredicate
    from tb_ce_client.models.alarm_rule_numeric_operation import AlarmRuleNumericOperation
    from tb_ce_client.models.alarm_rule_string_filter_predicate import AlarmRuleStringFilterPredicate
    from tb_ce_client.models.alarm_rule_string_operation import AlarmRuleStringOperation
    from tb_ce_client.models.alarm_schedule import AlarmSchedule
    from tb_ce_client.models.alarm_search_status import AlarmSearchStatus
    from tb_ce_client.models.alarm_severity import AlarmSeverity
    from tb_ce_client.models.alarm_status import AlarmStatus
    from tb_ce_client.models.alias_entity_id import AliasEntityId
    from tb_ce_client.models.alias_entity_type import AliasEntityType
    from tb_ce_client.models.all_users_filter import AllUsersFilter
    from tb_ce_client.models.allow_create_new_devices_device_profile_provision_configuration import AllowCreateNewDevicesDeviceProfileProvisionConfiguration
    from tb_ce_client.models.amazon_bedrock_chat_model_config import AmazonBedrockChatModelConfig
    from tb_ce_client.models.amazon_bedrock_provider_config import AmazonBedrockProviderConfig
    from tb_ce_client.models.anthropic_chat_model_config import AnthropicChatModelConfig
    from tb_ce_client.models.anthropic_provider_config import AnthropicProviderConfig
    from tb_ce_client.models.any_time_schedule import AnyTimeSchedule
    from tb_ce_client.models.api_feature import ApiFeature
    from tb_ce_client.models.api_key import ApiKey
    from tb_ce_client.models.api_key_id import ApiKeyId
    from tb_ce_client.models.api_key_info import ApiKeyInfo
    from tb_ce_client.models.api_usage_limit_notification_rule_trigger_config import ApiUsageLimitNotificationRuleTriggerConfig
    from tb_ce_client.models.api_usage_limit_recipients_config import ApiUsageLimitRecipientsConfig
    from tb_ce_client.models.api_usage_state_filter import ApiUsageStateFilter
    from tb_ce_client.models.api_usage_state_id import ApiUsageStateId
    from tb_ce_client.models.api_usage_state_value import ApiUsageStateValue
    from tb_ce_client.models.argument import Argument
    from tb_ce_client.models.argument_type import ArgumentType
    from tb_ce_client.models.asset import Asset
    from tb_ce_client.models.asset_export_data import AssetExportData
    from tb_ce_client.models.asset_id import AssetId
    from tb_ce_client.models.asset_info import AssetInfo
    from tb_ce_client.models.asset_profile import AssetProfile
    from tb_ce_client.models.asset_profile_export_data import AssetProfileExportData
    from tb_ce_client.models.asset_profile_id import AssetProfileId
    from tb_ce_client.models.asset_profile_info import AssetProfileInfo
    from tb_ce_client.models.asset_search_query import AssetSearchQuery
    from tb_ce_client.models.asset_search_query_filter import AssetSearchQueryFilter
    from tb_ce_client.models.asset_type_filter import AssetTypeFilter
    from tb_ce_client.models.attribute_data import AttributeData
    from tb_ce_client.models.attribute_export_data import AttributeExportData
    from tb_ce_client.models.attribute_scope import AttributeScope
    from tb_ce_client.models.attributes_entity_view import AttributesEntityView
    from tb_ce_client.models.attributes_immediate_output_strategy import AttributesImmediateOutputStrategy
    from tb_ce_client.models.attributes_output import AttributesOutput
    from tb_ce_client.models.attributes_output_strategy import AttributesOutputStrategy
    from tb_ce_client.models.attributes_rule_chain_output_strategy import AttributesRuleChainOutputStrategy
    from tb_ce_client.models.audit_log import AuditLog
    from tb_ce_client.models.audit_log_id import AuditLogId
    from tb_ce_client.models.authentication_protocol import AuthenticationProtocol
    from tb_ce_client.models.authority import Authority
    from tb_ce_client.models.auto_version_create_config import AutoVersionCreateConfig
    from tb_ce_client.models.available_entity_keys import AvailableEntityKeys
    from tb_ce_client.models.available_entity_keys_v2 import AvailableEntityKeysV2
    from tb_ce_client.models.aws_sns_sms_provider_configuration import AwsSnsSmsProviderConfiguration
    from tb_ce_client.models.azure_open_ai_chat_model_config import AzureOpenAiChatModelConfig
    from tb_ce_client.models.azure_open_ai_provider_config import AzureOpenAiProviderConfig
    from tb_ce_client.models.backup_code_two_fa_account_config import BackupCodeTwoFaAccountConfig
    from tb_ce_client.models.backup_code_two_fa_provider_config import BackupCodeTwoFaProviderConfig
    from tb_ce_client.models.badge_position import BadgePosition
    from tb_ce_client.models.basic import Basic
    from tb_ce_client.models.boolean_filter_predicate import BooleanFilterPredicate
    from tb_ce_client.models.boolean_operation import BooleanOperation
    from tb_ce_client.models.branch_info import BranchInfo
    from tb_ce_client.models.bulk_import_column_type import BulkImportColumnType
    from tb_ce_client.models.bulk_import_request import BulkImportRequest
    from tb_ce_client.models.bulk_import_result_asset import BulkImportResultAsset
    from tb_ce_client.models.bulk_import_result_device import BulkImportResultDevice
    from tb_ce_client.models.bulk_import_result_edge import BulkImportResultEdge
    from tb_ce_client.models.button import Button
    from tb_ce_client.models.calculated_field import CalculatedField
    from tb_ce_client.models.calculated_field_configuration import CalculatedFieldConfiguration
    from tb_ce_client.models.calculated_field_debug_event_filter import CalculatedFieldDebugEventFilter
    from tb_ce_client.models.calculated_field_id import CalculatedFieldId
    from tb_ce_client.models.calculated_field_info import CalculatedFieldInfo
    from tb_ce_client.models.calculated_field_type import CalculatedFieldType
    from tb_ce_client.models.cf_argument_dynamic_source_configuration import CfArgumentDynamicSourceConfiguration
    from tb_ce_client.models.change_password_request import ChangePasswordRequest
    from tb_ce_client.models.check_pre_provisioned_devices_device_profile_provision_configuration import CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration
    from tb_ce_client.models.checksum_algorithm import ChecksumAlgorithm
    from tb_ce_client.models.claim_request import ClaimRequest
    from tb_ce_client.models.clear_rule import ClearRule
    from tb_ce_client.models.client_attributes_querying_snmp_communication_config import ClientAttributesQueryingSnmpCommunicationConfig
    from tb_ce_client.models.coap_device_profile_transport_configuration import CoapDeviceProfileTransportConfiguration
    from tb_ce_client.models.coap_device_transport_configuration import CoapDeviceTransportConfiguration
    from tb_ce_client.models.coap_device_type_configuration import CoapDeviceTypeConfiguration
    from tb_ce_client.models.column_mapping import ColumnMapping
    from tb_ce_client.models.comparison_ts_value import ComparisonTsValue
    from tb_ce_client.models.complex_filter_predicate import ComplexFilterPredicate
    from tb_ce_client.models.complex_version_create_request import ComplexVersionCreateRequest
    from tb_ce_client.models.component_clustering_mode import ComponentClusteringMode
    from tb_ce_client.models.component_descriptor import ComponentDescriptor
    from tb_ce_client.models.component_descriptor_id import ComponentDescriptorId
    from tb_ce_client.models.component_lifecycle_event import ComponentLifecycleEvent
    from tb_ce_client.models.component_scope import ComponentScope
    from tb_ce_client.models.component_type import ComponentType
    from tb_ce_client.models.current_owner_dynamic_source_configuration import CurrentOwnerDynamicSourceConfiguration
    from tb_ce_client.models.custom_interval import CustomInterval
    from tb_ce_client.models.custom_mobile_page import CustomMobilePage
    from tb_ce_client.models.custom_time_schedule import CustomTimeSchedule
    from tb_ce_client.models.custom_time_schedule_item import CustomTimeScheduleItem
    from tb_ce_client.models.customer import Customer
    from tb_ce_client.models.customer_export_data import CustomerExportData
    from tb_ce_client.models.customer_id import CustomerId
    from tb_ce_client.models.customer_users_filter import CustomerUsersFilter
    from tb_ce_client.models.dashboard import Dashboard
    from tb_ce_client.models.dashboard_export_data import DashboardExportData
    from tb_ce_client.models.dashboard_id import DashboardId
    from tb_ce_client.models.dashboard_info import DashboardInfo
    from tb_ce_client.models.dashboard_page import DashboardPage
    from tb_ce_client.models.data_type import DataType
    from tb_ce_client.models.day_interval import DayInterval
    from tb_ce_client.models.debug_settings import DebugSettings
    from tb_ce_client.models.default_coap_device_type_configuration import DefaultCoapDeviceTypeConfiguration
    from tb_ce_client.models.default_device_configuration import DefaultDeviceConfiguration
    from tb_ce_client.models.default_device_profile_configuration import DefaultDeviceProfileConfiguration
    from tb_ce_client.models.default_device_profile_transport_configuration import DefaultDeviceProfileTransportConfiguration
    from tb_ce_client.models.default_device_transport_configuration import DefaultDeviceTransportConfiguration
    from tb_ce_client.models.default_mobile_page import DefaultMobilePage
    from tb_ce_client.models.default_page_id import DefaultPageId
    from tb_ce_client.models.default_rule_chain_create_request import DefaultRuleChainCreateRequest
    from tb_ce_client.models.default_tenant_profile_configuration import DefaultTenantProfileConfiguration
    from tb_ce_client.models.delivery_method_notification_template import DeliveryMethodNotificationTemplate
    from tb_ce_client.models.device import Device
    from tb_ce_client.models.device_activity_notification_rule_trigger_config import DeviceActivityNotificationRuleTriggerConfig
    from tb_ce_client.models.device_activity_recipients_config import DeviceActivityRecipientsConfig
    from tb_ce_client.models.device_configuration import DeviceConfiguration
    from tb_ce_client.models.device_credentials import DeviceCredentials
    from tb_ce_client.models.device_credentials_id import DeviceCredentialsId
    from tb_ce_client.models.device_credentials_type import DeviceCredentialsType
    from tb_ce_client.models.device_data import DeviceData
    from tb_ce_client.models.device_event import DeviceEvent
    from tb_ce_client.models.device_export_data import DeviceExportData
    from tb_ce_client.models.device_id import DeviceId
    from tb_ce_client.models.device_info import DeviceInfo
    from tb_ce_client.models.device_profile import DeviceProfile
    from tb_ce_client.models.device_profile_configuration import DeviceProfileConfiguration
    from tb_ce_client.models.device_profile_data import DeviceProfileData
    from tb_ce_client.models.device_profile_export_data import DeviceProfileExportData
    from tb_ce_client.models.device_profile_id import DeviceProfileId
    from tb_ce_client.models.device_profile_info import DeviceProfileInfo
    from tb_ce_client.models.device_profile_provision_configuration import DeviceProfileProvisionConfiguration
    from tb_ce_client.models.device_profile_provision_type import DeviceProfileProvisionType
    from tb_ce_client.models.device_profile_transport_configuration import DeviceProfileTransportConfiguration
    from tb_ce_client.models.device_profile_type import DeviceProfileType
    from tb_ce_client.models.device_search_query import DeviceSearchQuery
    from tb_ce_client.models.device_search_query_filter import DeviceSearchQueryFilter
    from tb_ce_client.models.device_transport_configuration import DeviceTransportConfiguration
    from tb_ce_client.models.device_transport_type import DeviceTransportType
    from tb_ce_client.models.device_type_filter import DeviceTypeFilter
    from tb_ce_client.models.direction import Direction
    from tb_ce_client.models.disabled_device_profile_provision_configuration import DisabledDeviceProfileProvisionConfiguration
    from tb_ce_client.models.domain import Domain
    from tb_ce_client.models.domain_id import DomainId
    from tb_ce_client.models.domain_info import DomainInfo
    from tb_ce_client.models.dummy_job_configuration import DummyJobConfiguration
    from tb_ce_client.models.dummy_job_result import DummyJobResult
    from tb_ce_client.models.dummy_task_failure import DummyTaskFailure
    from tb_ce_client.models.dummy_task_result import DummyTaskResult
    from tb_ce_client.models.duration_alarm_condition import DurationAlarmCondition
    from tb_ce_client.models.dynamic_value_boolean import DynamicValueBoolean
    from tb_ce_client.models.dynamic_value_double import DynamicValueDouble
    from tb_ce_client.models.dynamic_value_source_type import DynamicValueSourceType
    from tb_ce_client.models.dynamic_value_string import DynamicValueString
    from tb_ce_client.models.edge import Edge
    from tb_ce_client.models.edge_communication_failure_notification_rule_trigger_config import EdgeCommunicationFailureNotificationRuleTriggerConfig
    from tb_ce_client.models.edge_communication_failure_recipients_config import EdgeCommunicationFailureRecipientsConfig
    from tb_ce_client.models.edge_connection_notification_rule_trigger_config import EdgeConnectionNotificationRuleTriggerConfig
    from tb_ce_client.models.edge_connection_recipients_config import EdgeConnectionRecipientsConfig
    from tb_ce_client.models.edge_connectivity_event import EdgeConnectivityEvent
    from tb_ce_client.models.edge_event import EdgeEvent
    from tb_ce_client.models.edge_event_action_type import EdgeEventActionType
    from tb_ce_client.models.edge_event_id import EdgeEventId
    from tb_ce_client.models.edge_event_type import EdgeEventType
    from tb_ce_client.models.edge_id import EdgeId
    from tb_ce_client.models.edge_info import EdgeInfo
    from tb_ce_client.models.edge_instructions import EdgeInstructions
    from tb_ce_client.models.edge_search_query import EdgeSearchQuery
    from tb_ce_client.models.edge_search_query_filter import EdgeSearchQueryFilter
    from tb_ce_client.models.edge_type_filter import EdgeTypeFilter
    from tb_ce_client.models.edqs_api_mode import EdqsApiMode
    from tb_ce_client.models.edqs_state import EdqsState
    from tb_ce_client.models.edqs_sync_request import EdqsSyncRequest
    from tb_ce_client.models.edqs_sync_status import EdqsSyncStatus
    from tb_ce_client.models.efento_coap_device_type_configuration import EfentoCoapDeviceTypeConfiguration
    from tb_ce_client.models.email_delivery_method_notification_template import EmailDeliveryMethodNotificationTemplate
    from tb_ce_client.models.email_two_fa_account_config import EmailTwoFaAccountConfig
    from tb_ce_client.models.email_two_fa_provider_config import EmailTwoFaProviderConfig
    from tb_ce_client.models.entities_limit_notification_rule_trigger_config import EntitiesLimitNotificationRuleTriggerConfig
    from tb_ce_client.models.entities_limit_recipients_config import EntitiesLimitRecipientsConfig
    from tb_ce_client.models.entity_action_notification_rule_trigger_config import EntityActionNotificationRuleTriggerConfig
    from tb_ce_client.models.entity_action_recipients_config import EntityActionRecipientsConfig
    from tb_ce_client.models.entity_aggregation_calculated_field_configuration import EntityAggregationCalculatedFieldConfiguration
    from tb_ce_client.models.entity_coordinates import EntityCoordinates
    from tb_ce_client.models.entity_count_query import EntityCountQuery
    from tb_ce_client.models.entity_data import EntityData
    from tb_ce_client.models.entity_data_diff import EntityDataDiff
    from tb_ce_client.models.entity_data_info import EntityDataInfo
    from tb_ce_client.models.entity_data_page_link import EntityDataPageLink
    from tb_ce_client.models.entity_data_query import EntityDataQuery
    from tb_ce_client.models.entity_data_sort_order import EntityDataSortOrder
    from tb_ce_client.models.entity_export_data import EntityExportData
    from tb_ce_client.models.entity_filter import EntityFilter
    from tb_ce_client.models.entity_id import EntityId
    from tb_ce_client.models.entity_info import EntityInfo
    from tb_ce_client.models.entity_key import EntityKey
    from tb_ce_client.models.entity_key_type import EntityKeyType
    from tb_ce_client.models.entity_key_value_type import EntityKeyValueType
    from tb_ce_client.models.entity_list_filter import EntityListFilter
    from tb_ce_client.models.entity_load_error import EntityLoadError
    from tb_ce_client.models.entity_name_filter import EntityNameFilter
    from tb_ce_client.models.entity_relation import EntityRelation
    from tb_ce_client.models.entity_relation_info import EntityRelationInfo
    from tb_ce_client.models.entity_relations_query import EntityRelationsQuery
    from tb_ce_client.models.entity_search_direction import EntitySearchDirection
    from tb_ce_client.models.entity_subtype import EntitySubtype
    from tb_ce_client.models.entity_type import EntityType
    from tb_ce_client.models.entity_type_filter import EntityTypeFilter
    from tb_ce_client.models.entity_type_load_result import EntityTypeLoadResult
    from tb_ce_client.models.entity_type_version_create_config import EntityTypeVersionCreateConfig
    from tb_ce_client.models.entity_type_version_load_config import EntityTypeVersionLoadConfig
    from tb_ce_client.models.entity_type_version_load_request import EntityTypeVersionLoadRequest
    from tb_ce_client.models.entity_version import EntityVersion
    from tb_ce_client.models.entity_view import EntityView
    from tb_ce_client.models.entity_view_export_data import EntityViewExportData
    from tb_ce_client.models.entity_view_id import EntityViewId
    from tb_ce_client.models.entity_view_info import EntityViewInfo
    from tb_ce_client.models.entity_view_search_query import EntityViewSearchQuery
    from tb_ce_client.models.entity_view_search_query_filter import EntityViewSearchQueryFilter
    from tb_ce_client.models.entity_view_type_filter import EntityViewTypeFilter
    from tb_ce_client.models.error_event_filter import ErrorEventFilter
    from tb_ce_client.models.escalated_notification_rule_recipients_config import EscalatedNotificationRuleRecipientsConfig
    from tb_ce_client.models.event_filter import EventFilter
    from tb_ce_client.models.event_id import EventId
    from tb_ce_client.models.event_info import EventInfo
    from tb_ce_client.models.event_type import EventType
    from tb_ce_client.models.exportable_entity import ExportableEntity
    from tb_ce_client.models.failure import Failure
    from tb_ce_client.models.features_info import FeaturesInfo
    from tb_ce_client.models.filter_predicate_value_boolean import FilterPredicateValueBoolean
    from tb_ce_client.models.filter_predicate_value_double import FilterPredicateValueDouble
    from tb_ce_client.models.filter_predicate_value_string import FilterPredicateValueString
    from tb_ce_client.models.geofencing_calculated_field_configuration import GeofencingCalculatedFieldConfiguration
    from tb_ce_client.models.geofencing_report_strategy import GeofencingReportStrategy
    from tb_ce_client.models.git_hub_models_chat_model_config import GitHubModelsChatModelConfig
    from tb_ce_client.models.git_hub_models_provider_config import GitHubModelsProviderConfig
    from tb_ce_client.models.google_ai_gemini_chat_model_config import GoogleAiGeminiChatModelConfig
    from tb_ce_client.models.google_ai_gemini_provider_config import GoogleAiGeminiProviderConfig
    from tb_ce_client.models.google_vertex_ai_gemini_chat_model_config import GoogleVertexAiGeminiChatModelConfig
    from tb_ce_client.models.google_vertex_ai_gemini_provider_config import GoogleVertexAiGeminiProviderConfig
    from tb_ce_client.models.has_id_object import HasIdObject
    from tb_ce_client.models.home_dashboard import HomeDashboard
    from tb_ce_client.models.home_dashboard_info import HomeDashboardInfo
    from tb_ce_client.models.hour_interval import HourInterval
    from tb_ce_client.models.job import Job
    from tb_ce_client.models.job_configuration import JobConfiguration
    from tb_ce_client.models.job_id import JobId
    from tb_ce_client.models.job_result import JobResult
    from tb_ce_client.models.job_status import JobStatus
    from tb_ce_client.models.job_type import JobType
    from tb_ce_client.models.json_transport_payload_configuration import JsonTransportPayloadConfiguration
    from tb_ce_client.models.jwt_pair import JwtPair
    from tb_ce_client.models.jwt_settings import JwtSettings
    from tb_ce_client.models.key_filter import KeyFilter
    from tb_ce_client.models.key_filter_predicate import KeyFilterPredicate
    from tb_ce_client.models.key_info import KeyInfo
    from tb_ce_client.models.key_sample import KeySample
    from tb_ce_client.models.last_visited_dashboard_info import LastVisitedDashboardInfo
    from tb_ce_client.models.life_cycle_event_filter import LifeCycleEventFilter
    from tb_ce_client.models.limited_api import LimitedApi
    from tb_ce_client.models.link_type import LinkType
    from tb_ce_client.models.login401_response import Login401Response
    from tb_ce_client.models.login_mobile_info import LoginMobileInfo
    from tb_ce_client.models.login_request import LoginRequest
    from tb_ce_client.models.login_response import LoginResponse
    from tb_ce_client.models.lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential
    from tb_ce_client.models.lw_m2_m_server_security_config_default import LwM2MServerSecurityConfigDefault
    from tb_ce_client.models.lw_m2m_instance import LwM2mInstance
    from tb_ce_client.models.lw_m2m_object import LwM2mObject
    from tb_ce_client.models.lw_m2m_resource_observe import LwM2mResourceObserve
    from tb_ce_client.models.lw_m2m_version import LwM2mVersion
    from tb_ce_client.models.lwm2m_device_profile_transport_configuration import Lwm2mDeviceProfileTransportConfiguration
    from tb_ce_client.models.lwm2m_device_transport_configuration import Lwm2mDeviceTransportConfiguration
    from tb_ce_client.models.mapper_type import MapperType
    from tb_ce_client.models.mapping import Mapping
    from tb_ce_client.models.microsoft_teams_delivery_method_notification_template import MicrosoftTeamsDeliveryMethodNotificationTemplate
    from tb_ce_client.models.microsoft_teams_notification_target_config import MicrosoftTeamsNotificationTargetConfig
    from tb_ce_client.models.mistral_ai_chat_model_config import MistralAiChatModelConfig
    from tb_ce_client.models.mistral_ai_provider_config import MistralAiProviderConfig
    from tb_ce_client.models.mobile_app import MobileApp
    from tb_ce_client.models.mobile_app_bundle import MobileAppBundle
    from tb_ce_client.models.mobile_app_bundle_id import MobileAppBundleId
    from tb_ce_client.models.mobile_app_bundle_info import MobileAppBundleInfo
    from tb_ce_client.models.mobile_app_delivery_method_notification_template import MobileAppDeliveryMethodNotificationTemplate
    from tb_ce_client.models.mobile_app_id import MobileAppId
    from tb_ce_client.models.mobile_app_notification_delivery_method_config import MobileAppNotificationDeliveryMethodConfig
    from tb_ce_client.models.mobile_app_status import MobileAppStatus
    from tb_ce_client.models.mobile_app_version_info import MobileAppVersionInfo
    from tb_ce_client.models.mobile_layout_config import MobileLayoutConfig
    from tb_ce_client.models.mobile_page import MobilePage
    from tb_ce_client.models.mobile_page_type import MobilePageType
    from tb_ce_client.models.mobile_session_info import MobileSessionInfo
    from tb_ce_client.models.model_none import ModelNone
    from tb_ce_client.models.month_interval import MonthInterval
    from tb_ce_client.models.mqtt_device_profile_transport_configuration import MqttDeviceProfileTransportConfiguration
    from tb_ce_client.models.mqtt_device_transport_configuration import MqttDeviceTransportConfiguration
    from tb_ce_client.models.name_conflict_policy import NameConflictPolicy
    from tb_ce_client.models.new_platform_version_notification_rule_trigger_config import NewPlatformVersionNotificationRuleTriggerConfig
    from tb_ce_client.models.new_platform_version_recipients_config import NewPlatformVersionRecipientsConfig
    from tb_ce_client.models.no_data_filter_predicate import NoDataFilterPredicate
    from tb_ce_client.models.no_sec_lw_m2_m_bootstrap_server_credential import NoSecLwM2MBootstrapServerCredential
    from tb_ce_client.models.node_connection_info import NodeConnectionInfo
    from tb_ce_client.models.notification import Notification
    from tb_ce_client.models.notification_delivery_method import NotificationDeliveryMethod
    from tb_ce_client.models.notification_delivery_method_config import NotificationDeliveryMethodConfig
    from tb_ce_client.models.notification_id import NotificationId
    from tb_ce_client.models.notification_info import NotificationInfo
    from tb_ce_client.models.notification_pref import NotificationPref
    from tb_ce_client.models.notification_request import NotificationRequest
    from tb_ce_client.models.notification_request_config import NotificationRequestConfig
    from tb_ce_client.models.notification_request_id import NotificationRequestId
    from tb_ce_client.models.notification_request_info import NotificationRequestInfo
    from tb_ce_client.models.notification_request_preview import NotificationRequestPreview
    from tb_ce_client.models.notification_request_stats import NotificationRequestStats
    from tb_ce_client.models.notification_request_status import NotificationRequestStatus
    from tb_ce_client.models.notification_rule import NotificationRule
    from tb_ce_client.models.notification_rule_config import NotificationRuleConfig
    from tb_ce_client.models.notification_rule_export_data import NotificationRuleExportData
    from tb_ce_client.models.notification_rule_id import NotificationRuleId
    from tb_ce_client.models.notification_rule_info import NotificationRuleInfo
    from tb_ce_client.models.notification_rule_recipients_config import NotificationRuleRecipientsConfig
    from tb_ce_client.models.notification_rule_trigger_config import NotificationRuleTriggerConfig
    from tb_ce_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
    from tb_ce_client.models.notification_settings import NotificationSettings
    from tb_ce_client.models.notification_status import NotificationStatus
    from tb_ce_client.models.notification_target import NotificationTarget
    from tb_ce_client.models.notification_target_config import NotificationTargetConfig
    from tb_ce_client.models.notification_target_export_data import NotificationTargetExportData
    from tb_ce_client.models.notification_target_id import NotificationTargetId
    from tb_ce_client.models.notification_template import NotificationTemplate
    from tb_ce_client.models.notification_template_config import NotificationTemplateConfig
    from tb_ce_client.models.notification_template_export_data import NotificationTemplateExportData
    from tb_ce_client.models.notification_template_id import NotificationTemplateId
    from tb_ce_client.models.notification_type import NotificationType
    from tb_ce_client.models.numeric_filter_predicate import NumericFilterPredicate
    from tb_ce_client.models.numeric_operation import NumericOperation
    from tb_ce_client.models.o_auth2_basic_mapper_config import OAuth2BasicMapperConfig
    from tb_ce_client.models.o_auth2_client import OAuth2Client
    from tb_ce_client.models.o_auth2_client_id import OAuth2ClientId
    from tb_ce_client.models.o_auth2_client_info import OAuth2ClientInfo
    from tb_ce_client.models.o_auth2_client_login_info import OAuth2ClientLoginInfo
    from tb_ce_client.models.o_auth2_client_registration_template import OAuth2ClientRegistrationTemplate
    from tb_ce_client.models.o_auth2_client_registration_template_id import OAuth2ClientRegistrationTemplateId
    from tb_ce_client.models.o_auth2_custom_mapper_config import OAuth2CustomMapperConfig
    from tb_ce_client.models.o_auth2_mapper_config import OAuth2MapperConfig
    from tb_ce_client.models.object_attributes import ObjectAttributes
    from tb_ce_client.models.object_type import ObjectType
    from tb_ce_client.models.ollama_auth import OllamaAuth
    from tb_ce_client.models.ollama_chat_model_config import OllamaChatModelConfig
    from tb_ce_client.models.ollama_provider_config import OllamaProviderConfig
    from tb_ce_client.models.open_ai_chat_model_config import OpenAiChatModelConfig
    from tb_ce_client.models.open_ai_provider_config import OpenAiProviderConfig
    from tb_ce_client.models.originator_entity_owner_users_filter import OriginatorEntityOwnerUsersFilter
    from tb_ce_client.models.ota_package import OtaPackage
    from tb_ce_client.models.ota_package_export_data import OtaPackageExportData
    from tb_ce_client.models.ota_package_id import OtaPackageId
    from tb_ce_client.models.ota_package_info import OtaPackageInfo
    from tb_ce_client.models.ota_package_type import OtaPackageType
    from tb_ce_client.models.other_configuration import OtherConfiguration
    from tb_ce_client.models.output import Output
    from tb_ce_client.models.psklw_m2_m_bootstrap_server_credential import PSKLwM2MBootstrapServerCredential
    from tb_ce_client.models.page_data_ai_model import PageDataAiModel
    from tb_ce_client.models.page_data_alarm_comment_info import PageDataAlarmCommentInfo
    from tb_ce_client.models.page_data_alarm_data import PageDataAlarmData
    from tb_ce_client.models.page_data_alarm_info import PageDataAlarmInfo
    from tb_ce_client.models.page_data_alarm_rule_definition import PageDataAlarmRuleDefinition
    from tb_ce_client.models.page_data_alarm_rule_definition_info import PageDataAlarmRuleDefinitionInfo
    from tb_ce_client.models.page_data_api_key_info import PageDataApiKeyInfo
    from tb_ce_client.models.page_data_asset import PageDataAsset
    from tb_ce_client.models.page_data_asset_info import PageDataAssetInfo
    from tb_ce_client.models.page_data_asset_profile import PageDataAssetProfile
    from tb_ce_client.models.page_data_asset_profile_info import PageDataAssetProfileInfo
    from tb_ce_client.models.page_data_audit_log import PageDataAuditLog
    from tb_ce_client.models.page_data_calculated_field import PageDataCalculatedField
    from tb_ce_client.models.page_data_calculated_field_info import PageDataCalculatedFieldInfo
    from tb_ce_client.models.page_data_customer import PageDataCustomer
    from tb_ce_client.models.page_data_dashboard_info import PageDataDashboardInfo
    from tb_ce_client.models.page_data_device import PageDataDevice
    from tb_ce_client.models.page_data_device_info import PageDataDeviceInfo
    from tb_ce_client.models.page_data_device_profile import PageDataDeviceProfile
    from tb_ce_client.models.page_data_device_profile_info import PageDataDeviceProfileInfo
    from tb_ce_client.models.page_data_domain_info import PageDataDomainInfo
    from tb_ce_client.models.page_data_edge import PageDataEdge
    from tb_ce_client.models.page_data_edge_event import PageDataEdgeEvent
    from tb_ce_client.models.page_data_edge_info import PageDataEdgeInfo
    from tb_ce_client.models.page_data_entity_data import PageDataEntityData
    from tb_ce_client.models.page_data_entity_info import PageDataEntityInfo
    from tb_ce_client.models.page_data_entity_subtype import PageDataEntitySubtype
    from tb_ce_client.models.page_data_entity_version import PageDataEntityVersion
    from tb_ce_client.models.page_data_entity_view import PageDataEntityView
    from tb_ce_client.models.page_data_entity_view_info import PageDataEntityViewInfo
    from tb_ce_client.models.page_data_event_info import PageDataEventInfo
    from tb_ce_client.models.page_data_job import PageDataJob
    from tb_ce_client.models.page_data_mobile_app import PageDataMobileApp
    from tb_ce_client.models.page_data_mobile_app_bundle_info import PageDataMobileAppBundleInfo
    from tb_ce_client.models.page_data_notification import PageDataNotification
    from tb_ce_client.models.page_data_notification_request_info import PageDataNotificationRequestInfo
    from tb_ce_client.models.page_data_notification_rule_info import PageDataNotificationRuleInfo
    from tb_ce_client.models.page_data_notification_target import PageDataNotificationTarget
    from tb_ce_client.models.page_data_notification_template import PageDataNotificationTemplate
    from tb_ce_client.models.page_data_o_auth2_client_info import PageDataOAuth2ClientInfo
    from tb_ce_client.models.page_data_ota_package_info import PageDataOtaPackageInfo
    from tb_ce_client.models.page_data_queue import PageDataQueue
    from tb_ce_client.models.page_data_queue_stats import PageDataQueueStats
    from tb_ce_client.models.page_data_rule_chain import PageDataRuleChain
    from tb_ce_client.models.page_data_string import PageDataString
    from tb_ce_client.models.page_data_tb_resource_info import PageDataTbResourceInfo
    from tb_ce_client.models.page_data_tenant import PageDataTenant
    from tb_ce_client.models.page_data_tenant_info import PageDataTenantInfo
    from tb_ce_client.models.page_data_tenant_profile import PageDataTenantProfile
    from tb_ce_client.models.page_data_user import PageDataUser
    from tb_ce_client.models.page_data_user_email_info import PageDataUserEmailInfo
    from tb_ce_client.models.page_data_widget_type_info import PageDataWidgetTypeInfo
    from tb_ce_client.models.page_data_widgets_bundle import PageDataWidgetsBundle
    from tb_ce_client.models.platform_two_fa_settings import PlatformTwoFaSettings
    from tb_ce_client.models.platform_type import PlatformType
    from tb_ce_client.models.platform_users_notification_target_config import PlatformUsersNotificationTargetConfig
    from tb_ce_client.models.power_mode import PowerMode
    from tb_ce_client.models.power_saving_configuration import PowerSavingConfiguration
    from tb_ce_client.models.privacy_protocol import PrivacyProtocol
    from tb_ce_client.models.processing_strategy import ProcessingStrategy
    from tb_ce_client.models.processing_strategy_type import ProcessingStrategyType
    from tb_ce_client.models.propagation_calculated_field_configuration import PropagationCalculatedFieldConfiguration
    from tb_ce_client.models.proto_transport_payload_configuration import ProtoTransportPayloadConfiguration
    from tb_ce_client.models.qr_code_config import QRCodeConfig
    from tb_ce_client.models.qr_code_settings import QrCodeSettings
    from tb_ce_client.models.qr_code_settings_id import QrCodeSettingsId
    from tb_ce_client.models.quarter_interval import QuarterInterval
    from tb_ce_client.models.queue import Queue
    from tb_ce_client.models.queue_id import QueueId
    from tb_ce_client.models.queue_stats import QueueStats
    from tb_ce_client.models.queue_stats_id import QueueStatsId
    from tb_ce_client.models.rpklw_m2_m_bootstrap_server_credential import RPKLwM2MBootstrapServerCredential
    from tb_ce_client.models.rate_limits_notification_rule_trigger_config import RateLimitsNotificationRuleTriggerConfig
    from tb_ce_client.models.rate_limits_recipients_config import RateLimitsRecipientsConfig
    from tb_ce_client.models.referenced_entity_key import ReferencedEntityKey
    from tb_ce_client.models.refresh_token_request import RefreshTokenRequest
    from tb_ce_client.models.related_entities_aggregation_calculated_field_configuration import RelatedEntitiesAggregationCalculatedFieldConfiguration
    from tb_ce_client.models.relation_entity_type_filter import RelationEntityTypeFilter
    from tb_ce_client.models.relation_path_level import RelationPathLevel
    from tb_ce_client.models.relation_path_query_dynamic_source_configuration import RelationPathQueryDynamicSourceConfiguration
    from tb_ce_client.models.relation_type_group import RelationTypeGroup
    from tb_ce_client.models.relations_query_filter import RelationsQueryFilter
    from tb_ce_client.models.relations_search_parameters import RelationsSearchParameters
    from tb_ce_client.models.repeating_alarm_condition import RepeatingAlarmCondition
    from tb_ce_client.models.repository_auth_method import RepositoryAuthMethod
    from tb_ce_client.models.repository_settings import RepositorySettings
    from tb_ce_client.models.repository_settings_info import RepositorySettingsInfo
    from tb_ce_client.models.reset_password_email_request import ResetPasswordEmailRequest
    from tb_ce_client.models.reset_password_request import ResetPasswordRequest
    from tb_ce_client.models.resource_export_data import ResourceExportData
    from tb_ce_client.models.resource_shortage_recipients_config import ResourceShortageRecipientsConfig
    from tb_ce_client.models.resource_sub_type import ResourceSubType
    from tb_ce_client.models.resource_type import ResourceType
    from tb_ce_client.models.resources_shortage_notification_rule_trigger_config import ResourcesShortageNotificationRuleTriggerConfig
    from tb_ce_client.models.rpc import Rpc
    from tb_ce_client.models.rpc_id import RpcId
    from tb_ce_client.models.rpc_status import RpcStatus
    from tb_ce_client.models.rule_chain import RuleChain
    from tb_ce_client.models.rule_chain_connection_info import RuleChainConnectionInfo
    from tb_ce_client.models.rule_chain_data import RuleChainData
    from tb_ce_client.models.rule_chain_debug_event_filter import RuleChainDebugEventFilter
    from tb_ce_client.models.rule_chain_export_data import RuleChainExportData
    from tb_ce_client.models.rule_chain_id import RuleChainId
    from tb_ce_client.models.rule_chain_import_result import RuleChainImportResult
    from tb_ce_client.models.rule_chain_meta_data import RuleChainMetaData
    from tb_ce_client.models.rule_chain_note import RuleChainNote
    from tb_ce_client.models.rule_chain_output_labels_usage import RuleChainOutputLabelsUsage
    from tb_ce_client.models.rule_chain_type import RuleChainType
    from tb_ce_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config import RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig
    from tb_ce_client.models.rule_engine_component_lifecycle_event_recipients_config import RuleEngineComponentLifecycleEventRecipientsConfig
    from tb_ce_client.models.rule_node import RuleNode
    from tb_ce_client.models.rule_node_debug_event_filter import RuleNodeDebugEventFilter
    from tb_ce_client.models.rule_node_id import RuleNodeId
    from tb_ce_client.models.save_device_with_credentials_request import SaveDeviceWithCredentialsRequest
    from tb_ce_client.models.save_ota_package_info_request import SaveOtaPackageInfoRequest
    from tb_ce_client.models.script_calculated_field_configuration import ScriptCalculatedFieldConfiguration
    from tb_ce_client.models.script_language import ScriptLanguage
    from tb_ce_client.models.security_settings import SecuritySettings
    from tb_ce_client.models.shared_attributes_setting_snmp_communication_config import SharedAttributesSettingSnmpCommunicationConfig
    from tb_ce_client.models.short_customer_info import ShortCustomerInfo
    from tb_ce_client.models.simple_alarm_condition import SimpleAlarmCondition
    from tb_ce_client.models.simple_alarm_condition_expression import SimpleAlarmConditionExpression
    from tb_ce_client.models.simple_calculated_field_configuration import SimpleCalculatedFieldConfiguration
    from tb_ce_client.models.single_entity_filter import SingleEntityFilter
    from tb_ce_client.models.single_entity_version_create_request import SingleEntityVersionCreateRequest
    from tb_ce_client.models.single_entity_version_load_request import SingleEntityVersionLoadRequest
    from tb_ce_client.models.slack_conversation import SlackConversation
    from tb_ce_client.models.slack_conversation_type import SlackConversationType
    from tb_ce_client.models.slack_delivery_method_notification_template import SlackDeliveryMethodNotificationTemplate
    from tb_ce_client.models.slack_notification_delivery_method_config import SlackNotificationDeliveryMethodConfig
    from tb_ce_client.models.slack_notification_target_config import SlackNotificationTargetConfig
    from tb_ce_client.models.smpp_bind_type import SmppBindType
    from tb_ce_client.models.smpp_sms_provider_configuration import SmppSmsProviderConfiguration
    from tb_ce_client.models.sms_delivery_method_notification_template import SmsDeliveryMethodNotificationTemplate
    from tb_ce_client.models.sms_provider_configuration import SmsProviderConfiguration
    from tb_ce_client.models.sms_two_fa_account_config import SmsTwoFaAccountConfig
    from tb_ce_client.models.sms_two_fa_provider_config import SmsTwoFaProviderConfig
    from tb_ce_client.models.snmp_communication_config import SnmpCommunicationConfig
    from tb_ce_client.models.snmp_communication_spec import SnmpCommunicationSpec
    from tb_ce_client.models.snmp_device_profile_transport_configuration import SnmpDeviceProfileTransportConfiguration
    from tb_ce_client.models.snmp_device_transport_configuration import SnmpDeviceTransportConfiguration
    from tb_ce_client.models.snmp_mapping import SnmpMapping
    from tb_ce_client.models.snmp_protocol_version import SnmpProtocolVersion
    from tb_ce_client.models.specific_time_schedule import SpecificTimeSchedule
    from tb_ce_client.models.starred_dashboard_info import StarredDashboardInfo
    from tb_ce_client.models.statistics_event_filter import StatisticsEventFilter
    from tb_ce_client.models.store_info import StoreInfo
    from tb_ce_client.models.string_filter_predicate import StringFilterPredicate
    from tb_ce_client.models.string_operation import StringOperation
    from tb_ce_client.models.submit_strategy import SubmitStrategy
    from tb_ce_client.models.submit_strategy_type import SubmitStrategyType
    from tb_ce_client.models.success import Success
    from tb_ce_client.models.sync_strategy import SyncStrategy
    from tb_ce_client.models.system_administrators_filter import SystemAdministratorsFilter
    from tb_ce_client.models.system_info import SystemInfo
    from tb_ce_client.models.system_info_data import SystemInfoData
    from tb_ce_client.models.task_processing_failure_notification_rule_trigger_config import TaskProcessingFailureNotificationRuleTriggerConfig
    from tb_ce_client.models.task_processing_failure_recipients_config import TaskProcessingFailureRecipientsConfig
    from tb_ce_client.models.task_result import TaskResult
    from tb_ce_client.models.tb_chat_request import TbChatRequest
    from tb_ce_client.models.tb_chat_response import TbChatResponse
    from tb_ce_client.models.tb_content import TbContent
    from tb_ce_client.models.tb_image_delete_result import TbImageDeleteResult
    from tb_ce_client.models.tb_resource import TbResource
    from tb_ce_client.models.tb_resource_delete_result import TbResourceDeleteResult
    from tb_ce_client.models.tb_resource_export_data import TbResourceExportData
    from tb_ce_client.models.tb_resource_id import TbResourceId
    from tb_ce_client.models.tb_resource_info import TbResourceInfo
    from tb_ce_client.models.tb_text_content import TbTextContent
    from tb_ce_client.models.tb_user_message import TbUserMessage
    from tb_ce_client.models.tbel_alarm_condition_expression import TbelAlarmConditionExpression
    from tb_ce_client.models.telemetry_entity_view import TelemetryEntityView
    from tb_ce_client.models.telemetry_mapping_configuration import TelemetryMappingConfiguration
    from tb_ce_client.models.telemetry_observe_strategy import TelemetryObserveStrategy
    from tb_ce_client.models.telemetry_querying_snmp_communication_config import TelemetryQueryingSnmpCommunicationConfig
    from tb_ce_client.models.tenant import Tenant
    from tb_ce_client.models.tenant_administrators_filter import TenantAdministratorsFilter
    from tb_ce_client.models.tenant_id import TenantId
    from tb_ce_client.models.tenant_info import TenantInfo
    from tb_ce_client.models.tenant_name_strategy_type import TenantNameStrategyType
    from tb_ce_client.models.tenant_profile import TenantProfile
    from tb_ce_client.models.tenant_profile_configuration import TenantProfileConfiguration
    from tb_ce_client.models.tenant_profile_data import TenantProfileData
    from tb_ce_client.models.tenant_profile_id import TenantProfileId
    from tb_ce_client.models.tenant_profile_queue_configuration import TenantProfileQueueConfiguration
    from tb_ce_client.models.test_sms_request import TestSmsRequest
    from tb_ce_client.models.thingsboard_credentials_expired_response import ThingsboardCredentialsExpiredResponse
    from tb_ce_client.models.thingsboard_error_code import ThingsboardErrorCode
    from tb_ce_client.models.thingsboard_error_response import ThingsboardErrorResponse
    from tb_ce_client.models.time_series_immediate_output_strategy import TimeSeriesImmediateOutputStrategy
    from tb_ce_client.models.time_series_output import TimeSeriesOutput
    from tb_ce_client.models.time_series_output_strategy import TimeSeriesOutputStrategy
    from tb_ce_client.models.time_series_rule_chain_output_strategy import TimeSeriesRuleChainOutputStrategy
    from tb_ce_client.models.time_unit import TimeUnit
    from tb_ce_client.models.to_core_edqs_request import ToCoreEdqsRequest
    from tb_ce_client.models.to_device_rpc_request_snmp_communication_config import ToDeviceRpcRequestSnmpCommunicationConfig
    from tb_ce_client.models.to_server_rpc_request_snmp_communication_config import ToServerRpcRequestSnmpCommunicationConfig
    from tb_ce_client.models.token import Token
    from tb_ce_client.models.totp_two_fa_account_config import TotpTwoFaAccountConfig
    from tb_ce_client.models.totp_two_fa_provider_config import TotpTwoFaProviderConfig
    from tb_ce_client.models.transport_payload_type_configuration import TransportPayloadTypeConfiguration
    from tb_ce_client.models.trendz_settings import TrendzSettings
    from tb_ce_client.models.ts_data import TsData
    from tb_ce_client.models.ts_value import TsValue
    from tb_ce_client.models.twilio_sms_provider_configuration import TwilioSmsProviderConfiguration
    from tb_ce_client.models.two_fa_account_config import TwoFaAccountConfig
    from tb_ce_client.models.two_fa_account_config_update_request import TwoFaAccountConfigUpdateRequest
    from tb_ce_client.models.two_fa_provider_config import TwoFaProviderConfig
    from tb_ce_client.models.two_fa_provider_info import TwoFaProviderInfo
    from tb_ce_client.models.two_fa_provider_type import TwoFaProviderType
    from tb_ce_client.models.uniquify_strategy import UniquifyStrategy
    from tb_ce_client.models.update_message import UpdateMessage
    from tb_ce_client.models.usage_info import UsageInfo
    from tb_ce_client.models.user import User
    from tb_ce_client.models.user_activation_link import UserActivationLink
    from tb_ce_client.models.user_dashboards_info import UserDashboardsInfo
    from tb_ce_client.models.user_email_info import UserEmailInfo
    from tb_ce_client.models.user_id import UserId
    from tb_ce_client.models.user_list_filter import UserListFilter
    from tb_ce_client.models.user_mobile_info import UserMobileInfo
    from tb_ce_client.models.user_notification_settings import UserNotificationSettings
    from tb_ce_client.models.user_password_policy import UserPasswordPolicy
    from tb_ce_client.models.users_filter import UsersFilter
    from tb_ce_client.models.version_create_config import VersionCreateConfig
    from tb_ce_client.models.version_create_request import VersionCreateRequest
    from tb_ce_client.models.version_create_request_type import VersionCreateRequestType
    from tb_ce_client.models.version_creation_result import VersionCreationResult
    from tb_ce_client.models.version_load_config import VersionLoadConfig
    from tb_ce_client.models.version_load_request import VersionLoadRequest
    from tb_ce_client.models.version_load_request_type import VersionLoadRequestType
    from tb_ce_client.models.version_load_result import VersionLoadResult
    from tb_ce_client.models.versioned_entity_info import VersionedEntityInfo
    from tb_ce_client.models.watermark import Watermark
    from tb_ce_client.models.web_delivery_method_notification_template import WebDeliveryMethodNotificationTemplate
    from tb_ce_client.models.web_view_page import WebViewPage
    from tb_ce_client.models.week_interval import WeekInterval
    from tb_ce_client.models.week_sun_sat_interval import WeekSunSatInterval
    from tb_ce_client.models.widget_bundle_info import WidgetBundleInfo
    from tb_ce_client.models.widget_type import WidgetType
    from tb_ce_client.models.widget_type_details import WidgetTypeDetails
    from tb_ce_client.models.widget_type_export_data import WidgetTypeExportData
    from tb_ce_client.models.widget_type_id import WidgetTypeId
    from tb_ce_client.models.widget_type_info import WidgetTypeInfo
    from tb_ce_client.models.widgets_bundle import WidgetsBundle
    from tb_ce_client.models.widgets_bundle_export_data import WidgetsBundleExportData
    from tb_ce_client.models.widgets_bundle_id import WidgetsBundleId
    from tb_ce_client.models.x509_certificate_chain_provision_configuration import X509CertificateChainProvisionConfiguration
    from tb_ce_client.models.x509_lw_m2_m_bootstrap_server_credential import X509LwM2MBootstrapServerCredential
    from tb_ce_client.models.year_interval import YearInterval
    from tb_ce_client.models.zone_group_configuration import ZoneGroupConfiguration

_MODEL_CLASSES = {
    "AccountTwoFaSettings": "tb_ce_client.models.account_two_fa_settings",
    "Action": "tb_ce_client.models.action",
    "ActionStatus": "tb_ce_client.models.action_status",
    "ActionType": "tb_ce_client.models.action_type",
    "ActivateUserRequest": "tb_ce_client.models.activate_user_request",
    "AdminSettings": "tb_ce_client.models.admin_settings",
    "AdminSettingsId": "tb_ce_client.models.admin_settings_id",
    "AffectedTenantAdministratorsFilter": "tb_ce_client.models.affected_tenant_administrators_filter",
    "AffectedUserFilter": "tb_ce_client.models.affected_user_filter",
    "AggFunction": "tb_ce_client.models.agg_function",
    "AggFunctionInput": "tb_ce_client.models.agg_function_input",
    "AggInput": "tb_ce_client.models.agg_input",
    "AggInterval": "tb_ce_client.models.agg_interval",
    "AggKeyInput": "tb_ce_client.models.agg_key_input",
    "AggMetric": "tb_ce_client.models.agg_metric",
    "AiChatModelConfig": "tb_ce_client.models.ai_chat_model_config",
    "AiModel": "tb_ce_client.models.ai_model",
    "AiModelConfig": "tb_ce_client.models.ai_model_config",
    "AiModelExportData": "tb_ce_client.models.ai_model_export_data",
    "AiModelId": "tb_ce_client.models.ai_model_id",
    "AiModelType": "tb_ce_client.models.ai_model_type",
    "Alarm": "tb_ce_client.models.alarm",
    "AlarmAction": "tb_ce_client.models.alarm_action",
    "AlarmAssignee": "tb_ce_client.models.alarm_assignee",
    "AlarmAssignmentNotificationRuleTriggerConfig": "tb_ce_client.models.alarm_assignment_notification_rule_trigger_config",
    "AlarmAssignmentRecipientsConfig": "tb_ce_client.models.alarm_assignment_recipients_config",
    "AlarmCalculatedFieldConfiguration": "tb_ce_client.models.alarm_calculated_field_configuration",
    "AlarmComment": "tb_ce_client.models.alarm_comment",
    "AlarmCommentId": "tb_ce_client.models.alarm_comment_id",
    "AlarmCommentInfo": "tb_ce_client.models.alarm_comment_info",
    "AlarmCommentNotificationRuleTriggerConfig": "tb_ce_client.models.alarm_comment_notification_rule_trigger_config",
    "AlarmCommentRecipientsConfig": "tb_ce_client.models.alarm_comment_recipients_config",
    "AlarmCommentType": "tb_ce_client.models.alarm_comment_type",
    "AlarmCondition": "tb_ce_client.models.alarm_condition",
    "AlarmConditionExpression": "tb_ce_client.models.alarm_condition_expression",
    "AlarmConditionFilter": "tb_ce_client.models.alarm_condition_filter",
    "AlarmConditionValueAlarmSchedule": "tb_ce_client.models.alarm_condition_value_alarm_schedule",
    "AlarmConditionValueBoolean": "tb_ce_client.models.alarm_condition_value_boolean",
    "AlarmConditionValueDouble": "tb_ce_client.models.alarm_condition_value_double",
    "AlarmConditionValueInteger": "tb_ce_client.models.alarm_condition_value_integer",
    "AlarmConditionValueLong": "tb_ce_client.models.alarm_condition_value_long",
    "AlarmConditionValueString": "tb_ce_client.models.alarm_condition_value_string",
    "AlarmCountQuery": "tb_ce_client.models.alarm_count_query",
    "AlarmData": "tb_ce_client.models.alarm_data",
    "AlarmDataPageLink": "tb_ce_client.models.alarm_data_page_link",
    "AlarmDataQuery": "tb_ce_client.models.alarm_data_query",
    "AlarmId": "tb_ce_client.models.alarm_id",
    "AlarmInfo": "tb_ce_client.models.alarm_info",
    "AlarmNotificationRuleTriggerConfig": "tb_ce_client.models.alarm_notification_rule_trigger_config",
    "AlarmRule": "tb_ce_client.models.alarm_rule",
    "AlarmRuleBooleanFilterPredicate": "tb_ce_client.models.alarm_rule_boolean_filter_predicate",
    "AlarmRuleBooleanOperation": "tb_ce_client.models.alarm_rule_boolean_operation",
    "AlarmRuleComplexFilterPredicate": "tb_ce_client.models.alarm_rule_complex_filter_predicate",
    "AlarmRuleComplexOperation": "tb_ce_client.models.alarm_rule_complex_operation",
    "AlarmRuleDefinition": "tb_ce_client.models.alarm_rule_definition",
    "AlarmRuleDefinitionInfo": "tb_ce_client.models.alarm_rule_definition_info",
    "AlarmRuleKeyFilterPredicate": "tb_ce_client.models.alarm_rule_key_filter_predicate",
    "AlarmRuleNumericFilterPredicate": "tb_ce_client.models.alarm_rule_numeric_filter_predicate",
    "AlarmRuleNumericOperation": "tb_ce_client.models.alarm_rule_numeric_operation",
    "AlarmRuleStringFilterPredicate": "tb_ce_client.models.alarm_rule_string_filter_predicate",
    "AlarmRuleStringOperation": "tb_ce_client.models.alarm_rule_string_operation",
    "AlarmSchedule": "tb_ce_client.models.alarm_schedule",
    "AlarmSearchStatus": "tb_ce_client.models.alarm_search_status",
    "AlarmSeverity": "tb_ce_client.models.alarm_severity",
    "AlarmStatus": "tb_ce_client.models.alarm_status",
    "AliasEntityId": "tb_ce_client.models.alias_entity_id",
    "AliasEntityType": "tb_ce_client.models.alias_entity_type",
    "AllUsersFilter": "tb_ce_client.models.all_users_filter",
    "AllowCreateNewDevicesDeviceProfileProvisionConfiguration": "tb_ce_client.models.allow_create_new_devices_device_profile_provision_configuration",
    "AmazonBedrockChatModelConfig": "tb_ce_client.models.amazon_bedrock_chat_model_config",
    "AmazonBedrockProviderConfig": "tb_ce_client.models.amazon_bedrock_provider_config",
    "AnthropicChatModelConfig": "tb_ce_client.models.anthropic_chat_model_config",
    "AnthropicProviderConfig": "tb_ce_client.models.anthropic_provider_config",
    "AnyTimeSchedule": "tb_ce_client.models.any_time_schedule",
    "ApiFeature": "tb_ce_client.models.api_feature",
    "ApiKey": "tb_ce_client.models.api_key",
    "ApiKeyId": "tb_ce_client.models.api_key_id",
    "ApiKeyInfo": "tb_ce_client.models.api_key_info",
    "ApiUsageLimitNotificationRuleTriggerConfig": "tb_ce_client.models.api_usage_limit_notification_rule_trigger_config",
    "ApiUsageLimitRecipientsConfig": "tb_ce_client.models.api_usage_limit_recipients_config",
    "ApiUsageStateFilter": "tb_ce_client.models.api_usage_state_filter",
    "ApiUsageStateId": "tb_ce_client.models.api_usage_state_id",
    "ApiUsageStateValue": "tb_ce_client.models.api_usage_state_value",
    "Argument": "tb_ce_client.models.argument",
    "ArgumentType": "tb_ce_client.models.argument_type",
    "Asset": "tb_ce_client.models.asset",
    "AssetExportData": "tb_ce_client.models.asset_export_data",
    "AssetId": "tb_ce_client.models.asset_id",
    "AssetInfo": "tb_ce_client.models.asset_info",
    "AssetProfile": "tb_ce_client.models.asset_profile",
    "AssetProfileExportData": "tb_ce_client.models.asset_profile_export_data",
    "AssetProfileId": "tb_ce_client.models.asset_profile_id",
    "AssetProfileInfo": "tb_ce_client.models.asset_profile_info",
    "AssetSearchQuery": "tb_ce_client.models.asset_search_query",
    "AssetSearchQueryFilter": "tb_ce_client.models.asset_search_query_filter",
    "AssetTypeFilter": "tb_ce_client.models.asset_type_filter",
    "AttributeData": "tb_ce_client.models.attribute_data",
    "AttributeExportData": "tb_ce_client.models.attribute_export_data",
    "AttributeScope": "tb_ce_client.models.attribute_scope",
    "AttributesEntityView": "tb_ce_client.models.attributes_entity_view",
    "AttributesImmediateOutputStrategy": "tb_ce_client.models.attributes_immediate_output_strategy",
    "AttributesOutput": "tb_ce_client.models.attributes_output",
    "AttributesOutputStrategy": "tb_ce_client.models.attributes_output_strategy",
    "AttributesRuleChainOutputStrategy": "tb_ce_client.models.attributes_rule_chain_output_strategy",
    "AuditLog": "tb_ce_client.models.audit_log",
    "AuditLogId": "tb_ce_client.models.audit_log_id",
    "AuthenticationProtocol": "tb_ce_client.models.authentication_protocol",
    "Authority": "tb_ce_client.models.authority",
    "AutoVersionCreateConfig": "tb_ce_client.models.auto_version_create_config",
    "AvailableEntityKeys": "tb_ce_client.models.available_entity_keys",
    "AvailableEntityKeysV2": "tb_ce_client.models.available_entity_keys_v2",
    "AwsSnsSmsProviderConfiguration": "tb_ce_client.models.aws_sns_sms_provider_configuration",
    "AzureOpenAiChatModelConfig": "tb_ce_client.models.azure_open_ai_chat_model_config",
    "AzureOpenAiProviderConfig": "tb_ce_client.models.azure_open_ai_provider_config",
    "BackupCodeTwoFaAccountConfig": "tb_ce_client.models.backup_code_two_fa_account_config",
    "BackupCodeTwoFaProviderConfig": "tb_ce_client.models.backup_code_two_fa_provider_config",
    "BadgePosition": "tb_ce_client.models.badge_position",
    "Basic": "tb_ce_client.models.basic",
    "BooleanFilterPredicate": "tb_ce_client.models.boolean_filter_predicate",
    "BooleanOperation": "tb_ce_client.models.boolean_operation",
    "BranchInfo": "tb_ce_client.models.branch_info",
    "BulkImportColumnType": "tb_ce_client.models.bulk_import_column_type",
    "BulkImportRequest": "tb_ce_client.models.bulk_import_request",
    "BulkImportResultAsset": "tb_ce_client.models.bulk_import_result_asset",
    "BulkImportResultDevice": "tb_ce_client.models.bulk_import_result_device",
    "BulkImportResultEdge": "tb_ce_client.models.bulk_import_result_edge",
    "Button": "tb_ce_client.models.button",
    "CalculatedField": "tb_ce_client.models.calculated_field",
    "CalculatedFieldConfiguration": "tb_ce_client.models.calculated_field_configuration",
    "CalculatedFieldDebugEventFilter": "tb_ce_client.models.calculated_field_debug_event_filter",
    "CalculatedFieldId": "tb_ce_client.models.calculated_field_id",
    "CalculatedFieldInfo": "tb_ce_client.models.calculated_field_info",
    "CalculatedFieldType": "tb_ce_client.models.calculated_field_type",
    "CfArgumentDynamicSourceConfiguration": "tb_ce_client.models.cf_argument_dynamic_source_configuration",
    "ChangePasswordRequest": "tb_ce_client.models.change_password_request",
    "CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration": "tb_ce_client.models.check_pre_provisioned_devices_device_profile_provision_configuration",
    "ChecksumAlgorithm": "tb_ce_client.models.checksum_algorithm",
    "ClaimRequest": "tb_ce_client.models.claim_request",
    "ClearRule": "tb_ce_client.models.clear_rule",
    "ClientAttributesQueryingSnmpCommunicationConfig": "tb_ce_client.models.client_attributes_querying_snmp_communication_config",
    "CoapDeviceProfileTransportConfiguration": "tb_ce_client.models.coap_device_profile_transport_configuration",
    "CoapDeviceTransportConfiguration": "tb_ce_client.models.coap_device_transport_configuration",
    "CoapDeviceTypeConfiguration": "tb_ce_client.models.coap_device_type_configuration",
    "ColumnMapping": "tb_ce_client.models.column_mapping",
    "ComparisonTsValue": "tb_ce_client.models.comparison_ts_value",
    "ComplexFilterPredicate": "tb_ce_client.models.complex_filter_predicate",
    "ComplexVersionCreateRequest": "tb_ce_client.models.complex_version_create_request",
    "ComponentClusteringMode": "tb_ce_client.models.component_clustering_mode",
    "ComponentDescriptor": "tb_ce_client.models.component_descriptor",
    "ComponentDescriptorId": "tb_ce_client.models.component_descriptor_id",
    "ComponentLifecycleEvent": "tb_ce_client.models.component_lifecycle_event",
    "ComponentScope": "tb_ce_client.models.component_scope",
    "ComponentType": "tb_ce_client.models.component_type",
    "CurrentOwnerDynamicSourceConfiguration": "tb_ce_client.models.current_owner_dynamic_source_configuration",
    "CustomInterval": "tb_ce_client.models.custom_interval",
    "CustomMobilePage": "tb_ce_client.models.custom_mobile_page",
    "CustomTimeSchedule": "tb_ce_client.models.custom_time_schedule",
    "CustomTimeScheduleItem": "tb_ce_client.models.custom_time_schedule_item",
    "Customer": "tb_ce_client.models.customer",
    "CustomerExportData": "tb_ce_client.models.customer_export_data",
    "CustomerId": "tb_ce_client.models.customer_id",
    "CustomerUsersFilter": "tb_ce_client.models.customer_users_filter",
    "Dashboard": "tb_ce_client.models.dashboard",
    "DashboardExportData": "tb_ce_client.models.dashboard_export_data",
    "DashboardId": "tb_ce_client.models.dashboard_id",
    "DashboardInfo": "tb_ce_client.models.dashboard_info",
    "DashboardPage": "tb_ce_client.models.dashboard_page",
    "DataType": "tb_ce_client.models.data_type",
    "DayInterval": "tb_ce_client.models.day_interval",
    "DebugSettings": "tb_ce_client.models.debug_settings",
    "DefaultCoapDeviceTypeConfiguration": "tb_ce_client.models.default_coap_device_type_configuration",
    "DefaultDeviceConfiguration": "tb_ce_client.models.default_device_configuration",
    "DefaultDeviceProfileConfiguration": "tb_ce_client.models.default_device_profile_configuration",
    "DefaultDeviceProfileTransportConfiguration": "tb_ce_client.models.default_device_profile_transport_configuration",
    "DefaultDeviceTransportConfiguration": "tb_ce_client.models.default_device_transport_configuration",
    "DefaultMobilePage": "tb_ce_client.models.default_mobile_page",
    "DefaultPageId": "tb_ce_client.models.default_page_id",
    "DefaultRuleChainCreateRequest": "tb_ce_client.models.default_rule_chain_create_request",
    "DefaultTenantProfileConfiguration": "tb_ce_client.models.default_tenant_profile_configuration",
    "DeliveryMethodNotificationTemplate": "tb_ce_client.models.delivery_method_notification_template",
    "Device": "tb_ce_client.models.device",
    "DeviceActivityNotificationRuleTriggerConfig": "tb_ce_client.models.device_activity_notification_rule_trigger_config",
    "DeviceActivityRecipientsConfig": "tb_ce_client.models.device_activity_recipients_config",
    "DeviceConfiguration": "tb_ce_client.models.device_configuration",
    "DeviceCredentials": "tb_ce_client.models.device_credentials",
    "DeviceCredentialsId": "tb_ce_client.models.device_credentials_id",
    "DeviceCredentialsType": "tb_ce_client.models.device_credentials_type",
    "DeviceData": "tb_ce_client.models.device_data",
    "DeviceEvent": "tb_ce_client.models.device_event",
    "DeviceExportData": "tb_ce_client.models.device_export_data",
    "DeviceId": "tb_ce_client.models.device_id",
    "DeviceInfo": "tb_ce_client.models.device_info",
    "DeviceProfile": "tb_ce_client.models.device_profile",
    "DeviceProfileConfiguration": "tb_ce_client.models.device_profile_configuration",
    "DeviceProfileData": "tb_ce_client.models.device_profile_data",
    "DeviceProfileExportData": "tb_ce_client.models.device_profile_export_data",
    "DeviceProfileId": "tb_ce_client.models.device_profile_id",
    "DeviceProfileInfo": "tb_ce_client.models.device_profile_info",
    "DeviceProfileProvisionConfiguration": "tb_ce_client.models.device_profile_provision_configuration",
    "DeviceProfileProvisionType": "tb_ce_client.models.device_profile_provision_type",
    "DeviceProfileTransportConfiguration": "tb_ce_client.models.device_profile_transport_configuration",
    "DeviceProfileType": "tb_ce_client.models.device_profile_type",
    "DeviceSearchQuery": "tb_ce_client.models.device_search_query",
    "DeviceSearchQueryFilter": "tb_ce_client.models.device_search_query_filter",
    "DeviceTransportConfiguration": "tb_ce_client.models.device_transport_configuration",
    "DeviceTransportType": "tb_ce_client.models.device_transport_type",
    "DeviceTypeFilter": "tb_ce_client.models.device_type_filter",
    "Direction": "tb_ce_client.models.direction",
    "DisabledDeviceProfileProvisionConfiguration": "tb_ce_client.models.disabled_device_profile_provision_configuration",
    "Domain": "tb_ce_client.models.domain",
    "DomainId": "tb_ce_client.models.domain_id",
    "DomainInfo": "tb_ce_client.models.domain_info",
    "DummyJobConfiguration": "tb_ce_client.models.dummy_job_configuration",
    "DummyJobResult": "tb_ce_client.models.dummy_job_result",
    "DummyTaskFailure": "tb_ce_client.models.dummy_task_failure",
    "DummyTaskResult": "tb_ce_client.models.dummy_task_result",
    "DurationAlarmCondition": "tb_ce_client.models.duration_alarm_condition",
    "DynamicValueBoolean": "tb_ce_client.models.dynamic_value_boolean",
    "DynamicValueDouble": "tb_ce_client.models.dynamic_value_double",
    "DynamicValueSourceType": "tb_ce_client.models.dynamic_value_source_type",
    "DynamicValueString": "tb_ce_client.models.dynamic_value_string",
    "Edge": "tb_ce_client.models.edge",
    "EdgeCommunicationFailureNotificationRuleTriggerConfig": "tb_ce_client.models.edge_communication_failure_notification_rule_trigger_config",
    "EdgeCommunicationFailureRecipientsConfig": "tb_ce_client.models.edge_communication_failure_recipients_config",
    "EdgeConnectionNotificationRuleTriggerConfig": "tb_ce_client.models.edge_connection_notification_rule_trigger_config",
    "EdgeConnectionRecipientsConfig": "tb_ce_client.models.edge_connection_recipients_config",
    "EdgeConnectivityEvent": "tb_ce_client.models.edge_connectivity_event",
    "EdgeEvent": "tb_ce_client.models.edge_event",
    "EdgeEventActionType": "tb_ce_client.models.edge_event_action_type",
    "EdgeEventId": "tb_ce_client.models.edge_event_id",
    "EdgeEventType": "tb_ce_client.models.edge_event_type",
    "EdgeId": "tb_ce_client.models.edge_id",
    "EdgeInfo": "tb_ce_client.models.edge_info",
    "EdgeInstructions": "tb_ce_client.models.edge_instructions",
    "EdgeSearchQuery": "tb_ce_client.models.edge_search_query",
    "EdgeSearchQueryFilter": "tb_ce_client.models.edge_search_query_filter",
    "EdgeTypeFilter": "tb_ce_client.models.edge_type_filter",
    "EdqsApiMode": "tb_ce_client.models.edqs_api_mode",
    "EdqsState": "tb_ce_client.models.edqs_state",
    "EdqsSyncRequest": "tb_ce_client.models.edqs_sync_request",
    "EdqsSyncStatus": "tb_ce_client.models.edqs_sync_status",
    "EfentoCoapDeviceTypeConfiguration": "tb_ce_client.models.efento_coap_device_type_configuration",
    "EmailDeliveryMethodNotificationTemplate": "tb_ce_client.models.email_delivery_method_notification_template",
    "EmailTwoFaAccountConfig": "tb_ce_client.models.email_two_fa_account_config",
    "EmailTwoFaProviderConfig": "tb_ce_client.models.email_two_fa_provider_config",
    "EntitiesLimitNotificationRuleTriggerConfig": "tb_ce_client.models.entities_limit_notification_rule_trigger_config",
    "EntitiesLimitRecipientsConfig": "tb_ce_client.models.entities_limit_recipients_config",
    "EntityActionNotificationRuleTriggerConfig": "tb_ce_client.models.entity_action_notification_rule_trigger_config",
    "EntityActionRecipientsConfig": "tb_ce_client.models.entity_action_recipients_config",
    "EntityAggregationCalculatedFieldConfiguration": "tb_ce_client.models.entity_aggregation_calculated_field_configuration",
    "EntityCoordinates": "tb_ce_client.models.entity_coordinates",
    "EntityCountQuery": "tb_ce_client.models.entity_count_query",
    "EntityData": "tb_ce_client.models.entity_data",
    "EntityDataDiff": "tb_ce_client.models.entity_data_diff",
    "EntityDataInfo": "tb_ce_client.models.entity_data_info",
    "EntityDataPageLink": "tb_ce_client.models.entity_data_page_link",
    "EntityDataQuery": "tb_ce_client.models.entity_data_query",
    "EntityDataSortOrder": "tb_ce_client.models.entity_data_sort_order",
    "EntityExportData": "tb_ce_client.models.entity_export_data",
    "EntityFilter": "tb_ce_client.models.entity_filter",
    "EntityId": "tb_ce_client.models.entity_id",
    "EntityInfo": "tb_ce_client.models.entity_info",
    "EntityKey": "tb_ce_client.models.entity_key",
    "EntityKeyType": "tb_ce_client.models.entity_key_type",
    "EntityKeyValueType": "tb_ce_client.models.entity_key_value_type",
    "EntityListFilter": "tb_ce_client.models.entity_list_filter",
    "EntityLoadError": "tb_ce_client.models.entity_load_error",
    "EntityNameFilter": "tb_ce_client.models.entity_name_filter",
    "EntityRelation": "tb_ce_client.models.entity_relation",
    "EntityRelationInfo": "tb_ce_client.models.entity_relation_info",
    "EntityRelationsQuery": "tb_ce_client.models.entity_relations_query",
    "EntitySearchDirection": "tb_ce_client.models.entity_search_direction",
    "EntitySubtype": "tb_ce_client.models.entity_subtype",
    "EntityType": "tb_ce_client.models.entity_type",
    "EntityTypeFilter": "tb_ce_client.models.entity_type_filter",
    "EntityTypeLoadResult": "tb_ce_client.models.entity_type_load_result",
    "EntityTypeVersionCreateConfig": "tb_ce_client.models.entity_type_version_create_config",
    "EntityTypeVersionLoadConfig": "tb_ce_client.models.entity_type_version_load_config",
    "EntityTypeVersionLoadRequest": "tb_ce_client.models.entity_type_version_load_request",
    "EntityVersion": "tb_ce_client.models.entity_version",
    "EntityView": "tb_ce_client.models.entity_view",
    "EntityViewExportData": "tb_ce_client.models.entity_view_export_data",
    "EntityViewId": "tb_ce_client.models.entity_view_id",
    "EntityViewInfo": "tb_ce_client.models.entity_view_info",
    "EntityViewSearchQuery": "tb_ce_client.models.entity_view_search_query",
    "EntityViewSearchQueryFilter": "tb_ce_client.models.entity_view_search_query_filter",
    "EntityViewTypeFilter": "tb_ce_client.models.entity_view_type_filter",
    "ErrorEventFilter": "tb_ce_client.models.error_event_filter",
    "EscalatedNotificationRuleRecipientsConfig": "tb_ce_client.models.escalated_notification_rule_recipients_config",
    "EventFilter": "tb_ce_client.models.event_filter",
    "EventId": "tb_ce_client.models.event_id",
    "EventInfo": "tb_ce_client.models.event_info",
    "EventType": "tb_ce_client.models.event_type",
    "ExportableEntity": "tb_ce_client.models.exportable_entity",
    "Failure": "tb_ce_client.models.failure",
    "FeaturesInfo": "tb_ce_client.models.features_info",
    "FilterPredicateValueBoolean": "tb_ce_client.models.filter_predicate_value_boolean",
    "FilterPredicateValueDouble": "tb_ce_client.models.filter_predicate_value_double",
    "FilterPredicateValueString": "tb_ce_client.models.filter_predicate_value_string",
    "GeofencingCalculatedFieldConfiguration": "tb_ce_client.models.geofencing_calculated_field_configuration",
    "GeofencingReportStrategy": "tb_ce_client.models.geofencing_report_strategy",
    "GitHubModelsChatModelConfig": "tb_ce_client.models.git_hub_models_chat_model_config",
    "GitHubModelsProviderConfig": "tb_ce_client.models.git_hub_models_provider_config",
    "GoogleAiGeminiChatModelConfig": "tb_ce_client.models.google_ai_gemini_chat_model_config",
    "GoogleAiGeminiProviderConfig": "tb_ce_client.models.google_ai_gemini_provider_config",
    "GoogleVertexAiGeminiChatModelConfig": "tb_ce_client.models.google_vertex_ai_gemini_chat_model_config",
    "GoogleVertexAiGeminiProviderConfig": "tb_ce_client.models.google_vertex_ai_gemini_provider_config",
    "HasIdObject": "tb_ce_client.models.has_id_object",
    "HomeDashboard": "tb_ce_client.models.home_dashboard",
    "HomeDashboardInfo": "tb_ce_client.models.home_dashboard_info",
    "HourInterval": "tb_ce_client.models.hour_interval",
    "Job": "tb_ce_client.models.job",
    "JobConfiguration": "tb_ce_client.models.job_configuration",
    "JobId": "tb_ce_client.models.job_id",
    "JobResult": "tb_ce_client.models.job_result",
    "JobStatus": "tb_ce_client.models.job_status",
    "JobType": "tb_ce_client.models.job_type",
    "JsonTransportPayloadConfiguration": "tb_ce_client.models.json_transport_payload_configuration",
    "JwtPair": "tb_ce_client.models.jwt_pair",
    "JwtSettings": "tb_ce_client.models.jwt_settings",
    "KeyFilter": "tb_ce_client.models.key_filter",
    "KeyFilterPredicate": "tb_ce_client.models.key_filter_predicate",
    "KeyInfo": "tb_ce_client.models.key_info",
    "KeySample": "tb_ce_client.models.key_sample",
    "LastVisitedDashboardInfo": "tb_ce_client.models.last_visited_dashboard_info",
    "LifeCycleEventFilter": "tb_ce_client.models.life_cycle_event_filter",
    "LimitedApi": "tb_ce_client.models.limited_api",
    "LinkType": "tb_ce_client.models.link_type",
    "Login401Response": "tb_ce_client.models.login401_response",
    "LoginMobileInfo": "tb_ce_client.models.login_mobile_info",
    "LoginRequest": "tb_ce_client.models.login_request",
    "LoginResponse": "tb_ce_client.models.login_response",
    "LwM2MBootstrapServerCredential": "tb_ce_client.models.lw_m2_m_bootstrap_server_credential",
    "LwM2MServerSecurityConfigDefault": "tb_ce_client.models.lw_m2_m_server_security_config_default",
    "LwM2mInstance": "tb_ce_client.models.lw_m2m_instance",
    "LwM2mObject": "tb_ce_client.models.lw_m2m_object",
    "LwM2mResourceObserve": "tb_ce_client.models.lw_m2m_resource_observe",
    "LwM2mVersion": "tb_ce_client.models.lw_m2m_version",
    "Lwm2mDeviceProfileTransportConfiguration": "tb_ce_client.models.lwm2m_device_profile_transport_configuration",
    "Lwm2mDeviceTransportConfiguration": "tb_ce_client.models.lwm2m_device_transport_configuration",
    "MapperType": "tb_ce_client.models.mapper_type",
    "Mapping": "tb_ce_client.models.mapping",
    "MicrosoftTeamsDeliveryMethodNotificationTemplate": "tb_ce_client.models.microsoft_teams_delivery_method_notification_template",
    "MicrosoftTeamsNotificationTargetConfig": "tb_ce_client.models.microsoft_teams_notification_target_config",
    "MistralAiChatModelConfig": "tb_ce_client.models.mistral_ai_chat_model_config",
    "MistralAiProviderConfig": "tb_ce_client.models.mistral_ai_provider_config",
    "MobileApp": "tb_ce_client.models.mobile_app",
    "MobileAppBundle": "tb_ce_client.models.mobile_app_bundle",
    "MobileAppBundleId": "tb_ce_client.models.mobile_app_bundle_id",
    "MobileAppBundleInfo": "tb_ce_client.models.mobile_app_bundle_info",
    "MobileAppDeliveryMethodNotificationTemplate": "tb_ce_client.models.mobile_app_delivery_method_notification_template",
    "MobileAppId": "tb_ce_client.models.mobile_app_id",
    "MobileAppNotificationDeliveryMethodConfig": "tb_ce_client.models.mobile_app_notification_delivery_method_config",
    "MobileAppStatus": "tb_ce_client.models.mobile_app_status",
    "MobileAppVersionInfo": "tb_ce_client.models.mobile_app_version_info",
    "MobileLayoutConfig": "tb_ce_client.models.mobile_layout_config",
    "MobilePage": "tb_ce_client.models.mobile_page",
    "MobilePageType": "tb_ce_client.models.mobile_page_type",
    "MobileSessionInfo": "tb_ce_client.models.mobile_session_info",
    "ModelNone": "tb_ce_client.models.model_none",
    "MonthInterval": "tb_ce_client.models.month_interval",
    "MqttDeviceProfileTransportConfiguration": "tb_ce_client.models.mqtt_device_profile_transport_configuration",
    "MqttDeviceTransportConfiguration": "tb_ce_client.models.mqtt_device_transport_configuration",
    "NameConflictPolicy": "tb_ce_client.models.name_conflict_policy",
    "NewPlatformVersionNotificationRuleTriggerConfig": "tb_ce_client.models.new_platform_version_notification_rule_trigger_config",
    "NewPlatformVersionRecipientsConfig": "tb_ce_client.models.new_platform_version_recipients_config",
    "NoDataFilterPredicate": "tb_ce_client.models.no_data_filter_predicate",
    "NoSecLwM2MBootstrapServerCredential": "tb_ce_client.models.no_sec_lw_m2_m_bootstrap_server_credential",
    "NodeConnectionInfo": "tb_ce_client.models.node_connection_info",
    "Notification": "tb_ce_client.models.notification",
    "NotificationDeliveryMethod": "tb_ce_client.models.notification_delivery_method",
    "NotificationDeliveryMethodConfig": "tb_ce_client.models.notification_delivery_method_config",
    "NotificationId": "tb_ce_client.models.notification_id",
    "NotificationInfo": "tb_ce_client.models.notification_info",
    "NotificationPref": "tb_ce_client.models.notification_pref",
    "NotificationRequest": "tb_ce_client.models.notification_request",
    "NotificationRequestConfig": "tb_ce_client.models.notification_request_config",
    "NotificationRequestId": "tb_ce_client.models.notification_request_id",
    "NotificationRequestInfo": "tb_ce_client.models.notification_request_info",
    "NotificationRequestPreview": "tb_ce_client.models.notification_request_preview",
    "NotificationRequestStats": "tb_ce_client.models.notification_request_stats",
    "NotificationRequestStatus": "tb_ce_client.models.notification_request_status",
    "NotificationRule": "tb_ce_client.models.notification_rule",
    "NotificationRuleConfig": "tb_ce_client.models.notification_rule_config",
    "NotificationRuleExportData": "tb_ce_client.models.notification_rule_export_data",
    "NotificationRuleId": "tb_ce_client.models.notification_rule_id",
    "NotificationRuleInfo": "tb_ce_client.models.notification_rule_info",
    "NotificationRuleRecipientsConfig": "tb_ce_client.models.notification_rule_recipients_config",
    "NotificationRuleTriggerConfig": "tb_ce_client.models.notification_rule_trigger_config",
    "NotificationRuleTriggerType": "tb_ce_client.models.notification_rule_trigger_type",
    "NotificationSettings": "tb_ce_client.models.notification_settings",
    "NotificationStatus": "tb_ce_client.models.notification_status",
    "NotificationTarget": "tb_ce_client.models.notification_target",
    "NotificationTargetConfig": "tb_ce_client.models.notification_target_config",
    "NotificationTargetExportData": "tb_ce_client.models.notification_target_export_data",
    "NotificationTargetId": "tb_ce_client.models.notification_target_id",
    "NotificationTemplate": "tb_ce_client.models.notification_template",
    "NotificationTemplateConfig": "tb_ce_client.models.notification_template_config",
    "NotificationTemplateExportData": "tb_ce_client.models.notification_template_export_data",
    "NotificationTemplateId": "tb_ce_client.models.notification_template_id",
    "NotificationType": "tb_ce_client.models.notification_type",
    "NumericFilterPredicate": "tb_ce_client.models.numeric_filter_predicate",
    "NumericOperation": "tb_ce_client.models.numeric_operation",
    "OAuth2BasicMapperConfig": "tb_ce_client.models.o_auth2_basic_mapper_config",
    "OAuth2Client": "tb_ce_client.models.o_auth2_client",
    "OAuth2ClientId": "tb_ce_client.models.o_auth2_client_id",
    "OAuth2ClientInfo": "tb_ce_client.models.o_auth2_client_info",
    "OAuth2ClientLoginInfo": "tb_ce_client.models.o_auth2_client_login_info",
    "OAuth2ClientRegistrationTemplate": "tb_ce_client.models.o_auth2_client_registration_template",
    "OAuth2ClientRegistrationTemplateId": "tb_ce_client.models.o_auth2_client_registration_template_id",
    "OAuth2CustomMapperConfig": "tb_ce_client.models.o_auth2_custom_mapper_config",
    "OAuth2MapperConfig": "tb_ce_client.models.o_auth2_mapper_config",
    "ObjectAttributes": "tb_ce_client.models.object_attributes",
    "ObjectType": "tb_ce_client.models.object_type",
    "OllamaAuth": "tb_ce_client.models.ollama_auth",
    "OllamaChatModelConfig": "tb_ce_client.models.ollama_chat_model_config",
    "OllamaProviderConfig": "tb_ce_client.models.ollama_provider_config",
    "OpenAiChatModelConfig": "tb_ce_client.models.open_ai_chat_model_config",
    "OpenAiProviderConfig": "tb_ce_client.models.open_ai_provider_config",
    "OriginatorEntityOwnerUsersFilter": "tb_ce_client.models.originator_entity_owner_users_filter",
    "OtaPackage": "tb_ce_client.models.ota_package",
    "OtaPackageExportData": "tb_ce_client.models.ota_package_export_data",
    "OtaPackageId": "tb_ce_client.models.ota_package_id",
    "OtaPackageInfo": "tb_ce_client.models.ota_package_info",
    "OtaPackageType": "tb_ce_client.models.ota_package_type",
    "OtherConfiguration": "tb_ce_client.models.other_configuration",
    "Output": "tb_ce_client.models.output",
    "PSKLwM2MBootstrapServerCredential": "tb_ce_client.models.psklw_m2_m_bootstrap_server_credential",
    "PageDataAiModel": "tb_ce_client.models.page_data_ai_model",
    "PageDataAlarmCommentInfo": "tb_ce_client.models.page_data_alarm_comment_info",
    "PageDataAlarmData": "tb_ce_client.models.page_data_alarm_data",
    "PageDataAlarmInfo": "tb_ce_client.models.page_data_alarm_info",
    "PageDataAlarmRuleDefinition": "tb_ce_client.models.page_data_alarm_rule_definition",
    "PageDataAlarmRuleDefinitionInfo": "tb_ce_client.models.page_data_alarm_rule_definition_info",
    "PageDataApiKeyInfo": "tb_ce_client.models.page_data_api_key_info",
    "PageDataAsset": "tb_ce_client.models.page_data_asset",
    "PageDataAssetInfo": "tb_ce_client.models.page_data_asset_info",
    "PageDataAssetProfile": "tb_ce_client.models.page_data_asset_profile",
    "PageDataAssetProfileInfo": "tb_ce_client.models.page_data_asset_profile_info",
    "PageDataAuditLog": "tb_ce_client.models.page_data_audit_log",
    "PageDataCalculatedField": "tb_ce_client.models.page_data_calculated_field",
    "PageDataCalculatedFieldInfo": "tb_ce_client.models.page_data_calculated_field_info",
    "PageDataCustomer": "tb_ce_client.models.page_data_customer",
    "PageDataDashboardInfo": "tb_ce_client.models.page_data_dashboard_info",
    "PageDataDevice": "tb_ce_client.models.page_data_device",
    "PageDataDeviceInfo": "tb_ce_client.models.page_data_device_info",
    "PageDataDeviceProfile": "tb_ce_client.models.page_data_device_profile",
    "PageDataDeviceProfileInfo": "tb_ce_client.models.page_data_device_profile_info",
    "PageDataDomainInfo": "tb_ce_client.models.page_data_domain_info",
    "PageDataEdge": "tb_ce_client.models.page_data_edge",
    "PageDataEdgeEvent": "tb_ce_client.models.page_data_edge_event",
    "PageDataEdgeInfo": "tb_ce_client.models.page_data_edge_info",
    "PageDataEntityData": "tb_ce_client.models.page_data_entity_data",
    "PageDataEntityInfo": "tb_ce_client.models.page_data_entity_info",
    "PageDataEntitySubtype": "tb_ce_client.models.page_data_entity_subtype",
    "PageDataEntityVersion": "tb_ce_client.models.page_data_entity_version",
    "PageDataEntityView": "tb_ce_client.models.page_data_entity_view",
    "PageDataEntityViewInfo": "tb_ce_client.models.page_data_entity_view_info",
    "PageDataEventInfo": "tb_ce_client.models.page_data_event_info",
    "PageDataJob": "tb_ce_client.models.page_data_job",
    "PageDataMobileApp": "tb_ce_client.models.page_data_mobile_app",
    "PageDataMobileAppBundleInfo": "tb_ce_client.models.page_data_mobile_app_bundle_info",
    "PageDataNotification": "tb_ce_client.models.page_data_notification",
    "PageDataNotificationRequestInfo": "tb_ce_client.models.page_data_notification_request_info",
    "PageDataNotificationRuleInfo": "tb_ce_client.models.page_data_notification_rule_info",
    "PageDataNotificationTarget": "tb_ce_client.models.page_data_notification_target",
    "PageDataNotificationTemplate": "tb_ce_client.models.page_data_notification_template",
    "PageDataOAuth2ClientInfo": "tb_ce_client.models.page_data_o_auth2_client_info",
    "PageDataOtaPackageInfo": "tb_ce_client.models.page_data_ota_package_info",
    "PageDataQueue": "tb_ce_client.models.page_data_queue",
    "PageDataQueueStats": "tb_ce_client.models.page_data_queue_stats",
    "PageDataRuleChain": "tb_ce_client.models.page_data_rule_chain",
    "PageDataString": "tb_ce_client.models.page_data_string",
    "PageDataTbResourceInfo": "tb_ce_client.models.page_data_tb_resource_info",
    "PageDataTenant": "tb_ce_client.models.page_data_tenant",
    "PageDataTenantInfo": "tb_ce_client.models.page_data_tenant_info",
    "PageDataTenantProfile": "tb_ce_client.models.page_data_tenant_profile",
    "PageDataUser": "tb_ce_client.models.page_data_user",
    "PageDataUserEmailInfo": "tb_ce_client.models.page_data_user_email_info",
    "PageDataWidgetTypeInfo": "tb_ce_client.models.page_data_widget_type_info",
    "PageDataWidgetsBundle": "tb_ce_client.models.page_data_widgets_bundle",
    "PlatformTwoFaSettings": "tb_ce_client.models.platform_two_fa_settings",
    "PlatformType": "tb_ce_client.models.platform_type",
    "PlatformUsersNotificationTargetConfig": "tb_ce_client.models.platform_users_notification_target_config",
    "PowerMode": "tb_ce_client.models.power_mode",
    "PowerSavingConfiguration": "tb_ce_client.models.power_saving_configuration",
    "PrivacyProtocol": "tb_ce_client.models.privacy_protocol",
    "ProcessingStrategy": "tb_ce_client.models.processing_strategy",
    "ProcessingStrategyType": "tb_ce_client.models.processing_strategy_type",
    "PropagationCalculatedFieldConfiguration": "tb_ce_client.models.propagation_calculated_field_configuration",
    "ProtoTransportPayloadConfiguration": "tb_ce_client.models.proto_transport_payload_configuration",
    "QRCodeConfig": "tb_ce_client.models.qr_code_config",
    "QrCodeSettings": "tb_ce_client.models.qr_code_settings",
    "QrCodeSettingsId": "tb_ce_client.models.qr_code_settings_id",
    "QuarterInterval": "tb_ce_client.models.quarter_interval",
    "Queue": "tb_ce_client.models.queue",
    "QueueId": "tb_ce_client.models.queue_id",
    "QueueStats": "tb_ce_client.models.queue_stats",
    "QueueStatsId": "tb_ce_client.models.queue_stats_id",
    "RPKLwM2MBootstrapServerCredential": "tb_ce_client.models.rpklw_m2_m_bootstrap_server_credential",
    "RateLimitsNotificationRuleTriggerConfig": "tb_ce_client.models.rate_limits_notification_rule_trigger_config",
    "RateLimitsRecipientsConfig": "tb_ce_client.models.rate_limits_recipients_config",
    "ReferencedEntityKey": "tb_ce_client.models.referenced_entity_key",
    "RefreshTokenRequest": "tb_ce_client.models.refresh_token_request",
    "RelatedEntitiesAggregationCalculatedFieldConfiguration": "tb_ce_client.models.related_entities_aggregation_calculated_field_configuration",
    "RelationEntityTypeFilter": "tb_ce_client.models.relation_entity_type_filter",
    "RelationPathLevel": "tb_ce_client.models.relation_path_level",
    "RelationPathQueryDynamicSourceConfiguration": "tb_ce_client.models.relation_path_query_dynamic_source_configuration",
    "RelationTypeGroup": "tb_ce_client.models.relation_type_group",
    "RelationsQueryFilter": "tb_ce_client.models.relations_query_filter",
    "RelationsSearchParameters": "tb_ce_client.models.relations_search_parameters",
    "RepeatingAlarmCondition": "tb_ce_client.models.repeating_alarm_condition",
    "RepositoryAuthMethod": "tb_ce_client.models.repository_auth_method",
    "RepositorySettings": "tb_ce_client.models.repository_settings",
    "RepositorySettingsInfo": "tb_ce_client.models.repository_settings_info",
    "ResetPasswordEmailRequest": "tb_ce_client.models.reset_password_email_request",
    "ResetPasswordRequest": "tb_ce_client.models.reset_password_request",
    "ResourceExportData": "tb_ce_client.models.resource_export_data",
    "ResourceShortageRecipientsConfig": "tb_ce_client.models.resource_shortage_recipients_config",
    "ResourceSubType": "tb_ce_client.models.resource_sub_type",
    "ResourceType": "tb_ce_client.models.resource_type",
    "ResourcesShortageNotificationRuleTriggerConfig": "tb_ce_client.models.resources_shortage_notification_rule_trigger_config",
    "Rpc": "tb_ce_client.models.rpc",
    "RpcId": "tb_ce_client.models.rpc_id",
    "RpcStatus": "tb_ce_client.models.rpc_status",
    "RuleChain": "tb_ce_client.models.rule_chain",
    "RuleChainConnectionInfo": "tb_ce_client.models.rule_chain_connection_info",
    "RuleChainData": "tb_ce_client.models.rule_chain_data",
    "RuleChainDebugEventFilter": "tb_ce_client.models.rule_chain_debug_event_filter",
    "RuleChainExportData": "tb_ce_client.models.rule_chain_export_data",
    "RuleChainId": "tb_ce_client.models.rule_chain_id",
    "RuleChainImportResult": "tb_ce_client.models.rule_chain_import_result",
    "RuleChainMetaData": "tb_ce_client.models.rule_chain_meta_data",
    "RuleChainNote": "tb_ce_client.models.rule_chain_note",
    "RuleChainOutputLabelsUsage": "tb_ce_client.models.rule_chain_output_labels_usage",
    "RuleChainType": "tb_ce_client.models.rule_chain_type",
    "RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig": "tb_ce_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config",
    "RuleEngineComponentLifecycleEventRecipientsConfig": "tb_ce_client.models.rule_engine_component_lifecycle_event_recipients_config",
    "RuleNode": "tb_ce_client.models.rule_node",
    "RuleNodeDebugEventFilter": "tb_ce_client.models.rule_node_debug_event_filter",
    "RuleNodeId": "tb_ce_client.models.rule_node_id",
    "SaveDeviceWithCredentialsRequest": "tb_ce_client.models.save_device_with_credentials_request",
    "SaveOtaPackageInfoRequest": "tb_ce_client.models.save_ota_package_info_request",
    "ScriptCalculatedFieldConfiguration": "tb_ce_client.models.script_calculated_field_configuration",
    "ScriptLanguage": "tb_ce_client.models.script_language",
    "SecuritySettings": "tb_ce_client.models.security_settings",
    "SharedAttributesSettingSnmpCommunicationConfig": "tb_ce_client.models.shared_attributes_setting_snmp_communication_config",
    "ShortCustomerInfo": "tb_ce_client.models.short_customer_info",
    "SimpleAlarmCondition": "tb_ce_client.models.simple_alarm_condition",
    "SimpleAlarmConditionExpression": "tb_ce_client.models.simple_alarm_condition_expression",
    "SimpleCalculatedFieldConfiguration": "tb_ce_client.models.simple_calculated_field_configuration",
    "SingleEntityFilter": "tb_ce_client.models.single_entity_filter",
    "SingleEntityVersionCreateRequest": "tb_ce_client.models.single_entity_version_create_request",
    "SingleEntityVersionLoadRequest": "tb_ce_client.models.single_entity_version_load_request",
    "SlackConversation": "tb_ce_client.models.slack_conversation",
    "SlackConversationType": "tb_ce_client.models.slack_conversation_type",
    "SlackDeliveryMethodNotificationTemplate": "tb_ce_client.models.slack_delivery_method_notification_template",
    "SlackNotificationDeliveryMethodConfig": "tb_ce_client.models.slack_notification_delivery_method_config",
    "SlackNotificationTargetConfig": "tb_ce_client.models.slack_notification_target_config",
    "SmppBindType": "tb_ce_client.models.smpp_bind_type",
    "SmppSmsProviderConfiguration": "tb_ce_client.models.smpp_sms_provider_configuration",
    "SmsDeliveryMethodNotificationTemplate": "tb_ce_client.models.sms_delivery_method_notification_template",
    "SmsProviderConfiguration": "tb_ce_client.models.sms_provider_configuration",
    "SmsTwoFaAccountConfig": "tb_ce_client.models.sms_two_fa_account_config",
    "SmsTwoFaProviderConfig": "tb_ce_client.models.sms_two_fa_provider_config",
    "SnmpCommunicationConfig": "tb_ce_client.models.snmp_communication_config",
    "SnmpCommunicationSpec": "tb_ce_client.models.snmp_communication_spec",
    "SnmpDeviceProfileTransportConfiguration": "tb_ce_client.models.snmp_device_profile_transport_configuration",
    "SnmpDeviceTransportConfiguration": "tb_ce_client.models.snmp_device_transport_configuration",
    "SnmpMapping": "tb_ce_client.models.snmp_mapping",
    "SnmpProtocolVersion": "tb_ce_client.models.snmp_protocol_version",
    "SpecificTimeSchedule": "tb_ce_client.models.specific_time_schedule",
    "StarredDashboardInfo": "tb_ce_client.models.starred_dashboard_info",
    "StatisticsEventFilter": "tb_ce_client.models.statistics_event_filter",
    "StoreInfo": "tb_ce_client.models.store_info",
    "StringFilterPredicate": "tb_ce_client.models.string_filter_predicate",
    "StringOperation": "tb_ce_client.models.string_operation",
    "SubmitStrategy": "tb_ce_client.models.submit_strategy",
    "SubmitStrategyType": "tb_ce_client.models.submit_strategy_type",
    "Success": "tb_ce_client.models.success",
    "SyncStrategy": "tb_ce_client.models.sync_strategy",
    "SystemAdministratorsFilter": "tb_ce_client.models.system_administrators_filter",
    "SystemInfo": "tb_ce_client.models.system_info",
    "SystemInfoData": "tb_ce_client.models.system_info_data",
    "TaskProcessingFailureNotificationRuleTriggerConfig": "tb_ce_client.models.task_processing_failure_notification_rule_trigger_config",
    "TaskProcessingFailureRecipientsConfig": "tb_ce_client.models.task_processing_failure_recipients_config",
    "TaskResult": "tb_ce_client.models.task_result",
    "TbChatRequest": "tb_ce_client.models.tb_chat_request",
    "TbChatResponse": "tb_ce_client.models.tb_chat_response",
    "TbContent": "tb_ce_client.models.tb_content",
    "TbImageDeleteResult": "tb_ce_client.models.tb_image_delete_result",
    "TbResource": "tb_ce_client.models.tb_resource",
    "TbResourceDeleteResult": "tb_ce_client.models.tb_resource_delete_result",
    "TbResourceExportData": "tb_ce_client.models.tb_resource_export_data",
    "TbResourceId": "tb_ce_client.models.tb_resource_id",
    "TbResourceInfo": "tb_ce_client.models.tb_resource_info",
    "TbTextContent": "tb_ce_client.models.tb_text_content",
    "TbUserMessage": "tb_ce_client.models.tb_user_message",
    "TbelAlarmConditionExpression": "tb_ce_client.models.tbel_alarm_condition_expression",
    "TelemetryEntityView": "tb_ce_client.models.telemetry_entity_view",
    "TelemetryMappingConfiguration": "tb_ce_client.models.telemetry_mapping_configuration",
    "TelemetryObserveStrategy": "tb_ce_client.models.telemetry_observe_strategy",
    "TelemetryQueryingSnmpCommunicationConfig": "tb_ce_client.models.telemetry_querying_snmp_communication_config",
    "Tenant": "tb_ce_client.models.tenant",
    "TenantAdministratorsFilter": "tb_ce_client.models.tenant_administrators_filter",
    "TenantId": "tb_ce_client.models.tenant_id",
    "TenantInfo": "tb_ce_client.models.tenant_info",
    "TenantNameStrategyType": "tb_ce_client.models.tenant_name_strategy_type",
    "TenantProfile": "tb_ce_client.models.tenant_profile",
    "TenantProfileConfiguration": "tb_ce_client.models.tenant_profile_configuration",
    "TenantProfileData": "tb_ce_client.models.tenant_profile_data",
    "TenantProfileId": "tb_ce_client.models.tenant_profile_id",
    "TenantProfileQueueConfiguration": "tb_ce_client.models.tenant_profile_queue_configuration",
    "TestSmsRequest": "tb_ce_client.models.test_sms_request",
    "ThingsboardCredentialsExpiredResponse": "tb_ce_client.models.thingsboard_credentials_expired_response",
    "ThingsboardErrorCode": "tb_ce_client.models.thingsboard_error_code",
    "ThingsboardErrorResponse": "tb_ce_client.models.thingsboard_error_response",
    "TimeSeriesImmediateOutputStrategy": "tb_ce_client.models.time_series_immediate_output_strategy",
    "TimeSeriesOutput": "tb_ce_client.models.time_series_output",
    "TimeSeriesOutputStrategy": "tb_ce_client.models.time_series_output_strategy",
    "TimeSeriesRuleChainOutputStrategy": "tb_ce_client.models.time_series_rule_chain_output_strategy",
    "TimeUnit": "tb_ce_client.models.time_unit",
    "ToCoreEdqsRequest": "tb_ce_client.models.to_core_edqs_request",
    "ToDeviceRpcRequestSnmpCommunicationConfig": "tb_ce_client.models.to_device_rpc_request_snmp_communication_config",
    "ToServerRpcRequestSnmpCommunicationConfig": "tb_ce_client.models.to_server_rpc_request_snmp_communication_config",
    "Token": "tb_ce_client.models.token",
    "TotpTwoFaAccountConfig": "tb_ce_client.models.totp_two_fa_account_config",
    "TotpTwoFaProviderConfig": "tb_ce_client.models.totp_two_fa_provider_config",
    "TransportPayloadTypeConfiguration": "tb_ce_client.models.transport_payload_type_configuration",
    "TrendzSettings": "tb_ce_client.models.trendz_settings",
    "TsData": "tb_ce_client.models.ts_data",
    "TsValue": "tb_ce_client.models.ts_value",
    "TwilioSmsProviderConfiguration": "tb_ce_client.models.twilio_sms_provider_configuration",
    "TwoFaAccountConfig": "tb_ce_client.models.two_fa_account_config",
    "TwoFaAccountConfigUpdateRequest": "tb_ce_client.models.two_fa_account_config_update_request",
    "TwoFaProviderConfig": "tb_ce_client.models.two_fa_provider_config",
    "TwoFaProviderInfo": "tb_ce_client.models.two_fa_provider_info",
    "TwoFaProviderType": "tb_ce_client.models.two_fa_provider_type",
    "UniquifyStrategy": "tb_ce_client.models.uniquify_strategy",
    "UpdateMessage": "tb_ce_client.models.update_message",
    "UsageInfo": "tb_ce_client.models.usage_info",
    "User": "tb_ce_client.models.user",
    "UserActivationLink": "tb_ce_client.models.user_activation_link",
    "UserDashboardsInfo": "tb_ce_client.models.user_dashboards_info",
    "UserEmailInfo": "tb_ce_client.models.user_email_info",
    "UserId": "tb_ce_client.models.user_id",
    "UserListFilter": "tb_ce_client.models.user_list_filter",
    "UserMobileInfo": "tb_ce_client.models.user_mobile_info",
    "UserNotificationSettings": "tb_ce_client.models.user_notification_settings",
    "UserPasswordPolicy": "tb_ce_client.models.user_password_policy",
    "UsersFilter": "tb_ce_client.models.users_filter",
    "VersionCreateConfig": "tb_ce_client.models.version_create_config",
    "VersionCreateRequest": "tb_ce_client.models.version_create_request",
    "VersionCreateRequestType": "tb_ce_client.models.version_create_request_type",
    "VersionCreationResult": "tb_ce_client.models.version_creation_result",
    "VersionLoadConfig": "tb_ce_client.models.version_load_config",
    "VersionLoadRequest": "tb_ce_client.models.version_load_request",
    "VersionLoadRequestType": "tb_ce_client.models.version_load_request_type",
    "VersionLoadResult": "tb_ce_client.models.version_load_result",
    "VersionedEntityInfo": "tb_ce_client.models.versioned_entity_info",
    "Watermark": "tb_ce_client.models.watermark",
    "WebDeliveryMethodNotificationTemplate": "tb_ce_client.models.web_delivery_method_notification_template",
    "WebViewPage": "tb_ce_client.models.web_view_page",
    "WeekInterval": "tb_ce_client.models.week_interval",
    "WeekSunSatInterval": "tb_ce_client.models.week_sun_sat_interval",
    "WidgetBundleInfo": "tb_ce_client.models.widget_bundle_info",
    "WidgetType": "tb_ce_client.models.widget_type",
    "WidgetTypeDetails": "tb_ce_client.models.widget_type_details",
    "WidgetTypeExportData": "tb_ce_client.models.widget_type_export_data",
    "WidgetTypeId": "tb_ce_client.models.widget_type_id",
    "WidgetTypeInfo": "tb_ce_client.models.widget_type_info",
    "WidgetsBundle": "tb_ce_client.models.widgets_bundle",
    "WidgetsBundleExportData": "tb_ce_client.models.widgets_bundle_export_data",
    "WidgetsBundleId": "tb_ce_client.models.widgets_bundle_id",
    "X509CertificateChainProvisionConfiguration": "tb_ce_client.models.x509_certificate_chain_provision_configuration",
    "X509LwM2MBootstrapServerCredential": "tb_ce_client.models.x509_lw_m2_m_bootstrap_server_credential",
    "YearInterval": "tb_ce_client.models.year_interval",
    "ZoneGroupConfiguration": "tb_ce_client.models.zone_group_configuration",
}

def __getattr__(name: str):
    if name in _MODEL_CLASSES:
        module = importlib.import_module(_MODEL_CLASSES[name])
        cls = getattr(module, name)
        globals()[name] = cls  # Cache for subsequent access
        return cls
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return list(_MODEL_CLASSES.keys())
