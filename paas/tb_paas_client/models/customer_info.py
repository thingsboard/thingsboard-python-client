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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.custom_menu_id import CustomMenuId
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_info import EntityInfo
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class CustomerInfo(BaseModel):
    """
    CustomerInfo
    """ # noqa: E501
    id: Optional[CustomerId] = Field(default=None, description="JSON object with the customer Id. Specify this field to update the customer. Referencing non-existing customer Id will cause error. Omit this field to create new customer.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the customer creation, in milliseconds", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the customer. May include: 'description' (string), 'homeDashboardId' (string, UUID of the home dashboard), 'homeDashboardHideToolbar' (boolean, whether to hide the dashboard toolbar), 'isPublic' (boolean, whether this is a public customer).", serialization_alias="additionalInfo")
    country: Optional[StrictStr] = Field(default=None, description="Country")
    state: Optional[StrictStr] = Field(default=None, description="State")
    city: Optional[StrictStr] = Field(default=None, description="City")
    address: Optional[StrictStr] = Field(default=None, description="Address Line 1")
    address2: Optional[StrictStr] = Field(default=None, description="Address Line 2")
    zip: Optional[StrictStr] = Field(default=None, description="Zip code")
    phone: Optional[StrictStr] = Field(default=None, description="Phone number")
    email: Optional[StrictStr] = Field(default=None, description="Email")
    title: StrictStr = Field(description="Title of the customer")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    parent_customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with parent Customer Id", serialization_alias="parentCustomerId")
    version: Optional[StrictInt] = None
    custom_menu_id: Optional[CustomMenuId] = Field(default=None, serialization_alias="customMenuId")
    owner_name: Optional[StrictStr] = Field(default=None, description="Owner name", serialization_alias="ownerName")
    groups: Optional[List[EntityInfo]] = Field(default=None, description="Groups")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with parent Customer Id", serialization_alias="customerId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the customer. Read-only, duplicated from title for backward compatibility")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "country", "state", "city", "address", "address2", "zip", "phone", "email", "title", "tenantId", "parentCustomerId", "version", "customMenuId", "ownerName", "groups", "customerId", "name", "ownerId"]

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
        """Create an instance of CustomerInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "owner_name",
            "customer_id",
            "name",
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
        # override the default output from pydantic by calling `to_dict()` of parent_customer_id
        if self.parent_customer_id:
            _dict['parentCustomerId'] = self.parent_customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_menu_id
        if self.custom_menu_id:
            _dict['customMenuId'] = self.custom_menu_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": CustomerId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "city": obj.get("city"),
            "address": obj.get("address"),
            "address2": obj.get("address2"),
            "zip": obj.get("zip"),
            "phone": obj.get("phone"),
            "email": obj.get("email"),
            "title": obj.get("title"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "parent_customer_id": CustomerId.from_dict(obj["parentCustomerId"]) if obj.get("parentCustomerId") is not None else None,
            "version": obj.get("version"),
            "custom_menu_id": CustomMenuId.from_dict(obj["customMenuId"]) if obj.get("customMenuId") is not None else None,
            "owner_name": obj.get("ownerName"),
            "groups": [EntityInfo.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


