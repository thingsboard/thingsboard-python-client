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
    "AdminControllerApi",
    "AiChatControllerApi",
    "AiDeviceDashboardControllerApi",
    "AiModelControllerApi",
    "AiSolutionControllerApi",
    "AiToolControllerApi",
    "AlarmCommentControllerApi",
    "AlarmControllerApi",
    "AlarmRuleControllerApi",
    "ApiKeyControllerApi",
    "AssetControllerApi",
    "AssetProfileControllerApi",
    "AuditLogControllerApi",
    "AuthControllerApi",
    "BlobEntityControllerApi",
    "CalculatedFieldControllerApi",
    "ComponentDescriptorControllerApi",
    "ConverterControllerApi",
    "ConverterLibraryControllerApi",
    "CustomMenuControllerApi",
    "CustomTranslationControllerApi",
    "CustomerControllerApi",
    "DashboardControllerApi",
    "DashboardReportControllerApi",
    "DeviceConnectivityControllerApi",
    "DeviceControllerApi",
    "DeviceGroupOtaPackageControllerApi",
    "DeviceProfileControllerApi",
    "DomainControllerApi",
    "EdgeControllerApi",
    "EdgeEventControllerApi",
    "EntitiesVersionControlControllerApi",
    "EntityGroupControllerApi",
    "EntityQueryControllerApi",
    "EntityRelationControllerApi",
    "EntityViewControllerApi",
    "EventControllerApi",
    "GroupPermissionControllerApi",
    "ImageControllerApi",
    "IntegrationControllerApi",
    "JobControllerApi",
    "LoginEndpointApi",
    "Lwm2mControllerApi",
    "MailConfigTemplateControllerApi",
    "MobileAppBundleControllerApi",
    "MobileAppControllerApi",
    "NotificationControllerApi",
    "NotificationRuleControllerApi",
    "NotificationTargetControllerApi",
    "NotificationTemplateControllerApi",
    "OAuth2ConfigTemplateControllerApi",
    "OAuth2ControllerApi",
    "OtaPackageControllerApi",
    "OwnerControllerApi",
    "QrCodeSettingsControllerApi",
    "QueueControllerApi",
    "QueueStatsControllerApi",
    "ReportControllerApi",
    "ReportTemplateControllerApi",
    "RoleControllerApi",
    "RpcV1ControllerApi",
    "RpcV2ControllerApi",
    "RuleChainControllerApi",
    "RuleEngineControllerApi",
    "SchedulerEventControllerApi",
    "SecretControllerApi",
    "SelfRegistrationControllerApi",
    "SignUpControllerApi",
    "SolutionExportImportControllerApi",
    "TbResourceControllerApi",
    "TelemetryControllerApi",
    "TenantControllerApi",
    "TenantProfileControllerApi",
    "TranslationControllerApi",
    "TrendzApiControllerApi",
    "TrendzControllerApi",
    "TwoFactorAuthConfigControllerApi",
    "TwoFactorAuthControllerApi",
    "UiSettingsControllerApi",
    "UsageInfoControllerApi",
    "UserControllerApi",
    "UserPermissionsControllerApi",
    "WhiteLabelingControllerApi",
    "WidgetTypeControllerApi",
    "WidgetsBundleControllerApi",
]

