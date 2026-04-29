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
from typing import Optional, Set
from typing_extensions import Self

class UsageInfo(BaseModel):
    """
    UsageInfo
    """ # noqa: E501
    devices: Optional[StrictInt] = None
    max_devices: Optional[StrictInt] = Field(default=None, serialization_alias="maxDevices")
    assets: Optional[StrictInt] = None
    max_assets: Optional[StrictInt] = Field(default=None, serialization_alias="maxAssets")
    customers: Optional[StrictInt] = None
    max_customers: Optional[StrictInt] = Field(default=None, serialization_alias="maxCustomers")
    users: Optional[StrictInt] = None
    max_users: Optional[StrictInt] = Field(default=None, serialization_alias="maxUsers")
    dashboards: Optional[StrictInt] = None
    max_dashboards: Optional[StrictInt] = Field(default=None, serialization_alias="maxDashboards")
    edges: Optional[StrictInt] = None
    max_edges: Optional[StrictInt] = Field(default=None, serialization_alias="maxEdges")
    transport_messages: Optional[StrictInt] = Field(default=None, serialization_alias="transportMessages")
    max_transport_messages: Optional[StrictInt] = Field(default=None, serialization_alias="maxTransportMessages")
    js_executions: Optional[StrictInt] = Field(default=None, serialization_alias="jsExecutions")
    tbel_executions: Optional[StrictInt] = Field(default=None, serialization_alias="tbelExecutions")
    max_js_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxJsExecutions")
    max_tbel_executions: Optional[StrictInt] = Field(default=None, serialization_alias="maxTbelExecutions")
    emails: Optional[StrictInt] = None
    max_emails: Optional[StrictInt] = Field(default=None, serialization_alias="maxEmails")
    sms: Optional[StrictInt] = None
    max_sms: Optional[StrictInt] = Field(default=None, serialization_alias="maxSms")
    sms_enabled: Optional[StrictBool] = Field(default=None, serialization_alias="smsEnabled")
    alarms: Optional[StrictInt] = None
    max_alarms: Optional[StrictInt] = Field(default=None, serialization_alias="maxAlarms")
    reports: Optional[StrictInt] = None
    max_reports: Optional[StrictInt] = Field(default=None, serialization_alias="maxReports")
    ai_credits: Optional[StrictInt] = Field(default=None, serialization_alias="aiCredits")
    max_ai_credits: Optional[StrictInt] = Field(default=None, serialization_alias="maxAiCredits")
    __properties: ClassVar[List[str]] = ["devices", "maxDevices", "assets", "maxAssets", "customers", "maxCustomers", "users", "maxUsers", "dashboards", "maxDashboards", "edges", "maxEdges", "transportMessages", "maxTransportMessages", "jsExecutions", "tbelExecutions", "maxJsExecutions", "maxTbelExecutions", "emails", "maxEmails", "sms", "maxSms", "smsEnabled", "alarms", "maxAlarms", "reports", "maxReports", "aiCredits", "maxAiCredits"]

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
        """Create an instance of UsageInfo from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "devices": obj.get("devices"),
            "max_devices": obj.get("maxDevices"),
            "assets": obj.get("assets"),
            "max_assets": obj.get("maxAssets"),
            "customers": obj.get("customers"),
            "max_customers": obj.get("maxCustomers"),
            "users": obj.get("users"),
            "max_users": obj.get("maxUsers"),
            "dashboards": obj.get("dashboards"),
            "max_dashboards": obj.get("maxDashboards"),
            "edges": obj.get("edges"),
            "max_edges": obj.get("maxEdges"),
            "transport_messages": obj.get("transportMessages"),
            "max_transport_messages": obj.get("maxTransportMessages"),
            "js_executions": obj.get("jsExecutions"),
            "tbel_executions": obj.get("tbelExecutions"),
            "max_js_executions": obj.get("maxJsExecutions"),
            "max_tbel_executions": obj.get("maxTbelExecutions"),
            "emails": obj.get("emails"),
            "max_emails": obj.get("maxEmails"),
            "sms": obj.get("sms"),
            "max_sms": obj.get("maxSms"),
            "sms_enabled": obj.get("smsEnabled"),
            "alarms": obj.get("alarms"),
            "max_alarms": obj.get("maxAlarms"),
            "reports": obj.get("reports"),
            "max_reports": obj.get("maxReports"),
            "ai_credits": obj.get("aiCredits"),
            "max_ai_credits": obj.get("maxAiCredits")
        })
        return _obj


