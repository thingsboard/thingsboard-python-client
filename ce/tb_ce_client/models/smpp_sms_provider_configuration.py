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

from pydantic import ConfigDict, Field, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from tb_ce_client.models.smpp_bind_type import SmppBindType
from tb_ce_client.models.sms_provider_configuration import SmsProviderConfiguration
from typing import Optional, Set
from typing_extensions import Self

class SmppSmsProviderConfiguration(SmsProviderConfiguration):
    """
    SmppSmsProviderConfiguration
    """ # noqa: E501
    type: StrictStr = "SMPP"  # post_process: discriminator default
    protocol_version: StrictStr = Field(description="SMPP version", serialization_alias="protocolVersion")
    host: StrictStr = Field(description="SMPP host")
    port: StrictInt = Field(description="SMPP port")
    system_id: StrictStr = Field(description="System ID", serialization_alias="systemId")
    password: StrictStr = Field(description="Password")
    system_type: Optional[StrictStr] = Field(default=None, description="System type", serialization_alias="systemType")
    bind_type: Optional[SmppBindType] = Field(default=None, description="TX - Transmitter, RX - Receiver, TRX - Transciever. By default TX is used", serialization_alias="bindType")
    service_type: Optional[StrictStr] = Field(default=None, description="Service type", serialization_alias="serviceType")
    source_address: Optional[StrictStr] = Field(default=None, description="Source address", serialization_alias="sourceAddress")
    source_ton: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="Source TON (Type of Number). Needed is source address is set. 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated", serialization_alias="sourceTon")
    source_npi: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="Source NPI (Numbering Plan Identification). Needed is source address is set. 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)", serialization_alias="sourceNpi")
    destination_ton: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="Destination TON (Type of Number). 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated", serialization_alias="destinationTon")
    destination_npi: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="Destination NPI (Numbering Plan Identification). 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)", serialization_alias="destinationNpi")
    address_range: Optional[StrictStr] = Field(default=None, description="Address range", serialization_alias="addressRange")
    coding_scheme: Optional[Union[Annotated[bytes, Field(strict=True)], Annotated[str, Field(strict=True)]]] = Field(default=None, description="0 - SMSC Default Alphabet (ASCII for short and long code and to GSM for toll-free, used as default) 1 - IA5 (ASCII for short and long code, Latin 9 for toll-free (ISO-8859-9)) 2 - Octet Unspecified (8-bit binary) 3 - Latin 1 (ISO-8859-1) 4 - Octet Unspecified (8-bit binary) 5 - JIS (X 0208-1990) 6 - Cyrillic (ISO-8859-5) 7 - Latin/Hebrew (ISO-8859-8) 8 - UCS2/UTF-16 (ISO/IEC-10646) 9 - Pictogram Encoding 10 - Music Codes (ISO-2022-JP) 13 - Extended Kanji JIS (X 0212-1990) 14 - Korean Graphic Character Set (KS C 5601/KS X 1001)", serialization_alias="codingScheme")
    __properties: ClassVar[List[str]] = ["type", "protocolVersion", "host", "port", "systemId", "password", "systemType", "bindType", "serviceType", "sourceAddress", "sourceTon", "sourceNpi", "destinationTon", "destinationNpi", "addressRange", "codingScheme"]

    @field_validator('protocol_version')
    def protocol_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['3.3, 3.4']):
            raise ValueError("must be one of enum values ('3.3, 3.4')")
        return value

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
        """Create an instance of SmppSmsProviderConfiguration from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmppSmsProviderConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "protocol_version": obj.get("protocolVersion"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "system_id": obj.get("systemId"),
            "password": obj.get("password"),
            "system_type": obj.get("systemType"),
            "bind_type": obj.get("bindType"),
            "service_type": obj.get("serviceType"),
            "source_address": obj.get("sourceAddress"),
            "source_ton": obj.get("sourceTon"),
            "source_npi": obj.get("sourceNpi"),
            "destination_ton": obj.get("destinationTon"),
            "destination_npi": obj.get("destinationNpi"),
            "address_range": obj.get("addressRange"),
            "coding_scheme": obj.get("codingScheme")
        })
        return _obj


