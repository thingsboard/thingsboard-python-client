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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_info import EntityInfo
from tb_paas_client.models.report_id import ReportId
from tb_paas_client.models.report_template_id import ReportTemplateId
from tb_paas_client.models.tb_report_format import TbReportFormat
from tb_paas_client.models.tenant_id import TenantId
from tb_paas_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class ReportInfo(BaseModel):
    """
    ReportInfo
    """ # noqa: E501
    id: Optional[ReportId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    tenant_id: TenantId = Field(serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, serialization_alias="customerId")
    template_id: ReportTemplateId = Field(serialization_alias="templateId")
    format: TbReportFormat
    name: Annotated[str, Field(min_length=1, strict=True)]
    user_id: UserId = Field(serialization_alias="userId")
    public_key: Optional[StrictStr] = Field(default=None, serialization_alias="publicKey")
    template_info: Optional[EntityInfo] = Field(default=None, serialization_alias="templateInfo")
    customer_title: Optional[StrictStr] = Field(default=None, serialization_alias="customerTitle")
    user_name: Optional[StrictStr] = Field(default=None, serialization_alias="userName")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    public: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "templateId", "format", "name", "userId", "publicKey", "templateInfo", "customerTitle", "userName", "ownerId", "public"]

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
        """Create an instance of ReportInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "owner_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template_id
        if self.template_id:
            _dict['templateId'] = self.template_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_id
        if self.user_id:
            _dict['userId'] = self.user_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of template_info
        if self.template_info:
            _dict['templateInfo'] = self.template_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ReportId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "template_id": ReportTemplateId.from_dict(obj["templateId"]) if obj.get("templateId") is not None else None,
            "format": obj.get("format"),
            "name": obj.get("name"),
            "user_id": UserId.from_dict(obj["userId"]) if obj.get("userId") is not None else None,
            "public_key": obj.get("publicKey"),
            "template_info": EntityInfo.from_dict(obj["templateInfo"]) if obj.get("templateInfo") is not None else None,
            "customer_title": obj.get("customerTitle"),
            "user_name": obj.get("userName"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "public": obj.get("public")
        })
        return _obj


