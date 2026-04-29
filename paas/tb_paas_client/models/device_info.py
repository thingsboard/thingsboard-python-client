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
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.device_data import DeviceData
from tb_paas_client.models.device_id import DeviceId
from tb_paas_client.models.device_profile_id import DeviceProfileId
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.entity_info import EntityInfo
from tb_paas_client.models.ota_package_id import OtaPackageId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class DeviceInfo(BaseModel):
    """
    DeviceInfo
    """ # noqa: E501
    id: Optional[DeviceId] = Field(default=None, description="JSON object with the Device Id. Specify this field to update the Device. Referencing non-existing Device Id will cause error. Omit this field to create new Device.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the device creation, in milliseconds", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the device. May include: 'gateway' (boolean, whether the device is a gateway), 'description' (string), 'lastConnectedGateway' (string, UUID of the last gateway that connected this device).", serialization_alias="additionalInfo")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Use 'assignDeviceToTenant' to change the Tenant Id.", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id. Use 'assignDeviceToCustomer' to change the Customer Id.", serialization_alias="customerId")
    name: Optional[StrictStr] = Field(default=None, description="Unique Device Name in scope of Tenant")
    type: Optional[StrictStr] = Field(default=None, description="Device Profile Name")
    label: Optional[StrictStr] = Field(default=None, description="Label that may be used in widgets")
    device_profile_id: Optional[DeviceProfileId] = Field(default=None, description="JSON object with Device Profile Id. If not provided, the type will be used to determine the profile. If neither deviceProfileId nor type is specified, the default device profile will be used.", serialization_alias="deviceProfileId")
    device_data: Optional[DeviceData] = Field(default=None, description="JSON object with content specific to type of transport in the device profile.", serialization_alias="deviceData")
    firmware_id: Optional[OtaPackageId] = Field(default=None, description="JSON object with Ota Package Id.", serialization_alias="firmwareId")
    software_id: Optional[OtaPackageId] = Field(default=None, description="JSON object with Ota Package Id.", serialization_alias="softwareId")
    version: Optional[StrictInt] = None
    owner_name: Optional[StrictStr] = Field(default=None, description="Owner name", serialization_alias="ownerName")
    groups: Optional[List[EntityInfo]] = Field(default=None, description="Groups")
    active: Optional[StrictBool] = Field(default=None, description="Device active flag.")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "tenantId", "customerId", "name", "type", "label", "deviceProfileId", "deviceData", "firmwareId", "softwareId", "version", "ownerName", "groups", "active", "ownerId"]

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
        """Create an instance of DeviceInfo from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "customer_id",
            "owner_name",
            "active",
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
        # override the default output from pydantic by calling `to_dict()` of device_profile_id
        if self.device_profile_id:
            _dict['deviceProfileId'] = self.device_profile_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of device_data
        if self.device_data:
            _dict['deviceData'] = self.device_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firmware_id
        if self.firmware_id:
            _dict['firmwareId'] = self.firmware_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of software_id
        if self.software_id:
            _dict['softwareId'] = self.software_id.to_dict()
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
        """Create an instance of DeviceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DeviceId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "device_profile_id": DeviceProfileId.from_dict(obj["deviceProfileId"]) if obj.get("deviceProfileId") is not None else None,
            "device_data": DeviceData.from_dict(obj["deviceData"]) if obj.get("deviceData") is not None else None,
            "firmware_id": OtaPackageId.from_dict(obj["firmwareId"]) if obj.get("firmwareId") is not None else None,
            "software_id": OtaPackageId.from_dict(obj["softwareId"]) if obj.get("softwareId") is not None else None,
            "version": obj.get("version"),
            "owner_name": obj.get("ownerName"),
            "groups": [EntityInfo.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "active": obj.get("active"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


