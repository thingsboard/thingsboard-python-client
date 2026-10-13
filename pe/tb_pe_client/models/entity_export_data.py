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
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.attribute_export_data import AttributeExportData
from tb_pe_client.models.calculated_field import CalculatedField
from tb_pe_client.models.entity_relation import EntityRelation
from tb_pe_client.models.entity_type import EntityType
from tb_pe_client.models.exportable_entity import ExportableEntity
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.ai_model_export_data import AiModelExportData
    from tb_pe_client.models.asset_export_data import AssetExportData
    from tb_pe_client.models.asset_profile_export_data import AssetProfileExportData
    from tb_pe_client.models.converter_export_data import ConverterExportData
    from tb_pe_client.models.customer_export_data import CustomerExportData
    from tb_pe_client.models.dashboard_export_data import DashboardExportData
    from tb_pe_client.models.device_export_data import DeviceExportData
    from tb_pe_client.models.device_profile_export_data import DeviceProfileExportData
    from tb_pe_client.models.entity_group_export_data import EntityGroupExportData
    from tb_pe_client.models.entity_view_export_data import EntityViewExportData
    from tb_pe_client.models.integration_export_data import IntegrationExportData
    from tb_pe_client.models.notification_rule_export_data import NotificationRuleExportData
    from tb_pe_client.models.notification_target_export_data import NotificationTargetExportData
    from tb_pe_client.models.notification_template_export_data import NotificationTemplateExportData
    from tb_pe_client.models.ota_package_export_data import OtaPackageExportData
    from tb_pe_client.models.report_template_export_data import ReportTemplateExportData
    from tb_pe_client.models.role_export_data import RoleExportData
    from tb_pe_client.models.rule_chain_export_data import RuleChainExportData
    from tb_pe_client.models.scheduler_event_export_data import SchedulerEventExportData
    from tb_pe_client.models.tb_resource_export_data import TbResourceExportData
    from tb_pe_client.models.user_export_data import UserExportData
    from tb_pe_client.models.widgets_bundle_export_data import WidgetsBundleExportData
    from tb_pe_client.models.widget_type_export_data import WidgetTypeExportData

