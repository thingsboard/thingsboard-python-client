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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.skipped_app import SkippedApp
from typing import Optional, Set
from typing_extensions import Self

class BulkOperationPreview(BaseModel):
    """
    BulkOperationPreview
    """ # noqa: E501
    total: Optional[StrictInt] = Field(default=None, description="Total number of apps targeted by the bulk operation")
    eligible: Optional[StrictInt] = Field(default=None, description="Number of apps that would be submitted (total minus skipped)")
    skipped_counts_by_reason: Optional[Dict[str, StrictInt]] = Field(default=None, description="Skip count per reason for the targeted apps", serialization_alias="skippedCountsByReason")
    skipped_sample: Optional[List[SkippedApp]] = Field(default=None, description="Sample of skipped apps, capped per reason. Use the run history to inspect the full list.", serialization_alias="skippedSample")
    __properties: ClassVar[List[str]] = ["total", "eligible", "skippedCountsByReason", "skippedSample"]

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
        """Create an instance of BulkOperationPreview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in skipped_sample (list)
        _items = []
        if self.skipped_sample:
            for _item_skipped_sample in self.skipped_sample:
                if _item_skipped_sample:
                    _items.append(_item_skipped_sample.to_dict())
            _dict['skippedSample'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BulkOperationPreview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": obj.get("total"),
            "eligible": obj.get("eligible"),
            "skipped_counts_by_reason": obj.get("skippedCountsByReason"),
            "skipped_sample": [SkippedApp.from_dict(_item) for _item in obj["skippedSample"]] if obj.get("skippedSample") is not None else None
        })
        return _obj


