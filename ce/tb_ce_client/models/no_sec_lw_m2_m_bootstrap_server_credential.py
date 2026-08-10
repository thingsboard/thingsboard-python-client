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
from tb_ce_client.models.lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential
from typing import Optional, Set
from typing_extensions import Self

class NoSecLwM2MBootstrapServerCredential(LwM2MBootstrapServerCredential):
    """
    NoSecLwM2MBootstrapServerCredential
    """ # noqa: E501
    security_mode: StrictStr = Field(default="NO_SEC", serialization_alias="securityMode")  # post_process: discriminator default
    short_server_id: Optional[StrictInt] = Field(default=None, description="Server short Id. Used as link to associate server Object Instance. This identifier uniquely identifies each LwM2M Server configured for the LwM2M Client. This Resource MUST be set when the Bootstrap-Server Resource has a value of 'false'. The values ID:0 and ID:65535 values MUST NOT be used for identifying the LwM2M Server.", serialization_alias="shortServerId")
    bootstrap_server_is: Optional[StrictBool] = Field(default=None, description="Is Bootstrap Server or Lwm2m Server. The LwM2M Client MAY be configured to use one or more LwM2M Server Account(s). The LwM2M Client MUST have at most one LwM2M Bootstrap-Server Account. (*) The LwM2M client MUST have at least one LwM2M server account after completing the boot sequence specified.", serialization_alias="bootstrapServerIs")
    host: Optional[StrictStr] = Field(default=None, description="Host for 'No Security' mode")
    port: Optional[StrictInt] = Field(default=None, description="Port for  Lwm2m Server: 'No Security' mode: Lwm2m Server or Bootstrap Server")
    client_hold_off_time: Optional[StrictInt] = Field(default=None, description="Client Hold Off Time. The number of seconds to wait before initiating a Client Initiated Bootstrap once the LwM2M Client has determined it should initiate this bootstrap mode. (This information is relevant for use with a Bootstrap-Server only.)", serialization_alias="clientHoldOffTime")
    server_public_key: Optional[StrictStr] = Field(default=None, description="Server Public Key for 'Security' mode (DTLS): RPK or X509. Format: base64 encoded", serialization_alias="serverPublicKey")
    server_certificate: Optional[StrictStr] = Field(default=None, description="Server Public Key for 'Security' mode (DTLS): X509. Format: base64 encoded", serialization_alias="serverCertificate")
    bootstrap_server_account_timeout: Optional[StrictInt] = Field(default=None, description="Bootstrap Server Account Timeout (If the value is set to 0, or if this resource is not instantiated, the Bootstrap-Server Account lifetime is infinite.)", serialization_alias="bootstrapServerAccountTimeout")
    lifetime: Optional[StrictInt] = Field(default=None, description="Specify the lifetime of the registration in seconds.")
    default_min_period: Optional[StrictInt] = Field(default=None, description="The default value the LwM2M Client should use for the Minimum Period of an Observation in the absence of this parameter being included in an Observation. If this Resource doesn’t exist, the default value is 0.", serialization_alias="defaultMinPeriod")
    notif_if_disabled: Optional[StrictBool] = Field(default=None, description="If true, the LwM2M Client stores “Notify” operations to the LwM2M Server while the LwM2M Server account is disabled or the LwM2M Client is offline. After the LwM2M Server account is enabled or the LwM2M Client is online, the LwM2M Client reports the stored “Notify” operations to the Server. If false, the LwM2M Client discards all the “Notify” operations or temporarily disables the Observe function while the LwM2M Server is disabled or the LwM2M Client is offline. The default value is true.", serialization_alias="notifIfDisabled")
    binding: Optional[StrictStr] = Field(default=None, description="This Resource defines the transport binding configured for the LwM2M Client. If the LwM2M Client supports the binding specified in this Resource, the LwM2M Client MUST use that transport for the Current Binding Mode.")
    __properties: ClassVar[List[str]] = ["securityMode", "shortServerId", "bootstrapServerIs", "host", "port", "clientHoldOffTime", "serverPublicKey", "serverCertificate", "bootstrapServerAccountTimeout", "lifetime", "defaultMinPeriod", "notifIfDisabled", "binding"]

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
        """Create an instance of NoSecLwM2MBootstrapServerCredential from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "short_server_id",
            "bootstrap_server_is",
            "host",
            "port",
            "client_hold_off_time",
            "server_public_key",
            "server_certificate",
            "bootstrap_server_account_timeout",
            "lifetime",
            "default_min_period",
            "notif_if_disabled",
            "binding",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NoSecLwM2MBootstrapServerCredential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "security_mode": obj.get("securityMode"),
            "short_server_id": obj.get("shortServerId"),
            "bootstrap_server_is": obj.get("bootstrapServerIs"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "client_hold_off_time": obj.get("clientHoldOffTime"),
            "server_public_key": obj.get("serverPublicKey"),
            "server_certificate": obj.get("serverCertificate"),
            "bootstrap_server_account_timeout": obj.get("bootstrapServerAccountTimeout"),
            "lifetime": obj.get("lifetime"),
            "default_min_period": obj.get("defaultMinPeriod"),
            "notif_if_disabled": obj.get("notifIfDisabled"),
            "binding": obj.get("binding")
        })
        return _obj


