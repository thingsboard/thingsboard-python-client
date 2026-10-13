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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Union
from uuid import UUID
from tb_paas_client.models.entity_type import EntityType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.admin_settings_id import AdminSettingsId
    from tb_paas_client.models.agent_id import AgentId
    from tb_paas_client.models.agent_application_id import AgentApplicationId
    from tb_paas_client.models.agent_app_event_id import AgentAppEventId
    from tb_paas_client.models.agent_app_profile_id import AgentAppProfileId
    from tb_paas_client.models.agent_app_unit_id import AgentAppUnitId
    from tb_paas_client.models.agent_bulk_action_id import AgentBulkActionId
    from tb_paas_client.models.agent_profile_id import AgentProfileId
    from tb_paas_client.models.ai_model_id import AiModelId
    from tb_paas_client.models.alarm_id import AlarmId
    from tb_paas_client.models.api_key_id import ApiKeyId
    from tb_paas_client.models.api_usage_state_id import ApiUsageStateId
    from tb_paas_client.models.asset_id import AssetId
    from tb_paas_client.models.asset_profile_id import AssetProfileId
    from tb_paas_client.models.billing_customer_id import BillingCustomerId
    from tb_paas_client.models.blob_entity_id import BlobEntityId
    from tb_paas_client.models.calculated_field_id import CalculatedFieldId
    from tb_paas_client.models.converter_id import ConverterId
    from tb_paas_client.models.coupon_id import CouponId
    from tb_paas_client.models.customer_id import CustomerId
    from tb_paas_client.models.dashboard_id import DashboardId
    from tb_paas_client.models.device_id import DeviceId
    from tb_paas_client.models.device_profile_id import DeviceProfileId
    from tb_paas_client.models.domain_id import DomainId
    from tb_paas_client.models.edge_id import EdgeId
    from tb_paas_client.models.entity_group_id import EntityGroupId
    from tb_paas_client.models.entity_view_id import EntityViewId
    from tb_paas_client.models.group_permission_id import GroupPermissionId
    from tb_paas_client.models.integration_id import IntegrationId
    from tb_paas_client.models.job_id import JobId
    from tb_paas_client.models.mobile_app_id import MobileAppId
    from tb_paas_client.models.mobile_app_bundle_id import MobileAppBundleId
    from tb_paas_client.models.notification_id import NotificationId
    from tb_paas_client.models.notification_request_id import NotificationRequestId
    from tb_paas_client.models.notification_rule_id import NotificationRuleId
    from tb_paas_client.models.notification_target_id import NotificationTargetId
    from tb_paas_client.models.notification_template_id import NotificationTemplateId
    from tb_paas_client.models.o_auth2_client_id import OAuth2ClientId
    from tb_paas_client.models.ota_package_id import OtaPackageId
    from tb_paas_client.models.product_id import ProductId
    from tb_paas_client.models.queue_id import QueueId
    from tb_paas_client.models.queue_stats_id import QueueStatsId
    from tb_paas_client.models.report_id import ReportId
    from tb_paas_client.models.report_template_id import ReportTemplateId
    from tb_paas_client.models.role_id import RoleId
    from tb_paas_client.models.rpc_id import RpcId
    from tb_paas_client.models.rule_chain_id import RuleChainId
    from tb_paas_client.models.rule_node_id import RuleNodeId
    from tb_paas_client.models.scheduler_event_id import SchedulerEventId
    from tb_paas_client.models.secret_id import SecretId
    from tb_paas_client.models.subscription_id import SubscriptionId
    from tb_paas_client.models.subscription_addon_id import SubscriptionAddonId
    from tb_paas_client.models.subscription_plan_id import SubscriptionPlanId
    from tb_paas_client.models.tb_resource_id import TbResourceId
    from tb_paas_client.models.tenant_id import TenantId
    from tb_paas_client.models.tenant_profile_id import TenantProfileId
    from tb_paas_client.models.user_id import UserId
    from tb_paas_client.models.widgets_bundle_id import WidgetsBundleId
    from tb_paas_client.models.widget_type_id import WidgetTypeId

