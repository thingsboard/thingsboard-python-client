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

from pydantic import ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.event_filter import EventFilter
from tb_pe_client.models.event_type import EventType
from typing import Optional, Set
from typing_extensions import Self

class RuleChainDebugEventFilter(EventFilter):
    """
    RuleChainDebugEventFilter
    """ # noqa: E501
    event_type: EventType = Field(default=EventType.DEBUG_RULE_CHAIN, serialization_alias="eventType")  # post_process: discriminator default
    server: Optional[StrictStr] = Field(default=None, description="String value representing the server name, identifier or ip address where the platform is running")
    is_error: Optional[StrictBool] = Field(default=None, description="Boolean value to filter the errors", serialization_alias="isError")
    error_str: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on error message", serialization_alias="errorStr")
    message: Optional[StrictStr] = Field(default=None, description="String value representing the message")
    __properties: ClassVar[List[str]] = ["eventType", "notEmpty", "server", "isError", "errorStr", "message"]

    @field_validator('is_error')
    def is_error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false', 'true']):
            raise ValueError("must be one of enum values ('false', 'true')")
        return value

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
        """Create an instance of RuleChainDebugEventFilter from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleChainDebugEventFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event_type": obj.get("eventType"),
            "not_empty": obj.get("notEmpty"),
            "server": obj.get("server"),
            "is_error": obj.get("isError"),
            "error_str": obj.get("errorStr"),
            "message": obj.get("message")
        })
        return _obj


