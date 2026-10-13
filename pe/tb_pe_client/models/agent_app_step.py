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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID
from tb_pe_client.models.agent_app_step_type import AgentAppStepType
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_pe_client.models.agent_finalize_step import AgentFinalizeStep
    from tb_pe_client.models.agent_prepare_step import AgentPrepareStep
    from tb_pe_client.models.backup_volumes_remove_step import BackupVolumesRemoveStep
    from tb_pe_client.models.backup_volumes_step import BackupVolumesStep
    from tb_pe_client.models.compose_down_step import ComposeDownStep
    from tb_pe_client.models.compose_restart_step import ComposeRestartStep
    from tb_pe_client.models.compose_start_step import ComposeStartStep
    from tb_pe_client.models.compose_step import ComposeStep
    from tb_pe_client.models.compose_type_choice_step import ComposeTypeChoiceStep
    from tb_pe_client.models.roll_back_step import RollBackStep
    from tb_pe_client.models.run_job_step import RunJobStep

class AgentAppStep(BaseModel):
    """
    AgentAppStep
    """ # noqa: E501
    id: Optional[UUID] = None
    next_id: Optional[UUID] = Field(default=None, serialization_alias="nextId")
    title: Optional[StrictStr] = None
    template_only: Optional[StrictBool] = Field(default=None, serialization_alias="templateOnly")
    condition: Optional[StrictStr] = None
    stateful: Optional[StrictBool] = None
    type: Optional[AgentAppStepType] = None
    __properties: ClassVar[List[str]] = ["id", "nextId", "title", "templateOnly", "condition", "stateful", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'AgentFinalizeStep': 'AgentFinalizeStep','AgentPrepareStep': 'AgentPrepareStep','BackupVolumesRemoveStep': 'BackupVolumesRemoveStep','BackupVolumesStep': 'BackupVolumesStep','ComposeDownStep': 'ComposeDownStep','ComposeRestartStep': 'ComposeRestartStep','ComposeStartStep': 'ComposeStartStep','ComposeStep': 'ComposeStep','ComposeTypeChoiceStep': 'ComposeTypeChoiceStep','RollBackStep': 'RollBackStep','RunJobStep': 'RunJobStep'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

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
    def from_json(cls, json_str: str) -> Optional[Union[AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep]]:
        """Create an instance of AgentAppStep from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AgentFinalizeStep, AgentPrepareStep, BackupVolumesRemoveStep, BackupVolumesStep, ComposeDownStep, ComposeRestartStep, ComposeStartStep, ComposeStep, ComposeTypeChoiceStep, RollBackStep, RunJobStep]]:
        """Create an instance of AgentAppStep from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AgentFinalizeStep':
            return import_module("tb_pe_client.models.agent_finalize_step").AgentFinalizeStep.from_dict(obj)
        if object_type ==  'AgentPrepareStep':
            return import_module("tb_pe_client.models.agent_prepare_step").AgentPrepareStep.from_dict(obj)
        if object_type ==  'BackupVolumesRemoveStep':
            return import_module("tb_pe_client.models.backup_volumes_remove_step").BackupVolumesRemoveStep.from_dict(obj)
        if object_type ==  'BackupVolumesStep':
            return import_module("tb_pe_client.models.backup_volumes_step").BackupVolumesStep.from_dict(obj)
        if object_type ==  'ComposeDownStep':
            return import_module("tb_pe_client.models.compose_down_step").ComposeDownStep.from_dict(obj)
        if object_type ==  'ComposeRestartStep':
            return import_module("tb_pe_client.models.compose_restart_step").ComposeRestartStep.from_dict(obj)
        if object_type ==  'ComposeStartStep':
            return import_module("tb_pe_client.models.compose_start_step").ComposeStartStep.from_dict(obj)
        if object_type ==  'ComposeStep':
            return import_module("tb_pe_client.models.compose_step").ComposeStep.from_dict(obj)
        if object_type ==  'ComposeTypeChoiceStep':
            return import_module("tb_pe_client.models.compose_type_choice_step").ComposeTypeChoiceStep.from_dict(obj)
        if object_type ==  'RollBackStep':
            return import_module("tb_pe_client.models.roll_back_step").RollBackStep.from_dict(obj)
        if object_type ==  'RunJobStep':
            return import_module("tb_pe_client.models.run_job_step").RunJobStep.from_dict(obj)

        raise ValueError("AgentAppStep failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


