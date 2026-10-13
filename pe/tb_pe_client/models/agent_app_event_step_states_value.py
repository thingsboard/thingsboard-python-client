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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from tb_pe_client.models.backup_volumes_step_state import BackupVolumesStepState
from tb_pe_client.models.compose_down_step_state import ComposeDownStepState
from tb_pe_client.models.compose_step_state import ComposeStepState
from tb_pe_client.models.roll_back_step_state import RollBackStepState
from tb_pe_client.models.run_job_step_state import RunJobStepState
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

AGENTAPPEVENTSTEPSTATESVALUE_ONE_OF_SCHEMAS = ["BackupVolumesStepState", "ComposeDownStepState", "ComposeStepState", "RollBackStepState", "RunJobStepState"]

class AgentAppEventStepStatesValue(BaseModel):
    """
    AgentAppEventStepStatesValue
    """
    # data type: BackupVolumesStepState
    oneof_schema_1_validator: Optional[BackupVolumesStepState] = None
    # data type: ComposeDownStepState
    oneof_schema_2_validator: Optional[ComposeDownStepState] = None
    # data type: ComposeStepState
    oneof_schema_3_validator: Optional[ComposeStepState] = None
    # data type: RollBackStepState
    oneof_schema_4_validator: Optional[RollBackStepState] = None
    # data type: RunJobStepState
    oneof_schema_5_validator: Optional[RunJobStepState] = None
    actual_instance: Optional[Union[BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState]] = None
    one_of_schemas: Set[str] = { "BackupVolumesStepState", "ComposeDownStepState", "ComposeStepState", "RollBackStepState", "RunJobStepState" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = AgentAppEventStepStatesValue.model_construct()
        error_messages = []
        match = 0
        # validate data type: BackupVolumesStepState
        if not isinstance(v, BackupVolumesStepState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackupVolumesStepState`")
        else:
            match += 1
        # validate data type: ComposeDownStepState
        if not isinstance(v, ComposeDownStepState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeDownStepState`")
        else:
            match += 1
        # validate data type: ComposeStepState
        if not isinstance(v, ComposeStepState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeStepState`")
        else:
            match += 1
        # validate data type: RollBackStepState
        if not isinstance(v, RollBackStepState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RollBackStepState`")
        else:
            match += 1
        # validate data type: RunJobStepState
        if not isinstance(v, RunJobStepState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RunJobStepState`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AgentAppEventStepStatesValue with oneOf schemas: BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AgentAppEventStepStatesValue with oneOf schemas: BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BackupVolumesStepState
        try:
            instance.actual_instance = BackupVolumesStepState.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeDownStepState
        try:
            instance.actual_instance = ComposeDownStepState.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeStepState
        try:
            instance.actual_instance = ComposeStepState.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RollBackStepState
        try:
            instance.actual_instance = RollBackStepState.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RunJobStepState
        try:
            instance.actual_instance = RunJobStepState.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AgentAppEventStepStatesValue with oneOf schemas: BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AgentAppEventStepStatesValue with oneOf schemas: BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BackupVolumesStepState, ComposeDownStepState, ComposeStepState, RollBackStepState, RunJobStepState]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump(mode='json'))

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()


