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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.alarm_rule_definition_info import AlarmRuleDefinitionInfo
from typing import Optional, Set
from typing_extensions import Self

class PageDataAlarmRuleDefinitionInfo(BaseModel):
    """
    PageDataAlarmRuleDefinitionInfo
    """ # noqa: E501
    data: Optional[List[AlarmRuleDefinitionInfo]] = Field(default=None, description="Array of the entities")
    total_pages: Optional[StrictInt] = Field(default=None, description="Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria", serialization_alias="totalPages")
    total_elements: Optional[StrictInt] = Field(default=None, description="Total number of elements in all available pages", serialization_alias="totalElements")
    has_next: Optional[StrictBool] = Field(default=None, description="'false' value indicates the end of the result set", serialization_alias="hasNext")
    __properties: ClassVar[List[str]] = ["data", "totalPages", "totalElements", "hasNext"]

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
        """Create an instance of PageDataAlarmRuleDefinitionInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "total_pages",
            "total_elements",
            "has_next",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PageDataAlarmRuleDefinitionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [AlarmRuleDefinitionInfo.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "total_pages": obj.get("totalPages"),
            "total_elements": obj.get("totalElements"),
            "has_next": obj.get("hasNext")
        })
        return _obj


