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
from tb_pe_client.models.agent_application_id import AgentApplicationId
from tb_pe_client.models.agent_id import AgentId
from tb_pe_client.models.skip_reason import SkipReason
from typing import Optional, Set
from typing_extensions import Self

class SkippedApp(BaseModel):
    """
    SkippedApp
    """ # noqa: E501
    agent_id: Optional[AgentId] = Field(default=None, description="Agent Id owning the application", serialization_alias="agentId")
    agent_name: Optional[StrictStr] = Field(default=None, description="Agent name", serialization_alias="agentName")
    application_id: Optional[AgentApplicationId] = Field(default=None, description="Application Id", serialization_alias="applicationId")
    application_name: Optional[StrictStr] = Field(default=None, description="Application name", serialization_alias="applicationName")
    reason: Optional[SkipReason] = Field(default=None, description="Reason for skipping")
    msg: Optional[StrictStr] = Field(default=None, description="Optional message in case of a failure")
    __properties: ClassVar[List[str]] = ["agentId", "agentName", "applicationId", "applicationName", "reason", "msg"]

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
        """Create an instance of SkippedApp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agent_id
        if self.agent_id:
            _dict['agentId'] = self.agent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application_id
        if self.application_id:
            _dict['applicationId'] = self.application_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SkippedApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agent_id": AgentId.from_dict(obj["agentId"]) if obj.get("agentId") is not None else None,
            "agent_name": obj.get("agentName"),
            "application_id": AgentApplicationId.from_dict(obj["applicationId"]) if obj.get("applicationId") is not None else None,
            "application_name": obj.get("applicationName"),
            "reason": obj.get("reason"),
            "msg": obj.get("msg")
        })
        return _obj


