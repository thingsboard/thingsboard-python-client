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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from tb_pe_client.models.agent_app_event_action_type import AgentAppEventActionType
from tb_pe_client.models.agent_app_event_step_states_value import AgentAppEventStepStatesValue
from tb_pe_client.models.agent_application import AgentApplication
from tb_pe_client.models.entity_id import EntityId
from typing import Optional, Set
from typing_extensions import Self

class AgentAppEventRequest(BaseModel):
    """
    Request payload for creating an agent application event (install, update, upgrade, restart, delete, etc.).
    """ # noqa: E501
    action_type: Optional[AgentAppEventActionType] = Field(default=None, description="Action to perform against the agent application.", serialization_alias="actionType")
    application: Optional[AgentApplication] = Field(default=None, description="Agent application payload supplied by the caller. Used to carry name/config changes for UPDATE and the target state for INSTALL/UPGRADE.")
    step_inputs: Optional[Dict[str, AgentAppEventStepStatesValue]] = Field(default=None, description="Per-step input overrides keyed by step id (e.g. pullImages flag, backup volume selection).", serialization_alias="stepInputs")
    related_entity_id: Optional[EntityId] = Field(default=None, description="INSTALL-action optional related entity (Edge or Gateway Device) to link to the application in the same operation. When set, the application is created and the relation is assigned atomically. Ignored for non-INSTALL actions.", serialization_alias="relatedEntityId")
    bulk_action_id: Optional[UUID] = Field(default=None, description="Optional bulk-action correlation id. When the same value is used across multiple application events, duplicates are deduplicated server-side.", serialization_alias="bulkActionId")
    skip_profile_refetch: Optional[StrictBool] = Field(default=None, description="UPDATE-action flag for profile-managed apps. When true, the compose is not re-resolved from the (possibly upgraded) profile — only the credentials carried by `application.config` are applied. Ignored for non-UPDATE actions and for non-profile-managed apps.", serialization_alias="skipProfileRefetch")
    __properties: ClassVar[List[str]] = ["actionType", "application", "stepInputs", "relatedEntityId", "bulkActionId", "skipProfileRefetch"]

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
        """Create an instance of AgentAppEventRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in step_inputs (dict)
        _field_dict = {}
        if self.step_inputs:
            for _key_step_inputs in self.step_inputs:
                if self.step_inputs[_key_step_inputs]:
                    _field_dict[_key_step_inputs] = self.step_inputs[_key_step_inputs].to_dict()
            _dict['stepInputs'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of related_entity_id
        if self.related_entity_id:
            _dict['relatedEntityId'] = self.related_entity_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentAppEventRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action_type": obj.get("actionType"),
            "application": AgentApplication.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "step_inputs": dict(
                (_k, AgentAppEventStepStatesValue.from_dict(_v))
                for _k, _v in obj["stepInputs"].items()
            )
            if obj.get("stepInputs") is not None
            else None,
            "related_entity_id": EntityId.from_dict(obj["relatedEntityId"]) if obj.get("relatedEntityId") is not None else None,
            "bulk_action_id": obj.get("bulkActionId"),
            "skip_profile_refetch": obj.get("skipProfileRefetch")
        })
        return _obj


