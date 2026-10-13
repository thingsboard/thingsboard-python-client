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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from tb_pe_client.models.agent_app_event_action_type import AgentAppEventActionType
from tb_pe_client.models.agent_app_event_id import AgentAppEventId
from tb_pe_client.models.agent_app_event_step_states_value import AgentAppEventStepStatesValue
from tb_pe_client.models.agent_application_id import AgentApplicationId
from tb_pe_client.models.agent_id import AgentId
from tb_pe_client.models.agent_processing_status import AgentProcessingStatus
from tb_pe_client.models.processing_start_status import ProcessingStartStatus
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AgentAppEventInfo(BaseModel):
    """
    AgentAppEventInfo
    """ # noqa: E501
    id: Optional[AgentAppEventId] = Field(default=None, description="JSON object with the Agent App Event Id.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the event creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, serialization_alias="tenantId")
    application_id: Optional[AgentApplicationId] = Field(default=None, serialization_alias="applicationId")
    agent_id: Optional[AgentId] = Field(default=None, serialization_alias="agentId")
    application_name: Optional[StrictStr] = Field(default=None, serialization_alias="applicationName")
    action_type: Optional[AgentAppEventActionType] = Field(default=None, serialization_alias="actionType")
    start_status: Optional[ProcessingStartStatus] = Field(default=None, serialization_alias="startStatus")
    processing_status: Optional[AgentProcessingStatus] = Field(default=None, serialization_alias="processingStatus")
    current_step_id: Optional[UUID] = Field(default=None, serialization_alias="currentStepId")
    current_activity: Optional[StrictStr] = Field(default=None, serialization_alias="currentActivity")
    error_message: Optional[StrictStr] = Field(default=None, serialization_alias="errorMessage")
    updated_time: Optional[StrictInt] = Field(default=None, serialization_alias="updatedTime")
    step_states: Optional[Dict[str, AgentAppEventStepStatesValue]] = Field(default=None, serialization_alias="stepStates")
    bulk_action_id: Optional[UUID] = Field(default=None, serialization_alias="bulkActionId")
    resolved_arguments: Optional[Dict[str, StrictStr]] = Field(default=None, serialization_alias="resolvedArguments")
    winner_container_id: Optional[StrictStr] = Field(default=None, serialization_alias="winnerContainerId")
    finalize_deadline_ts: Optional[StrictInt] = Field(default=None, serialization_alias="finalizeDeadlineTs")
    context_metadata: Optional[Dict[str, StrictStr]] = Field(default=None, serialization_alias="contextMetadata")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the Agent that owns the Application.", serialization_alias="agentName")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "applicationId", "agentId", "applicationName", "actionType", "startStatus", "processingStatus", "currentStepId", "currentActivity", "errorMessage", "updatedTime", "stepStates", "bulkActionId", "resolvedArguments", "winnerContainerId", "finalizeDeadlineTs", "contextMetadata", "agentName"]

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
        """Create an instance of AgentAppEventInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "agent_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application_id
        if self.application_id:
            _dict['applicationId'] = self.application_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent_id
        if self.agent_id:
            _dict['agentId'] = self.agent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in step_states (dict)
        _field_dict = {}
        if self.step_states:
            for _key_step_states in self.step_states:
                if self.step_states[_key_step_states]:
                    _field_dict[_key_step_states] = self.step_states[_key_step_states].to_dict()
            _dict['stepStates'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentAppEventInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AgentAppEventId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "application_id": AgentApplicationId.from_dict(obj["applicationId"]) if obj.get("applicationId") is not None else None,
            "agent_id": AgentId.from_dict(obj["agentId"]) if obj.get("agentId") is not None else None,
            "application_name": obj.get("applicationName"),
            "action_type": obj.get("actionType"),
            "start_status": obj.get("startStatus"),
            "processing_status": obj.get("processingStatus"),
            "current_step_id": obj.get("currentStepId"),
            "current_activity": obj.get("currentActivity"),
            "error_message": obj.get("errorMessage"),
            "updated_time": obj.get("updatedTime"),
            "step_states": dict(
                (_k, AgentAppEventStepStatesValue.from_dict(_v))
                for _k, _v in obj["stepStates"].items()
            )
            if obj.get("stepStates") is not None
            else None,
            "bulk_action_id": obj.get("bulkActionId"),
            "resolved_arguments": obj.get("resolvedArguments"),
            "winner_container_id": obj.get("winnerContainerId"),
            "finalize_deadline_ts": obj.get("finalizeDeadlineTs"),
            "context_metadata": obj.get("contextMetadata"),
            "agent_name": obj.get("agentName")
        })
        return _obj


