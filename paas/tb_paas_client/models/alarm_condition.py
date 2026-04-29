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
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tb_paas_client.models.alarm_condition_expression import AlarmConditionExpression
from tb_paas_client.models.alarm_condition_value_alarm_schedule import AlarmConditionValueAlarmSchedule
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_paas_client.models.duration_alarm_condition import DurationAlarmCondition
    from tb_paas_client.models.repeating_alarm_condition import RepeatingAlarmCondition
    from tb_paas_client.models.simple_alarm_condition import SimpleAlarmCondition

class AlarmCondition(BaseModel):
    """
    AlarmCondition
    """ # noqa: E501
    expression: AlarmConditionExpression
    schedule: Optional[AlarmConditionValueAlarmSchedule] = None
    type: StrictStr
    __properties: ClassVar[List[str]] = ["expression", "schedule", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'DURATION': 'DurationAlarmCondition','REPEATING': 'RepeatingAlarmCondition','SIMPLE': 'SimpleAlarmCondition'
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
    def from_json(cls, json_str: str) -> Optional[Union[DurationAlarmCondition, RepeatingAlarmCondition, SimpleAlarmCondition]]:
        """Create an instance of AlarmCondition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of expression
        if self.expression:
            _dict['expression'] = self.expression.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[DurationAlarmCondition, RepeatingAlarmCondition, SimpleAlarmCondition]]:
        """Create an instance of AlarmCondition from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'DurationAlarmCondition':
            return import_module("tb_paas_client.models.duration_alarm_condition").DurationAlarmCondition.from_dict(obj)
        if object_type ==  'RepeatingAlarmCondition':
            return import_module("tb_paas_client.models.repeating_alarm_condition").RepeatingAlarmCondition.from_dict(obj)
        if object_type ==  'SimpleAlarmCondition':
            return import_module("tb_paas_client.models.simple_alarm_condition").SimpleAlarmCondition.from_dict(obj)

        raise ValueError("AlarmCondition failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


