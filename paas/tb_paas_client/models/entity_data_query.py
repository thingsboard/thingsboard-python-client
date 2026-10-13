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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.alarm_rule_complex_operation import AlarmRuleComplexOperation
from tb_paas_client.models.entity_data_page_link import EntityDataPageLink
from tb_paas_client.models.entity_filter import EntityFilter
from tb_paas_client.models.entity_key import EntityKey
from tb_paas_client.models.key_filter import KeyFilter
from typing import Optional, Set
from typing_extensions import Self

class EntityDataQuery(BaseModel):
    """
    Entity data query to find entities. Page size is capped at 100.
    """ # noqa: E501
    entity_filter: Optional[EntityFilter] = Field(default=None, serialization_alias="entityFilter")
    key_filters: Optional[List[KeyFilter]] = Field(default=None, serialization_alias="keyFilters")
    key_filters_operation: Optional[AlarmRuleComplexOperation] = Field(default=None, serialization_alias="keyFiltersOperation")
    page_link: Optional[EntityDataPageLink] = Field(default=None, serialization_alias="pageLink")
    entity_fields: Optional[List[EntityKey]] = Field(default=None, serialization_alias="entityFields")
    latest_values: Optional[List[EntityKey]] = Field(default=None, serialization_alias="latestValues")
    key_filters_operation_or_default: Optional[AlarmRuleComplexOperation] = Field(default=None, serialization_alias="keyFiltersOperationOrDefault")
    __properties: ClassVar[List[str]] = ["entityFilter", "keyFilters", "keyFiltersOperation", "pageLink", "entityFields", "latestValues", "keyFiltersOperationOrDefault"]

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
        """Create an instance of EntityDataQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_filter
        if self.entity_filter:
            _dict['entityFilter'] = self.entity_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in key_filters (list)
        _items = []
        if self.key_filters:
            for _item_key_filters in self.key_filters:
                if _item_key_filters:
                    _items.append(_item_key_filters.to_dict())
            _dict['keyFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of page_link
        if self.page_link:
            _dict['pageLink'] = self.page_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in entity_fields (list)
        _items = []
        if self.entity_fields:
            for _item_entity_fields in self.entity_fields:
                if _item_entity_fields:
                    _items.append(_item_entity_fields.to_dict())
            _dict['entityFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in latest_values (list)
        _items = []
        if self.latest_values:
            for _item_latest_values in self.latest_values:
                if _item_latest_values:
                    _items.append(_item_latest_values.to_dict())
            _dict['latestValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityDataQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entity_filter": EntityFilter.from_dict(obj["entityFilter"]) if obj.get("entityFilter") is not None else None,
            "key_filters": [KeyFilter.from_dict(_item) for _item in obj["keyFilters"]] if obj.get("keyFilters") is not None else None,
            "key_filters_operation": obj.get("keyFiltersOperation"),
            "page_link": EntityDataPageLink.from_dict(obj["pageLink"]) if obj.get("pageLink") is not None else None,
            "entity_fields": [EntityKey.from_dict(_item) for _item in obj["entityFields"]] if obj.get("entityFields") is not None else None,
            "latest_values": [EntityKey.from_dict(_item) for _item in obj["latestValues"]] if obj.get("latestValues") is not None else None,
            "key_filters_operation_or_default": obj.get("keyFiltersOperationOrDefault")
        })
        return _obj


