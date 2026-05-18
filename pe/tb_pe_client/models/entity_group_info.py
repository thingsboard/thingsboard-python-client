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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from tb_pe_client.models.entity_group_id import EntityGroupId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.entity_type import EntityType
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class EntityGroupInfo(BaseModel):
    """
    EntityGroupInfo
    """ # noqa: E501
    id: Optional[EntityGroupId] = Field(default=None, description="JSON object with the EntityGroupId Id. Specify this field to update the Entity Group. Referencing non-existing Entity Group Id will cause error. Omit this field to create new Entity Group.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the entity group creation, in milliseconds", serialization_alias="createdTime")
    type: EntityType
    name: StrictStr = Field(description="Name of the entity group")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with the owner of the group - Tenant or Customer Id. When omitted or null on creation, defaults to the current user's owner (Tenant for tenant admins, Customer for customer users).", serialization_alias="ownerId")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the entity group. May include: 'description' (string), 'isPublic' (boolean, whether this group is shared publicly), 'publicCustomerId' (string, UUID of the public customer associated with this group).", serialization_alias="additionalInfo")
    configuration: Optional[Any] = Field(default=None, description="JSON with the configuration for UI components: list of columns, settings, actions, etc ")
    version: Optional[StrictInt] = None
    owner_ids: Optional[List[EntityId]] = Field(default=None, serialization_alias="ownerIds")
    edge_group_all: Optional[StrictBool] = Field(default=None, description="Indicates special edge group 'All' that contains all entities and can't be deleted.", serialization_alias="edgeGroupAll")
    group_all: Optional[StrictBool] = Field(default=None, description="Indicates special group 'All' that contains all entities and can't be deleted.", serialization_alias="groupAll")
    tenant_id: Optional[TenantId] = Field(default=None, serialization_alias="tenantId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "type", "name", "ownerId", "additionalInfo", "configuration", "version", "ownerIds", "edgeGroupAll", "groupAll", "tenantId"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TENANT', 'CUSTOMER', 'USER', 'DASHBOARD', 'ASSET', 'DEVICE', 'ALARM', 'ENTITY_GROUP', 'CONVERTER', 'INTEGRATION', 'RULE_CHAIN', 'RULE_NODE', 'SCHEDULER_EVENT', 'BLOB_ENTITY', 'REPORT_TEMPLATE', 'REPORT', 'ENTITY_VIEW', 'WIDGETS_BUNDLE', 'WIDGET_TYPE', 'ROLE', 'GROUP_PERMISSION', 'TENANT_PROFILE', 'DEVICE_PROFILE', 'ASSET_PROFILE', 'API_USAGE_STATE', 'TB_RESOURCE', 'OTA_PACKAGE', 'EDGE', 'RPC', 'QUEUE', 'NOTIFICATION_TARGET', 'NOTIFICATION_TEMPLATE', 'NOTIFICATION_REQUEST', 'NOTIFICATION', 'NOTIFICATION_RULE', 'QUEUE_STATS', 'OAUTH2_CLIENT', 'DOMAIN', 'MOBILE_APP', 'MOBILE_APP_BUNDLE', 'CALCULATED_FIELD', 'JOB', 'SECRET', 'ADMIN_SETTINGS', 'AI_MODEL', 'API_KEY']):
            raise ValueError("must be one of enum values ('TENANT', 'CUSTOMER', 'USER', 'DASHBOARD', 'ASSET', 'DEVICE', 'ALARM', 'ENTITY_GROUP', 'CONVERTER', 'INTEGRATION', 'RULE_CHAIN', 'RULE_NODE', 'SCHEDULER_EVENT', 'BLOB_ENTITY', 'REPORT_TEMPLATE', 'REPORT', 'ENTITY_VIEW', 'WIDGETS_BUNDLE', 'WIDGET_TYPE', 'ROLE', 'GROUP_PERMISSION', 'TENANT_PROFILE', 'DEVICE_PROFILE', 'ASSET_PROFILE', 'API_USAGE_STATE', 'TB_RESOURCE', 'OTA_PACKAGE', 'EDGE', 'RPC', 'QUEUE', 'NOTIFICATION_TARGET', 'NOTIFICATION_TEMPLATE', 'NOTIFICATION_REQUEST', 'NOTIFICATION', 'NOTIFICATION_RULE', 'QUEUE_STATS', 'OAUTH2_CLIENT', 'DOMAIN', 'MOBILE_APP', 'MOBILE_APP_BUNDLE', 'CALCULATED_FIELD', 'JOB', 'SECRET', 'ADMIN_SETTINGS', 'AI_MODEL', 'API_KEY')")
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
        """Create an instance of EntityGroupInfo from a JSON string"""
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
            "edge_group_all",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in owner_ids (list)
        _items = []
        if self.owner_ids:
            for _item_owner_ids in self.owner_ids:
                if _item_owner_ids:
                    _items.append(_item_owner_ids.to_dict())
            _dict['ownerIds'] = _items
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntityGroupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": EntityGroupId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "additional_info": obj.get("additionalInfo"),
            "configuration": obj.get("configuration"),
            "version": obj.get("version"),
            "owner_ids": [EntityId.from_dict(_item) for _item in obj["ownerIds"]] if obj.get("ownerIds") is not None else None,
            "edge_group_all": obj.get("edgeGroupAll"),
            "group_all": obj.get("groupAll"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None
        })
        return _obj


