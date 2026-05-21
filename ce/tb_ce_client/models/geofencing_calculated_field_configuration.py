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

from pydantic import ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.calculated_field_configuration import CalculatedFieldConfiguration
from tb_ce_client.models.entity_coordinates import EntityCoordinates
from tb_ce_client.models.output import Output
from tb_ce_client.models.zone_group_configuration import ZoneGroupConfiguration
from typing import Optional, Set
from typing_extensions import Self

class GeofencingCalculatedFieldConfiguration(CalculatedFieldConfiguration):
    """
    GeofencingCalculatedFieldConfiguration
    """ # noqa: E501
    type: StrictStr = "GEOFENCING"  # post_process: discriminator default
    entity_coordinates: EntityCoordinates = Field(serialization_alias="entityCoordinates")
    zone_groups: Dict[str, ZoneGroupConfiguration] = Field(serialization_alias="zoneGroups")
    scheduled_update_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="scheduledUpdateEnabled")
    scheduled_update_interval: Optional[StrictInt] = Field(default=None, serialization_alias="scheduledUpdateInterval")
    __properties: ClassVar[List[str]] = ["output", "type", "entityCoordinates", "zoneGroups", "scheduledUpdateEnabled", "scheduledUpdateInterval"]

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
        """Create an instance of GeofencingCalculatedFieldConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entity_coordinates
        if self.entity_coordinates:
            _dict['entityCoordinates'] = self.entity_coordinates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in zone_groups (dict)
        _field_dict = {}
        if self.zone_groups:
            for _key_zone_groups in self.zone_groups:
                if self.zone_groups[_key_zone_groups]:
                    _field_dict[_key_zone_groups] = self.zone_groups[_key_zone_groups].to_dict()
            _dict['zoneGroups'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeofencingCalculatedFieldConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "output": Output.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "type": obj.get("type"),
            "entity_coordinates": EntityCoordinates.from_dict(obj["entityCoordinates"]) if obj.get("entityCoordinates") is not None else None,
            "zone_groups": dict(
                (_k, ZoneGroupConfiguration.from_dict(_v))
                for _k, _v in obj["zoneGroups"].items()
            )
            if obj.get("zoneGroups") is not None
            else None,
            "scheduled_update_enabled": obj.get("scheduledUpdateEnabled"),
            "scheduled_update_interval": obj.get("scheduledUpdateInterval")
        })
        return _obj


