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
from tb_paas_client.models.agent_profile_id import AgentProfileId
from tb_paas_client.models.agent_provision_type import AgentProvisionType
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AgentProfile(BaseModel):
    """
    AgentProfile
    """ # noqa: E501
    id: Optional[AgentProfileId] = Field(default=None, description="JSON object with the Agent Profile Id.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the profile creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", serialization_alias="tenantId")
    name: StrictStr = Field(description="Unique profile name within tenant")
    description: Optional[StrictStr] = Field(default=None, description="Profile description")
    provision_key: Optional[StrictStr] = Field(default=None, description="Provision key for future auto-provisioning", serialization_alias="provisionKey")
    provision_secret: Optional[StrictStr] = Field(default=None, description="Provision secret for future auto-provisioning", serialization_alias="provisionSecret")
    provision_type: Optional[AgentProvisionType] = Field(default=None, description="Provisioning strategy. DISABLED by default.", serialization_alias="provisionType")
    version: Optional[StrictInt] = None
    default: Optional[StrictBool] = Field(default=None, description="Used to mark the default profile that will be assigned to agents when no profile is specified.")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "name", "description", "provisionKey", "provisionSecret", "provisionType", "version", "default"]

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
        """Create an instance of AgentProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AgentProfileId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "provision_key": obj.get("provisionKey"),
            "provision_secret": obj.get("provisionSecret"),
            "provision_type": obj.get("provisionType"),
            "version": obj.get("version"),
            "default": obj.get("default")
        })
        return _obj


