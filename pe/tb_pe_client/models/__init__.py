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
    "Aggregation",
    "AggregationConfiguration",
    "AggregationParams",
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
    "AlarmFilterConfig",
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
    "AlarmTableComponent",
    "AliasEntityId",
    "AliasEntityType",
    "AllUsersFilter",
    "AllowCreateNewDevicesDeviceProfileProvisionConfiguration",
    "AllowedPermissionsInfo",
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
    "AxisPosition",
    "AzureOpenAiChatModelConfig",
    "AzureOpenAiProviderConfig",
    "BackupCodeTwoFaAccountConfig",
    "BackupCodeTwoFaProviderConfig",
    "BadgePosition",
    "BarSeriesSettings",
    "BaseReadTsKvQuery",
    "Basic",
    "BlobEntityId",
    "BlobEntityInfo",
    "BlobEntityWithCustomerInfo",
    "BooleanFilterPredicate",
    "BooleanOperation",
    "BorderLength",
    "BorderType",
    "BranchInfo",
    "BulkImportColumnType",
    "BulkImportRequest",
    "BulkImportResultAsset",
    "BulkImportResultDevice",
    "BulkImportResultEdge",
    "Button",
    "CMAssigneeType",
    "CMItemLinkType",
    "CMItemType",
    "CMScope",
    "CalculatedField",
    "CalculatedFieldConfiguration",
    "CalculatedFieldDebugEventFilter",
    "CalculatedFieldId",
    "CalculatedFieldInfo",
    "CalculatedFieldType",
    "CaptchaParams",
    "CellSettings",
    "CfArgumentDynamicSourceConfiguration",
    "CfReprocessingJobConfiguration",
    "CfReprocessingJobResult",
    "CfReprocessingTaskFailure",
    "CfReprocessingTaskResult",
    "CfReprocessingValidationResult",
    "ChangePasswordRequest",
    "ChartFillSettings",
    "ChartFillSettingsGradient",
    "ChartFillType",
    "ChartLabelPosition",
    "ChartLineType",
    "ChartShape",
    "ChatType",
    "CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration",
    "ChecksumAlgorithm",
    "ClaimRequest",
    "ClearRule",
    "ClientAttributesQueryingSnmpCommunicationConfig",
    "CoapDeviceProfileTransportConfiguration",
    "CoapDeviceTransportConfiguration",
    "CoapDeviceTypeConfiguration",
    "ColorRange",
    "ColumnMapping",
    "ColumnSettings",
    "ComparisonDuration",
    "ComparisonTsValue",
    "ComplexFilterPredicate",
    "ComplexOperation",
    "ComplexVersionCreateRequest",
    "ComponentClusteringMode",
    "ComponentDescriptor",
    "ComponentDescriptorId",
    "ComponentLifecycleEvent",
    "ComponentScope",
    "ComponentType",
    "ContactBasedObject",
    "Converter",
    "ConverterExportData",
    "ConverterId",
    "ConverterType",
    "ConvertersInfo",
    "CreateReportRequest",
    "CsvReportTemplateConfig",
    "CurrentOwnerDynamicSourceConfiguration",
    "CustomInterval",
    "CustomMenu",
    "CustomMenuConfig",
    "CustomMenuDeleteResult",
    "CustomMenuId",
    "CustomMenuInfo",
    "CustomMenuItem",
    "CustomMobilePage",
    "CustomTimeSchedule",
    "CustomTimeScheduleItem",
    "Customer",
    "CustomerExportData",
    "CustomerId",
    "CustomerInfo",
    "CustomerUsersFilter",
    "Dashboard",
    "DashboardComponent",
    "DashboardExportData",
    "DashboardId",
    "DashboardInfo",
    "DashboardPage",
    "DashboardReportConfig",
    "DataKey",
    "DataKeyComparisonSettings",
    "DataKeySettings",
    "DataKeySettingsType",
    "DataSource",
    "DataSourceType",
    "DataType",
    "DayInterval",
    "DebugConverterEventFilter",
    "DebugIntegrationEventFilter",
    "DebugSettings",
    "DefaultCoapDeviceTypeConfiguration",
    "DefaultDashboardParams",
    "DefaultDataKeySettings",
    "DefaultDeviceConfiguration",
    "DefaultDeviceProfileConfiguration",
    "DefaultDeviceProfileTransportConfiguration",
    "DefaultDeviceTransportConfiguration",
    "DefaultMenuItem",
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
    "DeviceGroupOtaPackage",
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
    "DividerComponent",
    "Domain",
    "DomainId",
    "DomainInfo",
    "DoughnutLayout",
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
    "EnterpriseCaptchaParams",
    "EntitiesByGroupNameFilter",
    "EntitiesLimitNotificationRuleTriggerConfig",
    "EntitiesLimitRecipientsConfig",
    "Entity",
    "EntityActionNotificationRuleTriggerConfig",
    "EntityActionRecipientsConfig",
    "EntityAggregationCalculatedFieldConfiguration",
    "EntityAlias",
    "EntityCoordinates",
    "EntityCountQuery",
    "EntityData",
    "EntityDataDiff",
    "EntityDataInfo",
    "EntityDataPageLink",
    "EntityDataQuery",
    "EntityDataSortOrder",
    "EntityExportData",
    "EntityExportSettings",
    "EntityFilter",
    "EntityGroup",
    "EntityGroupExportData",
    "EntityGroupFilter",
    "EntityGroupId",
    "EntityGroupInfo",
    "EntityGroupListFilter",
    "EntityGroupNameFilter",
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
    "EntityTableComponent",
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
    "ErrorComponent",
    "ErrorComponentAllOfException",
    "ErrorComponentAllOfExceptionCause",
    "ErrorComponentAllOfExceptionCauseStackTrace",
    "ErrorEventFilter",
    "EscalatedNotificationRuleRecipientsConfig",
    "EventFilter",
    "EventId",
    "EventInfo",
    "EventType",
    "ExportableEntity",
    "Failure",
    "Favicon",
    "FeaturesInfo",
    "Filter",
    "FilterPredicateValueBoolean",
    "FilterPredicateValueDouble",
    "FilterPredicateValueString",
    "FixedTimeWindow",
    "Font",
    "FontStyle",
    "FontWeight",
    "GeofencingCalculatedFieldConfiguration",
    "GeofencingReportStrategy",
    "GitHubModelsChatModelConfig",
    "GitHubModelsProviderConfig",
    "GoogleAiGeminiChatModelConfig",
    "GoogleAiGeminiProviderConfig",
    "GoogleVertexAiGeminiChatModelConfig",
    "GoogleVertexAiGeminiProviderConfig",
    "GroupPermission",
    "GroupPermissionId",
    "GroupPermissionInfo",
    "HasIdObject",
    "HeaderFooter",
    "Heading",
    "HeadingComponent",
    "History",
    "HomeDashboard",
    "HomeDashboardInfo",
    "HomeDashboardParams",
    "HomeMenuItem",
    "HomeMenuItemType",
    "HourInterval",
    "ImageAlignment",
    "ImageComponent",
    "ImageSourceType",
    "ImageWidthType",
    "Insets",
    "Integration",
    "IntegrationConvertersInfo",
    "IntegrationExportData",
    "IntegrationId",
    "IntegrationInfo",
    "IntegrationLifecycleEventNotificationRuleTriggerConfig",
    "IntegrationLifecycleEventRecipientsConfig",
    "IntegrationType",
    "Interval",
    "IntervalType",
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
    "LatestChartComponent",
    "LegendConfig",
    "LegendPosition",
    "LicenseUsageInfo",
    "LifeCycleEventFilter",
    "LimitedApi",
    "LineSeriesSettings",
    "LineSeriesStepType",
    "LinkType",
    "Login401Response",
    "LoginMobileInfo",
    "LoginRequest",
    "LoginResponse",
    "LoginWhiteLabelingParams",
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
    "MenuItem",
    "MenuItemType",
    "MergedGroupPermissionInfo",
    "MergedGroupTypePermissionInfo",
    "MergedUserPermissions",
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
    "MobileRedirectParams",
    "MobileSelfRegistrationParams",
    "MobileSessionInfo",
    "Model",
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
    "Operation",
    "OriginatorEntityOwnerUsersFilter",
    "OtaPackage",
    "OtaPackageExportData",
    "OtaPackageId",
    "OtaPackageInfo",
    "OtaPackageType",
    "OtherConfiguration",
    "Output",
    "PSKLwM2MBootstrapServerCredential",
    "PageBreakComponent",
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
    "PageDataBlobEntityWithCustomerInfo",
    "PageDataCalculatedField",
    "PageDataCalculatedFieldInfo",
    "PageDataContactBasedObject",
    "PageDataConverter",
    "PageDataCustomMenuInfo",
    "PageDataCustomer",
    "PageDataCustomerInfo",
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
    "PageDataEntityGroupInfo",
    "PageDataEntityInfo",
    "PageDataEntitySubtype",
    "PageDataEntityVersion",
    "PageDataEntityView",
    "PageDataEntityViewInfo",
    "PageDataEventInfo",
    "PageDataIntegration",
    "PageDataIntegrationInfo",
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
    "PageDataReport",
    "PageDataReportInfo",
    "PageDataReportTemplateInfo",
    "PageDataRole",
    "PageDataRuleChain",
    "PageDataScheduledReportInfo",
    "PageDataSchedulerEventInfo",
    "PageDataSchedulerEventWithCustomerInfo",
    "PageDataSecretInfo",
    "PageDataShortEntityView",
    "PageDataString",
    "PageDataTbResourceInfo",
    "PageDataTenant",
    "PageDataTenantInfo",
    "PageDataTenantProfile",
    "PageDataTrendzViewConfigLite",
    "PageDataUser",
    "PageDataUserEmailInfo",
    "PageDataUserInfo",
    "PageDataWidgetTypeInfo",
    "PageDataWidgetsBundle",
    "PageOrientation",
    "PageSize",
    "Palette",
    "PaletteSettings",
    "PdfReportTemplateConfig",
    "PieChartLabelPosition",
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
    "QuickTimeInterval",
    "RPKLwM2MBootstrapServerCredential",
    "RateLimitsNotificationRuleTriggerConfig",
    "RateLimitsRecipientsConfig",
    "RawDataEventFilter",
    "ReadTsKvQueryResult",
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
    "Report",
    "ReportBarChartSettings",
    "ReportBarChartWithLabelsSettings",
    "ReportComponent",
    "ReportComponentSubType",
    "ReportComponentType",
    "ReportDoughnutChartSettings",
    "ReportId",
    "ReportInfo",
    "ReportJobConfiguration",
    "ReportJobResult",
    "ReportLatestChartSettings",
    "ReportPieChartSettings",
    "ReportRangeChartSettings",
    "ReportRequest",
    "ReportTaskResult",
    "ReportTemplate",
    "ReportTemplateConfig",
    "ReportTemplateExportData",
    "ReportTemplateId",
    "ReportTemplateInfo",
    "ReportTemplateType",
    "ReportTimeSeriesChartSettings",
    "RepositoryAuthMethod",
    "RepositorySettings",
    "RepositorySettingsInfo",
    "ResetPasswordEmailRequest",
    "ResetPasswordRequest",
    "Resource",
    "ResourceExportData",
    "ResourceShortageRecipientsConfig",
    "ResourceSubType",
    "ResourceType",
    "ResourcesShortageNotificationRuleTriggerConfig",
    "RichTextComponent",
    "Role",
    "RoleExportData",
    "RoleId",
    "RoleType",
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
    "RuleChainOutputLabelsUsage",
    "RuleChainType",
    "RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig",
    "RuleEngineComponentLifecycleEventRecipientsConfig",
    "RuleNode",
    "RuleNodeDebugEventFilter",
    "RuleNodeId",
    "SaveDeviceWithCredentialsRequest",
    "SaveOtaPackageInfoRequest",
    "ScheduledReportInfo",
    "SchedulerEvent",
    "SchedulerEventExportData",
    "SchedulerEventFilter",
    "SchedulerEventId",
    "SchedulerEventInfo",
    "SchedulerEventWithCustomerInfo",
    "ScriptCalculatedFieldConfiguration",
    "ScriptLanguage",
    "Secret",
    "SecretId",
    "SecretInfo",
    "SecretType",
    "SecuritySettings",
    "SelfRegistrationParams",
    "SelfRegistrationType",
    "ShareGroupRequest",
    "SharedAttributesSettingSnmpCommunicationConfig",
    "ShortCustomerInfo",
    "ShortEntityView",
    "SignUpField",
    "SignUpFieldId",
    "SignUpRequest",
    "SignUpResult",
    "SignUpSelfRegistrationParams",
    "SimpleAlarmCondition",
    "SimpleAlarmConditionExpression",
    "SimpleCalculatedFieldConfiguration",
    "SimpleEntity",
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
    "SolutionData",
    "SolutionExportRequest",
    "SolutionExportResponse",
    "SolutionImportResult",
    "SolutionInstallResponse",
    "SolutionStep",
    "SolutionTemplateLevel",
    "SolutionValidationResult",
    "SpecificTimeSchedule",
    "SplitViewComponent",
    "StarredDashboardInfo",
    "StateEntityFilter",
    "StateEntityOwnerFilter",
    "StatisticsEventFilter",
    "StoreInfo",
    "StringFilterPredicate",
    "StringOperation",
    "SubReportComponent",
    "SubmitStrategy",
    "SubmitStrategyType",
    "Success",
    "SyncStrategy",
    "SystemAdministratorsFilter",
    "SystemInfo",
    "SystemInfoData",
    "TableSortDirection",
    "TableSortOrder",
    "TaskProcessingFailureNotificationRuleTriggerConfig",
    "TaskProcessingFailureRecipientsConfig",
    "TaskResult",
    "TbChatRequest",
    "TbChatResponse",
    "TbContent",
    "TbImageDeleteResult",
    "TbReportFormat",
    "TbResource",
    "TbResourceDeleteResult",
    "TbResourceExportData",
    "TbResourceId",
    "TbResourceInfo",
    "TbSecretDeleteResult",
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
    "TenantSolutionTemplateDetails",
    "TenantSolutionTemplateInfo",
    "TenantSolutionTemplateInstructions",
    "TestSmsRequest",
    "TextAlignment",
    "ThingsboardCredentialsExpiredResponse",
    "ThingsboardErrorCode",
    "ThingsboardErrorResponse",
    "ThresholdLabelPosition",
    "TimeSeriesChartBarWidth",
    "TimeSeriesChartBarWidthSettings",
    "TimeSeriesChartGridSettings",
    "TimeSeriesChartKeySettings",
    "TimeSeriesChartNoAggregationBarWidthSettings",
    "TimeSeriesChartNoAggregationBarWidthStrategy",
    "TimeSeriesChartSeriesType",
    "TimeSeriesChartStateSettings",
    "TimeSeriesChartStateSourceType",
    "TimeSeriesChartThreshold",
    "TimeSeriesChartXAxisSettings",
    "TimeSeriesChartYAxisSettings",
    "TimeSeriesImmediateOutputStrategy",
    "TimeSeriesOutput",
    "TimeSeriesOutputStrategy",
    "TimeSeriesRuleChainOutputStrategy",
    "TimeUnit",
    "TimeWindowConfiguration",
    "TimeseriesChartComponent",
    "TimeseriesTableComponent",
    "ToCoreEdqsRequest",
    "ToDeviceRpcRequestSnmpCommunicationConfig",
    "ToServerRpcRequestSnmpCommunicationConfig",
    "Token",
    "TotpTwoFaAccountConfig",
    "TotpTwoFaProviderConfig",
    "TranslationInfo",
    "TransportPayloadTypeConfiguration",
    "TrendzConfiguration",
    "TrendzHealthcheckResult",
    "TrendzSummary",
    "TrendzSynchronizationResult",
    "TrendzSynchronizationResultType",
    "TrendzSynchronizationStatus",
    "TrendzUsage",
    "TrendzViewConfig",
    "TrendzViewConfigLite",
    "TsData",
    "TsKvEntry",
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
    "UserExportData",
    "UserGroupListFilter",
    "UserId",
    "UserInfo",
    "UserListFilter",
    "UserMobileInfo",
    "UserNotificationSettings",
    "UserPasswordPolicy",
    "UserRoleFilter",
    "UsersFilter",
    "V2CaptchaParams",
    "V3CaptchaParams",
    "ValueSourceType",
    "Vendor",
    "VersionCreateConfig",
    "VersionCreateRequest",
    "VersionCreateRequestType",
    "VersionCreationResult",
    "VersionLoadConfig",
    "VersionLoadRequest",
    "VersionLoadRequestType",
    "VersionLoadResult",
    "VersionedEntityInfo",
    "VerticalAlignment",
    "Watermark",
    "WebDeliveryMethodNotificationTemplate",
    "WebSelfRegistrationParams",
    "WebViewPage",
    "WeekInterval",
    "WeekSunSatInterval",
    "WhiteLabeling",
    "WhiteLabelingParams",
    "WhiteLabelingType",
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
    from tb_pe_client.models.account_two_fa_settings import AccountTwoFaSettings
    from tb_pe_client.models.action import Action
    from tb_pe_client.models.action_status import ActionStatus
    from tb_pe_client.models.action_type import ActionType
    from tb_pe_client.models.activate_user_request import ActivateUserRequest
    from tb_pe_client.models.admin_settings import AdminSettings
    from tb_pe_client.models.admin_settings_id import AdminSettingsId
    from tb_pe_client.models.affected_tenant_administrators_filter import AffectedTenantAdministratorsFilter
    from tb_pe_client.models.affected_user_filter import AffectedUserFilter
    from tb_pe_client.models.agg_function import AggFunction
    from tb_pe_client.models.agg_function_input import AggFunctionInput
    from tb_pe_client.models.agg_input import AggInput
    from tb_pe_client.models.agg_interval import AggInterval
    from tb_pe_client.models.agg_key_input import AggKeyInput
    from tb_pe_client.models.agg_metric import AggMetric
    from tb_pe_client.models.aggregation import Aggregation
    from tb_pe_client.models.aggregation_configuration import AggregationConfiguration
    from tb_pe_client.models.aggregation_params import AggregationParams
    from tb_pe_client.models.ai_chat_model_config import AiChatModelConfig
    from tb_pe_client.models.ai_model import AiModel
    from tb_pe_client.models.ai_model_config import AiModelConfig
    from tb_pe_client.models.ai_model_export_data import AiModelExportData
    from tb_pe_client.models.ai_model_id import AiModelId
    from tb_pe_client.models.ai_model_type import AiModelType
    from tb_pe_client.models.alarm import Alarm
    from tb_pe_client.models.alarm_action import AlarmAction
    from tb_pe_client.models.alarm_assignee import AlarmAssignee
    from tb_pe_client.models.alarm_assignment_notification_rule_trigger_config import AlarmAssignmentNotificationRuleTriggerConfig
    from tb_pe_client.models.alarm_assignment_recipients_config import AlarmAssignmentRecipientsConfig
    from tb_pe_client.models.alarm_calculated_field_configuration import AlarmCalculatedFieldConfiguration
    from tb_pe_client.models.alarm_comment import AlarmComment
    from tb_pe_client.models.alarm_comment_id import AlarmCommentId
    from tb_pe_client.models.alarm_comment_info import AlarmCommentInfo
    from tb_pe_client.models.alarm_comment_notification_rule_trigger_config import AlarmCommentNotificationRuleTriggerConfig
    from tb_pe_client.models.alarm_comment_recipients_config import AlarmCommentRecipientsConfig
    from tb_pe_client.models.alarm_comment_type import AlarmCommentType
    from tb_pe_client.models.alarm_condition import AlarmCondition
    from tb_pe_client.models.alarm_condition_expression import AlarmConditionExpression
    from tb_pe_client.models.alarm_condition_filter import AlarmConditionFilter
    from tb_pe_client.models.alarm_condition_value_alarm_schedule import AlarmConditionValueAlarmSchedule
    from tb_pe_client.models.alarm_condition_value_boolean import AlarmConditionValueBoolean
    from tb_pe_client.models.alarm_condition_value_double import AlarmConditionValueDouble
    from tb_pe_client.models.alarm_condition_value_integer import AlarmConditionValueInteger
    from tb_pe_client.models.alarm_condition_value_long import AlarmConditionValueLong
    from tb_pe_client.models.alarm_condition_value_string import AlarmConditionValueString
    from tb_pe_client.models.alarm_count_query import AlarmCountQuery
    from tb_pe_client.models.alarm_data import AlarmData
    from tb_pe_client.models.alarm_data_page_link import AlarmDataPageLink
    from tb_pe_client.models.alarm_data_query import AlarmDataQuery
    from tb_pe_client.models.alarm_filter_config import AlarmFilterConfig
    from tb_pe_client.models.alarm_id import AlarmId
    from tb_pe_client.models.alarm_info import AlarmInfo
    from tb_pe_client.models.alarm_notification_rule_trigger_config import AlarmNotificationRuleTriggerConfig
    from tb_pe_client.models.alarm_rule import AlarmRule
    from tb_pe_client.models.alarm_rule_boolean_filter_predicate import AlarmRuleBooleanFilterPredicate
    from tb_pe_client.models.alarm_rule_boolean_operation import AlarmRuleBooleanOperation
    from tb_pe_client.models.alarm_rule_complex_filter_predicate import AlarmRuleComplexFilterPredicate
    from tb_pe_client.models.alarm_rule_complex_operation import AlarmRuleComplexOperation
    from tb_pe_client.models.alarm_rule_definition import AlarmRuleDefinition
    from tb_pe_client.models.alarm_rule_definition_info import AlarmRuleDefinitionInfo
    from tb_pe_client.models.alarm_rule_key_filter_predicate import AlarmRuleKeyFilterPredicate
    from tb_pe_client.models.alarm_rule_numeric_filter_predicate import AlarmRuleNumericFilterPredicate
    from tb_pe_client.models.alarm_rule_numeric_operation import AlarmRuleNumericOperation
    from tb_pe_client.models.alarm_rule_string_filter_predicate import AlarmRuleStringFilterPredicate
    from tb_pe_client.models.alarm_rule_string_operation import AlarmRuleStringOperation
    from tb_pe_client.models.alarm_schedule import AlarmSchedule
    from tb_pe_client.models.alarm_search_status import AlarmSearchStatus
    from tb_pe_client.models.alarm_severity import AlarmSeverity
    from tb_pe_client.models.alarm_status import AlarmStatus
    from tb_pe_client.models.alarm_table_component import AlarmTableComponent
    from tb_pe_client.models.alias_entity_id import AliasEntityId
    from tb_pe_client.models.alias_entity_type import AliasEntityType
    from tb_pe_client.models.all_users_filter import AllUsersFilter
    from tb_pe_client.models.allow_create_new_devices_device_profile_provision_configuration import AllowCreateNewDevicesDeviceProfileProvisionConfiguration
    from tb_pe_client.models.allowed_permissions_info import AllowedPermissionsInfo
    from tb_pe_client.models.amazon_bedrock_chat_model_config import AmazonBedrockChatModelConfig
    from tb_pe_client.models.amazon_bedrock_provider_config import AmazonBedrockProviderConfig
    from tb_pe_client.models.anthropic_chat_model_config import AnthropicChatModelConfig
    from tb_pe_client.models.anthropic_provider_config import AnthropicProviderConfig
    from tb_pe_client.models.any_time_schedule import AnyTimeSchedule
    from tb_pe_client.models.api_feature import ApiFeature
    from tb_pe_client.models.api_key import ApiKey
    from tb_pe_client.models.api_key_id import ApiKeyId
    from tb_pe_client.models.api_key_info import ApiKeyInfo
    from tb_pe_client.models.api_usage_limit_notification_rule_trigger_config import ApiUsageLimitNotificationRuleTriggerConfig
    from tb_pe_client.models.api_usage_limit_recipients_config import ApiUsageLimitRecipientsConfig
    from tb_pe_client.models.api_usage_state_filter import ApiUsageStateFilter
    from tb_pe_client.models.api_usage_state_id import ApiUsageStateId
    from tb_pe_client.models.api_usage_state_value import ApiUsageStateValue
    from tb_pe_client.models.argument import Argument
    from tb_pe_client.models.argument_type import ArgumentType
    from tb_pe_client.models.asset import Asset
    from tb_pe_client.models.asset_export_data import AssetExportData
    from tb_pe_client.models.asset_id import AssetId
    from tb_pe_client.models.asset_info import AssetInfo
    from tb_pe_client.models.asset_profile import AssetProfile
    from tb_pe_client.models.asset_profile_export_data import AssetProfileExportData
    from tb_pe_client.models.asset_profile_id import AssetProfileId
    from tb_pe_client.models.asset_profile_info import AssetProfileInfo
    from tb_pe_client.models.asset_search_query import AssetSearchQuery
    from tb_pe_client.models.asset_search_query_filter import AssetSearchQueryFilter
    from tb_pe_client.models.asset_type_filter import AssetTypeFilter
    from tb_pe_client.models.attribute_data import AttributeData
    from tb_pe_client.models.attribute_export_data import AttributeExportData
    from tb_pe_client.models.attribute_scope import AttributeScope
    from tb_pe_client.models.attributes_entity_view import AttributesEntityView
    from tb_pe_client.models.attributes_immediate_output_strategy import AttributesImmediateOutputStrategy
    from tb_pe_client.models.attributes_output import AttributesOutput
    from tb_pe_client.models.attributes_output_strategy import AttributesOutputStrategy
    from tb_pe_client.models.attributes_rule_chain_output_strategy import AttributesRuleChainOutputStrategy
    from tb_pe_client.models.audit_log import AuditLog
    from tb_pe_client.models.audit_log_id import AuditLogId
    from tb_pe_client.models.authentication_protocol import AuthenticationProtocol
    from tb_pe_client.models.authority import Authority
    from tb_pe_client.models.auto_version_create_config import AutoVersionCreateConfig
    from tb_pe_client.models.available_entity_keys import AvailableEntityKeys
    from tb_pe_client.models.available_entity_keys_v2 import AvailableEntityKeysV2
    from tb_pe_client.models.aws_sns_sms_provider_configuration import AwsSnsSmsProviderConfiguration
    from tb_pe_client.models.axis_position import AxisPosition
    from tb_pe_client.models.azure_open_ai_chat_model_config import AzureOpenAiChatModelConfig
    from tb_pe_client.models.azure_open_ai_provider_config import AzureOpenAiProviderConfig
    from tb_pe_client.models.backup_code_two_fa_account_config import BackupCodeTwoFaAccountConfig
    from tb_pe_client.models.backup_code_two_fa_provider_config import BackupCodeTwoFaProviderConfig
    from tb_pe_client.models.badge_position import BadgePosition
    from tb_pe_client.models.bar_series_settings import BarSeriesSettings
    from tb_pe_client.models.base_read_ts_kv_query import BaseReadTsKvQuery
    from tb_pe_client.models.basic import Basic
    from tb_pe_client.models.blob_entity_id import BlobEntityId
    from tb_pe_client.models.blob_entity_info import BlobEntityInfo
    from tb_pe_client.models.blob_entity_with_customer_info import BlobEntityWithCustomerInfo
    from tb_pe_client.models.boolean_filter_predicate import BooleanFilterPredicate
    from tb_pe_client.models.boolean_operation import BooleanOperation
    from tb_pe_client.models.border_length import BorderLength
    from tb_pe_client.models.border_type import BorderType
    from tb_pe_client.models.branch_info import BranchInfo
    from tb_pe_client.models.bulk_import_column_type import BulkImportColumnType
    from tb_pe_client.models.bulk_import_request import BulkImportRequest
    from tb_pe_client.models.bulk_import_result_asset import BulkImportResultAsset
    from tb_pe_client.models.bulk_import_result_device import BulkImportResultDevice
    from tb_pe_client.models.bulk_import_result_edge import BulkImportResultEdge
    from tb_pe_client.models.button import Button
    from tb_pe_client.models.cm_assignee_type import CMAssigneeType
    from tb_pe_client.models.cm_item_link_type import CMItemLinkType
    from tb_pe_client.models.cm_item_type import CMItemType
    from tb_pe_client.models.cm_scope import CMScope
    from tb_pe_client.models.calculated_field import CalculatedField
    from tb_pe_client.models.calculated_field_configuration import CalculatedFieldConfiguration
    from tb_pe_client.models.calculated_field_debug_event_filter import CalculatedFieldDebugEventFilter
    from tb_pe_client.models.calculated_field_id import CalculatedFieldId
    from tb_pe_client.models.calculated_field_info import CalculatedFieldInfo
    from tb_pe_client.models.calculated_field_type import CalculatedFieldType
    from tb_pe_client.models.captcha_params import CaptchaParams
    from tb_pe_client.models.cell_settings import CellSettings
    from tb_pe_client.models.cf_argument_dynamic_source_configuration import CfArgumentDynamicSourceConfiguration
    from tb_pe_client.models.cf_reprocessing_job_configuration import CfReprocessingJobConfiguration
    from tb_pe_client.models.cf_reprocessing_job_result import CfReprocessingJobResult
    from tb_pe_client.models.cf_reprocessing_task_failure import CfReprocessingTaskFailure
    from tb_pe_client.models.cf_reprocessing_task_result import CfReprocessingTaskResult
    from tb_pe_client.models.cf_reprocessing_validation_result import CfReprocessingValidationResult
    from tb_pe_client.models.change_password_request import ChangePasswordRequest
    from tb_pe_client.models.chart_fill_settings import ChartFillSettings
    from tb_pe_client.models.chart_fill_settings_gradient import ChartFillSettingsGradient
    from tb_pe_client.models.chart_fill_type import ChartFillType
    from tb_pe_client.models.chart_label_position import ChartLabelPosition
    from tb_pe_client.models.chart_line_type import ChartLineType
    from tb_pe_client.models.chart_shape import ChartShape
    from tb_pe_client.models.chat_type import ChatType
    from tb_pe_client.models.check_pre_provisioned_devices_device_profile_provision_configuration import CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration
    from tb_pe_client.models.checksum_algorithm import ChecksumAlgorithm
    from tb_pe_client.models.claim_request import ClaimRequest
    from tb_pe_client.models.clear_rule import ClearRule
    from tb_pe_client.models.client_attributes_querying_snmp_communication_config import ClientAttributesQueryingSnmpCommunicationConfig
    from tb_pe_client.models.coap_device_profile_transport_configuration import CoapDeviceProfileTransportConfiguration
    from tb_pe_client.models.coap_device_transport_configuration import CoapDeviceTransportConfiguration
    from tb_pe_client.models.coap_device_type_configuration import CoapDeviceTypeConfiguration
    from tb_pe_client.models.color_range import ColorRange
    from tb_pe_client.models.column_mapping import ColumnMapping
    from tb_pe_client.models.column_settings import ColumnSettings
    from tb_pe_client.models.comparison_duration import ComparisonDuration
    from tb_pe_client.models.comparison_ts_value import ComparisonTsValue
    from tb_pe_client.models.complex_filter_predicate import ComplexFilterPredicate
    from tb_pe_client.models.complex_operation import ComplexOperation
    from tb_pe_client.models.complex_version_create_request import ComplexVersionCreateRequest
    from tb_pe_client.models.component_clustering_mode import ComponentClusteringMode
    from tb_pe_client.models.component_descriptor import ComponentDescriptor
    from tb_pe_client.models.component_descriptor_id import ComponentDescriptorId
    from tb_pe_client.models.component_lifecycle_event import ComponentLifecycleEvent
    from tb_pe_client.models.component_scope import ComponentScope
    from tb_pe_client.models.component_type import ComponentType
    from tb_pe_client.models.contact_based_object import ContactBasedObject
    from tb_pe_client.models.converter import Converter
    from tb_pe_client.models.converter_export_data import ConverterExportData
    from tb_pe_client.models.converter_id import ConverterId
    from tb_pe_client.models.converter_type import ConverterType
    from tb_pe_client.models.converters_info import ConvertersInfo
    from tb_pe_client.models.create_report_request import CreateReportRequest
    from tb_pe_client.models.csv_report_template_config import CsvReportTemplateConfig
    from tb_pe_client.models.current_owner_dynamic_source_configuration import CurrentOwnerDynamicSourceConfiguration
    from tb_pe_client.models.custom_interval import CustomInterval
    from tb_pe_client.models.custom_menu import CustomMenu
    from tb_pe_client.models.custom_menu_config import CustomMenuConfig
    from tb_pe_client.models.custom_menu_delete_result import CustomMenuDeleteResult
    from tb_pe_client.models.custom_menu_id import CustomMenuId
    from tb_pe_client.models.custom_menu_info import CustomMenuInfo
    from tb_pe_client.models.custom_menu_item import CustomMenuItem
    from tb_pe_client.models.custom_mobile_page import CustomMobilePage
    from tb_pe_client.models.custom_time_schedule import CustomTimeSchedule
    from tb_pe_client.models.custom_time_schedule_item import CustomTimeScheduleItem
    from tb_pe_client.models.customer import Customer
    from tb_pe_client.models.customer_export_data import CustomerExportData
    from tb_pe_client.models.customer_id import CustomerId
    from tb_pe_client.models.customer_info import CustomerInfo
    from tb_pe_client.models.customer_users_filter import CustomerUsersFilter
    from tb_pe_client.models.dashboard import Dashboard
    from tb_pe_client.models.dashboard_component import DashboardComponent
    from tb_pe_client.models.dashboard_export_data import DashboardExportData
    from tb_pe_client.models.dashboard_id import DashboardId
    from tb_pe_client.models.dashboard_info import DashboardInfo
    from tb_pe_client.models.dashboard_page import DashboardPage
    from tb_pe_client.models.dashboard_report_config import DashboardReportConfig
    from tb_pe_client.models.data_key import DataKey
    from tb_pe_client.models.data_key_comparison_settings import DataKeyComparisonSettings
    from tb_pe_client.models.data_key_settings import DataKeySettings
    from tb_pe_client.models.data_key_settings_type import DataKeySettingsType
    from tb_pe_client.models.data_source import DataSource
    from tb_pe_client.models.data_source_type import DataSourceType
    from tb_pe_client.models.data_type import DataType
    from tb_pe_client.models.day_interval import DayInterval
    from tb_pe_client.models.debug_converter_event_filter import DebugConverterEventFilter
    from tb_pe_client.models.debug_integration_event_filter import DebugIntegrationEventFilter
    from tb_pe_client.models.debug_settings import DebugSettings
    from tb_pe_client.models.default_coap_device_type_configuration import DefaultCoapDeviceTypeConfiguration
    from tb_pe_client.models.default_dashboard_params import DefaultDashboardParams
    from tb_pe_client.models.default_data_key_settings import DefaultDataKeySettings
    from tb_pe_client.models.default_device_configuration import DefaultDeviceConfiguration
    from tb_pe_client.models.default_device_profile_configuration import DefaultDeviceProfileConfiguration
    from tb_pe_client.models.default_device_profile_transport_configuration import DefaultDeviceProfileTransportConfiguration
    from tb_pe_client.models.default_device_transport_configuration import DefaultDeviceTransportConfiguration
    from tb_pe_client.models.default_menu_item import DefaultMenuItem
    from tb_pe_client.models.default_mobile_page import DefaultMobilePage
    from tb_pe_client.models.default_page_id import DefaultPageId
    from tb_pe_client.models.default_rule_chain_create_request import DefaultRuleChainCreateRequest
    from tb_pe_client.models.default_tenant_profile_configuration import DefaultTenantProfileConfiguration
    from tb_pe_client.models.delivery_method_notification_template import DeliveryMethodNotificationTemplate
    from tb_pe_client.models.device import Device
    from tb_pe_client.models.device_activity_notification_rule_trigger_config import DeviceActivityNotificationRuleTriggerConfig
    from tb_pe_client.models.device_activity_recipients_config import DeviceActivityRecipientsConfig
    from tb_pe_client.models.device_configuration import DeviceConfiguration
    from tb_pe_client.models.device_credentials import DeviceCredentials
    from tb_pe_client.models.device_credentials_id import DeviceCredentialsId
    from tb_pe_client.models.device_credentials_type import DeviceCredentialsType
    from tb_pe_client.models.device_data import DeviceData
    from tb_pe_client.models.device_event import DeviceEvent
    from tb_pe_client.models.device_export_data import DeviceExportData
    from tb_pe_client.models.device_group_ota_package import DeviceGroupOtaPackage
    from tb_pe_client.models.device_id import DeviceId
    from tb_pe_client.models.device_info import DeviceInfo
    from tb_pe_client.models.device_profile import DeviceProfile
    from tb_pe_client.models.device_profile_configuration import DeviceProfileConfiguration
    from tb_pe_client.models.device_profile_data import DeviceProfileData
    from tb_pe_client.models.device_profile_export_data import DeviceProfileExportData
    from tb_pe_client.models.device_profile_id import DeviceProfileId
    from tb_pe_client.models.device_profile_info import DeviceProfileInfo
    from tb_pe_client.models.device_profile_provision_configuration import DeviceProfileProvisionConfiguration
    from tb_pe_client.models.device_profile_provision_type import DeviceProfileProvisionType
    from tb_pe_client.models.device_profile_transport_configuration import DeviceProfileTransportConfiguration
    from tb_pe_client.models.device_profile_type import DeviceProfileType
    from tb_pe_client.models.device_search_query import DeviceSearchQuery
    from tb_pe_client.models.device_search_query_filter import DeviceSearchQueryFilter
    from tb_pe_client.models.device_transport_configuration import DeviceTransportConfiguration
    from tb_pe_client.models.device_transport_type import DeviceTransportType
    from tb_pe_client.models.device_type_filter import DeviceTypeFilter
    from tb_pe_client.models.direction import Direction
    from tb_pe_client.models.disabled_device_profile_provision_configuration import DisabledDeviceProfileProvisionConfiguration
    from tb_pe_client.models.divider_component import DividerComponent
    from tb_pe_client.models.domain import Domain
    from tb_pe_client.models.domain_id import DomainId
    from tb_pe_client.models.domain_info import DomainInfo
    from tb_pe_client.models.doughnut_layout import DoughnutLayout
    from tb_pe_client.models.dummy_job_configuration import DummyJobConfiguration
    from tb_pe_client.models.dummy_job_result import DummyJobResult
    from tb_pe_client.models.dummy_task_failure import DummyTaskFailure
    from tb_pe_client.models.dummy_task_result import DummyTaskResult
    from tb_pe_client.models.duration_alarm_condition import DurationAlarmCondition
    from tb_pe_client.models.dynamic_value_boolean import DynamicValueBoolean
    from tb_pe_client.models.dynamic_value_double import DynamicValueDouble
    from tb_pe_client.models.dynamic_value_source_type import DynamicValueSourceType
    from tb_pe_client.models.dynamic_value_string import DynamicValueString
    from tb_pe_client.models.edge import Edge
    from tb_pe_client.models.edge_communication_failure_notification_rule_trigger_config import EdgeCommunicationFailureNotificationRuleTriggerConfig
    from tb_pe_client.models.edge_communication_failure_recipients_config import EdgeCommunicationFailureRecipientsConfig
    from tb_pe_client.models.edge_connection_notification_rule_trigger_config import EdgeConnectionNotificationRuleTriggerConfig
    from tb_pe_client.models.edge_connection_recipients_config import EdgeConnectionRecipientsConfig
    from tb_pe_client.models.edge_connectivity_event import EdgeConnectivityEvent
    from tb_pe_client.models.edge_event import EdgeEvent
    from tb_pe_client.models.edge_event_action_type import EdgeEventActionType
    from tb_pe_client.models.edge_event_id import EdgeEventId
    from tb_pe_client.models.edge_event_type import EdgeEventType
    from tb_pe_client.models.edge_id import EdgeId
    from tb_pe_client.models.edge_info import EdgeInfo
    from tb_pe_client.models.edge_instructions import EdgeInstructions
    from tb_pe_client.models.edge_search_query import EdgeSearchQuery
    from tb_pe_client.models.edge_search_query_filter import EdgeSearchQueryFilter
    from tb_pe_client.models.edge_type_filter import EdgeTypeFilter
    from tb_pe_client.models.edqs_api_mode import EdqsApiMode
    from tb_pe_client.models.edqs_state import EdqsState
    from tb_pe_client.models.edqs_sync_request import EdqsSyncRequest
    from tb_pe_client.models.edqs_sync_status import EdqsSyncStatus
    from tb_pe_client.models.efento_coap_device_type_configuration import EfentoCoapDeviceTypeConfiguration
    from tb_pe_client.models.email_delivery_method_notification_template import EmailDeliveryMethodNotificationTemplate
    from tb_pe_client.models.email_two_fa_account_config import EmailTwoFaAccountConfig
    from tb_pe_client.models.email_two_fa_provider_config import EmailTwoFaProviderConfig
    from tb_pe_client.models.enterprise_captcha_params import EnterpriseCaptchaParams
    from tb_pe_client.models.entities_by_group_name_filter import EntitiesByGroupNameFilter
    from tb_pe_client.models.entities_limit_notification_rule_trigger_config import EntitiesLimitNotificationRuleTriggerConfig
    from tb_pe_client.models.entities_limit_recipients_config import EntitiesLimitRecipientsConfig
    from tb_pe_client.models.entity import Entity
    from tb_pe_client.models.entity_action_notification_rule_trigger_config import EntityActionNotificationRuleTriggerConfig
    from tb_pe_client.models.entity_action_recipients_config import EntityActionRecipientsConfig
    from tb_pe_client.models.entity_aggregation_calculated_field_configuration import EntityAggregationCalculatedFieldConfiguration
    from tb_pe_client.models.entity_alias import EntityAlias
    from tb_pe_client.models.entity_coordinates import EntityCoordinates
    from tb_pe_client.models.entity_count_query import EntityCountQuery
    from tb_pe_client.models.entity_data import EntityData
    from tb_pe_client.models.entity_data_diff import EntityDataDiff
    from tb_pe_client.models.entity_data_info import EntityDataInfo
    from tb_pe_client.models.entity_data_page_link import EntityDataPageLink
    from tb_pe_client.models.entity_data_query import EntityDataQuery
    from tb_pe_client.models.entity_data_sort_order import EntityDataSortOrder
    from tb_pe_client.models.entity_export_data import EntityExportData
    from tb_pe_client.models.entity_export_settings import EntityExportSettings
    from tb_pe_client.models.entity_filter import EntityFilter
    from tb_pe_client.models.entity_group import EntityGroup
    from tb_pe_client.models.entity_group_export_data import EntityGroupExportData
    from tb_pe_client.models.entity_group_filter import EntityGroupFilter
    from tb_pe_client.models.entity_group_id import EntityGroupId
    from tb_pe_client.models.entity_group_info import EntityGroupInfo
    from tb_pe_client.models.entity_group_list_filter import EntityGroupListFilter
    from tb_pe_client.models.entity_group_name_filter import EntityGroupNameFilter
    from tb_pe_client.models.entity_id import EntityId
    from tb_pe_client.models.entity_info import EntityInfo
    from tb_pe_client.models.entity_key import EntityKey
    from tb_pe_client.models.entity_key_type import EntityKeyType
    from tb_pe_client.models.entity_key_value_type import EntityKeyValueType
    from tb_pe_client.models.entity_list_filter import EntityListFilter
    from tb_pe_client.models.entity_load_error import EntityLoadError
    from tb_pe_client.models.entity_name_filter import EntityNameFilter
    from tb_pe_client.models.entity_relation import EntityRelation
    from tb_pe_client.models.entity_relation_info import EntityRelationInfo
    from tb_pe_client.models.entity_relations_query import EntityRelationsQuery
    from tb_pe_client.models.entity_search_direction import EntitySearchDirection
    from tb_pe_client.models.entity_subtype import EntitySubtype
    from tb_pe_client.models.entity_table_component import EntityTableComponent
    from tb_pe_client.models.entity_type import EntityType
    from tb_pe_client.models.entity_type_filter import EntityTypeFilter
    from tb_pe_client.models.entity_type_load_result import EntityTypeLoadResult
    from tb_pe_client.models.entity_type_version_create_config import EntityTypeVersionCreateConfig
    from tb_pe_client.models.entity_type_version_load_config import EntityTypeVersionLoadConfig
    from tb_pe_client.models.entity_type_version_load_request import EntityTypeVersionLoadRequest
    from tb_pe_client.models.entity_version import EntityVersion
    from tb_pe_client.models.entity_view import EntityView
    from tb_pe_client.models.entity_view_export_data import EntityViewExportData
    from tb_pe_client.models.entity_view_id import EntityViewId
    from tb_pe_client.models.entity_view_info import EntityViewInfo
    from tb_pe_client.models.entity_view_search_query import EntityViewSearchQuery
    from tb_pe_client.models.entity_view_search_query_filter import EntityViewSearchQueryFilter
    from tb_pe_client.models.entity_view_type_filter import EntityViewTypeFilter
    from tb_pe_client.models.error_component import ErrorComponent
    from tb_pe_client.models.error_component_all_of_exception import ErrorComponentAllOfException
    from tb_pe_client.models.error_component_all_of_exception_cause import ErrorComponentAllOfExceptionCause
    from tb_pe_client.models.error_component_all_of_exception_cause_stack_trace import ErrorComponentAllOfExceptionCauseStackTrace
    from tb_pe_client.models.error_event_filter import ErrorEventFilter
    from tb_pe_client.models.escalated_notification_rule_recipients_config import EscalatedNotificationRuleRecipientsConfig
    from tb_pe_client.models.event_filter import EventFilter
    from tb_pe_client.models.event_id import EventId
    from tb_pe_client.models.event_info import EventInfo
    from tb_pe_client.models.event_type import EventType
    from tb_pe_client.models.exportable_entity import ExportableEntity
    from tb_pe_client.models.failure import Failure
    from tb_pe_client.models.favicon import Favicon
    from tb_pe_client.models.features_info import FeaturesInfo
    from tb_pe_client.models.filter import Filter
    from tb_pe_client.models.filter_predicate_value_boolean import FilterPredicateValueBoolean
    from tb_pe_client.models.filter_predicate_value_double import FilterPredicateValueDouble
    from tb_pe_client.models.filter_predicate_value_string import FilterPredicateValueString
    from tb_pe_client.models.fixed_time_window import FixedTimeWindow
    from tb_pe_client.models.font import Font
    from tb_pe_client.models.font_style import FontStyle
    from tb_pe_client.models.font_weight import FontWeight
    from tb_pe_client.models.geofencing_calculated_field_configuration import GeofencingCalculatedFieldConfiguration
    from tb_pe_client.models.geofencing_report_strategy import GeofencingReportStrategy
    from tb_pe_client.models.git_hub_models_chat_model_config import GitHubModelsChatModelConfig
    from tb_pe_client.models.git_hub_models_provider_config import GitHubModelsProviderConfig
    from tb_pe_client.models.google_ai_gemini_chat_model_config import GoogleAiGeminiChatModelConfig
    from tb_pe_client.models.google_ai_gemini_provider_config import GoogleAiGeminiProviderConfig
    from tb_pe_client.models.google_vertex_ai_gemini_chat_model_config import GoogleVertexAiGeminiChatModelConfig
    from tb_pe_client.models.google_vertex_ai_gemini_provider_config import GoogleVertexAiGeminiProviderConfig
    from tb_pe_client.models.group_permission import GroupPermission
    from tb_pe_client.models.group_permission_id import GroupPermissionId
    from tb_pe_client.models.group_permission_info import GroupPermissionInfo
    from tb_pe_client.models.has_id_object import HasIdObject
    from tb_pe_client.models.header_footer import HeaderFooter
    from tb_pe_client.models.heading import Heading
    from tb_pe_client.models.heading_component import HeadingComponent
    from tb_pe_client.models.history import History
    from tb_pe_client.models.home_dashboard import HomeDashboard
    from tb_pe_client.models.home_dashboard_info import HomeDashboardInfo
    from tb_pe_client.models.home_dashboard_params import HomeDashboardParams
    from tb_pe_client.models.home_menu_item import HomeMenuItem
    from tb_pe_client.models.home_menu_item_type import HomeMenuItemType
    from tb_pe_client.models.hour_interval import HourInterval
    from tb_pe_client.models.image_alignment import ImageAlignment
    from tb_pe_client.models.image_component import ImageComponent
    from tb_pe_client.models.image_source_type import ImageSourceType
    from tb_pe_client.models.image_width_type import ImageWidthType
    from tb_pe_client.models.insets import Insets
    from tb_pe_client.models.integration import Integration
    from tb_pe_client.models.integration_converters_info import IntegrationConvertersInfo
    from tb_pe_client.models.integration_export_data import IntegrationExportData
    from tb_pe_client.models.integration_id import IntegrationId
    from tb_pe_client.models.integration_info import IntegrationInfo
    from tb_pe_client.models.integration_lifecycle_event_notification_rule_trigger_config import IntegrationLifecycleEventNotificationRuleTriggerConfig
    from tb_pe_client.models.integration_lifecycle_event_recipients_config import IntegrationLifecycleEventRecipientsConfig
    from tb_pe_client.models.integration_type import IntegrationType
    from tb_pe_client.models.interval import Interval
    from tb_pe_client.models.interval_type import IntervalType
    from tb_pe_client.models.job import Job
    from tb_pe_client.models.job_configuration import JobConfiguration
    from tb_pe_client.models.job_id import JobId
    from tb_pe_client.models.job_result import JobResult
    from tb_pe_client.models.job_status import JobStatus
    from tb_pe_client.models.job_type import JobType
    from tb_pe_client.models.json_transport_payload_configuration import JsonTransportPayloadConfiguration
    from tb_pe_client.models.jwt_pair import JwtPair
    from tb_pe_client.models.jwt_settings import JwtSettings
    from tb_pe_client.models.key_filter import KeyFilter
    from tb_pe_client.models.key_filter_predicate import KeyFilterPredicate
    from tb_pe_client.models.key_info import KeyInfo
    from tb_pe_client.models.key_sample import KeySample
    from tb_pe_client.models.last_visited_dashboard_info import LastVisitedDashboardInfo
    from tb_pe_client.models.latest_chart_component import LatestChartComponent
    from tb_pe_client.models.legend_config import LegendConfig
    from tb_pe_client.models.legend_position import LegendPosition
    from tb_pe_client.models.license_usage_info import LicenseUsageInfo
    from tb_pe_client.models.life_cycle_event_filter import LifeCycleEventFilter
    from tb_pe_client.models.limited_api import LimitedApi
    from tb_pe_client.models.line_series_settings import LineSeriesSettings
    from tb_pe_client.models.line_series_step_type import LineSeriesStepType
    from tb_pe_client.models.link_type import LinkType
    from tb_pe_client.models.login401_response import Login401Response
    from tb_pe_client.models.login_mobile_info import LoginMobileInfo
    from tb_pe_client.models.login_request import LoginRequest
    from tb_pe_client.models.login_response import LoginResponse
    from tb_pe_client.models.login_white_labeling_params import LoginWhiteLabelingParams
    from tb_pe_client.models.lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential
    from tb_pe_client.models.lw_m2_m_server_security_config_default import LwM2MServerSecurityConfigDefault
    from tb_pe_client.models.lw_m2m_instance import LwM2mInstance
    from tb_pe_client.models.lw_m2m_object import LwM2mObject
    from tb_pe_client.models.lw_m2m_resource_observe import LwM2mResourceObserve
    from tb_pe_client.models.lw_m2m_version import LwM2mVersion
    from tb_pe_client.models.lwm2m_device_profile_transport_configuration import Lwm2mDeviceProfileTransportConfiguration
    from tb_pe_client.models.lwm2m_device_transport_configuration import Lwm2mDeviceTransportConfiguration
    from tb_pe_client.models.mapper_type import MapperType
    from tb_pe_client.models.mapping import Mapping
    from tb_pe_client.models.menu_item import MenuItem
    from tb_pe_client.models.menu_item_type import MenuItemType
    from tb_pe_client.models.merged_group_permission_info import MergedGroupPermissionInfo
    from tb_pe_client.models.merged_group_type_permission_info import MergedGroupTypePermissionInfo
    from tb_pe_client.models.merged_user_permissions import MergedUserPermissions
    from tb_pe_client.models.microsoft_teams_delivery_method_notification_template import MicrosoftTeamsDeliveryMethodNotificationTemplate
    from tb_pe_client.models.microsoft_teams_notification_target_config import MicrosoftTeamsNotificationTargetConfig
    from tb_pe_client.models.mistral_ai_chat_model_config import MistralAiChatModelConfig
    from tb_pe_client.models.mistral_ai_provider_config import MistralAiProviderConfig
    from tb_pe_client.models.mobile_app import MobileApp
    from tb_pe_client.models.mobile_app_bundle import MobileAppBundle
    from tb_pe_client.models.mobile_app_bundle_id import MobileAppBundleId
    from tb_pe_client.models.mobile_app_bundle_info import MobileAppBundleInfo
    from tb_pe_client.models.mobile_app_delivery_method_notification_template import MobileAppDeliveryMethodNotificationTemplate
    from tb_pe_client.models.mobile_app_id import MobileAppId
    from tb_pe_client.models.mobile_app_notification_delivery_method_config import MobileAppNotificationDeliveryMethodConfig
    from tb_pe_client.models.mobile_app_status import MobileAppStatus
    from tb_pe_client.models.mobile_app_version_info import MobileAppVersionInfo
    from tb_pe_client.models.mobile_layout_config import MobileLayoutConfig
    from tb_pe_client.models.mobile_page import MobilePage
    from tb_pe_client.models.mobile_page_type import MobilePageType
    from tb_pe_client.models.mobile_redirect_params import MobileRedirectParams
    from tb_pe_client.models.mobile_self_registration_params import MobileSelfRegistrationParams
    from tb_pe_client.models.mobile_session_info import MobileSessionInfo
    from tb_pe_client.models.model import Model
    from tb_pe_client.models.model_none import ModelNone
    from tb_pe_client.models.month_interval import MonthInterval
    from tb_pe_client.models.mqtt_device_profile_transport_configuration import MqttDeviceProfileTransportConfiguration
    from tb_pe_client.models.mqtt_device_transport_configuration import MqttDeviceTransportConfiguration
    from tb_pe_client.models.name_conflict_policy import NameConflictPolicy
    from tb_pe_client.models.new_platform_version_notification_rule_trigger_config import NewPlatformVersionNotificationRuleTriggerConfig
    from tb_pe_client.models.new_platform_version_recipients_config import NewPlatformVersionRecipientsConfig
    from tb_pe_client.models.no_data_filter_predicate import NoDataFilterPredicate
    from tb_pe_client.models.no_sec_lw_m2_m_bootstrap_server_credential import NoSecLwM2MBootstrapServerCredential
    from tb_pe_client.models.node_connection_info import NodeConnectionInfo
    from tb_pe_client.models.notification import Notification
    from tb_pe_client.models.notification_delivery_method import NotificationDeliveryMethod
    from tb_pe_client.models.notification_delivery_method_config import NotificationDeliveryMethodConfig
    from tb_pe_client.models.notification_id import NotificationId
    from tb_pe_client.models.notification_info import NotificationInfo
    from tb_pe_client.models.notification_pref import NotificationPref
    from tb_pe_client.models.notification_request import NotificationRequest
    from tb_pe_client.models.notification_request_config import NotificationRequestConfig
    from tb_pe_client.models.notification_request_id import NotificationRequestId
    from tb_pe_client.models.notification_request_info import NotificationRequestInfo
    from tb_pe_client.models.notification_request_preview import NotificationRequestPreview
    from tb_pe_client.models.notification_request_stats import NotificationRequestStats
    from tb_pe_client.models.notification_request_status import NotificationRequestStatus
    from tb_pe_client.models.notification_rule import NotificationRule
    from tb_pe_client.models.notification_rule_config import NotificationRuleConfig
    from tb_pe_client.models.notification_rule_export_data import NotificationRuleExportData
    from tb_pe_client.models.notification_rule_id import NotificationRuleId
    from tb_pe_client.models.notification_rule_info import NotificationRuleInfo
    from tb_pe_client.models.notification_rule_recipients_config import NotificationRuleRecipientsConfig
    from tb_pe_client.models.notification_rule_trigger_config import NotificationRuleTriggerConfig
    from tb_pe_client.models.notification_rule_trigger_type import NotificationRuleTriggerType
    from tb_pe_client.models.notification_settings import NotificationSettings
    from tb_pe_client.models.notification_status import NotificationStatus
    from tb_pe_client.models.notification_target import NotificationTarget
    from tb_pe_client.models.notification_target_config import NotificationTargetConfig
    from tb_pe_client.models.notification_target_export_data import NotificationTargetExportData
    from tb_pe_client.models.notification_target_id import NotificationTargetId
    from tb_pe_client.models.notification_template import NotificationTemplate
    from tb_pe_client.models.notification_template_config import NotificationTemplateConfig
    from tb_pe_client.models.notification_template_export_data import NotificationTemplateExportData
    from tb_pe_client.models.notification_template_id import NotificationTemplateId
    from tb_pe_client.models.notification_type import NotificationType
    from tb_pe_client.models.numeric_filter_predicate import NumericFilterPredicate
    from tb_pe_client.models.numeric_operation import NumericOperation
    from tb_pe_client.models.o_auth2_basic_mapper_config import OAuth2BasicMapperConfig
    from tb_pe_client.models.o_auth2_client import OAuth2Client
    from tb_pe_client.models.o_auth2_client_id import OAuth2ClientId
    from tb_pe_client.models.o_auth2_client_info import OAuth2ClientInfo
    from tb_pe_client.models.o_auth2_client_login_info import OAuth2ClientLoginInfo
    from tb_pe_client.models.o_auth2_client_registration_template import OAuth2ClientRegistrationTemplate
    from tb_pe_client.models.o_auth2_client_registration_template_id import OAuth2ClientRegistrationTemplateId
    from tb_pe_client.models.o_auth2_custom_mapper_config import OAuth2CustomMapperConfig
    from tb_pe_client.models.o_auth2_mapper_config import OAuth2MapperConfig
    from tb_pe_client.models.object_attributes import ObjectAttributes
    from tb_pe_client.models.object_type import ObjectType
    from tb_pe_client.models.ollama_auth import OllamaAuth
    from tb_pe_client.models.ollama_chat_model_config import OllamaChatModelConfig
    from tb_pe_client.models.ollama_provider_config import OllamaProviderConfig
    from tb_pe_client.models.open_ai_chat_model_config import OpenAiChatModelConfig
    from tb_pe_client.models.open_ai_provider_config import OpenAiProviderConfig
    from tb_pe_client.models.operation import Operation
    from tb_pe_client.models.originator_entity_owner_users_filter import OriginatorEntityOwnerUsersFilter
    from tb_pe_client.models.ota_package import OtaPackage
    from tb_pe_client.models.ota_package_export_data import OtaPackageExportData
    from tb_pe_client.models.ota_package_id import OtaPackageId
    from tb_pe_client.models.ota_package_info import OtaPackageInfo
    from tb_pe_client.models.ota_package_type import OtaPackageType
    from tb_pe_client.models.other_configuration import OtherConfiguration
    from tb_pe_client.models.output import Output
    from tb_pe_client.models.psklw_m2_m_bootstrap_server_credential import PSKLwM2MBootstrapServerCredential
    from tb_pe_client.models.page_break_component import PageBreakComponent
    from tb_pe_client.models.page_data_ai_model import PageDataAiModel
    from tb_pe_client.models.page_data_alarm_comment_info import PageDataAlarmCommentInfo
    from tb_pe_client.models.page_data_alarm_data import PageDataAlarmData
    from tb_pe_client.models.page_data_alarm_info import PageDataAlarmInfo
    from tb_pe_client.models.page_data_alarm_rule_definition import PageDataAlarmRuleDefinition
    from tb_pe_client.models.page_data_alarm_rule_definition_info import PageDataAlarmRuleDefinitionInfo
    from tb_pe_client.models.page_data_api_key_info import PageDataApiKeyInfo
    from tb_pe_client.models.page_data_asset import PageDataAsset
    from tb_pe_client.models.page_data_asset_info import PageDataAssetInfo
    from tb_pe_client.models.page_data_asset_profile import PageDataAssetProfile
    from tb_pe_client.models.page_data_asset_profile_info import PageDataAssetProfileInfo
    from tb_pe_client.models.page_data_audit_log import PageDataAuditLog
    from tb_pe_client.models.page_data_blob_entity_with_customer_info import PageDataBlobEntityWithCustomerInfo
    from tb_pe_client.models.page_data_calculated_field import PageDataCalculatedField
    from tb_pe_client.models.page_data_calculated_field_info import PageDataCalculatedFieldInfo
    from tb_pe_client.models.page_data_contact_based_object import PageDataContactBasedObject
    from tb_pe_client.models.page_data_converter import PageDataConverter
    from tb_pe_client.models.page_data_custom_menu_info import PageDataCustomMenuInfo
    from tb_pe_client.models.page_data_customer import PageDataCustomer
    from tb_pe_client.models.page_data_customer_info import PageDataCustomerInfo
    from tb_pe_client.models.page_data_dashboard_info import PageDataDashboardInfo
    from tb_pe_client.models.page_data_device import PageDataDevice
    from tb_pe_client.models.page_data_device_info import PageDataDeviceInfo
    from tb_pe_client.models.page_data_device_profile import PageDataDeviceProfile
    from tb_pe_client.models.page_data_device_profile_info import PageDataDeviceProfileInfo
    from tb_pe_client.models.page_data_domain_info import PageDataDomainInfo
    from tb_pe_client.models.page_data_edge import PageDataEdge
    from tb_pe_client.models.page_data_edge_event import PageDataEdgeEvent
    from tb_pe_client.models.page_data_edge_info import PageDataEdgeInfo
    from tb_pe_client.models.page_data_entity_data import PageDataEntityData
    from tb_pe_client.models.page_data_entity_group_info import PageDataEntityGroupInfo
    from tb_pe_client.models.page_data_entity_info import PageDataEntityInfo
    from tb_pe_client.models.page_data_entity_subtype import PageDataEntitySubtype
    from tb_pe_client.models.page_data_entity_version import PageDataEntityVersion
    from tb_pe_client.models.page_data_entity_view import PageDataEntityView
    from tb_pe_client.models.page_data_entity_view_info import PageDataEntityViewInfo
    from tb_pe_client.models.page_data_event_info import PageDataEventInfo
    from tb_pe_client.models.page_data_integration import PageDataIntegration
    from tb_pe_client.models.page_data_integration_info import PageDataIntegrationInfo
    from tb_pe_client.models.page_data_job import PageDataJob
    from tb_pe_client.models.page_data_mobile_app import PageDataMobileApp
    from tb_pe_client.models.page_data_mobile_app_bundle_info import PageDataMobileAppBundleInfo
    from tb_pe_client.models.page_data_notification import PageDataNotification
    from tb_pe_client.models.page_data_notification_request_info import PageDataNotificationRequestInfo
    from tb_pe_client.models.page_data_notification_rule_info import PageDataNotificationRuleInfo
    from tb_pe_client.models.page_data_notification_target import PageDataNotificationTarget
    from tb_pe_client.models.page_data_notification_template import PageDataNotificationTemplate
    from tb_pe_client.models.page_data_o_auth2_client_info import PageDataOAuth2ClientInfo
    from tb_pe_client.models.page_data_ota_package_info import PageDataOtaPackageInfo
    from tb_pe_client.models.page_data_queue import PageDataQueue
    from tb_pe_client.models.page_data_queue_stats import PageDataQueueStats
    from tb_pe_client.models.page_data_report import PageDataReport
    from tb_pe_client.models.page_data_report_info import PageDataReportInfo
    from tb_pe_client.models.page_data_report_template_info import PageDataReportTemplateInfo
    from tb_pe_client.models.page_data_role import PageDataRole
    from tb_pe_client.models.page_data_rule_chain import PageDataRuleChain
    from tb_pe_client.models.page_data_scheduled_report_info import PageDataScheduledReportInfo
    from tb_pe_client.models.page_data_scheduler_event_info import PageDataSchedulerEventInfo
    from tb_pe_client.models.page_data_scheduler_event_with_customer_info import PageDataSchedulerEventWithCustomerInfo
    from tb_pe_client.models.page_data_secret_info import PageDataSecretInfo
    from tb_pe_client.models.page_data_short_entity_view import PageDataShortEntityView
    from tb_pe_client.models.page_data_string import PageDataString
    from tb_pe_client.models.page_data_tb_resource_info import PageDataTbResourceInfo
    from tb_pe_client.models.page_data_tenant import PageDataTenant
    from tb_pe_client.models.page_data_tenant_info import PageDataTenantInfo
    from tb_pe_client.models.page_data_tenant_profile import PageDataTenantProfile
    from tb_pe_client.models.page_data_trendz_view_config_lite import PageDataTrendzViewConfigLite
    from tb_pe_client.models.page_data_user import PageDataUser
    from tb_pe_client.models.page_data_user_email_info import PageDataUserEmailInfo
    from tb_pe_client.models.page_data_user_info import PageDataUserInfo
    from tb_pe_client.models.page_data_widget_type_info import PageDataWidgetTypeInfo
    from tb_pe_client.models.page_data_widgets_bundle import PageDataWidgetsBundle
    from tb_pe_client.models.page_orientation import PageOrientation
    from tb_pe_client.models.page_size import PageSize
    from tb_pe_client.models.palette import Palette
    from tb_pe_client.models.palette_settings import PaletteSettings
    from tb_pe_client.models.pdf_report_template_config import PdfReportTemplateConfig
    from tb_pe_client.models.pie_chart_label_position import PieChartLabelPosition
    from tb_pe_client.models.platform_two_fa_settings import PlatformTwoFaSettings
    from tb_pe_client.models.platform_type import PlatformType
    from tb_pe_client.models.platform_users_notification_target_config import PlatformUsersNotificationTargetConfig
    from tb_pe_client.models.power_mode import PowerMode
    from tb_pe_client.models.power_saving_configuration import PowerSavingConfiguration
    from tb_pe_client.models.privacy_protocol import PrivacyProtocol
    from tb_pe_client.models.processing_strategy import ProcessingStrategy
    from tb_pe_client.models.processing_strategy_type import ProcessingStrategyType
    from tb_pe_client.models.propagation_calculated_field_configuration import PropagationCalculatedFieldConfiguration
    from tb_pe_client.models.proto_transport_payload_configuration import ProtoTransportPayloadConfiguration
    from tb_pe_client.models.qr_code_config import QRCodeConfig
    from tb_pe_client.models.qr_code_settings import QrCodeSettings
    from tb_pe_client.models.qr_code_settings_id import QrCodeSettingsId
    from tb_pe_client.models.quarter_interval import QuarterInterval
    from tb_pe_client.models.queue import Queue
    from tb_pe_client.models.queue_id import QueueId
    from tb_pe_client.models.queue_stats import QueueStats
    from tb_pe_client.models.queue_stats_id import QueueStatsId
    from tb_pe_client.models.quick_time_interval import QuickTimeInterval
    from tb_pe_client.models.rpklw_m2_m_bootstrap_server_credential import RPKLwM2MBootstrapServerCredential
    from tb_pe_client.models.rate_limits_notification_rule_trigger_config import RateLimitsNotificationRuleTriggerConfig
    from tb_pe_client.models.rate_limits_recipients_config import RateLimitsRecipientsConfig
    from tb_pe_client.models.raw_data_event_filter import RawDataEventFilter
    from tb_pe_client.models.read_ts_kv_query_result import ReadTsKvQueryResult
    from tb_pe_client.models.referenced_entity_key import ReferencedEntityKey
    from tb_pe_client.models.refresh_token_request import RefreshTokenRequest
    from tb_pe_client.models.related_entities_aggregation_calculated_field_configuration import RelatedEntitiesAggregationCalculatedFieldConfiguration
    from tb_pe_client.models.relation_entity_type_filter import RelationEntityTypeFilter
    from tb_pe_client.models.relation_path_level import RelationPathLevel
    from tb_pe_client.models.relation_path_query_dynamic_source_configuration import RelationPathQueryDynamicSourceConfiguration
    from tb_pe_client.models.relation_type_group import RelationTypeGroup
    from tb_pe_client.models.relations_query_filter import RelationsQueryFilter
    from tb_pe_client.models.relations_search_parameters import RelationsSearchParameters
    from tb_pe_client.models.repeating_alarm_condition import RepeatingAlarmCondition
    from tb_pe_client.models.report import Report
    from tb_pe_client.models.report_bar_chart_settings import ReportBarChartSettings
    from tb_pe_client.models.report_bar_chart_with_labels_settings import ReportBarChartWithLabelsSettings
    from tb_pe_client.models.report_component import ReportComponent
    from tb_pe_client.models.report_component_sub_type import ReportComponentSubType
    from tb_pe_client.models.report_component_type import ReportComponentType
    from tb_pe_client.models.report_doughnut_chart_settings import ReportDoughnutChartSettings
    from tb_pe_client.models.report_id import ReportId
    from tb_pe_client.models.report_info import ReportInfo
    from tb_pe_client.models.report_job_configuration import ReportJobConfiguration
    from tb_pe_client.models.report_job_result import ReportJobResult
    from tb_pe_client.models.report_latest_chart_settings import ReportLatestChartSettings
    from tb_pe_client.models.report_pie_chart_settings import ReportPieChartSettings
    from tb_pe_client.models.report_range_chart_settings import ReportRangeChartSettings
    from tb_pe_client.models.report_request import ReportRequest
    from tb_pe_client.models.report_task_result import ReportTaskResult
    from tb_pe_client.models.report_template import ReportTemplate
    from tb_pe_client.models.report_template_config import ReportTemplateConfig
    from tb_pe_client.models.report_template_export_data import ReportTemplateExportData
    from tb_pe_client.models.report_template_id import ReportTemplateId
    from tb_pe_client.models.report_template_info import ReportTemplateInfo
    from tb_pe_client.models.report_template_type import ReportTemplateType
    from tb_pe_client.models.report_time_series_chart_settings import ReportTimeSeriesChartSettings
    from tb_pe_client.models.repository_auth_method import RepositoryAuthMethod
    from tb_pe_client.models.repository_settings import RepositorySettings
    from tb_pe_client.models.repository_settings_info import RepositorySettingsInfo
    from tb_pe_client.models.reset_password_email_request import ResetPasswordEmailRequest
    from tb_pe_client.models.reset_password_request import ResetPasswordRequest
    from tb_pe_client.models.resource import Resource
    from tb_pe_client.models.resource_export_data import ResourceExportData
    from tb_pe_client.models.resource_shortage_recipients_config import ResourceShortageRecipientsConfig
    from tb_pe_client.models.resource_sub_type import ResourceSubType
    from tb_pe_client.models.resource_type import ResourceType
    from tb_pe_client.models.resources_shortage_notification_rule_trigger_config import ResourcesShortageNotificationRuleTriggerConfig
    from tb_pe_client.models.rich_text_component import RichTextComponent
    from tb_pe_client.models.role import Role
    from tb_pe_client.models.role_export_data import RoleExportData
    from tb_pe_client.models.role_id import RoleId
    from tb_pe_client.models.role_type import RoleType
    from tb_pe_client.models.rpc import Rpc
    from tb_pe_client.models.rpc_id import RpcId
    from tb_pe_client.models.rpc_status import RpcStatus
    from tb_pe_client.models.rule_chain import RuleChain
    from tb_pe_client.models.rule_chain_connection_info import RuleChainConnectionInfo
    from tb_pe_client.models.rule_chain_data import RuleChainData
    from tb_pe_client.models.rule_chain_debug_event_filter import RuleChainDebugEventFilter
    from tb_pe_client.models.rule_chain_export_data import RuleChainExportData
    from tb_pe_client.models.rule_chain_id import RuleChainId
    from tb_pe_client.models.rule_chain_import_result import RuleChainImportResult
    from tb_pe_client.models.rule_chain_meta_data import RuleChainMetaData
    from tb_pe_client.models.rule_chain_output_labels_usage import RuleChainOutputLabelsUsage
    from tb_pe_client.models.rule_chain_type import RuleChainType
    from tb_pe_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config import RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig
    from tb_pe_client.models.rule_engine_component_lifecycle_event_recipients_config import RuleEngineComponentLifecycleEventRecipientsConfig
    from tb_pe_client.models.rule_node import RuleNode
    from tb_pe_client.models.rule_node_debug_event_filter import RuleNodeDebugEventFilter
    from tb_pe_client.models.rule_node_id import RuleNodeId
    from tb_pe_client.models.save_device_with_credentials_request import SaveDeviceWithCredentialsRequest
    from tb_pe_client.models.save_ota_package_info_request import SaveOtaPackageInfoRequest
    from tb_pe_client.models.scheduled_report_info import ScheduledReportInfo
    from tb_pe_client.models.scheduler_event import SchedulerEvent
    from tb_pe_client.models.scheduler_event_export_data import SchedulerEventExportData
    from tb_pe_client.models.scheduler_event_filter import SchedulerEventFilter
    from tb_pe_client.models.scheduler_event_id import SchedulerEventId
    from tb_pe_client.models.scheduler_event_info import SchedulerEventInfo
    from tb_pe_client.models.scheduler_event_with_customer_info import SchedulerEventWithCustomerInfo
    from tb_pe_client.models.script_calculated_field_configuration import ScriptCalculatedFieldConfiguration
    from tb_pe_client.models.script_language import ScriptLanguage
    from tb_pe_client.models.secret import Secret
    from tb_pe_client.models.secret_id import SecretId
    from tb_pe_client.models.secret_info import SecretInfo
    from tb_pe_client.models.secret_type import SecretType
    from tb_pe_client.models.security_settings import SecuritySettings
    from tb_pe_client.models.self_registration_params import SelfRegistrationParams
    from tb_pe_client.models.self_registration_type import SelfRegistrationType
    from tb_pe_client.models.share_group_request import ShareGroupRequest
    from tb_pe_client.models.shared_attributes_setting_snmp_communication_config import SharedAttributesSettingSnmpCommunicationConfig
    from tb_pe_client.models.short_customer_info import ShortCustomerInfo
    from tb_pe_client.models.short_entity_view import ShortEntityView
    from tb_pe_client.models.sign_up_field import SignUpField
    from tb_pe_client.models.sign_up_field_id import SignUpFieldId
    from tb_pe_client.models.sign_up_request import SignUpRequest
    from tb_pe_client.models.sign_up_result import SignUpResult
    from tb_pe_client.models.sign_up_self_registration_params import SignUpSelfRegistrationParams
    from tb_pe_client.models.simple_alarm_condition import SimpleAlarmCondition
    from tb_pe_client.models.simple_alarm_condition_expression import SimpleAlarmConditionExpression
    from tb_pe_client.models.simple_calculated_field_configuration import SimpleCalculatedFieldConfiguration
    from tb_pe_client.models.simple_entity import SimpleEntity
    from tb_pe_client.models.single_entity_filter import SingleEntityFilter
    from tb_pe_client.models.single_entity_version_create_request import SingleEntityVersionCreateRequest
    from tb_pe_client.models.single_entity_version_load_request import SingleEntityVersionLoadRequest
    from tb_pe_client.models.slack_conversation import SlackConversation
    from tb_pe_client.models.slack_conversation_type import SlackConversationType
    from tb_pe_client.models.slack_delivery_method_notification_template import SlackDeliveryMethodNotificationTemplate
    from tb_pe_client.models.slack_notification_delivery_method_config import SlackNotificationDeliveryMethodConfig
    from tb_pe_client.models.slack_notification_target_config import SlackNotificationTargetConfig
    from tb_pe_client.models.smpp_bind_type import SmppBindType
    from tb_pe_client.models.smpp_sms_provider_configuration import SmppSmsProviderConfiguration
    from tb_pe_client.models.sms_delivery_method_notification_template import SmsDeliveryMethodNotificationTemplate
    from tb_pe_client.models.sms_provider_configuration import SmsProviderConfiguration
    from tb_pe_client.models.sms_two_fa_account_config import SmsTwoFaAccountConfig
    from tb_pe_client.models.sms_two_fa_provider_config import SmsTwoFaProviderConfig
    from tb_pe_client.models.snmp_communication_config import SnmpCommunicationConfig
    from tb_pe_client.models.snmp_communication_spec import SnmpCommunicationSpec
    from tb_pe_client.models.snmp_device_profile_transport_configuration import SnmpDeviceProfileTransportConfiguration
    from tb_pe_client.models.snmp_device_transport_configuration import SnmpDeviceTransportConfiguration
    from tb_pe_client.models.snmp_mapping import SnmpMapping
    from tb_pe_client.models.snmp_protocol_version import SnmpProtocolVersion
    from tb_pe_client.models.solution_data import SolutionData
    from tb_pe_client.models.solution_export_request import SolutionExportRequest
    from tb_pe_client.models.solution_export_response import SolutionExportResponse
    from tb_pe_client.models.solution_import_result import SolutionImportResult
    from tb_pe_client.models.solution_install_response import SolutionInstallResponse
    from tb_pe_client.models.solution_step import SolutionStep
    from tb_pe_client.models.solution_template_level import SolutionTemplateLevel
    from tb_pe_client.models.solution_validation_result import SolutionValidationResult
    from tb_pe_client.models.specific_time_schedule import SpecificTimeSchedule
    from tb_pe_client.models.split_view_component import SplitViewComponent
    from tb_pe_client.models.starred_dashboard_info import StarredDashboardInfo
    from tb_pe_client.models.state_entity_filter import StateEntityFilter
    from tb_pe_client.models.state_entity_owner_filter import StateEntityOwnerFilter
    from tb_pe_client.models.statistics_event_filter import StatisticsEventFilter
    from tb_pe_client.models.store_info import StoreInfo
    from tb_pe_client.models.string_filter_predicate import StringFilterPredicate
    from tb_pe_client.models.string_operation import StringOperation
    from tb_pe_client.models.sub_report_component import SubReportComponent
    from tb_pe_client.models.submit_strategy import SubmitStrategy
    from tb_pe_client.models.submit_strategy_type import SubmitStrategyType
    from tb_pe_client.models.success import Success
    from tb_pe_client.models.sync_strategy import SyncStrategy
    from tb_pe_client.models.system_administrators_filter import SystemAdministratorsFilter
    from tb_pe_client.models.system_info import SystemInfo
    from tb_pe_client.models.system_info_data import SystemInfoData
    from tb_pe_client.models.table_sort_direction import TableSortDirection
    from tb_pe_client.models.table_sort_order import TableSortOrder
    from tb_pe_client.models.task_processing_failure_notification_rule_trigger_config import TaskProcessingFailureNotificationRuleTriggerConfig
    from tb_pe_client.models.task_processing_failure_recipients_config import TaskProcessingFailureRecipientsConfig
    from tb_pe_client.models.task_result import TaskResult
    from tb_pe_client.models.tb_chat_request import TbChatRequest
    from tb_pe_client.models.tb_chat_response import TbChatResponse
    from tb_pe_client.models.tb_content import TbContent
    from tb_pe_client.models.tb_image_delete_result import TbImageDeleteResult
    from tb_pe_client.models.tb_report_format import TbReportFormat
    from tb_pe_client.models.tb_resource import TbResource
    from tb_pe_client.models.tb_resource_delete_result import TbResourceDeleteResult
    from tb_pe_client.models.tb_resource_export_data import TbResourceExportData
    from tb_pe_client.models.tb_resource_id import TbResourceId
    from tb_pe_client.models.tb_resource_info import TbResourceInfo
    from tb_pe_client.models.tb_secret_delete_result import TbSecretDeleteResult
    from tb_pe_client.models.tb_text_content import TbTextContent
    from tb_pe_client.models.tb_user_message import TbUserMessage
    from tb_pe_client.models.tbel_alarm_condition_expression import TbelAlarmConditionExpression
    from tb_pe_client.models.telemetry_entity_view import TelemetryEntityView
    from tb_pe_client.models.telemetry_mapping_configuration import TelemetryMappingConfiguration
    from tb_pe_client.models.telemetry_observe_strategy import TelemetryObserveStrategy
    from tb_pe_client.models.telemetry_querying_snmp_communication_config import TelemetryQueryingSnmpCommunicationConfig
    from tb_pe_client.models.tenant import Tenant
    from tb_pe_client.models.tenant_administrators_filter import TenantAdministratorsFilter
    from tb_pe_client.models.tenant_id import TenantId
    from tb_pe_client.models.tenant_info import TenantInfo
    from tb_pe_client.models.tenant_name_strategy_type import TenantNameStrategyType
    from tb_pe_client.models.tenant_profile import TenantProfile
    from tb_pe_client.models.tenant_profile_configuration import TenantProfileConfiguration
    from tb_pe_client.models.tenant_profile_data import TenantProfileData
    from tb_pe_client.models.tenant_profile_id import TenantProfileId
    from tb_pe_client.models.tenant_profile_queue_configuration import TenantProfileQueueConfiguration
    from tb_pe_client.models.tenant_solution_template_details import TenantSolutionTemplateDetails
    from tb_pe_client.models.tenant_solution_template_info import TenantSolutionTemplateInfo
    from tb_pe_client.models.tenant_solution_template_instructions import TenantSolutionTemplateInstructions
    from tb_pe_client.models.test_sms_request import TestSmsRequest
    from tb_pe_client.models.text_alignment import TextAlignment
    from tb_pe_client.models.thingsboard_credentials_expired_response import ThingsboardCredentialsExpiredResponse
    from tb_pe_client.models.thingsboard_error_code import ThingsboardErrorCode
    from tb_pe_client.models.thingsboard_error_response import ThingsboardErrorResponse
    from tb_pe_client.models.threshold_label_position import ThresholdLabelPosition
    from tb_pe_client.models.time_series_chart_bar_width import TimeSeriesChartBarWidth
    from tb_pe_client.models.time_series_chart_bar_width_settings import TimeSeriesChartBarWidthSettings
    from tb_pe_client.models.time_series_chart_grid_settings import TimeSeriesChartGridSettings
    from tb_pe_client.models.time_series_chart_key_settings import TimeSeriesChartKeySettings
    from tb_pe_client.models.time_series_chart_no_aggregation_bar_width_settings import TimeSeriesChartNoAggregationBarWidthSettings
    from tb_pe_client.models.time_series_chart_no_aggregation_bar_width_strategy import TimeSeriesChartNoAggregationBarWidthStrategy
    from tb_pe_client.models.time_series_chart_series_type import TimeSeriesChartSeriesType
    from tb_pe_client.models.time_series_chart_state_settings import TimeSeriesChartStateSettings
    from tb_pe_client.models.time_series_chart_state_source_type import TimeSeriesChartStateSourceType
    from tb_pe_client.models.time_series_chart_threshold import TimeSeriesChartThreshold
    from tb_pe_client.models.time_series_chart_x_axis_settings import TimeSeriesChartXAxisSettings
    from tb_pe_client.models.time_series_chart_y_axis_settings import TimeSeriesChartYAxisSettings
    from tb_pe_client.models.time_series_immediate_output_strategy import TimeSeriesImmediateOutputStrategy
    from tb_pe_client.models.time_series_output import TimeSeriesOutput
    from tb_pe_client.models.time_series_output_strategy import TimeSeriesOutputStrategy
    from tb_pe_client.models.time_series_rule_chain_output_strategy import TimeSeriesRuleChainOutputStrategy
    from tb_pe_client.models.time_unit import TimeUnit
    from tb_pe_client.models.time_window_configuration import TimeWindowConfiguration
    from tb_pe_client.models.timeseries_chart_component import TimeseriesChartComponent
    from tb_pe_client.models.timeseries_table_component import TimeseriesTableComponent
    from tb_pe_client.models.to_core_edqs_request import ToCoreEdqsRequest
    from tb_pe_client.models.to_device_rpc_request_snmp_communication_config import ToDeviceRpcRequestSnmpCommunicationConfig
    from tb_pe_client.models.to_server_rpc_request_snmp_communication_config import ToServerRpcRequestSnmpCommunicationConfig
    from tb_pe_client.models.token import Token
    from tb_pe_client.models.totp_two_fa_account_config import TotpTwoFaAccountConfig
    from tb_pe_client.models.totp_two_fa_provider_config import TotpTwoFaProviderConfig
    from tb_pe_client.models.translation_info import TranslationInfo
    from tb_pe_client.models.transport_payload_type_configuration import TransportPayloadTypeConfiguration
    from tb_pe_client.models.trendz_configuration import TrendzConfiguration
    from tb_pe_client.models.trendz_healthcheck_result import TrendzHealthcheckResult
    from tb_pe_client.models.trendz_summary import TrendzSummary
    from tb_pe_client.models.trendz_synchronization_result import TrendzSynchronizationResult
    from tb_pe_client.models.trendz_synchronization_result_type import TrendzSynchronizationResultType
    from tb_pe_client.models.trendz_synchronization_status import TrendzSynchronizationStatus
    from tb_pe_client.models.trendz_usage import TrendzUsage
    from tb_pe_client.models.trendz_view_config import TrendzViewConfig
    from tb_pe_client.models.trendz_view_config_lite import TrendzViewConfigLite
    from tb_pe_client.models.ts_data import TsData
    from tb_pe_client.models.ts_kv_entry import TsKvEntry
    from tb_pe_client.models.ts_value import TsValue
    from tb_pe_client.models.twilio_sms_provider_configuration import TwilioSmsProviderConfiguration
    from tb_pe_client.models.two_fa_account_config import TwoFaAccountConfig
    from tb_pe_client.models.two_fa_account_config_update_request import TwoFaAccountConfigUpdateRequest
    from tb_pe_client.models.two_fa_provider_config import TwoFaProviderConfig
    from tb_pe_client.models.two_fa_provider_info import TwoFaProviderInfo
    from tb_pe_client.models.two_fa_provider_type import TwoFaProviderType
    from tb_pe_client.models.uniquify_strategy import UniquifyStrategy
    from tb_pe_client.models.update_message import UpdateMessage
    from tb_pe_client.models.usage_info import UsageInfo
    from tb_pe_client.models.user import User
    from tb_pe_client.models.user_activation_link import UserActivationLink
    from tb_pe_client.models.user_dashboards_info import UserDashboardsInfo
    from tb_pe_client.models.user_email_info import UserEmailInfo
    from tb_pe_client.models.user_export_data import UserExportData
    from tb_pe_client.models.user_group_list_filter import UserGroupListFilter
    from tb_pe_client.models.user_id import UserId
    from tb_pe_client.models.user_info import UserInfo
    from tb_pe_client.models.user_list_filter import UserListFilter
    from tb_pe_client.models.user_mobile_info import UserMobileInfo
    from tb_pe_client.models.user_notification_settings import UserNotificationSettings
    from tb_pe_client.models.user_password_policy import UserPasswordPolicy
    from tb_pe_client.models.user_role_filter import UserRoleFilter
    from tb_pe_client.models.users_filter import UsersFilter
    from tb_pe_client.models.v2_captcha_params import V2CaptchaParams
    from tb_pe_client.models.v3_captcha_params import V3CaptchaParams
    from tb_pe_client.models.value_source_type import ValueSourceType
    from tb_pe_client.models.vendor import Vendor
    from tb_pe_client.models.version_create_config import VersionCreateConfig
    from tb_pe_client.models.version_create_request import VersionCreateRequest
    from tb_pe_client.models.version_create_request_type import VersionCreateRequestType
    from tb_pe_client.models.version_creation_result import VersionCreationResult
    from tb_pe_client.models.version_load_config import VersionLoadConfig
    from tb_pe_client.models.version_load_request import VersionLoadRequest
    from tb_pe_client.models.version_load_request_type import VersionLoadRequestType
    from tb_pe_client.models.version_load_result import VersionLoadResult
    from tb_pe_client.models.versioned_entity_info import VersionedEntityInfo
    from tb_pe_client.models.vertical_alignment import VerticalAlignment
    from tb_pe_client.models.watermark import Watermark
    from tb_pe_client.models.web_delivery_method_notification_template import WebDeliveryMethodNotificationTemplate
    from tb_pe_client.models.web_self_registration_params import WebSelfRegistrationParams
    from tb_pe_client.models.web_view_page import WebViewPage
    from tb_pe_client.models.week_interval import WeekInterval
    from tb_pe_client.models.week_sun_sat_interval import WeekSunSatInterval
    from tb_pe_client.models.white_labeling import WhiteLabeling
    from tb_pe_client.models.white_labeling_params import WhiteLabelingParams
    from tb_pe_client.models.white_labeling_type import WhiteLabelingType
    from tb_pe_client.models.widget_bundle_info import WidgetBundleInfo
    from tb_pe_client.models.widget_type import WidgetType
    from tb_pe_client.models.widget_type_details import WidgetTypeDetails
    from tb_pe_client.models.widget_type_export_data import WidgetTypeExportData
    from tb_pe_client.models.widget_type_id import WidgetTypeId
    from tb_pe_client.models.widget_type_info import WidgetTypeInfo
    from tb_pe_client.models.widgets_bundle import WidgetsBundle
    from tb_pe_client.models.widgets_bundle_export_data import WidgetsBundleExportData
    from tb_pe_client.models.widgets_bundle_id import WidgetsBundleId
    from tb_pe_client.models.x509_certificate_chain_provision_configuration import X509CertificateChainProvisionConfiguration
    from tb_pe_client.models.x509_lw_m2_m_bootstrap_server_credential import X509LwM2MBootstrapServerCredential
    from tb_pe_client.models.year_interval import YearInterval
    from tb_pe_client.models.zone_group_configuration import ZoneGroupConfiguration

