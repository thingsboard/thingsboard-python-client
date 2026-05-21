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

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from tb_ce_client.models.calculated_field import CalculatedField
from tb_ce_client.models.entity_export_data import EntityExportData
from tb_ce_client.models.entity_relation import EntityRelation
from tb_ce_client.models.entity_type import EntityType
from tb_ce_client.models.exportable_entity import ExportableEntity
from typing import Optional, Set
from typing_extensions import Self

class AssetExportData(EntityExportData):
    """
    AssetExportData
    """ # noqa: E501
    entity_type: EntityType = Field(default=EntityType.ASSET, serialization_alias="entityType")  # post_process: discriminator default
    __properties: ClassVar[List[str]] = ["entity", "relations", "attributes", "calculatedFields", "entityType"]

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
        """Create an instance of AssetExportData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity
        if self.entity:
            _dict['entity'] = self.entity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in relations (list)
        _items = []
        if self.relations:
            for _item_relations in self.relations:
                if _item_relations:
                    _items.append(_item_relations.to_dict())
            _dict['relations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict of array)
        _field_dict_of_array = {}
        if self.attributes:
            for _key_attributes in self.attributes:
                if self.attributes[_key_attributes] is not None:
                    _field_dict_of_array[_key_attributes] = [
                        _item.to_dict() for _item in self.attributes[_key_attributes]
                    ]
            _dict['attributes'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each item in calculated_fields (list)
        _items = []
        if self.calculated_fields:
            for _item_calculated_fields in self.calculated_fields:
                if _item_calculated_fields:
                    _items.append(_item_calculated_fields.to_dict())
            _dict['calculatedFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetExportData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entity": ExportableEntity.from_dict(obj["entity"]) if obj.get("entity") is not None else None,
            "relations": [EntityRelation.from_dict(_item) for _item in obj["relations"]] if obj.get("relations") is not None else None,
            "attributes": dict(
                (_k,
                        [AttributeExportData.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("attributes", {}).items()
            ),
            "calculatedFields": [CalculatedField.from_dict(_item) for _item in obj["calculatedFields"]] if obj.get("calculatedFields") is not None else None,
            "entityType": obj.get("entityType")
        })
        return _obj


