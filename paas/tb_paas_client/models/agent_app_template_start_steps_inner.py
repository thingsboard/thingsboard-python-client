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
from tb_paas_client.models.agent_finalize_step import AgentFinalizeStep
from tb_paas_client.models.agent_prepare_step import AgentPrepareStep
from tb_paas_client.models.backup_volumes_remove_step import BackupVolumesRemoveStep
from tb_paas_client.models.backup_volumes_step import BackupVolumesStep
from tb_paas_client.models.compose_down_step import ComposeDownStep
from tb_paas_client.models.compose_restart_step import ComposeRestartStep
from tb_paas_client.models.compose_start_step import ComposeStartStep
from tb_paas_client.models.compose_step import ComposeStep
from tb_paas_client.models.compose_type_choice_step import ComposeTypeChoiceStep
from tb_paas_client.models.roll_back_step import RollBackStep
from tb_paas_client.models.run_job_step import RunJobStep
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

AGENTAPPTEMPLATESTARTSTEPSINNER_ONE_OF_SCHEMAS = ["AgentFinalizeStep", "AgentPrepareStep", "BackupVolumesRemoveStep", "BackupVolumesStep", "ComposeDownStep", "ComposeRestartStep", "ComposeStartStep", "ComposeStep", "ComposeTypeChoiceStep", "RollBackStep", "RunJobStep"]

class AgentAppTemplateStartStepsInner(BaseModel):
    """
    AgentAppTemplateStartStepsInner
    """
    # data type: AgentFinalizeStep
    oneof_schema_1_validator: Optional[AgentFinalizeStep] = None
    # data type: AgentPrepareStep
    oneof_schema_2_validator: Optional[AgentPrepareStep] = None
    # data type: BackupVolumesRemoveStep
    oneof_schema_3_validator: Optional[BackupVolumesRemoveStep] = None
    # data type: BackupVolumesStep
    oneof_schema_4_validator: Optional[BackupVolumesStep] = None
    # data type: ComposeDownStep
    oneof_schema_5_validator: Optional[ComposeDownStep] = None
    # data type: ComposeRestartStep
    oneof_schema_6_validator: Optional[ComposeRestartStep] = None
    # data type: ComposeStartStep
    oneof_schema_7_validator: Optional[ComposeStartStep] = None
    # data type: ComposeStep
    oneof_schema_8_validator: Optional[ComposeStep] = None
    # data type: ComposeTypeChoiceStep
    oneof_schema_9_validator: Optional[ComposeTypeChoiceStep] = None
    # data type: RollBackStep
    oneof_schema_10_validator: Optional[RollBackStep] = None
    # data type: RunJobStep
    oneof_schema_11_validator: Optional[RunJobStep] = None
    actual_instance: Optional[Union[AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep]] = None
    one_of_schemas: Set[str] = { "AgentFinalizeStep", "AgentPrepareStep", "BackupVolumesRemoveStep", "BackupVolumesStep", "ComposeDownStep", "ComposeRestartStep", "ComposeStartStep", "ComposeStep", "ComposeTypeChoiceStep", "RollBackStep", "RunJobStep" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
        instance = AgentAppTemplateStartStepsInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: AgentFinalizeStep
        if not isinstance(v, AgentFinalizeStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentFinalizeStep`")
        else:
            match += 1
        # validate data type: AgentPrepareStep
        if not isinstance(v, AgentPrepareStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AgentPrepareStep`")
        else:
            match += 1
        # validate data type: BackupVolumesRemoveStep
        if not isinstance(v, BackupVolumesRemoveStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackupVolumesRemoveStep`")
        else:
            match += 1
        # validate data type: BackupVolumesStep
        if not isinstance(v, BackupVolumesStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BackupVolumesStep`")
        else:
            match += 1
        # validate data type: ComposeDownStep
        if not isinstance(v, ComposeDownStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeDownStep`")
        else:
            match += 1
        # validate data type: ComposeRestartStep
        if not isinstance(v, ComposeRestartStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeRestartStep`")
        else:
            match += 1
        # validate data type: ComposeStartStep
        if not isinstance(v, ComposeStartStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeStartStep`")
        else:
            match += 1
        # validate data type: ComposeStep
        if not isinstance(v, ComposeStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeStep`")
        else:
            match += 1
        # validate data type: ComposeTypeChoiceStep
        if not isinstance(v, ComposeTypeChoiceStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ComposeTypeChoiceStep`")
        else:
            match += 1
        # validate data type: RollBackStep
        if not isinstance(v, RollBackStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RollBackStep`")
        else:
            match += 1
        # validate data type: RunJobStep
        if not isinstance(v, RunJobStep):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RunJobStep`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in AgentAppTemplateStartStepsInner with oneOf schemas: AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in AgentAppTemplateStartStepsInner with oneOf schemas: AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep. Details: " + ", ".join(error_messages))
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

        # deserialize data into AgentFinalizeStep
        try:
            instance.actual_instance = AgentFinalizeStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AgentPrepareStep
        try:
            instance.actual_instance = AgentPrepareStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BackupVolumesRemoveStep
        try:
            instance.actual_instance = BackupVolumesRemoveStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BackupVolumesStep
        try:
            instance.actual_instance = BackupVolumesStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeDownStep
        try:
            instance.actual_instance = ComposeDownStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeRestartStep
        try:
            instance.actual_instance = ComposeRestartStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeStartStep
        try:
            instance.actual_instance = ComposeStartStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeStep
        try:
            instance.actual_instance = ComposeStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ComposeTypeChoiceStep
        try:
            instance.actual_instance = ComposeTypeChoiceStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RollBackStep
        try:
            instance.actual_instance = RollBackStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RunJobStep
        try:
            instance.actual_instance = RunJobStep.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AgentAppTemplateStartStepsInner with oneOf schemas: AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AgentAppTemplateStartStepsInner with oneOf schemas: AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep]]:
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


