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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.entity_alias import EntityAlias
from tb_paas_client.models.filter import Filter
from tb_paas_client.models.header_footer import HeaderFooter
from tb_paas_client.models.insets import Insets
from tb_paas_client.models.page_orientation import PageOrientation
from tb_paas_client.models.page_size import PageSize
from tb_paas_client.models.report_component import ReportComponent
from tb_paas_client.models.report_template_config import ReportTemplateConfig
from tb_paas_client.models.tb_report_format import TbReportFormat
from typing import Optional, Set
from typing_extensions import Self

class PdfReportTemplateConfig(ReportTemplateConfig):
    """
    PdfReportTemplateConfig
    """ # noqa: E501
    format: TbReportFormat = TbReportFormat.PDF  # post_process: discriminator default
    footer: Optional[HeaderFooter] = None
    header: Optional[HeaderFooter] = None
    page_background: Optional[StrictStr] = Field(default=None, serialization_alias="pageBackground")
    page_margins: Optional[Insets] = Field(default=None, serialization_alias="pageMargins")
    page_orientation: Optional[PageOrientation] = Field(default=None, serialization_alias="pageOrientation")
    page_size: Optional[PageSize] = Field(default=None, serialization_alias="pageSize")
    __properties: ClassVar[List[str]] = ["namePattern", "timeDataPattern", "format", "entityAliases", "filters", "components", "footer", "header", "pageBackground", "pageMargins", "pageOrientation", "pageSize"]

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
        """Create an instance of PdfReportTemplateConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entity_aliases (list)
        _items = []
        if self.entity_aliases:
            for _item_entity_aliases in self.entity_aliases:
                if _item_entity_aliases:
                    _items.append(_item_entity_aliases.to_dict())
            _dict['entityAliases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of footer
        if self.footer:
            _dict['footer'] = self.footer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of header
        if self.header:
            _dict['header'] = self.header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_margins
        if self.page_margins:
            _dict['pageMargins'] = self.page_margins.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PdfReportTemplateConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name_pattern": obj.get("namePattern"),
            "time_data_pattern": obj.get("timeDataPattern"),
            "format": obj.get("format"),
            "entity_aliases": [EntityAlias.from_dict(_item) for _item in obj["entityAliases"]] if obj.get("entityAliases") is not None else None,
            "filters": [Filter.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "components": [ReportComponent.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "footer": HeaderFooter.from_dict(obj["footer"]) if obj.get("footer") is not None else None,
            "header": HeaderFooter.from_dict(obj["header"]) if obj.get("header") is not None else None,
            "page_background": obj.get("pageBackground"),
            "page_margins": Insets.from_dict(obj["pageMargins"]) if obj.get("pageMargins") is not None else None,
            "page_orientation": obj.get("pageOrientation"),
            "page_size": obj.get("pageSize")
        })
        return _obj


