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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.argument import Argument
from tb_ce_client.models.calculated_field_configuration import CalculatedFieldConfiguration
from tb_ce_client.models.output import Output
from tb_ce_client.models.relation_path_level import RelationPathLevel
from typing import Optional, Set
from typing_extensions import Self

class PropagationCalculatedFieldConfiguration(CalculatedFieldConfiguration):
    """
    PropagationCalculatedFieldConfiguration
    """ # noqa: E501
    type: StrictStr = "PROPAGATION"  # post_process: discriminator default
    arguments: Dict[str, Argument]
    expression: Optional[StrictStr] = None
    relation: RelationPathLevel
    apply_expression_to_resolved_arguments: Optional[StrictBool] = Field(default=None, serialization_alias="applyExpressionToResolvedArguments")
    __properties: ClassVar[List[str]] = ["output", "type", "arguments", "expression", "relation", "applyExpressionToResolvedArguments"]

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
        """Create an instance of PropagationCalculatedFieldConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in arguments (dict)
        _field_dict = {}
        if self.arguments:
            for _key_arguments in self.arguments:
                if self.arguments[_key_arguments]:
                    _field_dict[_key_arguments] = self.arguments[_key_arguments].to_dict()
            _dict['arguments'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of relation
        if self.relation:
            _dict['relation'] = self.relation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PropagationCalculatedFieldConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "output": Output.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "type": obj.get("type"),
            "arguments": dict(
                (_k, Argument.from_dict(_v))
                for _k, _v in obj["arguments"].items()
            )
            if obj.get("arguments") is not None
            else None,
            "expression": obj.get("expression"),
            "relation": RelationPathLevel.from_dict(obj["relation"]) if obj.get("relation") is not None else None,
            "apply_expression_to_resolved_arguments": obj.get("applyExpressionToResolvedArguments")
        })
        return _obj


