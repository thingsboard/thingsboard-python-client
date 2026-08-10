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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tb_ce_client.models.no_sec_lw_m2_m_bootstrap_server_credential import NoSecLwM2MBootstrapServerCredential
    from tb_ce_client.models.psklw_m2_m_bootstrap_server_credential import PSKLwM2MBootstrapServerCredential
    from tb_ce_client.models.rpklw_m2_m_bootstrap_server_credential import RPKLwM2MBootstrapServerCredential
    from tb_ce_client.models.x509_lw_m2_m_bootstrap_server_credential import X509LwM2MBootstrapServerCredential

class LwM2MBootstrapServerCredential(BaseModel):
    """
    LwM2MBootstrapServerCredential
    """ # noqa: E501
    security_mode: StrictStr = Field(serialization_alias="securityMode")
    __properties: ClassVar[List[str]] = ["securityMode"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'securityMode'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'NO_SEC': 'NoSecLwM2MBootstrapServerCredential','PSK': 'PSKLwM2MBootstrapServerCredential','RPK': 'RPKLwM2MBootstrapServerCredential','X509': 'X509LwM2MBootstrapServerCredential'
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
    def from_json(cls, json_str: str) -> Optional[Union[NoSecLwM2MBootstrapServerCredential, PSKLwM2MBootstrapServerCredential, RPKLwM2MBootstrapServerCredential, X509LwM2MBootstrapServerCredential]]:
        """Create an instance of LwM2MBootstrapServerCredential from a JSON string"""
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
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[NoSecLwM2MBootstrapServerCredential, PSKLwM2MBootstrapServerCredential, RPKLwM2MBootstrapServerCredential, X509LwM2MBootstrapServerCredential]]:
        """Create an instance of LwM2MBootstrapServerCredential from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'NoSecLwM2MBootstrapServerCredential':
            return import_module("tb_ce_client.models.no_sec_lw_m2_m_bootstrap_server_credential").NoSecLwM2MBootstrapServerCredential.from_dict(obj)
        if object_type ==  'PSKLwM2MBootstrapServerCredential':
            return import_module("tb_ce_client.models.psklw_m2_m_bootstrap_server_credential").PSKLwM2MBootstrapServerCredential.from_dict(obj)
        if object_type ==  'RPKLwM2MBootstrapServerCredential':
            return import_module("tb_ce_client.models.rpklw_m2_m_bootstrap_server_credential").RPKLwM2MBootstrapServerCredential.from_dict(obj)
        if object_type ==  'X509LwM2MBootstrapServerCredential':
            return import_module("tb_ce_client.models.x509_lw_m2_m_bootstrap_server_credential").X509LwM2MBootstrapServerCredential.from_dict(obj)

        raise ValueError("LwM2MBootstrapServerCredential failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