if TYPE_CHECKING:
    from tb_pe_client.api.admin_controller_api import AdminControllerApi
    from tb_pe_client.api.ai_chat_controller_api import AiChatControllerApi
    from tb_pe_client.api.ai_device_dashboard_controller_api import AiDeviceDashboardControllerApi
    from tb_pe_client.api.ai_model_controller_api import AiModelControllerApi
    from tb_pe_client.api.ai_solution_controller_api import AiSolutionControllerApi
    from tb_pe_client.api.ai_tool_controller_api import AiToolControllerApi
    from tb_pe_client.api.alarm_comment_controller_api import AlarmCommentControllerApi
    from tb_pe_client.api.alarm_controller_api import AlarmControllerApi
    from tb_pe_client.api.alarm_rule_controller_api import AlarmRuleControllerApi
    from tb_pe_client.api.api_key_controller_api import ApiKeyControllerApi
    from tb_pe_client.api.asset_controller_api import AssetControllerApi
    from tb_pe_client.api.asset_profile_controller_api import AssetProfileControllerApi
    from tb_pe_client.api.audit_log_controller_api import AuditLogControllerApi
    from tb_pe_client.api.auth_controller_api import AuthControllerApi
    from tb_pe_client.api.blob_entity_controller_api import BlobEntityControllerApi
    from tb_pe_client.api.calculated_field_controller_api import CalculatedFieldControllerApi
    from tb_pe_client.api.component_descriptor_controller_api import ComponentDescriptorControllerApi
    from tb_pe_client.api.converter_controller_api import ConverterControllerApi
    from tb_pe_client.api.converter_library_controller_api import ConverterLibraryControllerApi
    from tb_pe_client.api.custom_menu_controller_api import CustomMenuControllerApi
    from tb_pe_client.api.custom_translation_controller_api import CustomTranslationControllerApi
    from tb_pe_client.api.customer_controller_api import CustomerControllerApi
    from tb_pe_client.api.dashboard_controller_api import DashboardControllerApi
    from tb_pe_client.api.dashboard_report_controller_api import DashboardReportControllerApi
    from tb_pe_client.api.device_connectivity_controller_api import DeviceConnectivityControllerApi
    from tb_pe_client.api.device_controller_api import DeviceControllerApi
    from tb_pe_client.api.device_group_ota_package_controller_api import DeviceGroupOtaPackageControllerApi
    from tb_pe_client.api.device_profile_controller_api import DeviceProfileControllerApi
    from tb_pe_client.api.domain_controller_api import DomainControllerApi
    from tb_pe_client.api.edge_controller_api import EdgeControllerApi
    from tb_pe_client.api.edge_event_controller_api import EdgeEventControllerApi
    from tb_pe_client.api.entities_version_control_controller_api import EntitiesVersionControlControllerApi
    from tb_pe_client.api.entity_group_controller_api import EntityGroupControllerApi
    from tb_pe_client.api.entity_query_controller_api import EntityQueryControllerApi
    from tb_pe_client.api.entity_relation_controller_api import EntityRelationControllerApi
    from tb_pe_client.api.entity_view_controller_api import EntityViewControllerApi
    from tb_pe_client.api.event_controller_api import EventControllerApi
    from tb_pe_client.api.group_permission_controller_api import GroupPermissionControllerApi
    from tb_pe_client.api.image_controller_api import ImageControllerApi
    from tb_pe_client.api.integration_controller_api import IntegrationControllerApi
    from tb_pe_client.api.job_controller_api import JobControllerApi
    from tb_pe_client.api.login_endpoint_api import LoginEndpointApi
    from tb_pe_client.api.lwm2m_controller_api import Lwm2mControllerApi
    from tb_pe_client.api.mail_config_template_controller_api import MailConfigTemplateControllerApi
    from tb_pe_client.api.mobile_app_bundle_controller_api import MobileAppBundleControllerApi
    from tb_pe_client.api.mobile_app_controller_api import MobileAppControllerApi
    from tb_pe_client.api.notification_controller_api import NotificationControllerApi
    from tb_pe_client.api.notification_rule_controller_api import NotificationRuleControllerApi
    from tb_pe_client.api.notification_target_controller_api import NotificationTargetControllerApi
    from tb_pe_client.api.notification_template_controller_api import NotificationTemplateControllerApi
    from tb_pe_client.api.o_auth2_config_template_controller_api import OAuth2ConfigTemplateControllerApi
    from tb_pe_client.api.o_auth2_controller_api import OAuth2ControllerApi
    from tb_pe_client.api.ota_package_controller_api import OtaPackageControllerApi
    from tb_pe_client.api.owner_controller_api import OwnerControllerApi
    from tb_pe_client.api.qr_code_settings_controller_api import QrCodeSettingsControllerApi
    from tb_pe_client.api.queue_controller_api import QueueControllerApi
    from tb_pe_client.api.queue_stats_controller_api import QueueStatsControllerApi
    from tb_pe_client.api.report_controller_api import ReportControllerApi
    from tb_pe_client.api.report_template_controller_api import ReportTemplateControllerApi
    from tb_pe_client.api.role_controller_api import RoleControllerApi
    from tb_pe_client.api.rpc_v1_controller_api import RpcV1ControllerApi
    from tb_pe_client.api.rpc_v2_controller_api import RpcV2ControllerApi
    from tb_pe_client.api.rule_chain_controller_api import RuleChainControllerApi
    from tb_pe_client.api.rule_engine_controller_api import RuleEngineControllerApi
    from tb_pe_client.api.scheduler_event_controller_api import SchedulerEventControllerApi
    from tb_pe_client.api.secret_controller_api import SecretControllerApi
    from tb_pe_client.api.self_registration_controller_api import SelfRegistrationControllerApi
    from tb_pe_client.api.sign_up_controller_api import SignUpControllerApi
    from tb_pe_client.api.solution_export_import_controller_api import SolutionExportImportControllerApi
    from tb_pe_client.api.tb_resource_controller_api import TbResourceControllerApi
    from tb_pe_client.api.telemetry_controller_api import TelemetryControllerApi
    from tb_pe_client.api.tenant_controller_api import TenantControllerApi
    from tb_pe_client.api.tenant_profile_controller_api import TenantProfileControllerApi
    from tb_pe_client.api.translation_controller_api import TranslationControllerApi
    from tb_pe_client.api.trendz_api_controller_api import TrendzApiControllerApi
    from tb_pe_client.api.trendz_controller_api import TrendzControllerApi
    from tb_pe_client.api.two_factor_auth_config_controller_api import TwoFactorAuthConfigControllerApi
    from tb_pe_client.api.two_factor_auth_controller_api import TwoFactorAuthControllerApi
    from tb_pe_client.api.ui_settings_controller_api import UiSettingsControllerApi
    from tb_pe_client.api.usage_info_controller_api import UsageInfoControllerApi
    from tb_pe_client.api.user_controller_api import UserControllerApi
    from tb_pe_client.api.user_permissions_controller_api import UserPermissionsControllerApi
    from tb_pe_client.api.white_labeling_controller_api import WhiteLabelingControllerApi
    from tb_pe_client.api.widget_type_controller_api import WidgetTypeControllerApi
    from tb_pe_client.api.widgets_bundle_controller_api import WidgetsBundleControllerApi

