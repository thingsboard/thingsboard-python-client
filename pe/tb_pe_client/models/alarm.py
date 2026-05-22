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
from tb_pe_client.models.alarm_id import AlarmId
from tb_pe_client.models.alarm_severity import AlarmSeverity
from tb_pe_client.models.alarm_status import AlarmStatus
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.tenant_id import TenantId
from tb_pe_client.models.user_id import UserId
from typing import Optional, Set
from typing_extensions import Self

class Alarm(BaseModel):
    """
    Alarm
    """ # noqa: E501
    id: Optional[AlarmId] = Field(default=None, description="JSON object with the alarm Id. Specify this field to update the alarm. Referencing non-existing alarm Id will cause error. Omit this field to create new alarm.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id. Derived from the originator entity owner and cannot be set independently; any value supplied in the request body must match the originator's customer or the request is rejected.", serialization_alias="customerId")
    type: StrictStr = Field(description="representing type of the Alarm")
    originator: EntityId = Field(description="JSON object with alarm originator id")
    severity: AlarmSeverity = Field(description="Alarm severity")
    acknowledged: StrictBool = Field(description="Acknowledged")
    cleared: StrictBool = Field(description="Cleared")
    assignee_id: Optional[UserId] = Field(default=None, description="Alarm assignee user id", serialization_alias="assigneeId")
    start_ts: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm start time, in milliseconds", serialization_alias="startTs")
    end_ts: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm end time(last time update), in milliseconds", serialization_alias="endTs")
    ack_ts: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm acknowledgement, in milliseconds", serialization_alias="ackTs")
    clear_ts: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm clearing, in milliseconds", serialization_alias="clearTs")
    assign_ts: Optional[StrictInt] = Field(default=None, description="Timestamp of the alarm assignment, in milliseconds", serialization_alias="assignTs")
    details: Optional[Any] = Field(default=None, description="JSON object with alarm details")
    propagate: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to parent entities of alarm originator")
    propagate_to_owner: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator", serialization_alias="propagateToOwner")
    propagate_to_owner_hierarchy: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) and all parent owners in the customer hierarchy", serialization_alias="propagateToOwnerHierarchy")
    propagate_to_tenant: Optional[StrictBool] = Field(default=None, description="Propagation flag to specify if alarm should be propagated to the tenant entity", serialization_alias="propagateToTenant")
    propagate_relation_types: Optional[List[StrictStr]] = Field(default=None, description="JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.", serialization_alias="propagateRelationTypes")
    name: StrictStr = Field(description="representing type of the Alarm")
    status: AlarmStatus = Field(description="status of the Alarm")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "customerId", "type", "originator", "severity", "acknowledged", "cleared", "assigneeId", "startTs", "endTs", "ackTs", "clearTs", "assignTs", "details", "propagate", "propagateToOwner", "propagateToOwnerHierarchy", "propagateToTenant", "propagateRelationTypes", "name", "status"]

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
        """Create an instance of Alarm from a JSON string"""
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
            "tenant_id",
            "customer_id",
            "name",
            "status",
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
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assignee_id
        if self.assignee_id:
            _dict['assigneeId'] = self.assignee_id.to_dict()
        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Alarm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AlarmId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "type": obj.get("type"),
            "originator": EntityId.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "severity": obj.get("severity"),
            "acknowledged": obj.get("acknowledged"),
            "cleared": obj.get("cleared"),
            "assignee_id": UserId.from_dict(obj["assigneeId"]) if obj.get("assigneeId") is not None else None,
            "start_ts": obj.get("startTs"),
            "end_ts": obj.get("endTs"),
            "ack_ts": obj.get("ackTs"),
            "clear_ts": obj.get("clearTs"),
            "assign_ts": obj.get("assignTs"),
            "details": obj.get("details"),
            "propagate": obj.get("propagate"),
            "propagate_to_owner": obj.get("propagateToOwner"),
            "propagate_to_owner_hierarchy": obj.get("propagateToOwnerHierarchy"),
            "propagate_to_tenant": obj.get("propagateToTenant"),
            "propagate_relation_types": obj.get("propagateRelationTypes"),
            "name": obj.get("name"),
            "status": obj.get("status")
        })
        return _obj


