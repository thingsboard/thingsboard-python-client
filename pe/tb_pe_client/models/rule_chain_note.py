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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RuleChainNote(BaseModel):
    """
    RuleChainNote
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the note on the canvas")
    x: Optional[StrictInt] = Field(default=None, description="Horizontal position of the note on the canvas, in pixels")
    y: Optional[StrictInt] = Field(default=None, description="Vertical position of the note on the canvas, in pixels")
    width: Optional[StrictInt] = Field(default=None, description="Width of the note, in pixels")
    height: Optional[StrictInt] = Field(default=None, description="Height of the note, in pixels")
    content: Optional[StrictStr] = Field(default=None, description="Markdown or HTML content of the note")
    background_color: Optional[StrictStr] = Field(default=None, description="Background color of the note in CSS hex format, e.g. '#FFF9C4'", serialization_alias="backgroundColor")
    border_color: Optional[StrictStr] = Field(default=None, description="Border color of the note in CSS hex format, e.g. '#E6C800'", serialization_alias="borderColor")
    border_width: Optional[StrictInt] = Field(default=None, description="Border width of the note in pixels", serialization_alias="borderWidth")
    apply_default_markdown_style: Optional[StrictBool] = Field(default=None, description="Whether to apply the default markdown stylesheet to the note content", serialization_alias="applyDefaultMarkdownStyle")
    markdown_css: Optional[StrictStr] = Field(default=None, description="Custom CSS styles applied to the note content", serialization_alias="markdownCss")
    __properties: ClassVar[List[str]] = ["id", "x", "y", "width", "height", "content", "backgroundColor", "borderColor", "borderWidth", "applyDefaultMarkdownStyle", "markdownCss"]

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
        """Create an instance of RuleChainNote from a JSON string"""
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
        """Create an instance of RuleChainNote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "x": obj.get("x"),
            "y": obj.get("y"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "content": obj.get("content"),
            "background_color": obj.get("backgroundColor"),
            "border_color": obj.get("borderColor"),
            "border_width": obj.get("borderWidth"),
            "apply_default_markdown_style": obj.get("applyDefaultMarkdownStyle"),
            "markdown_css": obj.get("markdownCss")
        })
        return _obj


