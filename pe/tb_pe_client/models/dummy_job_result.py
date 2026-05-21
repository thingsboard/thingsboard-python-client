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
from typing import Any, ClassVar, Dict, List
from tb_pe_client.models.job_result import JobResult
from tb_pe_client.models.task_result import TaskResult
from typing import Optional, Set
from typing_extensions import Self

class DummyJobResult(JobResult):
    """
    DummyJobResult
    """ # noqa: E501
    job_type: StrictStr = Field(default="DUMMY", serialization_alias="jobType")  # post_process: discriminator default
    __properties: ClassVar[List[str]] = ["successfulCount", "failedCount", "discardedCount", "totalCount", "results", "generalError", "startTs", "finishTs", "cancellationTs", "jobType"]

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
        """Create an instance of DummyJobResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item_results in self.results:
                if _item_results:
                    _items.append(_item_results.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DummyJobResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "successful_count": obj.get("successfulCount"),
            "failed_count": obj.get("failedCount"),
            "discarded_count": obj.get("discardedCount"),
            "total_count": obj.get("totalCount"),
            "results": [TaskResult.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "general_error": obj.get("generalError"),
            "start_ts": obj.get("startTs"),
            "finish_ts": obj.get("finishTs"),
            "cancellation_ts": obj.get("cancellationTs"),
            "job_type": obj.get("jobType")
        })
        return _obj


