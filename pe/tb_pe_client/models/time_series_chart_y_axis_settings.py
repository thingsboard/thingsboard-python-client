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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_pe_client.models.axis_position import AxisPosition
from tb_pe_client.models.font import Font
from tb_pe_client.models.simple_value_source_config import SimpleValueSourceConfig
from typing import Optional, Set
from typing_extensions import Self

class TimeSeriesChartYAxisSettings(BaseModel):
    """
    TimeSeriesChartYAxisSettings
    """ # noqa: E501
    show: Optional[StrictBool] = None
    label: Optional[StrictStr] = None
    label_font: Optional[Font] = Field(default=None, serialization_alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, serialization_alias="labelColor")
    position: Optional[AxisPosition] = None
    show_tick_labels: Optional[StrictBool] = Field(default=None, serialization_alias="showTickLabels")
    tick_label_font: Optional[Font] = Field(default=None, serialization_alias="tickLabelFont")
    tick_label_color: Optional[StrictStr] = Field(default=None, serialization_alias="tickLabelColor")
    show_ticks: Optional[StrictBool] = Field(default=None, serialization_alias="showTicks")
    ticks_color: Optional[StrictStr] = Field(default=None, serialization_alias="ticksColor")
    show_line: Optional[StrictBool] = Field(default=None, serialization_alias="showLine")
    line_color: Optional[StrictStr] = Field(default=None, serialization_alias="lineColor")
    show_split_lines: Optional[StrictBool] = Field(default=None, serialization_alias="showSplitLines")
    split_lines_color: Optional[StrictStr] = Field(default=None, serialization_alias="splitLinesColor")
    id: Optional[StrictStr] = None
    order: Optional[StrictInt] = None
    units: Optional[StrictStr] = None
    decimals: Optional[StrictInt] = None
    interval: Optional[Union[StrictFloat, StrictInt]] = None
    split_number: Optional[StrictInt] = Field(default=None, serialization_alias="splitNumber")
    min: Optional[SimpleValueSourceConfig] = None
    max: Optional[SimpleValueSourceConfig] = None
    __properties: ClassVar[List[str]] = ["show", "label", "labelFont", "labelColor", "position", "showTickLabels", "tickLabelFont", "tickLabelColor", "showTicks", "ticksColor", "showLine", "lineColor", "showSplitLines", "splitLinesColor", "id", "order", "units", "decimals", "interval", "splitNumber", "min", "max"]

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
        """Create an instance of TimeSeriesChartYAxisSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label_font
        if self.label_font:
            _dict['labelFont'] = self.label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tick_label_font
        if self.tick_label_font:
            _dict['tickLabelFont'] = self.tick_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min
        if self.min:
            _dict['min'] = self.min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max
        if self.max:
            _dict['max'] = self.max.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeSeriesChartYAxisSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "show": obj.get("show"),
            "label": obj.get("label"),
            "label_font": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "label_color": obj.get("labelColor"),
            "position": obj.get("position"),
            "show_tick_labels": obj.get("showTickLabels"),
            "tick_label_font": Font.from_dict(obj["tickLabelFont"]) if obj.get("tickLabelFont") is not None else None,
            "tick_label_color": obj.get("tickLabelColor"),
            "show_ticks": obj.get("showTicks"),
            "ticks_color": obj.get("ticksColor"),
            "show_line": obj.get("showLine"),
            "line_color": obj.get("lineColor"),
            "show_split_lines": obj.get("showSplitLines"),
            "split_lines_color": obj.get("splitLinesColor"),
            "id": obj.get("id"),
            "order": obj.get("order"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "interval": obj.get("interval"),
            "split_number": obj.get("splitNumber"),
            "min": SimpleValueSourceConfig.from_dict(obj["min"]) if obj.get("min") is not None else None,
            "max": SimpleValueSourceConfig.from_dict(obj["max"]) if obj.get("max") is not None else None
        })
        return _obj


