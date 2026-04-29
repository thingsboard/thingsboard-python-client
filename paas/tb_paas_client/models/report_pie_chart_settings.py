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
from tb_paas_client.models.font import Font
from tb_paas_client.models.legend_position import LegendPosition
from tb_paas_client.models.pie_chart_label_position import PieChartLabelPosition
from tb_paas_client.models.text_alignment import TextAlignment
from typing import Optional, Set
from typing_extensions import Self

class ReportPieChartSettings(BaseModel):
    """
    ReportPieChartSettings
    """ # noqa: E501
    show_title: Optional[StrictBool] = Field(default=None, serialization_alias="showTitle")
    title: Optional[StrictStr] = None
    title_font: Optional[Font] = Field(default=None, serialization_alias="titleFont")
    title_color: Optional[StrictStr] = Field(default=None, serialization_alias="titleColor")
    title_alignment: Optional[TextAlignment] = Field(default=None, serialization_alias="titleAlignment")
    units: Optional[StrictStr] = None
    decimals: Optional[StrictInt] = None
    auto_scale: Optional[StrictBool] = Field(default=None, serialization_alias="autoScale")
    sort_series: Optional[StrictBool] = Field(default=None, serialization_alias="sortSeries")
    show_total: Optional[StrictBool] = Field(default=None, serialization_alias="showTotal")
    show_legend: Optional[StrictBool] = Field(default=None, serialization_alias="showLegend")
    legend_position: Optional[LegendPosition] = Field(default=None, serialization_alias="legendPosition")
    legend_label_font: Optional[Font] = Field(default=None, serialization_alias="legendLabelFont")
    legend_label_color: Optional[StrictStr] = Field(default=None, serialization_alias="legendLabelColor")
    legend_value_font: Optional[Font] = Field(default=None, serialization_alias="legendValueFont")
    legend_value_color: Optional[StrictStr] = Field(default=None, serialization_alias="legendValueColor")
    legend_show_total: Optional[StrictBool] = Field(default=None, serialization_alias="legendShowTotal")
    show_label: Optional[StrictBool] = Field(default=None, serialization_alias="showLabel")
    label_position: Optional[PieChartLabelPosition] = Field(default=None, serialization_alias="labelPosition")
    label_font: Optional[Font] = Field(default=None, serialization_alias="labelFont")
    label_color: Optional[StrictStr] = Field(default=None, serialization_alias="labelColor")
    border_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, serialization_alias="borderWidth")
    border_color: Optional[StrictStr] = Field(default=None, serialization_alias="borderColor")
    radius: Optional[Union[StrictFloat, StrictInt]] = None
    clockwise: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["showTitle", "title", "titleFont", "titleColor", "titleAlignment", "units", "decimals", "autoScale", "sortSeries", "showTotal", "showLegend", "legendPosition", "legendLabelFont", "legendLabelColor", "legendValueFont", "legendValueColor", "legendShowTotal", "showLabel", "labelPosition", "labelFont", "labelColor", "borderWidth", "borderColor", "radius", "clockwise"]

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
        """Create an instance of ReportPieChartSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of title_font
        if self.title_font:
            _dict['titleFont'] = self.title_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_label_font
        if self.legend_label_font:
            _dict['legendLabelFont'] = self.legend_label_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of legend_value_font
        if self.legend_value_font:
            _dict['legendValueFont'] = self.legend_value_font.to_dict()
        # override the default output from pydantic by calling `to_dict()` of label_font
        if self.label_font:
            _dict['labelFont'] = self.label_font.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportPieChartSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "show_title": obj.get("showTitle"),
            "title": obj.get("title"),
            "title_font": Font.from_dict(obj["titleFont"]) if obj.get("titleFont") is not None else None,
            "title_color": obj.get("titleColor"),
            "title_alignment": obj.get("titleAlignment"),
            "units": obj.get("units"),
            "decimals": obj.get("decimals"),
            "auto_scale": obj.get("autoScale"),
            "sort_series": obj.get("sortSeries"),
            "show_total": obj.get("showTotal"),
            "show_legend": obj.get("showLegend"),
            "legend_position": obj.get("legendPosition"),
            "legend_label_font": Font.from_dict(obj["legendLabelFont"]) if obj.get("legendLabelFont") is not None else None,
            "legend_label_color": obj.get("legendLabelColor"),
            "legend_value_font": Font.from_dict(obj["legendValueFont"]) if obj.get("legendValueFont") is not None else None,
            "legend_value_color": obj.get("legendValueColor"),
            "legend_show_total": obj.get("legendShowTotal"),
            "show_label": obj.get("showLabel"),
            "label_position": obj.get("labelPosition"),
            "label_font": Font.from_dict(obj["labelFont"]) if obj.get("labelFont") is not None else None,
            "label_color": obj.get("labelColor"),
            "border_width": obj.get("borderWidth"),
            "border_color": obj.get("borderColor"),
            "radius": obj.get("radius"),
            "clockwise": obj.get("clockwise")
        })
        return _obj


