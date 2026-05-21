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
from tb_paas_client.models.calculated_field_id import CalculatedFieldId
from tb_paas_client.models.job_configuration import JobConfiguration
from tb_paas_client.models.task_result import TaskResult
from typing import Optional, Set
from typing_extensions import Self

class CfReprocessingJobConfiguration(JobConfiguration):
    """
    CfReprocessingJobConfiguration
    """ # noqa: E501
    type: StrictStr = "CF_REPROCESSING"  # post_process: discriminator default
    calculated_field_id: CalculatedFieldId = Field(serialization_alias="calculatedFieldId")
    calculated_field_name: Optional[StrictStr] = Field(default=None, serialization_alias="calculatedFieldName")
    start_ts: Optional[StrictInt] = Field(default=None, serialization_alias="startTs")
    end_ts: Optional[StrictInt] = Field(default=None, serialization_alias="endTs")
    __properties: ClassVar[List[str]] = ["tasksKey", "toReprocess", "type", "calculatedFieldId", "calculatedFieldName", "startTs", "endTs"]

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
        """Create an instance of CfReprocessingJobConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in to_reprocess (list)
        _items = []
        if self.to_reprocess:
            for _item_to_reprocess in self.to_reprocess:
                if _item_to_reprocess:
                    _items.append(_item_to_reprocess.to_dict())
            _dict['toReprocess'] = _items
        # override the default output from pydantic by calling `to_dict()` of calculated_field_id
        if self.calculated_field_id:
            _dict['calculatedFieldId'] = self.calculated_field_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CfReprocessingJobConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks_key": obj.get("tasksKey"),
            "to_reprocess": [TaskResult.from_dict(_item) for _item in obj["toReprocess"]] if obj.get("toReprocess") is not None else None,
            "type": obj.get("type"),
            "calculated_field_id": CalculatedFieldId.from_dict(obj["calculatedFieldId"]) if obj.get("calculatedFieldId") is not None else None,
            "calculated_field_name": obj.get("calculatedFieldName"),
            "start_ts": obj.get("startTs"),
            "end_ts": obj.get("endTs")
        })
        return _obj


