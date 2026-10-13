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
from tb_paas_client.models.asset_id import AssetId
from tb_paas_client.models.asset_profile_id import AssetProfileId
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_info import EntityInfo
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AssetInfo(BaseModel):
    """
    AssetInfo
    """ # noqa: E501
    id: Optional[AssetId] = Field(default=None, description="JSON object with the asset Id. Specify this field to update the asset. Referencing non-existing asset Id will cause error. Omit this field to create new asset.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the asset creation, in milliseconds", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the asset. May include: 'description' (string).", serialization_alias="additionalInfo")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id. Optional on create: when omitted, defaults to the owner of the target Entity Group or to the current Customer user. Cannot be changed on update via this endpoint; use the Owner API (changeOwnerToCustomer) to re-assign an existing Asset.", serialization_alias="customerId")
    name: StrictStr = Field(description="Unique Asset Name in scope of Tenant")
    type: Optional[StrictStr] = Field(default=None, description="Asset type")
    label: Optional[StrictStr] = Field(default=None, description="Label that may be used in widgets")
    asset_profile_id: Optional[AssetProfileId] = Field(default=None, description="JSON object with Asset Profile Id.", serialization_alias="assetProfileId")
    version: Optional[StrictInt] = None
    owner_name: Optional[StrictStr] = Field(default=None, description="Owner name", serialization_alias="ownerName")
    groups: Optional[List[EntityInfo]] = Field(default=None, description="Groups")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "tenantId", "customerId", "name", "type", "label", "assetProfileId", "version", "ownerName", "groups", "ownerId"]

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
        """Create an instance of AssetInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "owner_name",
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
        # override the default output from pydantic by calling `to_dict()` of asset_profile_id
        if self.asset_profile_id:
            _dict['assetProfileId'] = self.asset_profile_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
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
        """Create an instance of AssetInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AssetId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "asset_profile_id": AssetProfileId.from_dict(obj["assetProfileId"]) if obj.get("assetProfileId") is not None else None,
            "version": obj.get("version"),
            "owner_name": obj.get("ownerName"),
            "groups": [EntityInfo.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


