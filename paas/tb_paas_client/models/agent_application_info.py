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
from tb_paas_client.models.agent_app_profile_id import AgentAppProfileId
from tb_paas_client.models.agent_application_id import AgentApplicationId
from tb_paas_client.models.agent_application_origin import AgentApplicationOrigin
from tb_paas_client.models.agent_application_type import AgentApplicationType
from tb_paas_client.models.agent_id import AgentId
from tb_paas_client.models.docker_compose_config import DockerComposeConfig
from tb_paas_client.models.entity_id import EntityId
from tb_paas_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class AgentApplicationInfo(BaseModel):
    """
    AgentApplicationInfo
    """ # noqa: E501
    id: Optional[AgentApplicationId] = Field(default=None, description="JSON object with the Agent Application Id.")
    created_time: Optional[StrictInt] = Field(default=None, description="Timestamp of the agent application creation, in milliseconds", serialization_alias="createdTime")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id.", serialization_alias="tenantId")
    agent_id: AgentId = Field(description="Agent this application belongs to", serialization_alias="agentId")
    name: Optional[StrictStr] = Field(default=None, description="Application name (not unique across tenant)")
    template_version: StrictStr = Field(description="Template version this application is based on", serialization_alias="templateVersion")
    desired_template_version: Optional[StrictStr] = Field(default=None, serialization_alias="desiredTemplateVersion")
    app_type: AgentApplicationType = Field(description="Application type", serialization_alias="appType")
    config: Optional[DockerComposeConfig] = None
    version: Optional[StrictInt] = None
    project_name: Optional[StrictStr] = Field(default=None, serialization_alias="projectName")
    pending_deletion: Optional[StrictBool] = Field(default=None, serialization_alias="pendingDeletion")
    origin: Optional[AgentApplicationOrigin] = Field(default=None, description="Origin of the application (INSTALLED or DISCOVERED)")
    application_profile_id: Optional[AgentAppProfileId] = Field(default=None, description="Application Profile Id. When set, config is read-only and inherited from the profile.", serialization_alias="applicationProfileId")
    profile_config_version: Optional[StrictInt] = Field(default=None, serialization_alias="profileConfigVersion")
    current_version: Optional[StrictStr] = Field(default=None, description="Current version of the template this application is based on.", serialization_alias="currentVersion")
    next_version: Optional[StrictStr] = Field(default=None, description="Next version available for upgrade.", serialization_alias="nextVersion")
    profile_config_outdated: Optional[StrictBool] = Field(default=None, description="True if the app's config is outdated relative to its profile.", serialization_alias="profileConfigOutdated")
    profile_name: Optional[StrictStr] = Field(default=None, description="Name of the application profile this app is based on.", serialization_alias="profileName")
    profile_template_version: Optional[StrictStr] = Field(default=None, description="Template version of the application profile this app is based on.", serialization_alias="profileTemplateVersion")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the owning agent.", serialization_alias="agentName")
    related_entity_id: Optional[EntityId] = Field(default=None, description="Related entity id (Edge or Gateway device) currently assigned to this application.", serialization_alias="relatedEntityId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "tenantId", "agentId", "name", "templateVersion", "desiredTemplateVersion", "appType", "config", "version", "projectName", "pendingDeletion", "origin", "applicationProfileId", "profileConfigVersion", "currentVersion", "nextVersion", "profileConfigOutdated", "profileName", "profileTemplateVersion", "agentName", "relatedEntityId"]

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
        """Create an instance of AgentApplicationInfo from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_time",
            "tenant_id",
            "current_version",
            "next_version",
            "profile_config_outdated",
            "profile_name",
            "profile_template_version",
            "agent_name",
            "related_entity_id",
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
        # override the default output from pydantic by calling `to_dict()` of agent_id
        if self.agent_id:
            _dict['agentId'] = self.agent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application_profile_id
        if self.application_profile_id:
            _dict['applicationProfileId'] = self.application_profile_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_entity_id
        if self.related_entity_id:
            _dict['relatedEntityId'] = self.related_entity_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentApplicationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": AgentApplicationId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "agent_id": AgentId.from_dict(obj["agentId"]) if obj.get("agentId") is not None else None,
            "name": obj.get("name"),
            "template_version": obj.get("templateVersion"),
            "desired_template_version": obj.get("desiredTemplateVersion"),
            "app_type": obj.get("appType"),
            "config": DockerComposeConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "version": obj.get("version"),
            "project_name": obj.get("projectName"),
            "pending_deletion": obj.get("pendingDeletion"),
            "origin": obj.get("origin"),
            "application_profile_id": AgentAppProfileId.from_dict(obj["applicationProfileId"]) if obj.get("applicationProfileId") is not None else None,
            "profile_config_version": obj.get("profileConfigVersion"),
            "current_version": obj.get("currentVersion"),
            "next_version": obj.get("nextVersion"),
            "profile_config_outdated": obj.get("profileConfigOutdated"),
            "profile_name": obj.get("profileName"),
            "profile_template_version": obj.get("profileTemplateVersion"),
            "agent_name": obj.get("agentName"),
            "related_entity_id": EntityId.from_dict(obj["relatedEntityId"]) if obj.get("relatedEntityId") is not None else None
        })
        return _obj


