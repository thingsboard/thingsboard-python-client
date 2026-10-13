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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.agent_app_unit_id import AgentAppUnitId
from tb_paas_client.models.agent_app_unit_type import AgentAppUnitType
from tb_paas_client.models.agent_application_id import AgentApplicationId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AgentAppUnit(BaseModel):
    """
    AgentAppUnit
    """ # noqa: E501
    id: Optional[AgentAppUnitId] = Field(default=None, description="JSON object with the Agent App Unit Id.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the agent app unit creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: TenantId = Field(description="Tenant this unit belongs to", serialization_alias="tenantId")
    agent_application_id: AgentApplicationId = Field(description="Agent application this unit belongs to", serialization_alias="agentApplicationId")
    identifier: StrictStr = Field(description="Unit identifier")
    type: AgentAppUnitType = Field(description="Unit type")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "agentApplicationId", "identifier", "type"]

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
        """Create an instance of AgentAppUnit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agent_application_id
        if self.agent_application_id:
            _dict['agentApplicationId'] = self.agent_application_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentAppUnit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AgentAppUnitId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "agent_application_id": AgentApplicationId.from_dict(obj["agentApplicationId"]) if obj.get("agentApplicationId") is not None else None,
            "identifier": obj.get("identifier"),
            "type": obj.get("type")
        })
        return _obj


