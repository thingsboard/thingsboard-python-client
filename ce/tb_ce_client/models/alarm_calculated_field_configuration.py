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
from tb_ce_client.models.alarm_rule import AlarmRule
from tb_ce_client.models.argument import Argument
from tb_ce_client.models.calculated_field_configuration import CalculatedFieldConfiguration
from tb_ce_client.models.output import Output
from typing import Optional, Set
from typing_extensions import Self

class AlarmCalculatedFieldConfiguration(CalculatedFieldConfiguration):
    """
    AlarmCalculatedFieldConfiguration
    """ # noqa: E501
    type: StrictStr = "ALARM"  # post_process: discriminator default
    arguments: Dict[str, Argument]
    create_rules: Dict[str, AlarmRule] = Field(serialization_alias="createRules")
    clear_rule: Optional[AlarmRule] = Field(default=None, serialization_alias="clearRule")
    propagate: Optional[StrictBool] = None
    propagate_to_owner: Optional[StrictBool] = Field(default=None, serialization_alias="propagateToOwner")
    propagate_to_tenant: Optional[StrictBool] = Field(default=None, serialization_alias="propagateToTenant")
    propagate_relation_types: Optional[List[StrictStr]] = Field(default=None, serialization_alias="propagateRelationTypes")
    __properties: ClassVar[List[str]] = ["output", "type", "arguments", "createRules", "clearRule", "propagate", "propagateToOwner", "propagateToTenant", "propagateRelationTypes"]

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
        """Create an instance of AlarmCalculatedFieldConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in create_rules (dict)
        _field_dict = {}
        if self.create_rules:
            for _key_create_rules in self.create_rules:
                if self.create_rules[_key_create_rules]:
                    _field_dict[_key_create_rules] = self.create_rules[_key_create_rules].to_dict()
            _dict['createRules'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of clear_rule
        if self.clear_rule:
            _dict['clearRule'] = self.clear_rule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlarmCalculatedFieldConfiguration from a dict"""
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
            "create_rules": dict(
                (_k, AlarmRule.from_dict(_v))
                for _k, _v in obj["createRules"].items()
            )
            if obj.get("createRules") is not None
            else None,
            "clear_rule": AlarmRule.from_dict(obj["clearRule"]) if obj.get("clearRule") is not None else None,
            "propagate": obj.get("propagate"),
            "propagate_to_owner": obj.get("propagateToOwner"),
            "propagate_to_tenant": obj.get("propagateToTenant"),
            "propagate_relation_types": obj.get("propagateRelationTypes")
        })
        return _obj


