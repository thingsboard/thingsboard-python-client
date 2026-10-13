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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.notification_template_id import NotificationTemplateId
from tb_paas_client.models.report_template_config import ReportTemplateConfig
from tb_paas_client.models.report_template_id import ReportTemplateId
from typing import Optional, Set
from typing_extensions import Self

class ReportRequest(BaseModel):
    """
    ReportRequest
    """ # noqa: E501
    report_template_id: Optional[ReportTemplateId] = Field(default=None, description="Json object representing the report template id.", serialization_alias="reportTemplateId")
    report_template_config: Optional[ReportTemplateConfig] = Field(default=None, description="Json object representing the report template config.", serialization_alias="reportTemplateConfig")
    timezone: Optional[StrictStr] = Field(default=None, description="Timezone used for report generation.")
    user_id: Optional[StrictStr] = Field(default=None, description="A string value representing the user id.", serialization_alias="userId")
    make_public: Optional[StrictBool] = Field(default=None, description="A boolean value indicating whether the generated report should be made public.", serialization_alias="makePublic")
    originator: Optional[EntityId] = Field(default=None, description="Json object representing the originator id.")
    targets: Optional[List[UUID]] = None
    notification_template_id: Optional[NotificationTemplateId] = Field(default=None, serialization_alias="notificationTemplateId")
    __properties: ClassVar[List[str]] = ["reportTemplateId", "reportTemplateConfig", "timezone", "userId", "makePublic", "originator", "targets", "notificationTemplateId"]

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
        """Create an instance of ReportRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of report_template_id
        if self.report_template_id:
            _dict['reportTemplateId'] = self.report_template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of report_template_config
        if self.report_template_config:
            _dict['reportTemplateConfig'] = self.report_template_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notification_template_id
        if self.notification_template_id:
            _dict['notificationTemplateId'] = self.notification_template_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "report_template_id": ReportTemplateId.from_dict(obj["reportTemplateId"]) if obj.get("reportTemplateId") is not None else None,
            "report_template_config": ReportTemplateConfig.from_dict(obj["reportTemplateConfig"]) if obj.get("reportTemplateConfig") is not None else None,
            "timezone": obj.get("timezone"),
            "user_id": obj.get("userId"),
            "make_public": obj.get("makePublic"),
            "originator": EntityId.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "targets": obj.get("targets"),
            "notification_template_id": NotificationTemplateId.from_dict(obj["notificationTemplateId"]) if obj.get("notificationTemplateId") is not None else None
        })
        return _obj


