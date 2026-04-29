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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.asset_profile_id import AssetProfileId
from tb_paas_client.models.dashboard_id import DashboardId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AssetProfileInfo(BaseModel):
    """
    AssetProfileInfo
    """ # noqa: E501
    id: Optional[AssetProfileId] = Field(default=None, description="JSON object with the Asset Profile Id.")
    name: Optional[StrictStr] = Field(default=None, description="Entity Name")
    image: Optional[StrictStr] = Field(default=None, description="Either URL or Base64 data of the icon. Used in the mobile application to visualize set of asset profiles in the grid view. ")
    default_dashboard_id: Optional[DashboardId] = Field(default=None, description="Reference to the dashboard. Used in the mobile application to open the default dashboard when user navigates to asset details.", serialization_alias="defaultDashboardId")
    tenant_id: Optional[TenantId] = Field(default=None, description="Tenant id.", serialization_alias="tenantId")
    __properties: ClassVar[List[str]] = ["id", "name", "image", "defaultDashboardId", "tenantId"]

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
        """Create an instance of AssetProfileInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_dashboard_id
        if self.default_dashboard_id:
            _dict['defaultDashboardId'] = self.default_dashboard_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_id
        if self.tenant_id:
            _dict['tenantId'] = self.tenant_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetProfileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AssetProfileId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "name": obj.get("name"),
            "image": obj.get("image"),
            "default_dashboard_id": DashboardId.from_dict(obj["defaultDashboardId"]) if obj.get("defaultDashboardId") is not None else None,
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None
        })
        return _obj


