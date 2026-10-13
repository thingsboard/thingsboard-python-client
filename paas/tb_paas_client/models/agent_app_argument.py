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
from tb_paas_client.models.agent_app_argument_format import AgentAppArgumentFormat
from tb_paas_client.models.agent_app_argument_source import AgentAppArgumentSource
from tb_paas_client.models.agent_app_argument_value_type import AgentAppArgumentValueType
from tb_paas_client.models.attribute_scope import AttributeScope
from tb_paas_client.models.entity_id import EntityId
from typing import Optional, Set
from typing_extensions import Self

class AgentAppArgument(BaseModel):
    """
    AgentAppArgument
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Argument name, referenced in the compose as ${tb.<name>}.")
    source_type: Optional[AgentAppArgumentSource] = Field(default=None, description="Source entity the value is resolved from.", serialization_alias="sourceType")
    source_entity_id: Optional[EntityId] = Field(default=None, description="Concrete source entity id. Required when sourceType references a specific entity (DEVICE, ASSET, CUSTOMER, EDGE); ignored for the context-derived sources.", serialization_alias="sourceEntityId")
    value_type: Optional[AgentAppArgumentValueType] = Field(default=None, description="Whether the value is read from an attribute or the latest telemetry.", serialization_alias="valueType")
    scope: Optional[AttributeScope] = Field(default=None, description="Attribute scope. Applicable only when valueType is ATTRIBUTE. Defaults to SERVER_SCOPE.")
    key: Optional[StrictStr] = Field(default=None, description="Attribute or latest telemetry key to read.")
    default_value: Optional[StrictStr] = Field(default=None, description="Optional fallback value used when the source has no value for the key.", serialization_alias="defaultValue")
    format: Optional[AgentAppArgumentFormat] = Field(default=None, description="How the resolved value is injected into the compose: STRING (quoted) or JSON (raw, for arrays/objects/numbers when the placeholder is the whole value). Defaults to STRING.")
    __properties: ClassVar[List[str]] = ["name", "sourceType", "sourceEntityId", "valueType", "scope", "key", "defaultValue", "format"]

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
        """Create an instance of AgentAppArgument from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_entity_id
        if self.source_entity_id:
            _dict['sourceEntityId'] = self.source_entity_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentAppArgument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "source_type": obj.get("sourceType"),
            "source_entity_id": EntityId.from_dict(obj["sourceEntityId"]) if obj.get("sourceEntityId") is not None else None,
            "value_type": obj.get("valueType"),
            "scope": obj.get("scope"),
            "key": obj.get("key"),
            "default_value": obj.get("defaultValue"),
            "format": obj.get("format")
        })
        return _obj


