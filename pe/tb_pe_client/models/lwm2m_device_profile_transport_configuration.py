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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.device_profile_transport_configuration import DeviceProfileTransportConfiguration
from tb_pe_client.models.lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential
from tb_pe_client.models.other_configuration import OtherConfiguration
from tb_pe_client.models.telemetry_mapping_configuration import TelemetryMappingConfiguration
from typing import Optional, Set
from typing_extensions import Self

class Lwm2mDeviceProfileTransportConfiguration(DeviceProfileTransportConfiguration):
    """
    Lwm2mDeviceProfileTransportConfiguration
    """ # noqa: E501
    type: StrictStr = "LWM2M"  # post_process: discriminator default
    observe_attr: Optional[TelemetryMappingConfiguration] = Field(default=None, description="Configuration for mapping LwM2M resources to telemetry and attributes", serialization_alias="observeAttr")
    bootstrap_server_update_enable: Optional[StrictBool] = Field(default=None, description="Flag indicating whether LwM2M bootstrap server update is enabled", serialization_alias="bootstrapServerUpdateEnable")
    bootstrap: Optional[List[LwM2MBootstrapServerCredential]] = None
    client_lw_m2m_settings: Optional[OtherConfiguration] = Field(default=None, description="Other LwM2M client settings", serialization_alias="clientLwM2mSettings")
    __properties: ClassVar[List[str]] = ["type", "observeAttr", "bootstrapServerUpdateEnable", "bootstrap", "clientLwM2mSettings"]

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
        """Create an instance of Lwm2mDeviceProfileTransportConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of observe_attr
        if self.observe_attr:
            _dict['observeAttr'] = self.observe_attr.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bootstrap (list)
        _items = []
        if self.bootstrap:
            for _item_bootstrap in self.bootstrap:
                if _item_bootstrap:
                    _items.append(_item_bootstrap.to_dict())
            _dict['bootstrap'] = _items
        # override the default output from pydantic by calling `to_dict()` of client_lw_m2m_settings
        if self.client_lw_m2m_settings:
            _dict['clientLwM2mSettings'] = self.client_lw_m2m_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Lwm2mDeviceProfileTransportConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "observe_attr": TelemetryMappingConfiguration.from_dict(obj["observeAttr"]) if obj.get("observeAttr") is not None else None,
            "bootstrap_server_update_enable": obj.get("bootstrapServerUpdateEnable"),
            "bootstrap": [LwM2MBootstrapServerCredential.from_dict(_item) for _item in obj["bootstrap"]] if obj.get("bootstrap") is not None else None,
            "client_lw_m2m_settings": OtherConfiguration.from_dict(obj["clientLwM2mSettings"]) if obj.get("clientLwM2mSettings") is not None else None
        })
        return _obj


