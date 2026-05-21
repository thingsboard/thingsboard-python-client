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

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.complex_operation import ComplexOperation
from tb_ce_client.models.key_filter_predicate import KeyFilterPredicate
from typing import Optional, Set
from typing_extensions import Self

class ComplexFilterPredicate(KeyFilterPredicate):
    """
    ComplexFilterPredicate
    """ # noqa: E501
    type: StrictStr = "COMPLEX"  # post_process: discriminator default
    operation: Optional[ComplexOperation] = None
    predicates: Optional[List[KeyFilterPredicate]] = None
    __properties: ClassVar[List[str]] = ["type", "operation", "predicates"]

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
        """Create an instance of ComplexFilterPredicate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in predicates (list)
        _items = []
        if self.predicates:
            for _item_predicates in self.predicates:
                if _item_predicates:
                    _items.append(_item_predicates.to_dict())
            _dict['predicates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComplexFilterPredicate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "operation": obj.get("operation"),
            "predicates": [KeyFilterPredicate.from_dict(_item) for _item in obj["predicates"]] if obj.get("predicates") is not None else None
        })
        return _obj


