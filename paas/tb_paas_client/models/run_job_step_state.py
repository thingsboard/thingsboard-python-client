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
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.agent_app_step_state import AgentAppStepState
from tb_paas_client.models.agent_app_step_type import AgentAppStepType
from tb_paas_client.models.step_field_boolean import StepFieldBoolean
from tb_paas_client.models.step_field_integer import StepFieldInteger
from tb_paas_client.models.step_field_list_string import StepFieldListString
from tb_paas_client.models.step_field_string import StepFieldString
from typing import Optional, Set
from typing_extensions import Self

class RunJobStepState(AgentAppStepState):
    """
    RunJobStepState
    """ # noqa: E501
    image: Optional[StepFieldString] = None
    entrypoint: Optional[StepFieldListString] = None
    cmd: Optional[StepFieldListString] = None
    env: Optional[StepFieldListString] = None
    binds: Optional[StepFieldListString] = None
    networks: Optional[StepFieldListString] = None
    pull_images: Optional[StepFieldBoolean] = Field(default=None, serialization_alias="pullImages")
    retries: Optional[StepFieldInteger] = None
    network_from_service_image_regex_pattern: Optional[StepFieldString] = Field(default=None, serialization_alias="networkFromServiceImageRegexPattern")
    __properties: ClassVar[List[str]] = ["type", "image", "entrypoint", "cmd", "env", "binds", "networks", "pullImages", "retries", "networkFromServiceImageRegexPattern"]

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
        """Create an instance of RunJobStepState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entrypoint
        if self.entrypoint:
            _dict['entrypoint'] = self.entrypoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cmd
        if self.cmd:
            _dict['cmd'] = self.cmd.to_dict()
        # override the default output from pydantic by calling `to_dict()` of env
        if self.env:
            _dict['env'] = self.env.to_dict()
        # override the default output from pydantic by calling `to_dict()` of binds
        if self.binds:
            _dict['binds'] = self.binds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of networks
        if self.networks:
            _dict['networks'] = self.networks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pull_images
        if self.pull_images:
            _dict['pullImages'] = self.pull_images.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retries
        if self.retries:
            _dict['retries'] = self.retries.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network_from_service_image_regex_pattern
        if self.network_from_service_image_regex_pattern:
            _dict['networkFromServiceImageRegexPattern'] = self.network_from_service_image_regex_pattern.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RunJobStepState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "image": StepFieldString.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "entrypoint": StepFieldListString.from_dict(obj["entrypoint"]) if obj.get("entrypoint") is not None else None,
            "cmd": StepFieldListString.from_dict(obj["cmd"]) if obj.get("cmd") is not None else None,
            "env": StepFieldListString.from_dict(obj["env"]) if obj.get("env") is not None else None,
            "binds": StepFieldListString.from_dict(obj["binds"]) if obj.get("binds") is not None else None,
            "networks": StepFieldListString.from_dict(obj["networks"]) if obj.get("networks") is not None else None,
            "pull_images": StepFieldBoolean.from_dict(obj["pullImages"]) if obj.get("pullImages") is not None else None,
            "retries": StepFieldInteger.from_dict(obj["retries"]) if obj.get("retries") is not None else None,
            "network_from_service_image_regex_pattern": StepFieldString.from_dict(obj["networkFromServiceImageRegexPattern"]) if obj.get("networkFromServiceImageRegexPattern") is not None else None
        })
        return _obj


