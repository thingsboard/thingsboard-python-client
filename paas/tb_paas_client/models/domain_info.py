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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.domain_id import DomainId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.o_auth2_client_info import OAuth2ClientInfo
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class DomainInfo(BaseModel):
    """
    DomainInfo
    """ # noqa: E501
    id: Optional[DomainId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id", serialization_alias="customerId")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Domain name. Cannot be empty")
    oauth2_enabled: Optional[StrictBool] = Field(default=None, description="Whether OAuth2 settings are enabled or not", serialization_alias="oauth2Enabled")
    propagate_to_edge: Optional[StrictBool] = Field(default=None, description="Whether OAuth2 settings are enabled on Edge or not", serialization_alias="propagateToEdge")
    oauth2_client_infos: Optional[List[OAuth2ClientInfo]] = Field(default=None, description="List of available oauth2 clients", serialization_alias="oauth2ClientInfos")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "name", "oauth2Enabled", "propagateToEdge", "oauth2ClientInfos", "ownerId"]

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
        """Create an instance of DomainInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in oauth2_client_infos (list)
        _items = []
        if self.oauth2_client_infos:
            for _item_oauth2_client_infos in self.oauth2_client_infos:
                if _item_oauth2_client_infos:
                    _items.append(_item_oauth2_client_infos.to_dict())
            _dict['oauth2ClientInfos'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DomainId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "oauth2_enabled": obj.get("oauth2Enabled"),
            "propagate_to_edge": obj.get("propagateToEdge"),
            "oauth2_client_infos": [OAuth2ClientInfo.from_dict(_item) for _item in obj["oauth2ClientInfos"]] if obj.get("oauth2ClientInfos") is not None else None,
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


