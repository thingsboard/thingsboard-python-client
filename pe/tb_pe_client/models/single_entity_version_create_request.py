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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.version_create_config import VersionCreateConfig
from tb_pe_client.models.version_create_request import VersionCreateRequest
from tb_pe_client.models.version_create_request_type import VersionCreateRequestType
from typing import Optional, Set
from typing_extensions import Self

class SingleEntityVersionCreateRequest(VersionCreateRequest):
    """
    SingleEntityVersionCreateRequest
    """ # noqa: E501
    type: VersionCreateRequestType = VersionCreateRequestType.SINGLE_ENTITY  # post_process: discriminator default
    entity_id: Optional[EntityId] = Field(default=None, serialization_alias="entityId")
    config: Optional[VersionCreateConfig] = None
    __properties: ClassVar[List[str]] = ["versionName", "branch", "type", "entityId", "config"]

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
        """Create an instance of SingleEntityVersionCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SingleEntityVersionCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version_name": obj.get("versionName"),
            "branch": obj.get("branch"),
            "type": obj.get("type"),
            "entity_id": EntityId.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "config": VersionCreateConfig.from_dict(obj["config"]) if obj.get("config") is not None else None
        })
        return _obj


