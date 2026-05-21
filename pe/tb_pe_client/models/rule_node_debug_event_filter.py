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

class RuleNodeDebugEventFilter(EventFilter):
    """
    RuleNodeDebugEventFilter
    """ # noqa: E501
    event_type: EventType = Field(default=EventType.DEBUG_RULE_NODE, serialization_alias="eventType")  # post_process: discriminator default
    server: Optional[StrictStr] = Field(default=None, description="String value representing the server name, identifier or ip address where the platform is running")
    is_error: Optional[StrictBool] = Field(default=None, description="Boolean value to filter the errors", serialization_alias="isError")
    error_str: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on error message", serialization_alias="errorStr")
    msg_direction_type: Optional[StrictStr] = Field(default=None, description="String value representing msg direction type (incoming to entity or outcoming from entity)", serialization_alias="msgDirectionType")
    entity_id: Optional[StrictStr] = Field(default=None, description="String value representing the entity id in the event body (originator of the message)", serialization_alias="entityId")
    entity_type: Optional[StrictStr] = Field(default=None, description="String value representing the entity type", serialization_alias="entityType")
    msg_id: Optional[StrictStr] = Field(default=None, description="String value representing the message id in the rule engine", serialization_alias="msgId")
    msg_type: Optional[StrictStr] = Field(default=None, description="String value representing the message type", serialization_alias="msgType")
    relation_type: Optional[StrictStr] = Field(default=None, description="String value representing the type of message routing", serialization_alias="relationType")
    data_search: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on data (key and value) for the message.", serialization_alias="dataSearch")
    metadata_search: Optional[StrictStr] = Field(default=None, description="The case insensitive 'contains' filter based on metadata (key and value) for the message.", serialization_alias="metadataSearch")
    __properties: ClassVar[List[str]] = ["eventType", "notEmpty", "server", "isError", "errorStr", "msgDirectionType", "entityId", "entityType", "msgId", "msgType", "relationType", "dataSearch", "metadataSearch"]

    @field_validator('is_error')
    def is_error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['false', 'true']):
            raise ValueError("must be one of enum values ('false', 'true')")
        return value

    @field_validator('msg_direction_type')
    def msg_direction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['IN', 'OUT']):
            raise ValueError("must be one of enum values ('IN', 'OUT')")
        return value

    @field_validator('entity_type')
    def entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DEVICE']):
            raise ValueError("must be one of enum values ('DEVICE')")
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
        """Create an instance of RuleNodeDebugEventFilter from a JSON string"""
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
        """Create an instance of RuleNodeDebugEventFilter from a dict"""
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
            "msg_direction_type": obj.get("msgDirectionType"),
            "entity_id": obj.get("entityId"),
            "entity_type": obj.get("entityType"),
            "msg_id": obj.get("msgId"),
            "msg_type": obj.get("msgType"),
            "relation_type": obj.get("relationType"),
            "data_search": obj.get("dataSearch"),
            "metadata_search": obj.get("metadataSearch")
        })
        return _obj


