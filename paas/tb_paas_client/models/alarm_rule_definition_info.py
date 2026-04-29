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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.alarm_calculated_field_configuration import AlarmCalculatedFieldConfiguration
from tb_paas_client.models.calculated_field_id import CalculatedFieldId
from tb_paas_client.models.debug_settings import DebugSettings
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AlarmRuleDefinitionInfo(BaseModel):
    """
    AlarmRuleDefinitionInfo
    """ # noqa: E501
    id: Optional[CalculatedFieldId] = Field(default=None, description="JSON object with the Alarm Rule Id. Referencing non-existing Alarm Rule Id will cause error.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm rule creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, serialization_alias="tenantId")
    entity_id: Optional[EntityId] = Field(default=None, serialization_alias="entityId")
    name: Optional[StrictStr] = Field(default=None, description="User defined name of the alarm rule.")
    debug_settings: Optional[DebugSettings] = Field(default=None, description="Debug settings object.", serialization_alias="debugSettings")
    configuration_version: Optional[StrictInt] = Field(default=None, description="Version of alarm rule configuration.", serialization_alias="configurationVersion")
    configuration: AlarmCalculatedFieldConfiguration
    version: Optional[StrictInt] = None
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the alarm rule. May include: 'description' (string).", serialization_alias="additionalInfo")
    entity_name: Optional[StrictStr] = Field(default=None, serialization_alias="entityName")
    debug_mode: Optional[StrictBool] = Field(default=None, serialization_alias="debugMode")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "entityId", "name", "debugSettings", "configurationVersion", "configuration", "version", "additionalInfo", "entityName", "debugMode"]

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
        """Create an instance of AlarmRuleDefinitionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of debug_settings
        if self.debug_settings:
            _dict['debugSettings'] = self.debug_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlarmRuleDefinitionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": CalculatedFieldId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "entity_id": EntityId.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "name": obj.get("name"),
            "debug_settings": DebugSettings.from_dict(obj["debugSettings"]) if obj.get("debugSettings") is not None else None,
            "configuration_version": obj.get("configurationVersion"),
            "configuration": AlarmCalculatedFieldConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "version": obj.get("version"),
            "additional_info": obj.get("additionalInfo"),
            "entity_name": obj.get("entityName"),
            "debug_mode": obj.get("debugMode")
        })
        return _obj


