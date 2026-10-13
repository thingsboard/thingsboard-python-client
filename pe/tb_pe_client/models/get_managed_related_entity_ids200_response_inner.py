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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tb_pe_client.models.admin_settings_id import AdminSettingsId
from tb_pe_client.models.agent_app_event_id import AgentAppEventId
from tb_pe_client.models.agent_app_profile_id import AgentAppProfileId
from tb_pe_client.models.agent_app_unit_id import AgentAppUnitId
from tb_pe_client.models.agent_application_id import AgentApplicationId
from tb_pe_client.models.agent_bulk_action_id import AgentBulkActionId
from tb_pe_client.models.agent_id import AgentId
from tb_pe_client.models.agent_profile_id import AgentProfileId
from tb_pe_client.models.ai_model_id import AiModelId
from tb_pe_client.models.alarm_id import AlarmId
from tb_pe_client.models.api_key_id import ApiKeyId
from tb_pe_client.models.api_usage_state_id import ApiUsageStateId
from tb_pe_client.models.asset_id import AssetId
from tb_pe_client.models.asset_profile_id import AssetProfileId
from tb_pe_client.models.blob_entity_id import BlobEntityId
from tb_pe_client.models.calculated_field_id import CalculatedFieldId
from tb_pe_client.models.converter_id import ConverterId
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.dashboard_id import DashboardId
from tb_pe_client.models.device_id import DeviceId
from tb_pe_client.models.device_profile_id import DeviceProfileId
from tb_pe_client.models.domain_id import DomainId
from tb_pe_client.models.edge_id import EdgeId
from tb_pe_client.models.entity_group_id import EntityGroupId
from tb_pe_client.models.entity_view_id import EntityViewId
from tb_pe_client.models.group_permission_id import GroupPermissionId
from tb_pe_client.models.integration_id import IntegrationId
from tb_pe_client.models.job_id import JobId
from tb_pe_client.models.mobile_app_bundle_id import MobileAppBundleId
from tb_pe_client.models.mobile_app_id import MobileAppId
from tb_pe_client.models.notification_id import NotificationId
from tb_pe_client.models.notification_request_id import NotificationRequestId
from tb_pe_client.models.notification_rule_id import NotificationRuleId
from tb_pe_client.models.notification_target_id import NotificationTargetId
from tb_pe_client.models.notification_template_id import NotificationTemplateId
from tb_pe_client.models.o_auth2_client_id import OAuth2ClientId
from tb_pe_client.models.ota_package_id import OtaPackageId
from tb_pe_client.models.queue_id import QueueId
from tb_pe_client.models.queue_stats_id import QueueStatsId
from tb_pe_client.models.report_id import ReportId
from tb_pe_client.models.report_template_id import ReportTemplateId
from tb_pe_client.models.role_id import RoleId
from tb_pe_client.models.rpc_id import RpcId
from tb_pe_client.models.rule_chain_id import RuleChainId
from tb_pe_client.models.rule_node_id import RuleNodeId
from tb_pe_client.models.scheduler_event_id import SchedulerEventId
from tb_pe_client.models.secret_id import SecretId
from tb_pe_client.models.tb_resource_id import TbResourceId
from tb_pe_client.models.tenant_id import TenantId
from tb_pe_client.models.tenant_profile_id import TenantProfileId
from tb_pe_client.models.user_id import UserId
from tb_pe_client.models.widget_type_id import WidgetTypeId
from tb_pe_client.models.widgets_bundle_id import WidgetsBundleId
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETMANAGEDRELATEDENTITYIDS200RESPONSEINNER_ONE_OF_SCHEMAS = ["AdminSettingsId", "AgentAppEventId", "AgentAppProfileId", "AgentAppUnitId", "AgentApplicationId", "AgentBulkActionId", "AgentId", "AgentProfileId", "AiModelId", "AlarmId", "ApiKeyId", "ApiUsageStateId", "AssetId", "AssetProfileId", "BlobEntityId", "CalculatedFieldId", "ConverterId", "CustomerId", "DashboardId", "DeviceId", "DeviceProfileId", "DomainId", "EdgeId", "EntityGroupId", "EntityViewId", "GroupPermissionId", "IntegrationId", "JobId", "MobileAppBundleId", "MobileAppId", "NotificationId", "NotificationRequestId", "NotificationRuleId", "NotificationTargetId", "NotificationTemplateId", "OAuth2ClientId", "OtaPackageId", "QueueId", "QueueStatsId", "ReportId", "ReportTemplateId", "RoleId", "RpcId", "RuleChainId", "RuleNodeId", "SchedulerEventId", "SecretId", "TbResourceId", "TenantId", "TenantProfileId", "UserId", "WidgetTypeId", "WidgetsBundleId"]