class EntityExportData(BaseModel):
    """
    Base export container for ThingsBoard entities
    """ # noqa: E501
    entity: Optional[ExportableEntity] = None
    relations: Optional[List[EntityRelation]] = None
    attributes: Optional[Dict[str, List[AttributeExportData]]] = Field(default=None, description="Map of attributes where key is the scope of attributes and value is the list of attributes for that scope")
    calculated_fields: Optional[List[CalculatedField]] = Field(default=None, serialization_alias="calculatedFields")
    entity_type: EntityType = Field(serialization_alias="entityType")
    __properties: ClassVar[List[str]] = ["entity", "relations", "attributes", "calculatedFields", "entityType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'entityType'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'AI_MODEL': 'AiModelExportData','ASSET': 'AssetExportData','ASSET_PROFILE': 'AssetProfileExportData','CONVERTER': 'ConverterExportData','CUSTOMER': 'CustomerExportData','DASHBOARD': 'DashboardExportData','DEVICE': 'DeviceExportData','DEVICE_PROFILE': 'DeviceProfileExportData','ENTITY_GROUP': 'EntityGroupExportData','ENTITY_VIEW': 'EntityViewExportData','INTEGRATION': 'IntegrationExportData','NOTIFICATION_RULE': 'NotificationRuleExportData','NOTIFICATION_TARGET': 'NotificationTargetExportData','NOTIFICATION_TEMPLATE': 'NotificationTemplateExportData','OTA_PACKAGE': 'OtaPackageExportData','REPORT_TEMPLATE': 'ReportTemplateExportData','ROLE': 'RoleExportData','RULE_CHAIN': 'RuleChainExportData','SCHEDULER_EVENT': 'SchedulerEventExportData','TB_RESOURCE': 'TbResourceExportData','USER': 'UserExportData','WIDGETS_BUNDLE': 'WidgetsBundleExportData','WIDGET_TYPE': 'WidgetTypeExportData'
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

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[AiModelExportData, AssetExportData, AssetProfileExportData, ConverterExportData, CustomerExportData, DashboardExportData, DeviceExportData, DeviceProfileExportData, EntityGroupExportData, EntityViewExportData, IntegrationExportData, NotificationRuleExportData, NotificationTargetExportData, NotificationTemplateExportData, OtaPackageExportData, ReportTemplateExportData, RoleExportData, RuleChainExportData, SchedulerEventExportData, TbResourceExportData, UserExportData, WidgetsBundleExportData, WidgetTypeExportData]]:
        """Create an instance of EntityExportData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in relations (list)
        _items = []
        if self.relations:
            for _item_relations in self.relations:
                if _item_relations:
                    _items.append(_item_relations.to_dict())
            _dict['relations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict of array)
        _field_dict_of_array = {}
        if self.attributes:
            for _key_attributes in self.attributes:
                if self.attributes[_key_attributes] is not None:
                    _field_dict_of_array[_key_attributes] = [
                        _item.to_dict() for _item in self.attributes[_key_attributes]
                    ]
            _dict['attributes'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each item in calculated_fields (list)
        _items = []
        if self.calculated_fields:
            for _item_calculated_fields in self.calculated_fields:
                if _item_calculated_fields:
                    _items.append(_item_calculated_fields.to_dict())
            _dict['calculatedFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AiModelExportData, AssetExportData, AssetProfileExportData, ConverterExportData, CustomerExportData, DashboardExportData, DeviceExportData, DeviceProfileExportData, EntityGroupExportData, EntityViewExportData, IntegrationExportData, NotificationRuleExportData, NotificationTargetExportData, NotificationTemplateExportData, OtaPackageExportData, ReportTemplateExportData, RoleExportData, RuleChainExportData, SchedulerEventExportData, TbResourceExportData, UserExportData, WidgetsBundleExportData, WidgetTypeExportData]]:
        """Create an instance of EntityExportData from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AiModelExportData':
            return import_module("tb_pe_client.models.ai_model_export_data").AiModelExportData.from_dict(obj)
        if object_type ==  'AssetExportData':
            return import_module("tb_pe_client.models.asset_export_data").AssetExportData.from_dict(obj)
        if object_type ==  'AssetProfileExportData':
            return import_module("tb_pe_client.models.asset_profile_export_data").AssetProfileExportData.from_dict(obj)
        if object_type ==  'ConverterExportData':
            return import_module("tb_pe_client.models.converter_export_data").ConverterExportData.from_dict(obj)
        if object_type ==  'CustomerExportData':
            return import_module("tb_pe_client.models.customer_export_data").CustomerExportData.from_dict(obj)
        if object_type ==  'DashboardExportData':
            return import_module("tb_pe_client.models.dashboard_export_data").DashboardExportData.from_dict(obj)
        if object_type ==  'DeviceExportData':
            return import_module("tb_pe_client.models.device_export_data").DeviceExportData.from_dict(obj)
        if object_type ==  'DeviceProfileExportData':
            return import_module("tb_pe_client.models.device_profile_export_data").DeviceProfileExportData.from_dict(obj)
        if object_type ==  'EntityGroupExportData':
            return import_module("tb_pe_client.models.entity_group_export_data").EntityGroupExportData.from_dict(obj)
        if object_type ==  'EntityViewExportData':
            return import_module("tb_pe_client.models.entity_view_export_data").EntityViewExportData.from_dict(obj)
        if object_type ==  'IntegrationExportData':
            return import_module("tb_pe_client.models.integration_export_data").IntegrationExportData.from_dict(obj)
        if object_type ==  'NotificationRuleExportData':
            return import_module("tb_pe_client.models.notification_rule_export_data").NotificationRuleExportData.from_dict(obj)
        if object_type ==  'NotificationTargetExportData':
            return import_module("tb_pe_client.models.notification_target_export_data").NotificationTargetExportData.from_dict(obj)
        if object_type ==  'NotificationTemplateExportData':
            return import_module("tb_pe_client.models.notification_template_export_data").NotificationTemplateExportData.from_dict(obj)
        if object_type ==  'OtaPackageExportData':
            return import_module("tb_pe_client.models.ota_package_export_data").OtaPackageExportData.from_dict(obj)
        if object_type ==  'ReportTemplateExportData':
            return import_module("tb_pe_client.models.report_template_export_data").ReportTemplateExportData.from_dict(obj)
        if object_type ==  'RoleExportData':
            return import_module("tb_pe_client.models.role_export_data").RoleExportData.from_dict(obj)
        if object_type ==  'RuleChainExportData':
            return import_module("tb_pe_client.models.rule_chain_export_data").RuleChainExportData.from_dict(obj)
        if object_type ==  'SchedulerEventExportData':
            return import_module("tb_pe_client.models.scheduler_event_export_data").SchedulerEventExportData.from_dict(obj)
        if object_type ==  'TbResourceExportData':
            return import_module("tb_pe_client.models.tb_resource_export_data").TbResourceExportData.from_dict(obj)
        if object_type ==  'UserExportData':
            return import_module("tb_pe_client.models.user_export_data").UserExportData.from_dict(obj)
        if object_type ==  'WidgetsBundleExportData':
            return import_module("tb_pe_client.models.widgets_bundle_export_data").WidgetsBundleExportData.from_dict(obj)
        if object_type ==  'WidgetTypeExportData':
            return import_module("tb_pe_client.models.widget_type_export_data").WidgetTypeExportData.from_dict(obj)

        raise ValueError("EntityExportData failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


