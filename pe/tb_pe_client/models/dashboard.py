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
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.dashboard_id import DashboardId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.resource_export_data import ResourceExportData
from tb_pe_client.models.short_customer_info import ShortCustomerInfo
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class Dashboard(BaseModel):
    """
    Dashboard
    """ # noqa: E501
    id: Optional[DashboardId] = Field(default=None, description="JSON object with the dashboard Id. Specify existing dashboard Id to update the dashboard. Referencing non-existing dashboard id will cause error. Omit this field to create new dashboard.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the dashboard creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Tenant Id of the dashboard can't be changed.", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id. ", serialization_alias="customerId")
    owner_id: Optional[EntityId] = Field(default=None, description="JSON object with Customer or Tenant Id", serialization_alias="ownerId")
    title: Optional[StrictStr] = Field(default=None, description="Title of the dashboard.")
    name: Optional[StrictStr] = Field(default=None, description="Same as title of the dashboard. Read-only field. Update the 'title' to change the 'name' of the dashboard.")
    image: Optional[StrictStr] = Field(default=None, description="Thumbnail picture for rendering of the dashboards in a grid view on mobile devices.")
    assigned_customers: Optional[List[ShortCustomerInfo]] = Field(default=None, description="List of assigned customers with their info.", serialization_alias="assignedCustomers")
    mobile_hide: Optional[StrictBool] = Field(default=None, description="Hide dashboard from mobile devices. Useful if the dashboard is not designed for small screens.", serialization_alias="mobileHide")
    mobile_order: Optional[StrictInt] = Field(default=None, description="Order on mobile devices. Useful to adjust sorting of the dashboards for mobile applications", serialization_alias="mobileOrder")
    configuration: Optional[Any] = Field(default=None, description="JSON object with main configuration of the dashboard: layouts, widgets, aliases, etc. The JSON structure of the dashboard configuration is quite complex. The easiest way to learn it is to export existing dashboard to JSON.")
    resources: Optional[List[ResourceExportData]] = None
    version: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "ownerId", "title", "name", "image", "assignedCustomers", "mobileHide", "mobileOrder", "configuration", "resources", "version"]

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
        """Create an instance of Dashboard from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "owner_id",
            "name",
            "image",
            "mobile_hide",
            "mobile_order",
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
        # override the default output from pydantic by calling `to_dict()` of owner_id
        if self.owner_id:
            _dict['ownerId'] = self.owner_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assigned_customers (list)
        _items = []
        if self.assigned_customers:
            for _item_assigned_customers in self.assigned_customers:
                if _item_assigned_customers:
                    _items.append(_item_assigned_customers.to_dict())
            _dict['assignedCustomers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
        # set to None if configuration (nullable) is None
        # and model_fields_set contains the field
        if self.configuration is None and "configuration" in self.model_fields_set:
            _dict['configuration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dashboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": DashboardId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None,
            "title": obj.get("title"),
            "name": obj.get("name"),
            "image": obj.get("image"),
            "assigned_customers": [ShortCustomerInfo.from_dict(_item) for _item in obj["assignedCustomers"]] if obj.get("assignedCustomers") is not None else None,
            "mobile_hide": obj.get("mobileHide"),
            "mobile_order": obj.get("mobileOrder"),
            "configuration": obj.get("configuration"),
            "resources": [ResourceExportData.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None,
            "version": obj.get("version")
        })
        return _obj