class EntityId(BaseModel):
    """
    EntityId
    """ # noqa: E501
    entity_type: EntityType = Field(serialization_alias="entityType")
    id: UUID = Field(description="ID of the entity, time-based UUID v1")
    __properties: ClassVar[List[str]] = ["entityType", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'entityType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ADMIN_SETTINGS': 'AdminSettingsId','AGENT': 'AgentId','AGENT_APPLICATION': 'AgentApplicationId','AGENT_APP_EVENT': 'AgentAppEventId','AGENT_APP_PROFILE': 'AgentAppProfileId','AGENT_APP_UNIT': 'AgentAppUnitId','AGENT_BULK_ACTION': 'AgentBulkActionId','AGENT_PROFILE': 'AgentProfileId','AI_MODEL': 'AiModelId','ALARM': 'AlarmId','API_KEY': 'ApiKeyId','API_USAGE_STATE': 'ApiUsageStateId','ASSET': 'AssetId','ASSET_PROFILE': 'AssetProfileId','BILLING_CUSTOMER': 'BillingCustomerId','BLOB_ENTITY': 'BlobEntityId','CALCULATED_FIELD': 'CalculatedFieldId','CONVERTER': 'ConverterId','COUPON': 'CouponId','CUSTOMER': 'CustomerId','DASHBOARD': 'DashboardId','DEVICE': 'DeviceId','DEVICE_PROFILE': 'DeviceProfileId','DOMAIN': 'DomainId','EDGE': 'EdgeId','ENTITY_GROUP': 'EntityGroupId','ENTITY_VIEW': 'EntityViewId','GROUP_PERMISSION': 'GroupPermissionId','INTEGRATION': 'IntegrationId','JOB': 'JobId','MOBILE_APP': 'MobileAppId','MOBILE_APP_BUNDLE': 'MobileAppBundleId','NOTIFICATION': 'NotificationId','NOTIFICATION_REQUEST': 'NotificationRequestId','NOTIFICATION_RULE': 'NotificationRuleId','NOTIFICATION_TARGET': 'NotificationTargetId','NOTIFICATION_TEMPLATE': 'NotificationTemplateId','OAUTH2_CLIENT': 'OAuth2ClientId','OTA_PACKAGE': 'OtaPackageId','PRODUCT': 'ProductId','QUEUE': 'QueueId','QUEUE_STATS': 'QueueStatsId','REPORT': 'ReportId','REPORT_TEMPLATE': 'ReportTemplateId','ROLE': 'RoleId','RPC': 'RpcId','RULE_CHAIN': 'RuleChainId','RULE_NODE': 'RuleNodeId','SCHEDULER_EVENT': 'SchedulerEventId','SECRET': 'SecretId','SUBSCRIPTION': 'SubscriptionId','SUBSCRIPTION_ADDON': 'SubscriptionAddonId','SUBSCRIPTION_PLAN': 'SubscriptionPlanId','TB_RESOURCE': 'TbResourceId','TENANT': 'TenantId','TENANT_PROFILE': 'TenantProfileId','USER': 'UserId','WIDGETS_BUNDLE': 'WidgetsBundleId','WIDGET_TYPE': 'WidgetTypeId'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.model_dump(by_alias=False, mode='json'))

    def get_id(self) -> str:
        """Returns the entity ID as a string."""
        return str(self.id)

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(entity_type={self.entity_type.value!r}, id={str(self.id)!r})"

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AdminSettingsId, AgentId, AgentApplicationId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentBulkActionId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BillingCustomerId, BlobEntityId, CalculatedFieldId, ConverterId, CouponId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppId, MobileAppBundleId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, ProductId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, SubscriptionId, SubscriptionAddonId, SubscriptionPlanId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetsBundleId, WidgetTypeId]]:
        """Create an instance of EntityId from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AdminSettingsId, AgentId, AgentApplicationId, AgentAppEventId, AgentAppProfileId, AgentAppUnitId, AgentBulkActionId, AgentProfileId, AiModelId, AlarmId, ApiKeyId, ApiUsageStateId, AssetId, AssetProfileId, BillingCustomerId, BlobEntityId, CalculatedFieldId, ConverterId, CouponId, CustomerId, DashboardId, DeviceId, DeviceProfileId, DomainId, EdgeId, EntityGroupId, EntityViewId, GroupPermissionId, IntegrationId, JobId, MobileAppId, MobileAppBundleId, NotificationId, NotificationRequestId, NotificationRuleId, NotificationTargetId, NotificationTemplateId, OAuth2ClientId, OtaPackageId, ProductId, QueueId, QueueStatsId, ReportId, ReportTemplateId, RoleId, RpcId, RuleChainId, RuleNodeId, SchedulerEventId, SecretId, SubscriptionId, SubscriptionAddonId, SubscriptionPlanId, TbResourceId, TenantId, TenantProfileId, UserId, WidgetsBundleId, WidgetTypeId]]:
        """Create an instance of EntityId from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AdminSettingsId':
            return import_module("tb_paas_client.models.admin_settings_id").AdminSettingsId.from_dict(obj)
        if object_type ==  'AgentId':
            return import_module("tb_paas_client.models.agent_id").AgentId.from_dict(obj)
        if object_type ==  'AgentApplicationId':
            return import_module("tb_paas_client.models.agent_application_id").AgentApplicationId.from_dict(obj)
        if object_type ==  'AgentAppEventId':
            return import_module("tb_paas_client.models.agent_app_event_id").AgentAppEventId.from_dict(obj)
        if object_type ==  'AgentAppProfileId':
            return import_module("tb_paas_client.models.agent_app_profile_id").AgentAppProfileId.from_dict(obj)
        if object_type ==  'AgentAppUnitId':
            return import_module("tb_paas_client.models.agent_app_unit_id").AgentAppUnitId.from_dict(obj)
        if object_type ==  'AgentBulkActionId':
            return import_module("tb_paas_client.models.agent_bulk_action_id").AgentBulkActionId.from_dict(obj)
        if object_type ==  'AgentProfileId':
            return import_module("tb_paas_client.models.agent_profile_id").AgentProfileId.from_dict(obj)
        if object_type ==  'AiModelId':
            return import_module("tb_paas_client.models.ai_model_id").AiModelId.from_dict(obj)
        if object_type ==  'AlarmId':
            return import_module("tb_paas_client.models.alarm_id").AlarmId.from_dict(obj)
        if object_type ==  'ApiKeyId':
            return import_module("tb_paas_client.models.api_key_id").ApiKeyId.from_dict(obj)
        if object_type ==  'ApiUsageStateId':
            return import_module("tb_paas_client.models.api_usage_state_id").ApiUsageStateId.from_dict(obj)
        if object_type ==  'AssetId':
            return import_module("tb_paas_client.models.asset_id").AssetId.from_dict(obj)
        if object_type ==  'AssetProfileId':
            return import_module("tb_paas_client.models.asset_profile_id").AssetProfileId.from_dict(obj)
        if object_type ==  'BillingCustomerId':
            return import_module("tb_paas_client.models.billing_customer_id").BillingCustomerId.from_dict(obj)
        if object_type ==  'BlobEntityId':
            return import_module("tb_paas_client.models.blob_entity_id").BlobEntityId.from_dict(obj)
        if object_type ==  'CalculatedFieldId':
            return import_module("tb_paas_client.models.calculated_field_id").CalculatedFieldId.from_dict(obj)
        if object_type ==  'ConverterId':
            return import_module("tb_paas_client.models.converter_id").ConverterId.from_dict(obj)
        if object_type ==  'CouponId':
            return import_module("tb_paas_client.models.coupon_id").CouponId.from_dict(obj)
        if object_type ==  'CustomerId':
            return import_module("tb_paas_client.models.customer_id").CustomerId.from_dict(obj)
        if object_type ==  'DashboardId':
            return import_module("tb_paas_client.models.dashboard_id").DashboardId.from_dict(obj)
        if object_type ==  'DeviceId':
            return import_module("tb_paas_client.models.device_id").DeviceId.from_dict(obj)
        if object_type ==  'DeviceProfileId':
            return import_module("tb_paas_client.models.device_profile_id").DeviceProfileId.from_dict(obj)
        if object_type ==  'DomainId':
            return import_module("tb_paas_client.models.domain_id").DomainId.from_dict(obj)
        if object_type ==  'EdgeId':
            return import_module("tb_paas_client.models.edge_id").EdgeId.from_dict(obj)
        if object_type ==  'EntityGroupId':
            return import_module("tb_paas_client.models.entity_group_id").EntityGroupId.from_dict(obj)
        if object_type ==  'EntityViewId':
            return import_module("tb_paas_client.models.entity_view_id").EntityViewId.from_dict(obj)
        if object_type ==  'GroupPermissionId':
            return import_module("tb_paas_client.models.group_permission_id").GroupPermissionId.from_dict(obj)
        if object_type ==  'IntegrationId':
            return import_module("tb_paas_client.models.integration_id").IntegrationId.from_dict(obj)
        if object_type ==  'JobId':
            return import_module("tb_paas_client.models.job_id").JobId.from_dict(obj)
        if object_type ==  'MobileAppId':
            return import_module("tb_paas_client.models.mobile_app_id").MobileAppId.from_dict(obj)
        if object_type ==  'MobileAppBundleId':
            return import_module("tb_paas_client.models.mobile_app_bundle_id").MobileAppBundleId.from_dict(obj)
        if object_type ==  'NotificationId':
            return import_module("tb_paas_client.models.notification_id").NotificationId.from_dict(obj)
        if object_type ==  'NotificationRequestId':
            return import_module("tb_paas_client.models.notification_request_id").NotificationRequestId.from_dict(obj)
        if object_type ==  'NotificationRuleId':
            return import_module("tb_paas_client.models.notification_rule_id").NotificationRuleId.from_dict(obj)
        if object_type ==  'NotificationTargetId':
            return import_module("tb_paas_client.models.notification_target_id").NotificationTargetId.from_dict(obj)
        if object_type ==  'NotificationTemplateId':
            return import_module("tb_paas_client.models.notification_template_id").NotificationTemplateId.from_dict(obj)
        if object_type ==  'OAuth2ClientId':
            return import_module("tb_paas_client.models.o_auth2_client_id").OAuth2ClientId.from_dict(obj)
        if object_type ==  'OtaPackageId':
            return import_module("tb_paas_client.models.ota_package_id").OtaPackageId.from_dict(obj)
        if object_type ==  'ProductId':
            return import_module("tb_paas_client.models.product_id").ProductId.from_dict(obj)
        if object_type ==  'QueueId':
            return import_module("tb_paas_client.models.queue_id").QueueId.from_dict(obj)
        if object_type ==  'QueueStatsId':
            return import_module("tb_paas_client.models.queue_stats_id").QueueStatsId.from_dict(obj)
        if object_type ==  'ReportId':
            return import_module("tb_paas_client.models.report_id").ReportId.from_dict(obj)
        if object_type ==  'ReportTemplateId':
            return import_module("tb_paas_client.models.report_template_id").ReportTemplateId.from_dict(obj)
        if object_type ==  'RoleId':
            return import_module("tb_paas_client.models.role_id").RoleId.from_dict(obj)
        if object_type ==  'RpcId':
            return import_module("tb_paas_client.models.rpc_id").RpcId.from_dict(obj)
        if object_type ==  'RuleChainId':
            return import_module("tb_paas_client.models.rule_chain_id").RuleChainId.from_dict(obj)
        if object_type ==  'RuleNodeId':
            return import_module("tb_paas_client.models.rule_node_id").RuleNodeId.from_dict(obj)
        if object_type ==  'SchedulerEventId':
            return import_module("tb_paas_client.models.scheduler_event_id").SchedulerEventId.from_dict(obj)
        if object_type ==  'SecretId':
            return import_module("tb_paas_client.models.secret_id").SecretId.from_dict(obj)
        if object_type ==  'SubscriptionId':
            return import_module("tb_paas_client.models.subscription_id").SubscriptionId.from_dict(obj)
        if object_type ==  'SubscriptionAddonId':
            return import_module("tb_paas_client.models.subscription_addon_id").SubscriptionAddonId.from_dict(obj)
        if object_type ==  'SubscriptionPlanId':
            return import_module("tb_paas_client.models.subscription_plan_id").SubscriptionPlanId.from_dict(obj)
        if object_type ==  'TbResourceId':
            return import_module("tb_paas_client.models.tb_resource_id").TbResourceId.from_dict(obj)
        if object_type ==  'TenantId':
            return import_module("tb_paas_client.models.tenant_id").TenantId.from_dict(obj)
        if object_type ==  'TenantProfileId':
            return import_module("tb_paas_client.models.tenant_profile_id").TenantProfileId.from_dict(obj)
        if object_type ==  'UserId':
            return import_module("tb_paas_client.models.user_id").UserId.from_dict(obj)
        if object_type ==  'WidgetsBundleId':
            return import_module("tb_paas_client.models.widgets_bundle_id").WidgetsBundleId.from_dict(obj)
        if object_type ==  'WidgetTypeId':
            return import_module("tb_paas_client.models.widget_type_id").WidgetTypeId.from_dict(obj)

        raise ValueError("EntityId failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


