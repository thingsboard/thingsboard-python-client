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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.alarm_rule_complex_operation import AlarmRuleComplexOperation
from tb_ce_client.models.entity_filter import EntityFilter
from tb_ce_client.models.key_filter import KeyFilter
from typing import Optional, Set
from typing_extensions import Self

class EntityCountQuery(BaseModel):
    """
    A JSON value representing the entity count query. See API call notes above for more details.
    """ # noqa: E501
    entity_filter: Optional[EntityFilter] = Field(default=None, serialization_alias="entityFilter")
    key_filters: Optional[List[KeyFilter]] = Field(default=None, serialization_alias="keyFilters")
    key_filters_operation: Optional[AlarmRuleComplexOperation] = Field(default=None, serialization_alias="keyFiltersOperation")
    key_filters_operation_or_default: Optional[AlarmRuleComplexOperation] = Field(default=None, serialization_alias="keyFiltersOperationOrDefault")
    __properties: ClassVar[List[str]] = ["entityFilter", "keyFilters", "keyFiltersOperation", "keyFiltersOperationOrDefault"]

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
        """Create an instance of EntityCountQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_filter
        if self.entity_filter:
            _dict['entityFilter'] = self.entity_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in key_filters (list)
        _items = []
        if self.key_filters:
            for _item_key_filters in self.key_filters:
                if _item_key_filters:
                    _items.append(_item_key_filters.to_dict())
            _dict['keyFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityCountQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entity_filter": EntityFilter.from_dict(obj["entityFilter"]) if obj.get("entityFilter") is not None else None,
            "key_filters": [KeyFilter.from_dict(_item) for _item in obj["keyFilters"]] if obj.get("keyFilters") is not None else None,
            "key_filters_operation": obj.get("keyFiltersOperation"),
            "key_filters_operation_or_default": obj.get("keyFiltersOperationOrDefault")
        })
        return _obj


