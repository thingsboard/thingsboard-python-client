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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.captcha_params import CaptchaParams
from typing import Optional, Set
from typing_extensions import Self

class EnterpriseCaptchaParams(CaptchaParams):
    """
    EnterpriseCaptchaParams
    """ # noqa: E501
    version: StrictStr = "enterprise"  # post_process: discriminator default
    project_id: Optional[StrictStr] = Field(default=None, description="Your Google Cloud project ID", serialization_alias="projectId")
    service_account_credentials: Optional[StrictStr] = Field(default=None, description="Service account credentials", serialization_alias="serviceAccountCredentials")
    service_account_credentials_file_name: Optional[StrictStr] = Field(default=None, description="Service account credentials file name", serialization_alias="serviceAccountCredentialsFileName")
    android_key: Optional[StrictStr] = Field(default=None, description="The reCAPTCHA key associated with android app.", serialization_alias="androidKey")
    ios_key: Optional[StrictStr] = Field(default=None, description="The reCAPTCHA key associated with iOS app.", serialization_alias="iosKey")
    log_action_name: Optional[StrictStr] = Field(default=None, description="Optional action name used for logging", serialization_alias="logActionName")
    __properties: ClassVar[List[str]] = ["version", "projectId", "serviceAccountCredentials", "serviceAccountCredentialsFileName", "androidKey", "iosKey", "logActionName"]

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
        """Create an instance of EnterpriseCaptchaParams from a JSON string"""
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
        """Create an instance of EnterpriseCaptchaParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "project_id": obj.get("projectId"),
            "service_account_credentials": obj.get("serviceAccountCredentials"),
            "service_account_credentials_file_name": obj.get("serviceAccountCredentialsFileName"),
            "android_key": obj.get("androidKey"),
            "ios_key": obj.get("iosKey"),
            "log_action_name": obj.get("logActionName")
        })
        return _obj


