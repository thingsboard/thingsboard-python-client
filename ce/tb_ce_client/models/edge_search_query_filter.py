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

from pydantic import ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.alias_entity_id import AliasEntityId
from tb_ce_client.models.entity_filter import EntityFilter
from tb_ce_client.models.entity_search_direction import EntitySearchDirection
from typing import Optional, Set
from typing_extensions import Self

class EdgeSearchQueryFilter(EntityFilter):
    """
    EdgeSearchQueryFilter
    """ # noqa: E501
    type: StrictStr = "edgeSearchQuery"  # post_process: discriminator default
    root_entity: Optional[AliasEntityId] = Field(default=None, serialization_alias="rootEntity")
    relation_type: Optional[StrictStr] = Field(default=None, serialization_alias="relationType")
    direction: Optional[EntitySearchDirection] = None
    max_level: Optional[StrictInt] = Field(default=None, serialization_alias="maxLevel")
    fetch_last_level_only: Optional[StrictBool] = Field(default=None, serialization_alias="fetchLastLevelOnly")
    root_state_entity: Optional[StrictBool] = Field(default=None, serialization_alias="rootStateEntity")
    default_state_entity: Optional[AliasEntityId] = Field(default=None, serialization_alias="defaultStateEntity")
    edge_types: Optional[List[StrictStr]] = Field(default=None, serialization_alias="edgeTypes")
    __properties: ClassVar[List[str]] = ["type", "rootEntity", "relationType", "direction", "maxLevel", "fetchLastLevelOnly", "rootStateEntity", "defaultStateEntity", "edgeTypes"]

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
        """Create an instance of EdgeSearchQueryFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of root_entity
        if self.root_entity:
            _dict['rootEntity'] = self.root_entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_state_entity
        if self.default_state_entity:
            _dict['defaultStateEntity'] = self.default_state_entity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EdgeSearchQueryFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "root_entity": AliasEntityId.from_dict(obj["rootEntity"]) if obj.get("rootEntity") is not None else None,
            "relation_type": obj.get("relationType"),
            "direction": obj.get("direction"),
            "max_level": obj.get("maxLevel"),
            "fetch_last_level_only": obj.get("fetchLastLevelOnly"),
            "root_state_entity": obj.get("rootStateEntity"),
            "default_state_entity": AliasEntityId.from_dict(obj["defaultStateEntity"]) if obj.get("defaultStateEntity") is not None else None,
            "edge_types": obj.get("edgeTypes")
        })
        return _obj


