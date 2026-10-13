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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.agent_app_config_type import AgentAppConfigType
from tb_pe_client.models.agent_app_template_start_steps_inner import AgentAppTemplateStartStepsInner
from tb_pe_client.models.agent_application_type import AgentApplicationType
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AgentAppTemplate(BaseModel):
    """
    AgentAppTemplate
    """ # noqa: E501
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", serialization_alias="tenantId")
    app_type: AgentApplicationType = Field(description="Application type", serialization_alias="appType")
    config_type: Optional[AgentAppConfigType] = Field(default=None, description="Config type (e.g. 'DOCKER_COMPOSE'); the compose body lives in the template's compose-template step, not here", serialization_alias="configType")
    current_version: StrictStr = Field(description="Current template version", serialization_alias="currentVersion")
    next_version: Optional[StrictStr] = Field(default=None, description="Next template version", serialization_alias="nextVersion")
    start_steps: Optional[List[AgentAppTemplateStartStepsInner]] = Field(default=None, description="Start steps", serialization_alias="startSteps")
    upgrade_steps: Optional[List[AgentAppTemplateStartStepsInner]] = Field(default=None, description="Upgrade steps", serialization_alias="upgradeSteps")
    delete_steps: Optional[List[AgentAppTemplateStartStepsInner]] = Field(default=None, description="Delete steps", serialization_alias="deleteSteps")
    rollback_steps: Optional[List[AgentAppTemplateStartStepsInner]] = Field(default=None, description="Rollback steps", serialization_alias="rollbackSteps")
    restart_steps: Optional[List[AgentAppTemplateStartStepsInner]] = Field(default=None, description="Restart steps", serialization_alias="restartSteps")
    __properties: ClassVar[List[str]] = ["tenantId", "appType", "configType", "currentVersion", "nextVersion", "startSteps", "upgradeSteps", "deleteSteps", "rollbackSteps", "restartSteps"]

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
        """Create an instance of AgentAppTemplate from a JSON string"""
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
            "tenant_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in start_steps (list)
        _items = []
        if self.start_steps:
            for _item_start_steps in self.start_steps:
                if _item_start_steps:
                    _items.append(_item_start_steps.to_dict())
            _dict['startSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in upgrade_steps (list)
        _items = []
        if self.upgrade_steps:
            for _item_upgrade_steps in self.upgrade_steps:
                if _item_upgrade_steps:
                    _items.append(_item_upgrade_steps.to_dict())
            _dict['upgradeSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in delete_steps (list)
        _items = []
        if self.delete_steps:
            for _item_delete_steps in self.delete_steps:
                if _item_delete_steps:
                    _items.append(_item_delete_steps.to_dict())
            _dict['deleteSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rollback_steps (list)
        _items = []
        if self.rollback_steps:
            for _item_rollback_steps in self.rollback_steps:
                if _item_rollback_steps:
                    _items.append(_item_rollback_steps.to_dict())
            _dict['rollbackSteps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in restart_steps (list)
        _items = []
        if self.restart_steps:
            for _item_restart_steps in self.restart_steps:
                if _item_restart_steps:
                    _items.append(_item_restart_steps.to_dict())
            _dict['restartSteps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentAppTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "app_type": obj.get("appType"),
            "config_type": obj.get("configType"),
            "current_version": obj.get("currentVersion"),
            "next_version": obj.get("nextVersion"),
            "start_steps": [AgentAppTemplateStartStepsInner.from_dict(_item) for _item in obj["startSteps"]] if obj.get("startSteps") is not None else None,
            "upgrade_steps": [AgentAppTemplateStartStepsInner.from_dict(_item) for _item in obj["upgradeSteps"]] if obj.get("upgradeSteps") is not None else None,
            "delete_steps": [AgentAppTemplateStartStepsInner.from_dict(_item) for _item in obj["deleteSteps"]] if obj.get("deleteSteps") is not None else None,
            "rollback_steps": [AgentAppTemplateStartStepsInner.from_dict(_item) for _item in obj["rollbackSteps"]] if obj.get("rollbackSteps") is not None else None,
            "restart_steps": [AgentAppTemplateStartStepsInner.from_dict(_item) for _item in obj["restartSteps"]] if obj.get("restartSteps") is not None else None
        })
        return _obj


