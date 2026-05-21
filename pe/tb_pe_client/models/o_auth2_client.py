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
from typing_extensions import Annotated
from tb_pe_client.models.customer_id import CustomerId
from tb_pe_client.models.entity_id import EntityId
from tb_pe_client.models.o_auth2_client_id import OAuth2ClientId
from tb_pe_client.models.o_auth2_mapper_config import OAuth2MapperConfig
from tb_pe_client.models.platform_type import PlatformType
from tb_pe_client.models.tenant_id import TenantId
from typing import Optional, Set
from typing_extensions import Self

class OAuth2Client(BaseModel):
    """
    OAuth2Client
    """ # noqa: E501
    id: Optional[OAuth2ClientId] = None
    created_time: Optional[StrictInt] = Field(default=None, description="Entity creation timestamp in milliseconds since Unix epoch", serialization_alias="createdTime")
    additional_info: Optional[Any] = Field(default=None, description="Additional info of OAuth2 client. Must include: 'providerName' (string, name of the OAuth2 provider).", serialization_alias="additionalInfo")
    tenant_id: Optional[TenantId] = Field(default=None, description="JSON object with Tenant Id", serialization_alias="tenantId")
    customer_id: Optional[CustomerId] = Field(default=None, description="JSON object with Customer Id", serialization_alias="customerId")
    title: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Oauth2 client title")
    mapper_config: OAuth2MapperConfig = Field(description="Config for mapping OAuth2 log in response to platform entities", serialization_alias="mapperConfig")
    client_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="OAuth2 client ID. Cannot be empty", serialization_alias="clientId")
    client_secret: Annotated[str, Field(min_length=1, strict=True)] = Field(description="OAuth2 client secret. Cannot be empty", serialization_alias="clientSecret")
    authorization_uri: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Authorization URI of the OAuth2 provider. Cannot be empty", serialization_alias="authorizationUri")
    access_token_uri: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Access token URI of the OAuth2 provider. Cannot be empty", serialization_alias="accessTokenUri")
    scope: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="OAuth scopes that will be requested from OAuth2 platform. Cannot be empty")
    user_info_uri: Optional[StrictStr] = Field(default=None, description="User info URI of the OAuth2 provider", serialization_alias="userInfoUri")
    user_name_attribute_name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of the username attribute in OAuth2 provider response. Cannot be empty", serialization_alias="userNameAttributeName")
    jwk_set_uri: Optional[StrictStr] = Field(default=None, description="JSON Web Key URI of the OAuth2 provider", serialization_alias="jwkSetUri")
    client_authentication_method: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Client authentication method to use: 'BASIC' or 'POST'. Cannot be empty", serialization_alias="clientAuthenticationMethod")
    login_button_label: Annotated[str, Field(min_length=1, strict=True)] = Field(description="OAuth2 provider label. Cannot be empty", serialization_alias="loginButtonLabel")
    login_button_icon: Optional[StrictStr] = Field(default=None, description="Log in button icon for OAuth2 provider", serialization_alias="loginButtonIcon")
    platforms: Optional[List[PlatformType]] = Field(default=None, description="List of platforms for which usage of the OAuth2 client is allowed (empty for all allowed)")
    name: Optional[StrictStr] = None
    owner_id: Optional[EntityId] = Field(default=None, serialization_alias="ownerId")
    __properties: ClassVar[List[str]] = ["id", "createdTime", "additionalInfo", "tenantId", "customerId", "title", "mapperConfig", "clientId", "clientSecret", "authorizationUri", "accessTokenUri", "scope", "userInfoUri", "userNameAttributeName", "jwkSetUri", "clientAuthenticationMethod", "loginButtonLabel", "loginButtonIcon", "platforms", "name", "ownerId"]

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
        """Create an instance of OAuth2Client from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_time",
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
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customerId'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mapper_config
        if self.mapper_config:
            _dict['mapperConfig'] = self.mapper_config.to_dict()
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
        """Create an instance of OAuth2Client from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": OAuth2ClientId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_time": obj.get("createdTime"),
            "additional_info": obj.get("additionalInfo"),
            "tenant_id": TenantId.from_dict(obj["tenantId"]) if obj.get("tenantId") is not None else None,
            "customer_id": CustomerId.from_dict(obj["customerId"]) if obj.get("customerId") is not None else None,
            "title": obj.get("title"),
            "mapper_config": OAuth2MapperConfig.from_dict(obj["mapperConfig"]) if obj.get("mapperConfig") is not None else None,
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret"),
            "authorization_uri": obj.get("authorizationUri"),
            "access_token_uri": obj.get("accessTokenUri"),
            "scope": obj.get("scope"),
            "user_info_uri": obj.get("userInfoUri"),
            "user_name_attribute_name": obj.get("userNameAttributeName"),
            "jwk_set_uri": obj.get("jwkSetUri"),
            "client_authentication_method": obj.get("clientAuthenticationMethod"),
            "login_button_label": obj.get("loginButtonLabel"),
            "login_button_icon": obj.get("loginButtonIcon"),
            "platforms": obj.get("platforms"),
            "name": obj.get("name"),
            "owner_id": EntityId.from_dict(obj["ownerId"]) if obj.get("ownerId") is not None else None
        })
        return _obj


