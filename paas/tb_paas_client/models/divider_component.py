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

from pydantic import ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.border_length import BorderLength
from tb_paas_client.models.border_type import BorderType
from tb_paas_client.models.insets import Insets
from tb_paas_client.models.report_component import ReportComponent
from tb_paas_client.models.report_component_sub_type import ReportComponentSubType
from tb_paas_client.models.report_component_type import ReportComponentType
from typing import Optional, Set
from typing_extensions import Self

class DividerComponent(ReportComponent):
    """
    DividerComponent
    """ # noqa: E501
    type: ReportComponentType = ReportComponentType.DIVIDER  # post_process: discriminator default
    margins: Optional[Insets] = None
    paddings: Optional[Insets] = None
    background: Optional[StrictStr] = None
    border_width: Optional[StrictInt] = Field(default=None, serialization_alias="borderWidth")
    border_radius: Optional[StrictInt] = Field(default=None, serialization_alias="borderRadius")
    border_color: Optional[StrictStr] = Field(default=None, serialization_alias="borderColor")
    length: Optional[BorderLength] = None
    border_type: Optional[BorderType] = Field(default=None, serialization_alias="borderType")
    width_px: Optional[StrictInt] = Field(default=None, serialization_alias="widthPx")
    color: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["subType", "type", "margins", "paddings", "background", "borderWidth", "borderRadius", "borderColor", "length", "borderType", "widthPx", "color"]

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
        """Create an instance of DividerComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of margins
        if self.margins:
            _dict['margins'] = self.margins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of paddings
        if self.paddings:
            _dict['paddings'] = self.paddings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DividerComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sub_type": obj.get("subType"),
            "type": obj.get("type"),
            "margins": Insets.from_dict(obj["margins"]) if obj.get("margins") is not None else None,
            "paddings": Insets.from_dict(obj["paddings"]) if obj.get("paddings") is not None else None,
            "background": obj.get("background"),
            "border_width": obj.get("borderWidth"),
            "border_radius": obj.get("borderRadius"),
            "border_color": obj.get("borderColor"),
            "length": obj.get("length"),
            "border_type": obj.get("borderType"),
            "width_px": obj.get("widthPx"),
            "color": obj.get("color")
        })
        return _obj


