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
from tb_pe_client.models.entity_export_settings import EntityExportSettings
from tb_pe_client.models.entity_id import EntityId
from typing import Optional, Set
from typing_extensions import Self

class SolutionExportRequest(BaseModel):
    """
    Solution export request specifying which entities to include and export settings.
    """ # noqa: E501
    internal_ids: Optional[List[EntityId]] = Field(default=None, description="Set of internal entity IDs to export. The 'id' of each EntityId is the server-internal UUID. All listed entities must belong to the current tenant. Optional, but at least one of 'internalIds' or 'externalIds' must be non-empty.", serialization_alias="internalIds")
    external_ids: Optional[List[EntityId]] = Field(default=None, description="Set of external entity IDs to export. The 'id' of each EntityId is the external UUID (as stored in the 'externalId' field on the entity in the current tenant). The server looks up each entity by 'externalId' and 'entityType' within the current tenant. Optional, but at least one of 'internalIds' or 'externalIds' must be non-empty.", serialization_alias="externalIds")
    settings: Optional[EntityExportSettings] = Field(default=None, description="Optional export settings controlling what additional data is included (relations, attributes, credentials, etc.). If not specified, default settings will be used that include all available data.")
    __properties: ClassVar[List[str]] = ["internalIds", "externalIds", "settings"]

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
        """Create an instance of SolutionExportRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in internal_ids (list)
        _items = []
        if self.internal_ids:
            for _item_internal_ids in self.internal_ids:
                if _item_internal_ids:
                    _items.append(_item_internal_ids.to_dict())
            _dict['internalIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_ids (list)
        _items = []
        if self.external_ids:
            for _item_external_ids in self.external_ids:
                if _item_external_ids:
                    _items.append(_item_external_ids.to_dict())
            _dict['externalIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SolutionExportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "internal_ids": [EntityId.from_dict(_item) for _item in obj["internalIds"]] if obj.get("internalIds") is not None else None,
            "external_ids": [EntityId.from_dict(_item) for _item in obj["externalIds"]] if obj.get("externalIds") is not None else None,
            "settings": EntityExportSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None
        })
        return _obj


