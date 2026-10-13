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
from tb_paas_client.models.customer_id import CustomerId
from tb_paas_client.models.edge_id import EdgeId
from tb_paas_client.models.edge_license_type import EdgeLicenseType
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.rule_chain_id import RuleChainId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class Edge(BaseModel):
    """
    A JSON value representing the edge.
    """ # noqa: E501
    id: Optional[EdgeId] = Field(default=None, description="JSON object with the Edge Id. Specify this field to update the Edge. Referencing non-existing Edge Id will cause error. Omit this field to create new Edge.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the edge creation, in milliseconds", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional parameters of the edge. May include: 'description' (string).", serialization_alias="additionalInfo")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id. Always set to the tenant of the current user on save; cannot be changed after creation.", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id.", serialization_alias="customerId")
    root_rule_chain_id: Optional[RuleChainId] = Field(default=None, description="JSON object with Root Rule Chain Id. Use 'setEdgeRootRuleChain' to change the Root Rule Chain Id.", serialization_alias="rootRuleChainId")
    name: StrictStr = Field(description="Unique Edge Name in scope of Tenant")
    type: StrictStr = Field(description="Edge type")
    label: Optional[StrictStr] = Field(default=None, description="Label that may be used in widgets")
    routing_key: StrictStr = Field(description="Edge routing key ('username') to authorize on cloud", serialization_alias="routingKey")
    secret: StrictStr = Field(description="Edge secret ('password') to authorize on cloud")
    edge_license_key: StrictStr = Field(description="Edge license key obtained from license portal", serialization_alias="edgeLicenseKey")
    cloud_endpoint: StrictStr = Field(description="Edge uses this cloud URL to activate and periodically check it's license", serialization_alias="cloudEndpoint")
    edge_license_type: Optional[EdgeLicenseType] = Field(default=None, serialization_alias="edgeLicenseType")
    version: Optional[StrictInt] = None
    owner_id: Optional[EntityId] = Field(default=None, serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "tenantId", "customerId", "rootRuleChainId", "name", "type", "label", "routingKey", "secret", "edgeLicenseKey", "cloudEndpoint", "edgeLicenseType", "version", "ownerId"]

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
        """Create an instance of Edge from a JSON string"""
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
            "root_rule_chain_id",
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
        # override the default output from pydantic by calling `to_dict()` of root_rule_chain_id
        if self.root_rule_chain_id:
            _dict['rootRuleChainId'] = self.root_rule_chain_id.to_dict()
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
        """Create an instance of Edge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": EdgeId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "root_rule_chain_id": RuleChainId.from_dict(obj["rootRuleChainId"]) if obj.get("rootRuleChainId") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "label": obj.get("label"),
            "routing_key": obj.get("routingKey"),
            "secret": obj.get("secret"),
            "edge_license_key": obj.get("edgeLicenseKey"),
            "cloud_endpoint": obj.get("cloudEndpoint"),
            "edge_license_type": obj.get("edgeLicenseType"),
            "version": obj.get("version"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