_API_CLASSES = {
    "AdminControllerApi": "tb_pe_client.api.admin_controller_api",
    "AiChatControllerApi": "tb_pe_client.api.ai_chat_controller_api",
    "AiDeviceDashboardControllerApi": "tb_pe_client.api.ai_device_dashboard_controller_api",
    "AiModelControllerApi": "tb_pe_client.api.ai_model_controller_api",
    "AiSolutionControllerApi": "tb_pe_client.api.ai_solution_controller_api",
    "AiToolControllerApi": "tb_pe_client.api.ai_tool_controller_api",
    "AlarmCommentControllerApi": "tb_pe_client.api.alarm_comment_controller_api",
    "AlarmControllerApi": "tb_pe_client.api.alarm_controller_api",
    "AlarmRuleControllerApi": "tb_pe_client.api.alarm_rule_controller_api",
    "ApiKeyControllerApi": "tb_pe_client.api.api_key_controller_api",
    "AssetControllerApi": "tb_pe_client.api.asset_controller_api",
    "AssetProfileControllerApi": "tb_pe_client.api.asset_profile_controller_api",
    "AuditLogControllerApi": "tb_pe_client.api.audit_log_controller_api",
    "AuthControllerApi": "tb_pe_client.api.auth_controller_api",
    "BlobEntityControllerApi": "tb_pe_client.api.blob_entity_controller_api",
    "CalculatedFieldControllerApi": "tb_pe_client.api.calculated_field_controller_api",
    "ComponentDescriptorControllerApi": "tb_pe_client.api.component_descriptor_controller_api",
    "ConverterControllerApi": "tb_pe_client.api.converter_controller_api",
    "ConverterLibraryControllerApi": "tb_pe_client.api.converter_library_controller_api",
    "CustomMenuControllerApi": "tb_pe_client.api.custom_menu_controller_api",
    "CustomTranslationControllerApi": "tb_pe_client.api.custom_translation_controller_api",
    "CustomerControllerApi": "tb_pe_client.api.customer_controller_api",
    "DashboardControllerApi": "tb_pe_client.api.dashboard_controller_api",
    "DashboardReportControllerApi": "tb_pe_client.api.dashboard_report_controller_api",
    "DeviceConnectivityControllerApi": "tb_pe_client.api.device_connectivity_controller_api",
    "DeviceControllerApi": "tb_pe_client.api.device_controller_api",
    "DeviceGroupOtaPackageControllerApi": "tb_pe_client.api.device_group_ota_package_controller_api",
    "DeviceProfileControllerApi": "tb_pe_client.api.device_profile_controller_api",
    "DomainControllerApi": "tb_pe_client.api.domain_controller_api",
    "EdgeControllerApi": "tb_pe_client.api.edge_controller_api",
    "EdgeEventControllerApi": "tb_pe_client.api.edge_event_controller_api",
    "EntitiesVersionControlControllerApi": "tb_pe_client.api.entities_version_control_controller_api",
    "EntityGroupControllerApi": "tb_pe_client.api.entity_group_controller_api",
    "EntityQueryControllerApi": "tb_pe_client.api.entity_query_controller_api",
    "EntityRelationControllerApi": "tb_pe_client.api.entity_relation_controller_api",
    "EntityViewControllerApi": "tb_pe_client.api.entity_view_controller_api",
    "EventControllerApi": "tb_pe_client.api.event_controller_api",
    "GroupPermissionControllerApi": "tb_pe_client.api.group_permission_controller_api",
    "ImageControllerApi": "tb_pe_client.api.image_controller_api",
    "IntegrationControllerApi": "tb_pe_client.api.integration_controller_api",
    "JobControllerApi": "tb_pe_client.api.job_controller_api",
    "LoginEndpointApi": "tb_pe_client.api.login_endpoint_api",
    "Lwm2mControllerApi": "tb_pe_client.api.lwm2m_controller_api",
    "MailConfigTemplateControllerApi": "tb_pe_client.api.mail_config_template_controller_api",
    "MobileAppBundleControllerApi": "tb_pe_client.api.mobile_app_bundle_controller_api",
    "MobileAppControllerApi": "tb_pe_client.api.mobile_app_controller_api",
    "NotificationControllerApi": "tb_pe_client.api.notification_controller_api",
    "NotificationRuleControllerApi": "tb_pe_client.api.notification_rule_controller_api",
    "NotificationTargetControllerApi": "tb_pe_client.api.notification_target_controller_api",
    "NotificationTemplateControllerApi": "tb_pe_client.api.notification_template_controller_api",
    "OAuth2ConfigTemplateControllerApi": "tb_pe_client.api.o_auth2_config_template_controller_api",
    "OAuth2ControllerApi": "tb_pe_client.api.o_auth2_controller_api",
    "OtaPackageControllerApi": "tb_pe_client.api.ota_package_controller_api",
    "OwnerControllerApi": "tb_pe_client.api.owner_controller_api",
    "QrCodeSettingsControllerApi": "tb_pe_client.api.qr_code_settings_controller_api",
    "QueueControllerApi": "tb_pe_client.api.queue_controller_api",
    "QueueStatsControllerApi": "tb_pe_client.api.queue_stats_controller_api",
    "ReportControllerApi": "tb_pe_client.api.report_controller_api",
    "ReportTemplateControllerApi": "tb_pe_client.api.report_template_controller_api",
    "RoleControllerApi": "tb_pe_client.api.role_controller_api",
    "RpcV1ControllerApi": "tb_pe_client.api.rpc_v1_controller_api",
    "RpcV2ControllerApi": "tb_pe_client.api.rpc_v2_controller_api",
    "RuleChainControllerApi": "tb_pe_client.api.rule_chain_controller_api",
    "RuleEngineControllerApi": "tb_pe_client.api.rule_engine_controller_api",
    "SchedulerEventControllerApi": "tb_pe_client.api.scheduler_event_controller_api",
    "SecretControllerApi": "tb_pe_client.api.secret_controller_api",
    "SelfRegistrationControllerApi": "tb_pe_client.api.self_registration_controller_api",
    "SignUpControllerApi": "tb_pe_client.api.sign_up_controller_api",
    "SolutionExportImportControllerApi": "tb_pe_client.api.solution_export_import_controller_api",
    "TbResourceControllerApi": "tb_pe_client.api.tb_resource_controller_api",
    "TelemetryControllerApi": "tb_pe_client.api.telemetry_controller_api",
    "TenantControllerApi": "tb_pe_client.api.tenant_controller_api",
    "TenantProfileControllerApi": "tb_pe_client.api.tenant_profile_controller_api",
    "TranslationControllerApi": "tb_pe_client.api.translation_controller_api",
    "TrendzApiControllerApi": "tb_pe_client.api.trendz_api_controller_api",
    "TrendzControllerApi": "tb_pe_client.api.trendz_controller_api",
    "TwoFactorAuthConfigControllerApi": "tb_pe_client.api.two_factor_auth_config_controller_api",
    "TwoFactorAuthControllerApi": "tb_pe_client.api.two_factor_auth_controller_api",
    "UiSettingsControllerApi": "tb_pe_client.api.ui_settings_controller_api",
    "UsageInfoControllerApi": "tb_pe_client.api.usage_info_controller_api",
    "UserControllerApi": "tb_pe_client.api.user_controller_api",
    "UserPermissionsControllerApi": "tb_pe_client.api.user_permissions_controller_api",
    "WhiteLabelingControllerApi": "tb_pe_client.api.white_labeling_controller_api",
    "WidgetTypeControllerApi": "tb_pe_client.api.widget_type_controller_api",
    "WidgetsBundleControllerApi": "tb_pe_client.api.widgets_bundle_controller_api",
}

def __getattr__(name: str):
    if name in _API_CLASSES:
        module = importlib.import_module(_API_CLASSES[name])
        cls = getattr(module, name)
        globals()[name] = cls  # Cache for subsequent access
        return cls
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

def __dir__():
    return list(_API_CLASSES.keys())