_MODEL_CLASSES = {
    "AccountTwoFaSettings": "tb_pe_client.models.account_two_fa_settings",
    "Action": "tb_pe_client.models.action",
    "ActionStatus": "tb_pe_client.models.action_status",
    "ActionType": "tb_pe_client.models.action_type",
    "ActivateUserRequest": "tb_pe_client.models.activate_user_request",
    "AdminSettings": "tb_pe_client.models.admin_settings",
    "AdminSettingsId": "tb_pe_client.models.admin_settings_id",
    "AffectedTenantAdministratorsFilter": "tb_pe_client.models.affected_tenant_administrators_filter",
    "AffectedUserFilter": "tb_pe_client.models.affected_user_filter",
    "AggFunction": "tb_pe_client.models.agg_function",
    "AggFunctionInput": "tb_pe_client.models.agg_function_input",
    "AggInput": "tb_pe_client.models.agg_input",
    "AggInterval": "tb_pe_client.models.agg_interval",
    "AggKeyInput": "tb_pe_client.models.agg_key_input",
    "AggMetric": "tb_pe_client.models.agg_metric",
    "Aggregation": "tb_pe_client.models.aggregation",
    "AggregationConfiguration": "tb_pe_client.models.aggregation_configuration",
    "AggregationParams": "tb_pe_client.models.aggregation_params",
    "AiChatModelConfig": "tb_pe_client.models.ai_chat_model_config",
    "AiModel": "tb_pe_client.models.ai_model",
    "AiModelConfig": "tb_pe_client.models.ai_model_config",
    "AiModelExportData": "tb_pe_client.models.ai_model_export_data",
    "AiModelId": "tb_pe_client.models.ai_model_id",
    "AiModelType": "tb_pe_client.models.ai_model_type",
    "Alarm": "tb_pe_client.models.alarm",
    "AlarmAction": "tb_pe_client.models.alarm_action",
    "AlarmAssignee": "tb_pe_client.models.alarm_assignee",
    "AlarmAssignmentNotificationRuleTriggerConfig": "tb_pe_client.models.alarm_assignment_notification_rule_trigger_config",
    "AlarmAssignmentRecipientsConfig": "tb_pe_client.models.alarm_assignment_recipients_config",
    "AlarmCalculatedFieldConfiguration": "tb_pe_client.models.alarm_calculated_field_configuration",
    "AlarmComment": "tb_pe_client.models.alarm_comment",
    "AlarmCommentId": "tb_pe_client.models.alarm_comment_id",
    "AlarmCommentInfo": "tb_pe_client.models.alarm_comment_info",
    "AlarmCommentNotificationRuleTriggerConfig": "tb_pe_client.models.alarm_comment_notification_rule_trigger_config",
    "AlarmCommentRecipientsConfig": "tb_pe_client.models.alarm_comment_recipients_config",
    "AlarmCommentType": "tb_pe_client.models.alarm_comment_type",
    "AlarmCondition": "tb_pe_client.models.alarm_condition",
    "AlarmConditionExpression": "tb_pe_client.models.alarm_condition_expression",
    "AlarmConditionFilter": "tb_pe_client.models.alarm_condition_filter",
    "AlarmConditionValueAlarmSchedule": "tb_pe_client.models.alarm_condition_value_alarm_schedule",
    "AlarmConditionValueBoolean": "tb_pe_client.models.alarm_condition_value_boolean",
    "AlarmConditionValueDouble": "tb_pe_client.models.alarm_condition_value_double",
    "AlarmConditionValueInteger": "tb_pe_client.models.alarm_condition_value_integer",
    "AlarmConditionValueLong": "tb_pe_client.models.alarm_condition_value_long",
    "AlarmConditionValueString": "tb_pe_client.models.alarm_condition_value_string",
    "AlarmCountQuery": "tb_pe_client.models.alarm_count_query",
    "AlarmData": "tb_pe_client.models.alarm_data",
    "AlarmDataPageLink": "tb_pe_client.models.alarm_data_page_link",
    "AlarmDataQuery": "tb_pe_client.models.alarm_data_query",
    "AlarmFilterConfig": "tb_pe_client.models.alarm_filter_config",
    "AlarmId": "tb_pe_client.models.alarm_id",
    "AlarmInfo": "tb_pe_client.models.alarm_info",
    "AlarmNotificationRuleTriggerConfig": "tb_pe_client.models.alarm_notification_rule_trigger_config",
    "AlarmRule": "tb_pe_client.models.alarm_rule",
    "AlarmRuleBooleanFilterPredicate": "tb_pe_client.models.alarm_rule_boolean_filter_predicate",
    "AlarmRuleBooleanOperation": "tb_pe_client.models.alarm_rule_boolean_operation",
    "AlarmRuleComplexFilterPredicate": "tb_pe_client.models.alarm_rule_complex_filter_predicate",
    "AlarmRuleComplexOperation": "tb_pe_client.models.alarm_rule_complex_operation",
    "AlarmRuleDefinition": "tb_pe_client.models.alarm_rule_definition",
    "AlarmRuleDefinitionInfo": "tb_pe_client.models.alarm_rule_definition_info",
    "AlarmRuleKeyFilterPredicate": "tb_pe_client.models.alarm_rule_key_filter_predicate",
    "AlarmRuleNumericFilterPredicate": "tb_pe_client.models.alarm_rule_numeric_filter_predicate",
    "AlarmRuleNumericOperation": "tb_pe_client.models.alarm_rule_numeric_operation",
    "AlarmRuleStringFilterPredicate": "tb_pe_client.models.alarm_rule_string_filter_predicate",
    "AlarmRuleStringOperation": "tb_pe_client.models.alarm_rule_string_operation",
    "AlarmSchedule": "tb_pe_client.models.alarm_schedule",
    "AlarmSearchStatus": "tb_pe_client.models.alarm_search_status",
    "AlarmSeverity": "tb_pe_client.models.alarm_severity",
    "AlarmStatus": "tb_pe_client.models.alarm_status",
    "AlarmTableComponent": "tb_pe_client.models.alarm_table_component",
    "AliasEntityId": "tb_pe_client.models.alias_entity_id",
    "AliasEntityType": "tb_pe_client.models.alias_entity_type",
    "AllUsersFilter": "tb_pe_client.models.all_users_filter",
    "AllowCreateNewDevicesDeviceProfileProvisionConfiguration": "tb_pe_client.models.allow_create_new_devices_device_profile_provision_configuration",
    "AllowedPermissionsInfo": "tb_pe_client.models.allowed_permissions_info",
    "AmazonBedrockChatModelConfig": "tb_pe_client.models.amazon_bedrock_chat_model_config",
    "AmazonBedrockProviderConfig": "tb_pe_client.models.amazon_bedrock_provider_config",
    "AnthropicChatModelConfig": "tb_pe_client.models.anthropic_chat_model_config",
    "AnthropicProviderConfig": "tb_pe_client.models.anthropic_provider_config",
    "AnyTimeSchedule": "tb_pe_client.models.any_time_schedule",
    "ApiFeature": "tb_pe_client.models.api_feature",
    "ApiKey": "tb_pe_client.models.api_key",
    "ApiKeyId": "tb_pe_client.models.api_key_id",
    "ApiKeyInfo": "tb_pe_client.models.api_key_info",
    "ApiUsageLimitNotificationRuleTriggerConfig": "tb_pe_client.models.api_usage_limit_notification_rule_trigger_config",
    "ApiUsageLimitRecipientsConfig": "tb_pe_client.models.api_usage_limit_recipients_config",
    "ApiUsageStateFilter": "tb_pe_client.models.api_usage_state_filter",
    "ApiUsageStateId": "tb_pe_client.models.api_usage_state_id",
    "ApiUsageStateValue": "tb_pe_client.models.api_usage_state_value",
    "Argument": "tb_pe_client.models.argument",
    "ArgumentType": "tb_pe_client.models.argument_type",
    "Asset": "tb_pe_client.models.asset",
    "AssetExportData": "tb_pe_client.models.asset_export_data",
    "AssetId": "tb_pe_client.models.asset_id",
    "AssetInfo": "tb_pe_client.models.asset_info",
    "AssetProfile": "tb_pe_client.models.asset_profile",
    "AssetProfileExportData": "tb_pe_client.models.asset_profile_export_data",
    "AssetProfileId": "tb_pe_client.models.asset_profile_id",
    "AssetProfileInfo": "tb_pe_client.models.asset_profile_info",
    "AssetSearchQuery": "tb_pe_client.models.asset_search_query",
    "AssetSearchQueryFilter": "tb_pe_client.models.asset_search_query_filter",
    "AssetTypeFilter": "tb_pe_client.models.asset_type_filter",
    "AttributeData": "tb_pe_client.models.attribute_data",
    "AttributeExportData": "tb_pe_client.models.attribute_export_data",
    "AttributeScope": "tb_pe_client.models.attribute_scope",
    "AttributesEntityView": "tb_pe_client.models.attributes_entity_view",
    "AttributesImmediateOutputStrategy": "tb_pe_client.models.attributes_immediate_output_strategy",
    "AttributesOutput": "tb_pe_client.models.attributes_output",
    "AttributesOutputStrategy": "tb_pe_client.models.attributes_output_strategy",
    "AttributesRuleChainOutputStrategy": "tb_pe_client.models.attributes_rule_chain_output_strategy",
    "AuditLog": "tb_pe_client.models.audit_log",
    "AuditLogId": "tb_pe_client.models.audit_log_id",
    "AuthenticationProtocol": "tb_pe_client.models.authentication_protocol",
    "Authority": "tb_pe_client.models.authority",
    "AutoVersionCreateConfig": "tb_pe_client.models.auto_version_create_config",
    "AvailableEntityKeys": "tb_pe_client.models.available_entity_keys",
    "AvailableEntityKeysV2": "tb_pe_client.models.available_entity_keys_v2",
    "AwsSnsSmsProviderConfiguration": "tb_pe_client.models.aws_sns_sms_provider_configuration",
    "AxisPosition": "tb_pe_client.models.axis_position",
    "AzureOpenAiChatModelConfig": "tb_pe_client.models.azure_open_ai_chat_model_config",
    "AzureOpenAiProviderConfig": "tb_pe_client.models.azure_open_ai_provider_config",
    "BackupCodeTwoFaAccountConfig": "tb_pe_client.models.backup_code_two_fa_account_config",
    "BackupCodeTwoFaProviderConfig": "tb_pe_client.models.backup_code_two_fa_provider_config",
    "BadgePosition": "tb_pe_client.models.badge_position",
    "BarSeriesSettings": "tb_pe_client.models.bar_series_settings",
    "BaseReadTsKvQuery": "tb_pe_client.models.base_read_ts_kv_query",
    "Basic": "tb_pe_client.models.basic",
    "BlobEntityId": "tb_pe_client.models.blob_entity_id",
    "BlobEntityInfo": "tb_pe_client.models.blob_entity_info",
    "BlobEntityWithCustomerInfo": "tb_pe_client.models.blob_entity_with_customer_info",
    "BooleanFilterPredicate": "tb_pe_client.models.boolean_filter_predicate",
    "BooleanOperation": "tb_pe_client.models.boolean_operation",
    "BorderLength": "tb_pe_client.models.border_length",
    "BorderType": "tb_pe_client.models.border_type",
    "BranchInfo": "tb_pe_client.models.branch_info",
    "BulkImportColumnType": "tb_pe_client.models.bulk_import_column_type",
    "BulkImportRequest": "tb_pe_client.models.bulk_import_request",
    "BulkImportResultAsset": "tb_pe_client.models.bulk_import_result_asset",
    "BulkImportResultDevice": "tb_pe_client.models.bulk_import_result_device",
    "BulkImportResultEdge": "tb_pe_client.models.bulk_import_result_edge",
    "Button": "tb_pe_client.models.button",
    "CMAssigneeType": "tb_pe_client.models.cm_assignee_type",
    "CMItemLinkType": "tb_pe_client.models.cm_item_link_type",
    "CMItemType": "tb_pe_client.models.cm_item_type",
    "CMScope": "tb_pe_client.models.cm_scope",
    "CalculatedField": "tb_pe_client.models.calculated_field",
    "CalculatedFieldConfiguration": "tb_pe_client.models.calculated_field_configuration",
    "CalculatedFieldDebugEventFilter": "tb_pe_client.models.calculated_field_debug_event_filter",
    "CalculatedFieldId": "tb_pe_client.models.calculated_field_id",
    "CalculatedFieldInfo": "tb_pe_client.models.calculated_field_info",
    "CalculatedFieldType": "tb_pe_client.models.calculated_field_type",
    "CaptchaParams": "tb_pe_client.models.captcha_params",
    "CellSettings": "tb_pe_client.models.cell_settings",
    "CfArgumentDynamicSourceConfiguration": "tb_pe_client.models.cf_argument_dynamic_source_configuration",
    "CfReprocessingJobConfiguration": "tb_pe_client.models.cf_reprocessing_job_configuration",
    "CfReprocessingJobResult": "tb_pe_client.models.cf_reprocessing_job_result",
    "CfReprocessingTaskFailure": "tb_pe_client.models.cf_reprocessing_task_failure",
    "CfReprocessingTaskResult": "tb_pe_client.models.cf_reprocessing_task_result",
    "CfReprocessingValidationResult": "tb_pe_client.models.cf_reprocessing_validation_result",
    "ChangePasswordRequest": "tb_pe_client.models.change_password_request",
    "ChartFillSettings": "tb_pe_client.models.chart_fill_settings",
    "ChartFillSettingsGradient": "tb_pe_client.models.chart_fill_settings_gradient",
    "ChartFillType": "tb_pe_client.models.chart_fill_type",
    "ChartLabelPosition": "tb_pe_client.models.chart_label_position",
    "ChartLineType": "tb_pe_client.models.chart_line_type",
    "ChartShape": "tb_pe_client.models.chart_shape",
    "ChatType": "tb_pe_client.models.chat_type",
    "CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration": "tb_pe_client.models.check_pre_provisioned_devices_device_profile_provision_configuration",
    "ChecksumAlgorithm": "tb_pe_client.models.checksum_algorithm",
    "ClaimRequest": "tb_pe_client.models.claim_request",
    "ClearRule": "tb_pe_client.models.clear_rule",
    "ClientAttributesQueryingSnmpCommunicationConfig": "tb_pe_client.models.client_attributes_querying_snmp_communication_config",
    "CoapDeviceProfileTransportConfiguration": "tb_pe_client.models.coap_device_profile_transport_configuration",
    "CoapDeviceTransportConfiguration": "tb_pe_client.models.coap_device_transport_configuration",
    "CoapDeviceTypeConfiguration": "tb_pe_client.models.coap_device_type_configuration",
    "ColorRange": "tb_pe_client.models.color_range",
    "ColumnMapping": "tb_pe_client.models.column_mapping",
    "ColumnSettings": "tb_pe_client.models.column_settings",
    "ComparisonDuration": "tb_pe_client.models.comparison_duration",
    "ComparisonTsValue": "tb_pe_client.models.comparison_ts_value",
    "ComplexFilterPredicate": "tb_pe_client.models.complex_filter_predicate",
    "ComplexOperation": "tb_pe_client.models.complex_operation",
    "ComplexVersionCreateRequest": "tb_pe_client.models.complex_version_create_request",
    "ComponentClusteringMode": "tb_pe_client.models.component_clustering_mode",
    "ComponentDescriptor": "tb_pe_client.models.component_descriptor",
    "ComponentDescriptorId": "tb_pe_client.models.component_descriptor_id",
    "ComponentLifecycleEvent": "tb_pe_client.models.component_lifecycle_event",
    "ComponentScope": "tb_pe_client.models.component_scope",
    "ComponentType": "tb_pe_client.models.component_type",
    "ContactBasedObject": "tb_pe_client.models.contact_based_object",
    "Converter": "tb_pe_client.models.converter",
    "ConverterExportData": "tb_pe_client.models.converter_export_data",
    "ConverterId": "tb_pe_client.models.converter_id",
    "ConverterType": "tb_pe_client.models.converter_type",
    "ConvertersInfo": "tb_pe_client.models.converters_info",
    "CreateReportRequest": "tb_pe_client.models.create_report_request",
    "CsvReportTemplateConfig": "tb_pe_client.models.csv_report_template_config",
    "CurrentOwnerDynamicSourceConfiguration": "tb_pe_client.models.current_owner_dynamic_source_configuration",
    "CustomInterval": "tb_pe_client.models.custom_interval",
    "CustomMenu": "tb_pe_client.models.custom_menu",
    "CustomMenuConfig": "tb_pe_client.models.custom_menu_config",
    "CustomMenuDeleteResult": "tb_pe_client.models.custom_menu_delete_result",
    "CustomMenuId": "tb_pe_client.models.custom_menu_id",
    "CustomMenuInfo": "tb_pe_client.models.custom_menu_info",
    "CustomMenuItem": "tb_pe_client.models.custom_menu_item",
    "CustomMobilePage": "tb_pe_client.models.custom_mobile_page",
    "CustomTimeSchedule": "tb_pe_client.models.custom_time_schedule",
    "CustomTimeScheduleItem": "tb_pe_client.models.custom_time_schedule_item",
    "Customer": "tb_pe_client.models.customer",
    "CustomerExportData": "tb_pe_client.models.customer_export_data",
    "CustomerId": "tb_pe_client.models.customer_id",
    "CustomerInfo": "tb_pe_client.models.customer_info",
    "CustomerUsersFilter": "tb_pe_client.models.customer_users_filter",
    "Dashboard": "tb_pe_client.models.dashboard",
    "DashboardComponent": "tb_pe_client.models.dashboard_component",
    "DashboardExportData": "tb_pe_client.models.dashboard_export_data",
    "DashboardId": "tb_pe_client.models.dashboard_id",
    "DashboardInfo": "tb_pe_client.models.dashboard_info",
    "DashboardPage": "tb_pe_client.models.dashboard_page",
    "DashboardReportConfig": "tb_pe_client.models.dashboard_report_config",
    "DataKey": "tb_pe_client.models.data_key",
    "DataKeyComparisonSettings": "tb_pe_client.models.data_key_comparison_settings",
    "DataKeySettings": "tb_pe_client.models.data_key_settings",
    "DataKeySettingsType": "tb_pe_client.models.data_key_settings_type",
    "DataSource": "tb_pe_client.models.data_source",
    "DataSourceType": "tb_pe_client.models.data_source_type",
    "DataType": "tb_pe_client.models.data_type",
    "DayInterval": "tb_pe_client.models.day_interval",
    "DebugConverterEventFilter": "tb_pe_client.models.debug_converter_event_filter",
    "DebugIntegrationEventFilter": "tb_pe_client.models.debug_integration_event_filter",
    "DebugSettings": "tb_pe_client.models.debug_settings",
    "DefaultCoapDeviceTypeConfiguration": "tb_pe_client.models.default_coap_device_type_configuration",
    "DefaultDashboardParams": "tb_pe_client.models.default_dashboard_params",
    "DefaultDataKeySettings": "tb_pe_client.models.default_data_key_settings",
    "DefaultDeviceConfiguration": "tb_pe_client.models.default_device_configuration",
    "DefaultDeviceProfileConfiguration": "tb_pe_client.models.default_device_profile_configuration",
    "DefaultDeviceProfileTransportConfiguration": "tb_pe_client.models.default_device_profile_transport_configuration",
    "DefaultDeviceTransportConfiguration": "tb_pe_client.models.default_device_transport_configuration",
    "DefaultMenuItem": "tb_pe_client.models.default_menu_item",
    "DefaultMobilePage": "tb_pe_client.models.default_mobile_page",
    "DefaultPageId": "tb_pe_client.models.default_page_id",
    "DefaultRuleChainCreateRequest": "tb_pe_client.models.default_rule_chain_create_request",
    "DefaultTenantProfileConfiguration": "tb_pe_client.models.default_tenant_profile_configuration",
    "DeliveryMethodNotificationTemplate": "tb_pe_client.models.delivery_method_notification_template",
    "Device": "tb_pe_client.models.device",
    "DeviceActivityNotificationRuleTriggerConfig": "tb_pe_client.models.device_activity_notification_rule_trigger_config",
    "DeviceActivityRecipientsConfig": "tb_pe_client.models.device_activity_recipients_config",
    "DeviceConfiguration": "tb_pe_client.models.device_configuration",
    "DeviceCredentials": "tb_pe_client.models.device_credentials",
    "DeviceCredentialsId": "tb_pe_client.models.device_credentials_id",
    "DeviceCredentialsType": "tb_pe_client.models.device_credentials_type",
    "DeviceData": "tb_pe_client.models.device_data",
    "DeviceEvent": "tb_pe_client.models.device_event",
    "DeviceExportData": "tb_pe_client.models.device_export_data",
    "DeviceGroupOtaPackage": "tb_pe_client.models.device_group_ota_package",
    "DeviceId": "tb_pe_client.models.device_id",
    "DeviceInfo": "tb_pe_client.models.device_info",
    "DeviceProfile": "tb_pe_client.models.device_profile",
    "DeviceProfileConfiguration": "tb_pe_client.models.device_profile_configuration",
    "DeviceProfileData": "tb_pe_client.models.device_profile_data",
    "DeviceProfileExportData": "tb_pe_client.models.device_profile_export_data",
    "DeviceProfileId": "tb_pe_client.models.device_profile_id",
    "DeviceProfileInfo": "tb_pe_client.models.device_profile_info",
    "DeviceProfileProvisionConfiguration": "tb_pe_client.models.device_profile_provision_configuration",
    "DeviceProfileProvisionType": "tb_pe_client.models.device_profile_provision_type",
    "DeviceProfileTransportConfiguration": "tb_pe_client.models.device_profile_transport_configuration",
    "DeviceProfileType": "tb_pe_client.models.device_profile_type",
    "DeviceSearchQuery": "tb_pe_client.models.device_search_query",
    "DeviceSearchQueryFilter": "tb_pe_client.models.device_search_query_filter",
    "DeviceTransportConfiguration": "tb_pe_client.models.device_transport_configuration",
    "DeviceTransportType": "tb_pe_client.models.device_transport_type",
    "DeviceTypeFilter": "tb_pe_client.models.device_type_filter",
    "Direction": "tb_pe_client.models.direction",
    "DisabledDeviceProfileProvisionConfiguration": "tb_pe_client.models.disabled_device_profile_provision_configuration",
    "DividerComponent": "tb_pe_client.models.divider_component",
    "Domain": "tb_pe_client.models.domain",
    "DomainId": "tb_pe_client.models.domain_id",
    "DomainInfo": "tb_pe_client.models.domain_info",
    "DoughnutLayout": "tb_pe_client.models.doughnut_layout",
    "DummyJobConfiguration": "tb_pe_client.models.dummy_job_configuration",
    "DummyJobResult": "tb_pe_client.models.dummy_job_result",
    "DummyTaskFailure": "tb_pe_client.models.dummy_task_failure",
    "DummyTaskResult": "tb_pe_client.models.dummy_task_result",
    "DurationAlarmCondition": "tb_pe_client.models.duration_alarm_condition",
    "DynamicValueBoolean": "tb_pe_client.models.dynamic_value_boolean",
    "DynamicValueDouble": "tb_pe_client.models.dynamic_value_double",
    "DynamicValueSourceType": "tb_pe_client.models.dynamic_value_source_type",
    "DynamicValueString": "tb_pe_client.models.dynamic_value_string",
    "Edge": "tb_pe_client.models.edge",
    "EdgeCommunicationFailureNotificationRuleTriggerConfig": "tb_pe_client.models.edge_communication_failure_notification_rule_trigger_config",
    "EdgeCommunicationFailureRecipientsConfig": "tb_pe_client.models.edge_communication_failure_recipients_config",
    "EdgeConnectionNotificationRuleTriggerConfig": "tb_pe_client.models.edge_connection_notification_rule_trigger_config",
    "EdgeConnectionRecipientsConfig": "tb_pe_client.models.edge_connection_recipients_config",
    "EdgeConnectivityEvent": "tb_pe_client.models.edge_connectivity_event",
    "EdgeEvent": "tb_pe_client.models.edge_event",
    "EdgeEventActionType": "tb_pe_client.models.edge_event_action_type",
    "EdgeEventId": "tb_pe_client.models.edge_event_id",
    "EdgeEventType": "tb_pe_client.models.edge_event_type",
    "EdgeId": "tb_pe_client.models.edge_id",
    "EdgeInfo": "tb_pe_client.models.edge_info",
    "EdgeInstructions": "tb_pe_client.models.edge_instructions",
    "EdgeSearchQuery": "tb_pe_client.models.edge_search_query",
    "EdgeSearchQueryFilter": "tb_pe_client.models.edge_search_query_filter",
    "EdgeTypeFilter": "tb_pe_client.models.edge_type_filter",
    "EdqsApiMode": "tb_pe_client.models.edqs_api_mode",
    "EdqsState": "tb_pe_client.models.edqs_state",
    "EdqsSyncRequest": "tb_pe_client.models.edqs_sync_request",
    "EdqsSyncStatus": "tb_pe_client.models.edqs_sync_status",
    "EfentoCoapDeviceTypeConfiguration": "tb_pe_client.models.efento_coap_device_type_configuration",
    "EmailDeliveryMethodNotificationTemplate": "tb_pe_client.models.email_delivery_method_notification_template",
    "EmailTwoFaAccountConfig": "tb_pe_client.models.email_two_fa_account_config",
    "EmailTwoFaProviderConfig": "tb_pe_client.models.email_two_fa_provider_config",
    "EnterpriseCaptchaParams": "tb_pe_client.models.enterprise_captcha_params",
    "EntitiesByGroupNameFilter": "tb_pe_client.models.entities_by_group_name_filter",
    "EntitiesLimitNotificationRuleTriggerConfig": "tb_pe_client.models.entities_limit_notification_rule_trigger_config",
    "EntitiesLimitRecipientsConfig": "tb_pe_client.models.entities_limit_recipients_config",
    "Entity": "tb_pe_client.models.entity",
    "EntityActionNotificationRuleTriggerConfig": "tb_pe_client.models.entity_action_notification_rule_trigger_config",
    "EntityActionRecipientsConfig": "tb_pe_client.models.entity_action_recipients_config",
    "EntityAggregationCalculatedFieldConfiguration": "tb_pe_client.models.entity_aggregation_calculated_field_configuration",
    "EntityAlias": "tb_pe_client.models.entity_alias",
    "EntityCoordinates": "tb_pe_client.models.entity_coordinates",
    "EntityCountQuery": "tb_pe_client.models.entity_count_query",
    "EntityData": "tb_pe_client.models.entity_data",
    "EntityDataDiff": "tb_pe_client.models.entity_data_diff",
    "EntityDataInfo": "tb_pe_client.models.entity_data_info",
    "EntityDataPageLink": "tb_pe_client.models.entity_data_page_link",
    "EntityDataQuery": "tb_pe_client.models.entity_data_query",
    "EntityDataSortOrder": "tb_pe_client.models.entity_data_sort_order",
    "EntityExportData": "tb_pe_client.models.entity_export_data",
    "EntityExportSettings": "tb_pe_client.models.entity_export_settings",
    "EntityFilter": "tb_pe_client.models.entity_filter",
    "EntityGroup": "tb_pe_client.models.entity_group",
    "EntityGroupExportData": "tb_pe_client.models.entity_group_export_data",
    "EntityGroupFilter": "tb_pe_client.models.entity_group_filter",
    "EntityGroupId": "tb_pe_client.models.entity_group_id",
    "EntityGroupInfo": "tb_pe_client.models.entity_group_info",
    "EntityGroupListFilter": "tb_pe_client.models.entity_group_list_filter",
    "EntityGroupNameFilter": "tb_pe_client.models.entity_group_name_filter",
    "EntityId": "tb_pe_client.models.entity_id",
    "EntityInfo": "tb_pe_client.models.entity_info",
    "EntityKey": "tb_pe_client.models.entity_key",
    "EntityKeyType": "tb_pe_client.models.entity_key_type",
    "EntityKeyValueType": "tb_pe_client.models.entity_key_value_type",
    "EntityListFilter": "tb_pe_client.models.entity_list_filter",
    "EntityLoadError": "tb_pe_client.models.entity_load_error",
    "EntityNameFilter": "tb_pe_client.models.entity_name_filter",
    "EntityRelation": "tb_pe_client.models.entity_relation",
    "EntityRelationInfo": "tb_pe_client.models.entity_relation_info",
    "EntityRelationsQuery": "tb_pe_client.models.entity_relations_query",
    "EntitySearchDirection": "tb_pe_client.models.entity_search_direction",
    "EntitySubtype": "tb_pe_client.models.entity_subtype",
    "EntityTableComponent": "tb_pe_client.models.entity_table_component",
    "EntityType": "tb_pe_client.models.entity_type",
    "EntityTypeFilter": "tb_pe_client.models.entity_type_filter",
    "EntityTypeLoadResult": "tb_pe_client.models.entity_type_load_result",
    "EntityTypeVersionCreateConfig": "tb_pe_client.models.entity_type_version_create_config",
    "EntityTypeVersionLoadConfig": "tb_pe_client.models.entity_type_version_load_config",
    "EntityTypeVersionLoadRequest": "tb_pe_client.models.entity_type_version_load_request",
    "EntityVersion": "tb_pe_client.models.entity_version",
    "EntityView": "tb_pe_client.models.entity_view",
    "EntityViewExportData": "tb_pe_client.models.entity_view_export_data",
    "EntityViewId": "tb_pe_client.models.entity_view_id",
    "EntityViewInfo": "tb_pe_client.models.entity_view_info",
    "EntityViewSearchQuery": "tb_pe_client.models.entity_view_search_query",
    "EntityViewSearchQueryFilter": "tb_pe_client.models.entity_view_search_query_filter",
    "EntityViewTypeFilter": "tb_pe_client.models.entity_view_type_filter",
    "ErrorComponent": "tb_pe_client.models.error_component",
    "ErrorComponentAllOfException": "tb_pe_client.models.error_component_all_of_exception",
    "ErrorComponentAllOfExceptionCause": "tb_pe_client.models.error_component_all_of_exception_cause",
    "ErrorComponentAllOfExceptionCauseStackTrace": "tb_pe_client.models.error_component_all_of_exception_cause_stack_trace",
    "ErrorEventFilter": "tb_pe_client.models.error_event_filter",
    "EscalatedNotificationRuleRecipientsConfig": "tb_pe_client.models.escalated_notification_rule_recipients_config",
    "EventFilter": "tb_pe_client.models.event_filter",
    "EventId": "tb_pe_client.models.event_id",
    "EventInfo": "tb_pe_client.models.event_info",
    "EventType": "tb_pe_client.models.event_type",
    "ExportableEntity": "tb_pe_client.models.exportable_entity",
    "Failure": "tb_pe_client.models.failure",
    "Favicon": "tb_pe_client.models.favicon",
    "FeaturesInfo": "tb_pe_client.models.features_info",
    "Filter": "tb_pe_client.models.filter",
    "FilterPredicateValueBoolean": "tb_pe_client.models.filter_predicate_value_boolean",
    "FilterPredicateValueDouble": "tb_pe_client.models.filter_predicate_value_double",
    "FilterPredicateValueString": "tb_pe_client.models.filter_predicate_value_string",
    "FixedTimeWindow": "tb_pe_client.models.fixed_time_window",
    "Font": "tb_pe_client.models.font",
    "FontStyle": "tb_pe_client.models.font_style",
    "FontWeight": "tb_pe_client.models.font_weight",
    "GeofencingCalculatedFieldConfiguration": "tb_pe_client.models.geofencing_calculated_field_configuration",
    "GeofencingReportStrategy": "tb_pe_client.models.geofencing_report_strategy",
    "GitHubModelsChatModelConfig": "tb_pe_client.models.git_hub_models_chat_model_config",
    "GitHubModelsProviderConfig": "tb_pe_client.models.git_hub_models_provider_config",
    "GoogleAiGeminiChatModelConfig": "tb_pe_client.models.google_ai_gemini_chat_model_config",
    "GoogleAiGeminiProviderConfig": "tb_pe_client.models.google_ai_gemini_provider_config",
    "GoogleVertexAiGeminiChatModelConfig": "tb_pe_client.models.google_vertex_ai_gemini_chat_model_config",
    "GoogleVertexAiGeminiProviderConfig": "tb_pe_client.models.google_vertex_ai_gemini_provider_config",
    "GroupPermission": "tb_pe_client.models.group_permission",
    "GroupPermissionId": "tb_pe_client.models.group_permission_id",
    "GroupPermissionInfo": "tb_pe_client.models.group_permission_info",
    "HasIdObject": "tb_pe_client.models.has_id_object",
    "HeaderFooter": "tb_pe_client.models.header_footer",
    "Heading": "tb_pe_client.models.heading",
    "HeadingComponent": "tb_pe_client.models.heading_component",
    "History": "tb_pe_client.models.history",
    "HomeDashboard": "tb_pe_client.models.home_dashboard",
    "HomeDashboardInfo": "tb_pe_client.models.home_dashboard_info",
    "HomeDashboardParams": "tb_pe_client.models.home_dashboard_params",
    "HomeMenuItem": "tb_pe_client.models.home_menu_item",
    "HomeMenuItemType": "tb_pe_client.models.home_menu_item_type",
    "HourInterval": "tb_pe_client.models.hour_interval",
    "ImageAlignment": "tb_pe_client.models.image_alignment",
    "ImageComponent": "tb_pe_client.models.image_component",
    "ImageSourceType": "tb_pe_client.models.image_source_type",
    "ImageWidthType": "tb_pe_client.models.image_width_type",
    "Insets": "tb_pe_client.models.insets",
    "Integration": "tb_pe_client.models.integration",
    "IntegrationConvertersInfo": "tb_pe_client.models.integration_converters_info",
    "IntegrationExportData": "tb_pe_client.models.integration_export_data",
    "IntegrationId": "tb_pe_client.models.integration_id",
    "IntegrationInfo": "tb_pe_client.models.integration_info",
    "IntegrationLifecycleEventNotificationRuleTriggerConfig": "tb_pe_client.models.integration_lifecycle_event_notification_rule_trigger_config",
    "IntegrationLifecycleEventRecipientsConfig": "tb_pe_client.models.integration_lifecycle_event_recipients_config",
    "IntegrationType": "tb_pe_client.models.integration_type",
    "Interval": "tb_pe_client.models.interval",
    "IntervalType": "tb_pe_client.models.interval_type",
    "Job": "tb_pe_client.models.job",
    "JobConfiguration": "tb_pe_client.models.job_configuration",
    "JobId": "tb_pe_client.models.job_id",
    "JobResult": "tb_pe_client.models.job_result",
    "JobStatus": "tb_pe_client.models.job_status",
    "JobType": "tb_pe_client.models.job_type",
    "JsonTransportPayloadConfiguration": "tb_pe_client.models.json_transport_payload_configuration",
    "JwtPair": "tb_pe_client.models.jwt_pair",
    "JwtSettings": "tb_pe_client.models.jwt_settings",
    "KeyFilter": "tb_pe_client.models.key_filter",
    "KeyFilterPredicate": "tb_pe_client.models.key_filter_predicate",
    "KeyInfo": "tb_pe_client.models.key_info",
    "KeySample": "tb_pe_client.models.key_sample",
    "LastVisitedDashboardInfo": "tb_pe_client.models.last_visited_dashboard_info",
    "LatestChartComponent": "tb_pe_client.models.latest_chart_component",
    "LegendConfig": "tb_pe_client.models.legend_config",
    "LegendPosition": "tb_pe_client.models.legend_position",
    "LicenseUsageInfo": "tb_pe_client.models.license_usage_info",
    "LifeCycleEventFilter": "tb_pe_client.models.life_cycle_event_filter",
    "LimitedApi": "tb_pe_client.models.limited_api",
    "LineSeriesSettings": "tb_pe_client.models.line_series_settings",
    "LineSeriesStepType": "tb_pe_client.models.line_series_step_type",
    "LinkType": "tb_pe_client.models.link_type",
    "Login401Response": "tb_pe_client.models.login401_response",
    "LoginMobileInfo": "tb_pe_client.models.login_mobile_info",
    "LoginRequest": "tb_pe_client.models.login_request",
    "LoginResponse": "tb_pe_client.models.login_response",
    "LoginWhiteLabelingParams": "tb_pe_client.models.login_white_labeling_params",
    "LwM2MBootstrapServerCredential": "tb_pe_client.models.lw_m2_m_bootstrap_server_credential",
    "LwM2MServerSecurityConfigDefault": "tb_pe_client.models.lw_m2_m_server_security_config_default",
    "LwM2mInstance": "tb_pe_client.models.lw_m2m_instance",
    "LwM2mObject": "tb_pe_client.models.lw_m2m_object",
    "LwM2mResourceObserve": "tb_pe_client.models.lw_m2m_resource_observe",
    "LwM2mVersion": "tb_pe_client.models.lw_m2m_version",
    "Lwm2mDeviceProfileTransportConfiguration": "tb_pe_client.models.lwm2m_device_profile_transport_configuration",
    "Lwm2mDeviceTransportConfiguration": "tb_pe_client.models.lwm2m_device_transport_configuration",
    "MapperType": "tb_pe_client.models.mapper_type",
    "Mapping": "tb_pe_client.models.mapping",
    "MenuItem": "tb_pe_client.models.menu_item",
    "MenuItemType": "tb_pe_client.models.menu_item_type",
    "MergedGroupPermissionInfo": "tb_pe_client.models.merged_group_permission_info",
    "MergedGroupTypePermissionInfo": "tb_pe_client.models.merged_group_type_permission_info",
    "MergedUserPermissions": "tb_pe_client.models.merged_user_permissions",
    "MicrosoftTeamsDeliveryMethodNotificationTemplate": "tb_pe_client.models.microsoft_teams_delivery_method_notification_template",
    "MicrosoftTeamsNotificationTargetConfig": "tb_pe_client.models.microsoft_teams_notification_target_config",
    "MistralAiChatModelConfig": "tb_pe_client.models.mistral_ai_chat_model_config",
    "MistralAiProviderConfig": "tb_pe_client.models.mistral_ai_provider_config",
    "MobileApp": "tb_pe_client.models.mobile_app",
    "MobileAppBundle": "tb_pe_client.models.mobile_app_bundle",
    "MobileAppBundleId": "tb_pe_client.models.mobile_app_bundle_id",
    "MobileAppBundleInfo": "tb_pe_client.models.mobile_app_bundle_info",
    "MobileAppDeliveryMethodNotificationTemplate": "tb_pe_client.models.mobile_app_delivery_method_notification_template",
    "MobileAppId": "tb_pe_client.models.mobile_app_id",
    "MobileAppNotificationDeliveryMethodConfig": "tb_pe_client.models.mobile_app_notification_delivery_method_config",
    "MobileAppStatus": "tb_pe_client.models.mobile_app_status",
    "MobileAppVersionInfo": "tb_pe_client.models.mobile_app_version_info",
    "MobileLayoutConfig": "tb_pe_client.models.mobile_layout_config",
    "MobilePage": "tb_pe_client.models.mobile_page",
    "MobilePageType": "tb_pe_client.models.mobile_page_type",
    "MobileRedirectParams": "tb_pe_client.models.mobile_redirect_params",
    "MobileSelfRegistrationParams": "tb_pe_client.models.mobile_self_registration_params",
    "MobileSessionInfo": "tb_pe_client.models.mobile_session_info",
    "Model": "tb_pe_client.models.model",
    "ModelNone": "tb_pe_client.models.model_none",
    "MonthInterval": "tb_pe_client.models.month_interval",
    "MqttDeviceProfileTransportConfiguration": "tb_pe_client.models.mqtt_device_profile_transport_configuration",
    "MqttDeviceTransportConfiguration": "tb_pe_client.models.mqtt_device_transport_configuration",
    "NameConflictPolicy": "tb_pe_client.models.name_conflict_policy",
    "NewPlatformVersionNotificationRuleTriggerConfig": "tb_pe_client.models.new_platform_version_notification_rule_trigger_config",
    "NewPlatformVersionRecipientsConfig": "tb_pe_client.models.new_platform_version_recipients_config",
    "NoDataFilterPredicate": "tb_pe_client.models.no_data_filter_predicate",
    "NoSecLwM2MBootstrapServerCredential": "tb_pe_client.models.no_sec_lw_m2_m_bootstrap_server_credential",
    "NodeConnectionInfo": "tb_pe_client.models.node_connection_info",
    "Notification": "tb_pe_client.models.notification",
    "NotificationDeliveryMethod": "tb_pe_client.models.notification_delivery_method",
    "NotificationDeliveryMethodConfig": "tb_pe_client.models.notification_delivery_method_config",
    "NotificationId": "tb_pe_client.models.notification_id",
    "NotificationInfo": "tb_pe_client.models.notification_info",
    "NotificationPref": "tb_pe_client.models.notification_pref",
    "NotificationRequest": "tb_pe_client.models.notification_request",
    "NotificationRequestConfig": "tb_pe_client.models.notification_request_config",
    "NotificationRequestId": "tb_pe_client.models.notification_request_id",
    "NotificationRequestInfo": "tb_pe_client.models.notification_request_info",
    "NotificationRequestPreview": "tb_pe_client.models.notification_request_preview",
    "NotificationRequestStats": "tb_pe_client.models.notification_request_stats",
    "NotificationRequestStatus": "tb_pe_client.models.notification_request_status",
    "NotificationRule": "tb_pe_client.models.notification_rule",
    "NotificationRuleConfig": "tb_pe_client.models.notification_rule_config",
    "NotificationRuleExportData": "tb_pe_client.models.notification_rule_export_data",
    "NotificationRuleId": "tb_pe_client.models.notification_rule_id",
    "NotificationRuleInfo": "tb_pe_client.models.notification_rule_info",
    "NotificationRuleRecipientsConfig": "tb_pe_client.models.notification_rule_recipients_config",
    "NotificationRuleTriggerConfig": "tb_pe_client.models.notification_rule_trigger_config",
    "NotificationRuleTriggerType": "tb_pe_client.models.notification_rule_trigger_type",
    "NotificationSettings": "tb_pe_client.models.notification_settings",
    "NotificationStatus": "tb_pe_client.models.notification_status",
    "NotificationTarget": "tb_pe_client.models.notification_target",
    "NotificationTargetConfig": "tb_pe_client.models.notification_target_config",
    "NotificationTargetExportData": "tb_pe_client.models.notification_target_export_data",
    "NotificationTargetId": "tb_pe_client.models.notification_target_id",
    "NotificationTemplate": "tb_pe_client.models.notification_template",
    "NotificationTemplateConfig": "tb_pe_client.models.notification_template_config",
    "NotificationTemplateExportData": "tb_pe_client.models.notification_template_export_data",
    "NotificationTemplateId": "tb_pe_client.models.notification_template_id",
    "NotificationType": "tb_pe_client.models.notification_type",
    "NumericFilterPredicate": "tb_pe_client.models.numeric_filter_predicate",
    "NumericOperation": "tb_pe_client.models.numeric_operation",
    "OAuth2BasicMapperConfig": "tb_pe_client.models.o_auth2_basic_mapper_config",
    "OAuth2Client": "tb_pe_client.models.o_auth2_client",
    "OAuth2ClientId": "tb_pe_client.models.o_auth2_client_id",
    "OAuth2ClientInfo": "tb_pe_client.models.o_auth2_client_info",
    "OAuth2ClientLoginInfo": "tb_pe_client.models.o_auth2_client_login_info",
    "OAuth2ClientRegistrationTemplate": "tb_pe_client.models.o_auth2_client_registration_template",
    "OAuth2ClientRegistrationTemplateId": "tb_pe_client.models.o_auth2_client_registration_template_id",
    "OAuth2CustomMapperConfig": "tb_pe_client.models.o_auth2_custom_mapper_config",
    "OAuth2MapperConfig": "tb_pe_client.models.o_auth2_mapper_config",
    "ObjectAttributes": "tb_pe_client.models.object_attributes",
    "ObjectType": "tb_pe_client.models.object_type",
    "OllamaAuth": "tb_pe_client.models.ollama_auth",
    "OllamaChatModelConfig": "tb_pe_client.models.ollama_chat_model_config",
    "OllamaProviderConfig": "tb_pe_client.models.ollama_provider_config",
    "OpenAiChatModelConfig": "tb_pe_client.models.open_ai_chat_model_config",
    "OpenAiProviderConfig": "tb_pe_client.models.open_ai_provider_config",
    "Operation": "tb_pe_client.models.operation",
    "OriginatorEntityOwnerUsersFilter": "tb_pe_client.models.originator_entity_owner_users_filter",
    "OtaPackage": "tb_pe_client.models.ota_package",
    "OtaPackageExportData": "tb_pe_client.models.ota_package_export_data",
    "OtaPackageId": "tb_pe_client.models.ota_package_id",
    "OtaPackageInfo": "tb_pe_client.models.ota_package_info",
    "OtaPackageType": "tb_pe_client.models.ota_package_type",
    "OtherConfiguration": "tb_pe_client.models.other_configuration",
    "Output": "tb_pe_client.models.output",
    "PSKLwM2MBootstrapServerCredential": "tb_pe_client.models.psklw_m2_m_bootstrap_server_credential",
    "PageBreakComponent": "tb_pe_client.models.page_break_component",
    "PageDataAiModel": "tb_pe_client.models.page_data_ai_model",
    "PageDataAlarmCommentInfo": "tb_pe_client.models.page_data_alarm_comment_info",
    "PageDataAlarmData": "tb_pe_client.models.page_data_alarm_data",
    "PageDataAlarmInfo": "tb_pe_client.models.page_data_alarm_info",
    "PageDataAlarmRuleDefinition": "tb_pe_client.models.page_data_alarm_rule_definition",
    "PageDataAlarmRuleDefinitionInfo": "tb_pe_client.models.page_data_alarm_rule_definition_info",
    "PageDataApiKeyInfo": "tb_pe_client.models.page_data_api_key_info",
    "PageDataAsset": "tb_pe_client.models.page_data_asset",
    "PageDataAssetInfo": "tb_pe_client.models.page_data_asset_info",
    "PageDataAssetProfile": "tb_pe_client.models.page_data_asset_profile",
    "PageDataAssetProfileInfo": "tb_pe_client.models.page_data_asset_profile_info",
    "PageDataAuditLog": "tb_pe_client.models.page_data_audit_log",
    "PageDataBlobEntityWithCustomerInfo": "tb_pe_client.models.page_data_blob_entity_with_customer_info",
    "PageDataCalculatedField": "tb_pe_client.models.page_data_calculated_field",
    "PageDataCalculatedFieldInfo": "tb_pe_client.models.page_data_calculated_field_info",
    "PageDataContactBasedObject": "tb_pe_client.models.page_data_contact_based_object",
    "PageDataConverter": "tb_pe_client.models.page_data_converter",
    "PageDataCustomMenuInfo": "tb_pe_client.models.page_data_custom_menu_info",
    "PageDataCustomer": "tb_pe_client.models.page_data_customer",
    "PageDataCustomerInfo": "tb_pe_client.models.page_data_customer_info",
    "PageDataDashboardInfo": "tb_pe_client.models.page_data_dashboard_info",
    "PageDataDevice": "tb_pe_client.models.page_data_device",
    "PageDataDeviceInfo": "tb_pe_client.models.page_data_device_info",
    "PageDataDeviceProfile": "tb_pe_client.models.page_data_device_profile",
    "PageDataDeviceProfileInfo": "tb_pe_client.models.page_data_device_profile_info",
    "PageDataDomainInfo": "tb_pe_client.models.page_data_domain_info",
    "PageDataEdge": "tb_pe_client.models.page_data_edge",
    "PageDataEdgeEvent": "tb_pe_client.models.page_data_edge_event",
    "PageDataEdgeInfo": "tb_pe_client.models.page_data_edge_info",
    "PageDataEntityData": "tb_pe_client.models.page_data_entity_data",
    "PageDataEntityGroupInfo": "tb_pe_client.models.page_data_entity_group_info",
    "PageDataEntityInfo": "tb_pe_client.models.page_data_entity_info",
    "PageDataEntitySubtype": "tb_pe_client.models.page_data_entity_subtype",
    "PageDataEntityVersion": "tb_pe_client.models.page_data_entity_version",
    "PageDataEntityView": "tb_pe_client.models.page_data_entity_view",
    "PageDataEntityViewInfo": "tb_pe_client.models.page_data_entity_view_info",
    "PageDataEventInfo": "tb_pe_client.models.page_data_event_info",
    "PageDataIntegration": "tb_pe_client.models.page_data_integration",
    "PageDataIntegrationInfo": "tb_pe_client.models.page_data_integration_info",
    "PageDataJob": "tb_pe_client.models.page_data_job",
    "PageDataMobileApp": "tb_pe_client.models.page_data_mobile_app",
    "PageDataMobileAppBundleInfo": "tb_pe_client.models.page_data_mobile_app_bundle_info",
    "PageDataNotification": "tb_pe_client.models.page_data_notification",
    "PageDataNotificationRequestInfo": "tb_pe_client.models.page_data_notification_request_info",
    "PageDataNotificationRuleInfo": "tb_pe_client.models.page_data_notification_rule_info",
    "PageDataNotificationTarget": "tb_pe_client.models.page_data_notification_target",
    "PageDataNotificationTemplate": "tb_pe_client.models.page_data_notification_template",
    "PageDataOAuth2ClientInfo": "tb_pe_client.models.page_data_o_auth2_client_info",
    "PageDataOtaPackageInfo": "tb_pe_client.models.page_data_ota_package_info",
    "PageDataQueue": "tb_pe_client.models.page_data_queue",
    "PageDataQueueStats": "tb_pe_client.models.page_data_queue_stats",
    "PageDataReport": "tb_pe_client.models.page_data_report",
    "PageDataReportInfo": "tb_pe_client.models.page_data_report_info",
    "PageDataReportTemplateInfo": "tb_pe_client.models.page_data_report_template_info",
    "PageDataRole": "tb_pe_client.models.page_data_role",
    "PageDataRuleChain": "tb_pe_client.models.page_data_rule_chain",
    "PageDataScheduledReportInfo": "tb_pe_client.models.page_data_scheduled_report_info",
    "PageDataSchedulerEventInfo": "tb_pe_client.models.page_data_scheduler_event_info",
    "PageDataSchedulerEventWithCustomerInfo": "tb_pe_client.models.page_data_scheduler_event_with_customer_info",
    "PageDataSecretInfo": "tb_pe_client.models.page_data_secret_info",
    "PageDataShortEntityView": "tb_pe_client.models.page_data_short_entity_view",
    "PageDataString": "tb_pe_client.models.page_data_string",
    "PageDataTbResourceInfo": "tb_pe_client.models.page_data_tb_resource_info",
    "PageDataTenant": "tb_pe_client.models.page_data_tenant",
    "PageDataTenantInfo": "tb_pe_client.models.page_data_tenant_info",
    "PageDataTenantProfile": "tb_pe_client.models.page_data_tenant_profile",
    "PageDataTrendzViewConfigLite": "tb_pe_client.models.page_data_trendz_view_config_lite",
    "PageDataUser": "tb_pe_client.models.page_data_user",
    "PageDataUserEmailInfo": "tb_pe_client.models.page_data_user_email_info",
    "PageDataUserInfo": "tb_pe_client.models.page_data_user_info",
    "PageDataWidgetTypeInfo": "tb_pe_client.models.page_data_widget_type_info",
    "PageDataWidgetsBundle": "tb_pe_client.models.page_data_widgets_bundle",
    "PageOrientation": "tb_pe_client.models.page_orientation",
    "PageSize": "tb_pe_client.models.page_size",
    "Palette": "tb_pe_client.models.palette",
    "PaletteSettings": "tb_pe_client.models.palette_settings",
    "PdfReportTemplateConfig": "tb_pe_client.models.pdf_report_template_config",
    "PieChartLabelPosition": "tb_pe_client.models.pie_chart_label_position",
    "PlatformTwoFaSettings": "tb_pe_client.models.platform_two_fa_settings",
    "PlatformType": "tb_pe_client.models.platform_type",
    "PlatformUsersNotificationTargetConfig": "tb_pe_client.models.platform_users_notification_target_config",
    "PowerMode": "tb_pe_client.models.power_mode",
    "PowerSavingConfiguration": "tb_pe_client.models.power_saving_configuration",
    "PrivacyProtocol": "tb_pe_client.models.privacy_protocol",
    "ProcessingStrategy": "tb_pe_client.models.processing_strategy",
    "ProcessingStrategyType": "tb_pe_client.models.processing_strategy_type",
    "PropagationCalculatedFieldConfiguration": "tb_pe_client.models.propagation_calculated_field_configuration",
    "ProtoTransportPayloadConfiguration": "tb_pe_client.models.proto_transport_payload_configuration",
    "QRCodeConfig": "tb_pe_client.models.qr_code_config",
    "QrCodeSettings": "tb_pe_client.models.qr_code_settings",
    "QrCodeSettingsId": "tb_pe_client.models.qr_code_settings_id",
    "QuarterInterval": "tb_pe_client.models.quarter_interval",
    "Queue": "tb_pe_client.models.queue",
    "QueueId": "tb_pe_client.models.queue_id",
    "QueueStats": "tb_pe_client.models.queue_stats",
    "QueueStatsId": "tb_pe_client.models.queue_stats_id",
    "QuickTimeInterval": "tb_pe_client.models.quick_time_interval",
    "RPKLwM2MBootstrapServerCredential": "tb_pe_client.models.rpklw_m2_m_bootstrap_server_credential",
    "RateLimitsNotificationRuleTriggerConfig": "tb_pe_client.models.rate_limits_notification_rule_trigger_config",
    "RateLimitsRecipientsConfig": "tb_pe_client.models.rate_limits_recipients_config",
    "RawDataEventFilter": "tb_pe_client.models.raw_data_event_filter",
    "ReadTsKvQueryResult": "tb_pe_client.models.read_ts_kv_query_result",
    "ReferencedEntityKey": "tb_pe_client.models.referenced_entity_key",
    "RefreshTokenRequest": "tb_pe_client.models.refresh_token_request",
    "RelatedEntitiesAggregationCalculatedFieldConfiguration": "tb_pe_client.models.related_entities_aggregation_calculated_field_configuration",
    "RelationEntityTypeFilter": "tb_pe_client.models.relation_entity_type_filter",
    "RelationPathLevel": "tb_pe_client.models.relation_path_level",
    "RelationPathQueryDynamicSourceConfiguration": "tb_pe_client.models.relation_path_query_dynamic_source_configuration",
    "RelationTypeGroup": "tb_pe_client.models.relation_type_group",
    "RelationsQueryFilter": "tb_pe_client.models.relations_query_filter",
    "RelationsSearchParameters": "tb_pe_client.models.relations_search_parameters",
    "RepeatingAlarmCondition": "tb_pe_client.models.repeating_alarm_condition",
    "Report": "tb_pe_client.models.report",
    "ReportBarChartSettings": "tb_pe_client.models.report_bar_chart_settings",
    "ReportBarChartWithLabelsSettings": "tb_pe_client.models.report_bar_chart_with_labels_settings",
    "ReportComponent": "tb_pe_client.models.report_component",
    "ReportComponentSubType": "tb_pe_client.models.report_component_sub_type",
    "ReportComponentType": "tb_pe_client.models.report_component_type",
    "ReportDoughnutChartSettings": "tb_pe_client.models.report_doughnut_chart_settings",
    "ReportId": "tb_pe_client.models.report_id",
    "ReportInfo": "tb_pe_client.models.report_info",
    "ReportJobConfiguration": "tb_pe_client.models.report_job_configuration",
    "ReportJobResult": "tb_pe_client.models.report_job_result",
    "ReportLatestChartSettings": "tb_pe_client.models.report_latest_chart_settings",
    "ReportPieChartSettings": "tb_pe_client.models.report_pie_chart_settings",
    "ReportRangeChartSettings": "tb_pe_client.models.report_range_chart_settings",
    "ReportRequest": "tb_pe_client.models.report_request",
    "ReportTaskResult": "tb_pe_client.models.report_task_result",
    "ReportTemplate": "tb_pe_client.models.report_template",
    "ReportTemplateConfig": "tb_pe_client.models.report_template_config",
    "ReportTemplateExportData": "tb_pe_client.models.report_template_export_data",
    "ReportTemplateId": "tb_pe_client.models.report_template_id",
    "ReportTemplateInfo": "tb_pe_client.models.report_template_info",
    "ReportTemplateType": "tb_pe_client.models.report_template_type",
    "ReportTimeSeriesChartSettings": "tb_pe_client.models.report_time_series_chart_settings",
    "RepositoryAuthMethod": "tb_pe_client.models.repository_auth_method",
    "RepositorySettings": "tb_pe_client.models.repository_settings",
    "RepositorySettingsInfo": "tb_pe_client.models.repository_settings_info",
    "ResetPasswordEmailRequest": "tb_pe_client.models.reset_password_email_request",
    "ResetPasswordRequest": "tb_pe_client.models.reset_password_request",
    "Resource": "tb_pe_client.models.resource",
    "ResourceExportData": "tb_pe_client.models.resource_export_data",
    "ResourceShortageRecipientsConfig": "tb_pe_client.models.resource_shortage_recipients_config",
    "ResourceSubType": "tb_pe_client.models.resource_sub_type",
    "ResourceType": "tb_pe_client.models.resource_type",
    "ResourcesShortageNotificationRuleTriggerConfig": "tb_pe_client.models.resources_shortage_notification_rule_trigger_config",
    "RichTextComponent": "tb_pe_client.models.rich_text_component",
    "Role": "tb_pe_client.models.role",
    "RoleExportData": "tb_pe_client.models.role_export_data",
    "RoleId": "tb_pe_client.models.role_id",
    "RoleType": "tb_pe_client.models.role_type",
    "Rpc": "tb_pe_client.models.rpc",
    "RpcId": "tb_pe_client.models.rpc_id",
    "RpcStatus": "tb_pe_client.models.rpc_status",
    "RuleChain": "tb_pe_client.models.rule_chain",
    "RuleChainConnectionInfo": "tb_pe_client.models.rule_chain_connection_info",
    "RuleChainData": "tb_pe_client.models.rule_chain_data",
    "RuleChainDebugEventFilter": "tb_pe_client.models.rule_chain_debug_event_filter",
    "RuleChainExportData": "tb_pe_client.models.rule_chain_export_data",
    "RuleChainId": "tb_pe_client.models.rule_chain_id",
    "RuleChainImportResult": "tb_pe_client.models.rule_chain_import_result",
    "RuleChainMetaData": "tb_pe_client.models.rule_chain_meta_data",
    "RuleChainOutputLabelsUsage": "tb_pe_client.models.rule_chain_output_labels_usage",
    "RuleChainType": "tb_pe_client.models.rule_chain_type",
    "RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig": "tb_pe_client.models.rule_engine_component_lifecycle_event_notification_rule_trigger_config",
    "RuleEngineComponentLifecycleEventRecipientsConfig": "tb_pe_client.models.rule_engine_component_lifecycle_event_recipients_config",
    "RuleNode": "tb_pe_client.models.rule_node",
    "RuleNodeDebugEventFilter": "tb_pe_client.models.rule_node_debug_event_filter",
    "RuleNodeId": "tb_pe_client.models.rule_node_id",
    "SaveDeviceWithCredentialsRequest": "tb_pe_client.models.save_device_with_credentials_request",
    "SaveOtaPackageInfoRequest": "tb_pe_client.models.save_ota_package_info_request",
    "ScheduledReportInfo": "tb_pe_client.models.scheduled_report_info",
    "SchedulerEvent": "tb_pe_client.models.scheduler_event",
    "SchedulerEventExportData": "tb_pe_client.models.scheduler_event_export_data",
    "SchedulerEventFilter": "tb_pe_client.models.scheduler_event_filter",
    "SchedulerEventId": "tb_pe_client.models.scheduler_event_id",
    "SchedulerEventInfo": "tb_pe_client.models.scheduler_event_info",
    "SchedulerEventWithCustomerInfo": "tb_pe_client.models.scheduler_event_with_customer_info",
    "ScriptCalculatedFieldConfiguration": "tb_pe_client.models.script_calculated_field_configuration",
    "ScriptLanguage": "tb_pe_client.models.script_language",
    "Secret": "tb_pe_client.models.secret",
    "SecretId": "tb_pe_client.models.secret_id",
    "SecretInfo": "tb_pe_client.models.secret_info",
    "SecretType": "tb_pe_client.models.secret_type",
    "SecuritySettings": "tb_pe_client.models.security_settings",
    "SelfRegistrationParams": "tb_pe_client.models.self_registration_params",
    "SelfRegistrationType": "tb_pe_client.models.self_registration_type",
    "ShareGroupRequest": "tb_pe_client.models.share_group_request",
    "SharedAttributesSettingSnmpCommunicationConfig": "tb_pe_client.models.shared_attributes_setting_snmp_communication_config",
    "ShortCustomerInfo": "tb_pe_client.models.short_customer_info",
    "ShortEntityView": "tb_pe_client.models.short_entity_view",
    "SignUpField": "tb_pe_client.models.sign_up_field",
    "SignUpFieldId": "tb_pe_client.models.sign_up_field_id",
    "SignUpRequest": "tb_pe_client.models.sign_up_request",
    "SignUpResult": "tb_pe_client.models.sign_up_result",
    "SignUpSelfRegistrationParams": "tb_pe_client.models.sign_up_self_registration_params",
    "SimpleAlarmCondition": "tb_pe_client.models.simple_alarm_condition",
    "SimpleAlarmConditionExpression": "tb_pe_client.models.simple_alarm_condition_expression",
    "SimpleCalculatedFieldConfiguration": "tb_pe_client.models.simple_calculated_field_configuration",
    "SimpleEntity": "tb_pe_client.models.simple_entity",
    "SingleEntityFilter": "tb_pe_client.models.single_entity_filter",
    "SingleEntityVersionCreateRequest": "tb_pe_client.models.single_entity_version_create_request",
    "SingleEntityVersionLoadRequest": "tb_pe_client.models.single_entity_version_load_request",
    "SlackConversation": "tb_pe_client.models.slack_conversation",
    "SlackConversationType": "tb_pe_client.models.slack_conversation_type",
    "SlackDeliveryMethodNotificationTemplate": "tb_pe_client.models.slack_delivery_method_notification_template",
    "SlackNotificationDeliveryMethodConfig": "tb_pe_client.models.slack_notification_delivery_method_config",
    "SlackNotificationTargetConfig": "tb_pe_client.models.slack_notification_target_config",
    "SmppBindType": "tb_pe_client.models.smpp_bind_type",
    "SmppSmsProviderConfiguration": "tb_pe_client.models.smpp_sms_provider_configuration",
    "SmsDeliveryMethodNotificationTemplate": "tb_pe_client.models.sms_delivery_method_notification_template",
    "SmsProviderConfiguration": "tb_pe_client.models.sms_provider_configuration",
    "SmsTwoFaAccountConfig": "tb_pe_client.models.sms_two_fa_account_config",
    "SmsTwoFaProviderConfig": "tb_pe_client.models.sms_two_fa_provider_config",
    "SnmpCommunicationConfig": "tb_pe_client.models.snmp_communication_config",
    "SnmpCommunicationSpec": "tb_pe_client.models.snmp_communication_spec",
    "SnmpDeviceProfileTransportConfiguration": "tb_pe_client.models.snmp_device_profile_transport_configuration",
    "SnmpDeviceTransportConfiguration": "tb_pe_client.models.snmp_device_transport_configuration",
    "SnmpMapping": "tb_pe_client.models.snmp_mapping",
    "SnmpProtocolVersion": "tb_pe_client.models.snmp_protocol_version",
    "SolutionData": "tb_pe_client.models.solution_data",
    "SolutionExportRequest": "tb_pe_client.models.solution_export_request",
    "SolutionExportResponse": "tb_pe_client.models.solution_export_response",
    "SolutionImportResult": "tb_pe_client.models.solution_import_result",
    "SolutionInstallResponse": "tb_pe_client.models.solution_install_response",
    "SolutionStep": "tb_pe_client.models.solution_step",
    "SolutionTemplateLevel": "tb_pe_client.models.solution_template_level",
    "SolutionValidationResult": "tb_pe_client.models.solution_validation_result",
    "SpecificTimeSchedule": "tb_pe_client.models.specific_time_schedule",
    "SplitViewComponent": "tb_pe_client.models.split_view_component",
    "StarredDashboardInfo": "tb_pe_client.models.starred_dashboard_info",
    "StateEntityFilter": "tb_pe_client.models.state_entity_filter",
    "StateEntityOwnerFilter": "tb_pe_client.models.state_entity_owner_filter",
    "StatisticsEventFilter": "tb_pe_client.models.statistics_event_filter",
    "StoreInfo": "tb_pe_client.models.store_info",
    "StringFilterPredicate": "tb_pe_client.models.string_filter_predicate",
    "StringOperation": "tb_pe_client.models.string_operation",
    "SubReportComponent": "tb_pe_client.models.sub_report_component",
    "SubmitStrategy": "tb_pe_client.models.submit_strategy",
    "SubmitStrategyType": "tb_pe_client.models.submit_strategy_type",
    "Success": "tb_pe_client.models.success",
    "SyncStrategy": "tb_pe_client.models.sync_strategy",
    "SystemAdministratorsFilter": "tb_pe_client.models.system_administrators_filter",
    "SystemInfo": "tb_pe_client.models.system_info",
    "SystemInfoData": "tb_pe_client.models.system_info_data",
    "TableSortDirection": "tb_pe_client.models.table_sort_direction",
    "TableSortOrder": "tb_pe_client.models.table_sort_order",
    "TaskProcessingFailureNotificationRuleTriggerConfig": "tb_pe_client.models.task_processing_failure_notification_rule_trigger_config",
    "TaskProcessingFailureRecipientsConfig": "tb_pe_client.models.task_processing_failure_recipients_config",
    "TaskResult": "tb_pe_client.models.task_result",
    "TbChatRequest": "tb_pe_client.models.tb_chat_request",
    "TbChatResponse": "tb_pe_client.models.tb_chat_response",
    "TbContent": "tb_pe_client.models.tb_content",
    "TbImageDeleteResult": "tb_pe_client.models.tb_image_delete_result",
    "TbReportFormat": "tb_pe_client.models.tb_report_format",
    "TbResource": "tb_pe_client.models.tb_resource",
    "TbResourceDeleteResult": "tb_pe_client.models.tb_resource_delete_result",
    "TbResourceExportData": "tb_pe_client.models.tb_resource_export_data",
    "TbResourceId": "tb_pe_client.models.tb_resource_id",
    "TbResourceInfo": "tb_pe_client.models.tb_resource_info",
    "TbSecretDeleteResult": "tb_pe_client.models.tb_secret_delete_result",
    "TbTextContent": "tb_pe_client.models.tb_text_content",
    "TbUserMessage": "tb_pe_client.models.tb_user_message",
    "TbelAlarmConditionExpression": "tb_pe_client.models.tbel_alarm_condition_expression",
    "TelemetryEntityView": "tb_pe_client.models.telemetry_entity_view",
    "TelemetryMappingConfiguration": "tb_pe_client.models.telemetry_mapping_configuration",
    "TelemetryObserveStrategy": "tb_pe_client.models.telemetry_observe_strategy",
    "TelemetryQueryingSnmpCommunicationConfig": "tb_pe_client.models.telemetry_querying_snmp_communication_config",
    "Tenant": "tb_pe_client.models.tenant",
    "TenantAdministratorsFilter": "tb_pe_client.models.tenant_administrators_filter",
    "TenantId": "tb_pe_client.models.tenant_id",
    "TenantInfo": "tb_pe_client.models.tenant_info",
    "TenantNameStrategyType": "tb_pe_client.models.tenant_name_strategy_type",
    "TenantProfile": "tb_pe_client.models.tenant_profile",
    "TenantProfileConfiguration": "tb_pe_client.models.tenant_profile_configuration",
    "TenantProfileData": "tb_pe_client.models.tenant_profile_data",
    "TenantProfileId": "tb_pe_client.models.tenant_profile_id",
    "TenantProfileQueueConfiguration": "tb_pe_client.models.tenant_profile_queue_configuration",
    "TenantSolutionTemplateDetails": "tb_pe_client.models.tenant_solution_template_details",
    "TenantSolutionTemplateInfo": "tb_pe_client.models.tenant_solution_template_info",
    "TenantSolutionTemplateInstructions": "tb_pe_client.models.tenant_solution_template_instructions",
    "TestSmsRequest": "tb_pe_client.models.test_sms_request",
    "TextAlignment": "tb_pe_client.models.text_alignment",
    "ThingsboardCredentialsExpiredResponse": "tb_pe_client.models.thingsboard_credentials_expired_response",
    "ThingsboardErrorCode": "tb_pe_client.models.thingsboard_error_code",
    "ThingsboardErrorResponse": "tb_pe_client.models.thingsboard_error_response",
    "ThresholdLabelPosition": "tb_pe_client.models.threshold_label_position",
    "TimeSeriesChartBarWidth": "tb_pe_client.models.time_series_chart_bar_width",
    "TimeSeriesChartBarWidthSettings": "tb_pe_client.models.time_series_chart_bar_width_settings",
    "TimeSeriesChartGridSettings": "tb_pe_client.models.time_series_chart_grid_settings",
    "TimeSeriesChartKeySettings": "tb_pe_client.models.time_series_chart_key_settings",
    "TimeSeriesChartNoAggregationBarWidthSettings": "tb_pe_client.models.time_series_chart_no_aggregation_bar_width_settings",
    "TimeSeriesChartNoAggregationBarWidthStrategy": "tb_pe_client.models.time_series_chart_no_aggregation_bar_width_strategy",
    "TimeSeriesChartSeriesType": "tb_pe_client.models.time_series_chart_series_type",
    "TimeSeriesChartStateSettings": "tb_pe_client.models.time_series_chart_state_settings",
    "TimeSeriesChartStateSourceType": "tb_pe_client.models.time_series_chart_state_source_type",
    "TimeSeriesChartThreshold": "tb_pe_client.models.time_series_chart_threshold",
    "TimeSeriesChartXAxisSettings": "tb_pe_client.models.time_series_chart_x_axis_settings",
    "TimeSeriesChartYAxisSettings": "tb_pe_client.models.time_series_chart_y_axis_settings",
    "TimeSeriesImmediateOutputStrategy": "tb_pe_client.models.time_series_immediate_output_strategy",
    "TimeSeriesOutput": "tb_pe_client.models.time_series_output",
    "TimeSeriesOutputStrategy": "tb_pe_client.models.time_series_output_strategy",
    "TimeSeriesRuleChainOutputStrategy": "tb_pe_client.models.time_series_rule_chain_output_strategy",
    "TimeUnit": "tb_pe_client.models.time_unit",
    "TimeWindowConfiguration": "tb_pe_client.models.time_window_configuration",
    "TimeseriesChartComponent": "tb_pe_client.models.timeseries_chart_component",
    "TimeseriesTableComponent": "tb_pe_client.models.timeseries_table_component",
    "ToCoreEdqsRequest": "tb_pe_client.models.to_core_edqs_request",
    "ToDeviceRpcRequestSnmpCommunicationConfig": "tb_pe_client.models.to_device_rpc_request_snmp_communication_config",
    "ToServerRpcRequestSnmpCommunicationConfig": "tb_pe_client.models.to_server_rpc_request_snmp_communication_config",
    "Token": "tb_pe_client.models.token",
    "TotpTwoFaAccountConfig": "tb_pe_client.models.totp_two_fa_account_config",
    "TotpTwoFaProviderConfig": "tb_pe_client.models.totp_two_fa_provider_config",
    "TranslationInfo": "tb_pe_client.models.translation_info",
    "TransportPayloadTypeConfiguration": "tb_pe_client.models.transport_payload_type_configuration",
    "TrendzConfiguration": "tb_pe_client.models.trendz_configuration",
    "TrendzHealthcheckResult": "tb_pe_client.models.trendz_healthcheck_result",
    "TrendzSummary": "tb_pe_client.models.trendz_summary",
    "TrendzSynchronizationResult": "tb_pe_client.models.trendz_synchronization_result",
    "TrendzSynchronizationResultType": "tb_pe_client.models.trendz_synchronization_result_type",
    "TrendzSynchronizationStatus": "tb_pe_client.models.trendz_synchronization_status",
    "TrendzUsage": "tb_pe_client.models.trendz_usage",
    "TrendzViewConfig": "tb_pe_client.models.trendz_view_config",
    "TrendzViewConfigLite": "tb_pe_client.models.trendz_view_config_lite",
    "TsData": "tb_pe_client.models.ts_data",
    "TsKvEntry": "tb_pe_client.models.ts_kv_entry",
    "TsValue": "tb_pe_client.models.ts_value",
    "TwilioSmsProviderConfiguration": "tb_pe_client.models.twilio_sms_provider_configuration",
    "TwoFaAccountConfig": "tb_pe_client.models.two_fa_account_config",
    "TwoFaAccountConfigUpdateRequest": "tb_pe_client.models.two_fa_account_config_update_request",
    "TwoFaProviderConfig": "tb_pe_client.models.two_fa_provider_config",
    "TwoFaProviderInfo": "tb_pe_client.models.two_fa_provider_info",
    "TwoFaProviderType": "tb_pe_client.models.two_fa_provider_type",
    "UniquifyStrategy": "tb_pe_client.models.uniquify_strategy",
    "UpdateMessage": "tb_pe_client.models.update_message",
    "UsageInfo": "tb_pe_client.models.usage_info",
    "User": "tb_pe_client.models.user",
    "UserActivationLink": "tb_pe_client.models.user_activation_link",
    "UserDashboardsInfo": "tb_pe_client.models.user_dashboards_info",
    "UserEmailInfo": "tb_pe_client.models.user_email_info",
    "UserExportData": "tb_pe_client.models.user_export_data",
    "UserGroupListFilter": "tb_pe_client.models.user_group_list_filter",
    "UserId": "tb_pe_client.models.user_id",
    "UserInfo": "tb_pe_client.models.user_info",
    "UserListFilter": "tb_pe_client.models.user_list_filter",
    "UserMobileInfo": "tb_pe_client.models.user_mobile_info",
    "UserNotificationSettings": "tb_pe_client.models.user_notification_settings",
    "UserPasswordPolicy": "tb_pe_client.models.user_password_policy",
    "UserRoleFilter": "tb_pe_client.models.user_role_filter",
    "UsersFilter": "tb_pe_client.models.users_filter",
    "V2CaptchaParams": "tb_pe_client.models.v2_captcha_params",
    "V3CaptchaParams": "tb_pe_client.models.v3_captcha_params",
    "ValueSourceType": "tb_pe_client.models.value_source_type",
    "Vendor": "tb_pe_client.models.vendor",
    "VersionCreateConfig": "tb_pe_client.models.version_create_config",
    "VersionCreateRequest": "tb_pe_client.models.version_create_request",
    "VersionCreateRequestType": "tb_pe_client.models.version_create_request_type",
    "VersionCreationResult": "tb_pe_client.models.version_creation_result",
    "VersionLoadConfig": "tb_pe_client.models.version_load_config",
    "VersionLoadRequest": "tb_pe_client.models.version_load_request",
    "VersionLoadRequestType": "tb_pe_client.models.version_load_request_type",
    "VersionLoadResult": "tb_pe_client.models.version_load_result",
    "VersionedEntityInfo": "tb_pe_client.models.versioned_entity_info",
    "VerticalAlignment": "tb_pe_client.models.vertical_alignment",
    "Watermark": "tb_pe_client.models.watermark",
    "WebDeliveryMethodNotificationTemplate": "tb_pe_client.models.web_delivery_method_notification_template",
    "WebSelfRegistrationParams": "tb_pe_client.models.web_self_registration_params",
    "WebViewPage": "tb_pe_client.models.web_view_page",
    "WeekInterval": "tb_pe_client.models.week_interval",
    "WeekSunSatInterval": "tb_pe_client.models.week_sun_sat_interval",
    "WhiteLabeling": "tb_pe_client.models.white_labeling",
    "WhiteLabelingParams": "tb_pe_client.models.white_labeling_params",
    "WhiteLabelingType": "tb_pe_client.models.white_labeling_type",
    "WidgetBundleInfo": "tb_pe_client.models.widget_bundle_info",
    "WidgetType": "tb_pe_client.models.widget_type",
    "WidgetTypeDetails": "tb_pe_client.models.widget_type_details",
    "WidgetTypeExportData": "tb_pe_client.models.widget_type_export_data",
    "WidgetTypeId": "tb_pe_client.models.widget_type_id",
    "WidgetTypeInfo": "tb_pe_client.models.widget_type_info",
    "WidgetsBundle": "tb_pe_client.models.widgets_bundle",
    "WidgetsBundleExportData": "tb_pe_client.models.widgets_bundle_export_data",
    "WidgetsBundleId": "tb_pe_client.models.widgets_bundle_id",
    "X509CertificateChainProvisionConfiguration": "tb_pe_client.models.x509_certificate_chain_provision_configuration",
    "X509LwM2MBootstrapServerCredential": "tb_pe_client.models.x509_lw_m2_m_bootstrap_server_credential",
    "YearInterval": "tb_pe_client.models.year_interval",
    "ZoneGroupConfiguration": "tb_pe_client.models.zone_group_configuration",
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