class GetManagedRelatedEntityIds200ResponseInner(BaseModel):
    """
    GetManagedRelatedEntityIds200ResponseInner
    """
    # data type: AdminSettingsId
    oneof_schema_1_validator: Optional[AdminSettingsId] = None
    # data type: AgentAppEventId
    oneof_schema_2_validator: Optional[AgentAppEventId] = None
    # data type: AgentAppProfileId
    oneof_schema_3_validator: Optional[AgentAppProfileId] = None
    # data type: AgentAppUnitId
    oneof_schema_4_validator: Optional[AgentAppUnitId] = None
    # data type: AgentApplicationId
    oneof_schema_5_validator: Optional[AgentApplicationId] = None
    # data type: AgentBulkActionId
    oneof_schema_6_validator: Optional[AgentBulkActionId] = None
    # data type: AgentId
    oneof_schema_7_validator: Optional[AgentId] = None
    # data type: AgentProfileId
    oneof_schema_8_validator: Optional[AgentProfileId] = None
    # data type: AiModelId
    oneof_schema_9_validator: Optional[AiModelId] = None
    # data type: AlarmId
    oneof_schema_10_validator: Optional[AlarmId] = None
    # data type: ApiKeyId
    oneof_schema_11_validator: Optional[ApiKeyId] = None
    # data type: ApiUsageStateId
    oneof_schema_12_validator: Optional[ApiUsageStateId] = None
    # data type: AssetId
    oneof_schema_13_validator: Optional[AssetId] = None
    # data type: AssetProfileId
    oneof_schema_14_validator: Optional[AssetProfileId] = None
    # data type: BlobEntityId
    oneof_schema_15_validator: Optional[BlobEntityId] = None
    # data type: CalculatedFieldId
    oneof_schema_16_validator: Optional[CalculatedFieldId] = None
    # data type: ConverterId
    oneof_schema_17_validator: Optional[ConverterId] = None
    # data type: CustomerId
    oneof_schema_18_validator: Optional[CustomerId] = None
    # data type: DashboardId
    oneof_schema_19_validator: Optional[DashboardId] = None
    # data type: DeviceId
    oneof_schema_20_validator: Optional[DeviceId] = None
    # data type: DeviceProfileId
    oneof_schema_21_validator: Optional[DeviceProfileId] = None
    # data type: DomainId
    oneof_schema_22_validator: Optional[DomainId] = None
    # data type: EdgeId
    oneof_schema_23_validator: Optional[EdgeId] = None
    # data type: EntityGroupId
    oneof_schema_24_validator: Optional[EntityGroupId] = None
    # data type: EntityViewId
    oneof_schema_25_validator: Optional[EntityViewId] = None
    # data type: GroupPermissionId
    oneof_schema_26_validator: Optional[GroupPermissionId] = None
    # data type: IntegrationId
    oneof_schema_27_validator: Optional[IntegrationId] = None
    # data type: JobId
    oneof_schema_28_validator: Optional[JobId] = None
    # data type: MobileAppBundleId
    oneof_schema_29_validator: Optional[MobileAppBundleId] = None
    # data type: MobileAppId
    oneof_schema_30_validator: Optional[MobileAppId] = None
    # data type: NotificationId
    oneof_schema_31_validator: Optional[NotificationId] = None
    # data type: NotificationRequestId
    oneof_schema_32_validator: Optional[NotificationRequestId] = None
    # data type: NotificationRuleId
    oneof_schema_33_validator: Optional[NotificationRuleId] = None
    # data type: NotificationTargetId
    oneof_schema_34_validator: Optional[NotificationTargetId] = None
    # data type: NotificationTemplateId
    oneof_schema_35_validator: Optional[NotificationTemplateId] = None
    # data type: OAuth2ClientId
    oneof_schema_36_validator: Optional[OAuth2ClientId] = None
    # data type: OtaPackageId
    oneof_schema_37_validator: Optional[OtaPackageId] = None
    # data type: QueueId
    oneof_schema_38_validator: Optional[QueueId] = None
    # data type: QueueStatsId
    oneof_schema_39_validator: Optional[QueueStatsId] = None
    # data type: ReportId
    oneof_schema_40_validator: Optional[ReportId] = None
    # data type: ReportTemplateId
    oneof_schema_41_validator: Optional[ReportTemplateId] = None
    # data type: RoleId
    oneof_schema_42_validator: Optional[RoleId] = None
    # data type: RpcId
    oneof_schema_43_validator: Optional[RpcId] = None
    # data type: RuleChainId
    oneof_schema_44_validator: Optional[RuleChainId] = None
    # data type: RuleNodeId
    oneof_schema_45_validator: Optional[RuleNodeId] = None
    # data type: SchedulerEventId
    oneof_schema_46_validator: Optional[SchedulerEventId] = None
    # data type: SecretId
    oneof_schema_47_validator: Optional[SecretId] = None
    # data type: TbResourceId
    oneof_schema_48_validator: Optional[TbResourceId] = None
    # data type: TenantId
    oneof_schema_49_validator: Optional[TenantId] = None
    # data type: TenantProfileId
    oneof_schema_50_validator: Optional[TenantProfileId] = None
    # data type: UserId
    oneof_schema_51_validator: Optional[UserId] = None
    # data type: WidgetTypeId
    oneof_schema_52_validator: Optional[WidgetTypeId] = None
    # data type: WidgetsBundleId
    oneof_schema_53_validator: Optional[WidgetsBundleId] = None
    actual_instance: Optional[Union[AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId]] = None
    one_of_schemas: Set[str] = { "AdminSettingsId", "AgentAppEventId", "AgentAppProfileId", "AgentAppUnitId", "AgentApplicationId", "AgentBulkActionId", "AgentId", "AgentProfileId", "AiModelId", "AlarmId", "ApiKeyId", "ApiUsageStateId", "AssetId", "AssetProfileId", "BlobEntityId", "CalculatedFieldId", "ConverterId", "CustomerId", "DashboardId", "DeviceId", "DeviceProfileId", "DomainId", "EdgeId", "EntityGroupId", "EntityViewId", "GroupPermissionId", "IntegrationId", "JobId", "MobileAppBundleId", "MobileAppId", "NotificationId", "NotificationRequestId", "NotificationRuleId", "NotificationTargetId", "NotificationTemplateId", "OAuth2ClientId", "OtaPackageId", "QueueId", "QueueStatsId", "ReportId", "ReportTemplateId", "RoleId", "RpcId", "RuleChainId", "RuleNodeId", "SchedulerEventId", "SecretId", "TbResourceId", "TenantId", "TenantProfileId", "UserId", "WidgetTypeId", "WidgetsBundleId" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetManagedRelatedEntityIds200ResponseInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: AdminSettingsId
        if not isinstance(v, AdminSettingsId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AdminSettingsId`")
        else:
            match += 1
        # validate data type: AgentAppEventId
        if not isinstance(v, AgentAppEventId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentAppEventId`")
        else:
            match += 1
        # validate data type: AgentAppProfileId
        if not isinstance(v, AgentAppProfileId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentAppProfileId`")
        else:
            match += 1
        # validate data type: AgentAppUnitId
        if not isinstance(v, AgentAppUnitId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentAppUnitId`")
        else:
            match += 1
        # validate data type: AgentApplicationId
        if not isinstance(v, AgentApplicationId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentApplicationId`")
        else:
            match += 1
        # validate data type: AgentBulkActionId
        if not isinstance(v, AgentBulkActionId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentBulkActionId`")
        else:
            match += 1
        # validate data type: AgentId
        if not isinstance(v, AgentId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentId`")
        else:
            match += 1
        # validate data type: AgentProfileId
        if not isinstance(v, AgentProfileId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentProfileId`")
        else:
            match += 1
        # validate data type: AiModelId
        if not isinstance(v, AiModelId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AiModelId`")
        else:
            match += 1
        # validate data type: AlarmId
        if not isinstance(v, AlarmId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AlarmId`")
        else:
            match += 1
        # validate data type: ApiKeyId
        if not isinstance(v, ApiKeyId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiKeyId`")
        else:
            match += 1
        # validate data type: ApiUsageStateId
        if not isinstance(v, ApiUsageStateId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiUsageStateId`")
        else:
            match += 1
        # validate data type: AssetId
        if not isinstance(v, AssetId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AssetId`")
        else:
            match += 1
        # validate data type: AssetProfileId
        if not isinstance(v, AssetProfileId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AssetProfileId`")
        else:
            match += 1
        # validate data type: BlobEntityId
        if not isinstance(v, BlobEntityId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BlobEntityId`")
        else:
            match += 1
        # validate data type: CalculatedFieldId
        if not isinstance(v, CalculatedFieldId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CalculatedFieldId`")
        else:
            match += 1
        # validate data type: ConverterId
        if not isinstance(v, ConverterId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConverterId`")
        else:
            match += 1
        # validate data type: CustomerId
        if not isinstance(v, CustomerId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustomerId`")
        else:
            match += 1
        # validate data type: DashboardId
        if not isinstance(v, DashboardId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DashboardId`")
        else:
            match += 1
        # validate data type: DeviceId
        if not isinstance(v, DeviceId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeviceId`")
        else:
            match += 1
        # validate data type: DeviceProfileId
        if not isinstance(v, DeviceProfileId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DeviceProfileId`")
        else:
            match += 1
        # validate data type: DomainId
        if not isinstance(v, DomainId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DomainId`")
        else:
            match += 1
        # validate data type: EdgeId
        if not isinstance(v, EdgeId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EdgeId`")
        else:
            match += 1
        # validate data type: EntityGroupId
        if not isinstance(v, EntityGroupId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EntityGroupId`")
        else:
            match += 1
        # validate data type: EntityViewId
        if not isinstance(v, EntityViewId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EntityViewId`")
        else:
            match += 1
        # validate data type: GroupPermissionId
        if not isinstance(v, GroupPermissionId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GroupPermissionId`")
        else:
            match += 1
        # validate data type: IntegrationId
        if not isinstance(v, IntegrationId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IntegrationId`")
        else:
            match += 1
        # validate data type: JobId
        if not isinstance(v, JobId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `JobId`")
        else:
            match += 1
        # validate data type: MobileAppBundleId
        if not isinstance(v, MobileAppBundleId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MobileAppBundleId`")
        else:
            match += 1
        # validate data type: MobileAppId
        if not isinstance(v, MobileAppId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MobileAppId`")
        else:
            match += 1
        # validate data type: NotificationId
        if not isinstance(v, NotificationId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NotificationId`")
        else:
            match += 1
        # validate data type: NotificationRequestId
        if not isinstance(v, NotificationRequestId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NotificationRequestId`")
        else:
            match += 1
        # validate data type: NotificationRuleId
        if not isinstance(v, NotificationRuleId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NotificationRuleId`")
        else:
            match += 1
        # validate data type: NotificationTargetId
        if not isinstance(v, NotificationTargetId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NotificationTargetId`")
        else:
            match += 1
        # validate data type: NotificationTemplateId
        if not isinstance(v, NotificationTemplateId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NotificationTemplateId`")
        else:
            match += 1
        # validate data type: OAuth2ClientId
        if not isinstance(v, OAuth2ClientId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OAuth2ClientId`")
        else:
            match += 1
        # validate data type: OtaPackageId
        if not isinstance(v, OtaPackageId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OtaPackageId`")
        else:
            match += 1
        # validate data type: QueueId
        if not isinstance(v, QueueId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QueueId`")
        else:
            match += 1
        # validate data type: QueueStatsId
        if not isinstance(v, QueueStatsId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QueueStatsId`")
        else:
            match += 1
        # validate data type: ReportId
        if not isinstance(v, ReportId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReportId`")
        else:
            match += 1
        # validate data type: ReportTemplateId
        if not isinstance(v, ReportTemplateId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReportTemplateId`")
        else:
            match += 1
        # validate data type: RoleId
        if not isinstance(v, RoleId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RoleId`")
        else:
            match += 1
        # validate data type: RpcId
        if not isinstance(v, RpcId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RpcId`")
        else:
            match += 1
        # validate data type: RuleChainId
        if not isinstance(v, RuleChainId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RuleChainId`")
        else:
            match += 1
        # validate data type: RuleNodeId
        if not isinstance(v, RuleNodeId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RuleNodeId`")
        else:
            match += 1
        # validate data type: SchedulerEventId
        if not isinstance(v, SchedulerEventId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SchedulerEventId`")
        else:
            match += 1
        # validate data type: SecretId
        if not isinstance(v, SecretId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SecretId`")
        else:
            match += 1
        # validate data type: TbResourceId
        if not isinstance(v, TbResourceId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TbResourceId`")
        else:
            match += 1
        # validate data type: TenantId
        if not isinstance(v, TenantId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TenantId`")
        else:
            match += 1
        # validate data type: TenantProfileId
        if not isinstance(v, TenantProfileId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TenantProfileId`")
        else:
            match += 1
        # validate data type: UserId
        if not isinstance(v, UserId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UserId`")
        else:
            match += 1
        # validate data type: WidgetTypeId
        if not isinstance(v, WidgetTypeId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WidgetTypeId`")
        else:
            match += 1
        # validate data type: WidgetsBundleId
        if not isinstance(v, WidgetsBundleId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WidgetsBundleId`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetManagedRelatedEntityIds200ResponseInner with oneOf schemas: AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetManagedRelatedEntityIds200ResponseInner with oneOf schemas: AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AdminSettingsId
        try:
            instance.actual_instance = AdminSettingsId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentAppEventId
        try:
            instance.actual_instance = AgentAppEventId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentAppProfileId
        try:
            instance.actual_instance = AgentAppProfileId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentAppUnitId
        try:
            instance.actual_instance = AgentAppUnitId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentApplicationId
        try:
            instance.actual_instance = AgentApplicationId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentBulkActionId
        try:
            instance.actual_instance = AgentBulkActionId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentId
        try:
            instance.actual_instance = AgentId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentProfileId
        try:
            instance.actual_instance = AgentProfileId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AiModelId
        try:
            instance.actual_instance = AiModelId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AlarmId
        try:
            instance.actual_instance = AlarmId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiKeyId
        try:
            instance.actual_instance = ApiKeyId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiUsageStateId
        try:
            instance.actual_instance = ApiUsageStateId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AssetId
        try:
            instance.actual_instance = AssetId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AssetProfileId
        try:
            instance.actual_instance = AssetProfileId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BlobEntityId
        try:
            instance.actual_instance = BlobEntityId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CalculatedFieldId
        try:
            instance.actual_instance = CalculatedFieldId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConverterId
        try:
            instance.actual_instance = ConverterId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CustomerId
        try:
            instance.actual_instance = CustomerId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DashboardId
        try:
            instance.actual_instance = DashboardId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DeviceId
        try:
            instance.actual_instance = DeviceId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DeviceProfileId
        try:
            instance.actual_instance = DeviceProfileId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DomainId
        try:
            instance.actual_instance = DomainId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EdgeId
        try:
            instance.actual_instance = EdgeId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EntityGroupId
        try:
            instance.actual_instance = EntityGroupId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EntityViewId
        try:
            instance.actual_instance = EntityViewId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GroupPermissionId
        try:
            instance.actual_instance = GroupPermissionId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IntegrationId
        try:
            instance.actual_instance = IntegrationId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into JobId
        try:
            instance.actual_instance = JobId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MobileAppBundleId
        try:
            instance.actual_instance = MobileAppBundleId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MobileAppId
        try:
            instance.actual_instance = MobileAppId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NotificationId
        try:
            instance.actual_instance = NotificationId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NotificationRequestId
        try:
            instance.actual_instance = NotificationRequestId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NotificationRuleId
        try:
            instance.actual_instance = NotificationRuleId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NotificationTargetId
        try:
            instance.actual_instance = NotificationTargetId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NotificationTemplateId
        try:
            instance.actual_instance = NotificationTemplateId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OAuth2ClientId
        try:
            instance.actual_instance = OAuth2ClientId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OtaPackageId
        try:
            instance.actual_instance = OtaPackageId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into QueueId
        try:
            instance.actual_instance = QueueId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into QueueStatsId
        try:
            instance.actual_instance = QueueStatsId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReportId
        try:
            instance.actual_instance = ReportId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReportTemplateId
        try:
            instance.actual_instance = ReportTemplateId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RoleId
        try:
            instance.actual_instance = RoleId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RpcId
        try:
            instance.actual_instance = RpcId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RuleChainId
        try:
            instance.actual_instance = RuleChainId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RuleNodeId
        try:
            instance.actual_instance = RuleNodeId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SchedulerEventId
        try:
            instance.actual_instance = SchedulerEventId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SecretId
        try:
            instance.actual_instance = SecretId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TbResourceId
        try:
            instance.actual_instance = TbResourceId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TenantId
        try:
            instance.actual_instance = TenantId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TenantProfileId
        try:
            instance.actual_instance = TenantProfileId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UserId
        try:
            instance.actual_instance = UserId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WidgetTypeId
        try:
            instance.actual_instance = WidgetTypeId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into WidgetsBundleId
        try:
            instance.actual_instance = WidgetsBundleId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetManagedRelatedEntityIds200ResponseInner with oneOf schemas: AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetManagedRelatedEntityIds200ResponseInner with oneOf schemas: AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AdminSettingsId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentApplicationId, AgentBulkActionId, AgentId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BlobEntityId, CalculatedFieldId, ConverterId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppBundleId, MobileAppId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetTypeId, WidgetsBundleId]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump(mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()


