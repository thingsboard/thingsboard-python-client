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

from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from tb_paas_client.models.captcha_params import CaptchaParams
from tb_paas_client.models.custom_menu_id import CustomMenuId
from tb_paas_client.models.default_dashboard_params import DefaultDashboardParams
from tb_paas_client.models.domain_id import DomainId
from tb_paas_client.models.entity_group_id import EntityGroupId
from tb_paas_client.models.group_permission import GroupPermission
from tb_paas_client.models.home_dashboard_params import HomeDashboardParams
from tb_paas_client.models.notification_target_id import NotificationTargetId
from tb_paas_client.models.self_registration_params import SelfRegistrationParams
from tb_paas_client.models.self_registration_type import SelfRegistrationType
from tb_paas_client.models.sign_up_field import SignUpField
from typing import Optional, Set
from typing_extensions import Self

class WebSelfRegistrationParams(SelfRegistrationParams):
    """
    WebSelfRegistrationParams
    """ # noqa: E501
    type: SelfRegistrationType = SelfRegistrationType.WEB  # post_process: discriminator default
    domain_id: DomainId = Field(description="Domain name for self registration URL. Typically this matches the domain name from the Login White Labeling page.", serialization_alias="domainId")
    privacy_policy: Optional[StrictStr] = Field(default=None, description="Privacy policy text. Supports HTML.", serialization_alias="privacyPolicy")
    terms_of_use: Optional[StrictStr] = Field(default=None, description="Terms of User text. Supports HTML.", serialization_alias="termsOfUse")
    __properties: ClassVar[List[str]] = ["type", "enabled", "title", "captcha", "permissions", "notificationRecipient", "signUpFields", "customerTitlePrefix", "showPrivacyPolicy", "showTermsOfUse", "defaultDashboard", "homeDashboard", "customerGroupId", "customMenuId", "domainId", "privacyPolicy", "termsOfUse"]

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
        """Create an instance of WebSelfRegistrationParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of captcha
        if self.captcha:
            _dict['captcha'] = self.captcha.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of notification_recipient
        if self.notification_recipient:
            _dict['notificationRecipient'] = self.notification_recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sign_up_fields (list)
        _items = []
        if self.sign_up_fields:
            for _item_sign_up_fields in self.sign_up_fields:
                if _item_sign_up_fields:
                    _items.append(_item_sign_up_fields.to_dict())
            _dict['signUpFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_dashboard
        if self.default_dashboard:
            _dict['defaultDashboard'] = self.default_dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of home_dashboard
        if self.home_dashboard:
            _dict['homeDashboard'] = self.home_dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_group_id
        if self.customer_group_id:
            _dict['customerGroupId'] = self.customer_group_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_menu_id
        if self.custom_menu_id:
            _dict['customMenuId'] = self.custom_menu_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_id
        if self.domain_id:
            _dict['domainId'] = self.domain_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebSelfRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "enabled": obj.get("enabled"),
            "title": obj.get("title"),
            "captcha": CaptchaParams.from_dict(obj["captcha"]) if obj.get("captcha") is not None else None,
            "permissions": [GroupPermission.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "notification_recipient": NotificationTargetId.from_dict(obj["notificationRecipient"]) if obj.get("notificationRecipient") is not None else None,
            "sign_up_fields": [SignUpField.from_dict(_item) for _item in obj["signUpFields"]] if obj.get("signUpFields") is not None else None,
            "customer_title_prefix": obj.get("customerTitlePrefix"),
            "show_privacy_policy": obj.get("showPrivacyPolicy"),
            "show_terms_of_use": obj.get("showTermsOfUse"),
            "default_dashboard": DefaultDashboardParams.from_dict(obj["defaultDashboard"]) if obj.get("defaultDashboard") is not None else None,
            "home_dashboard": HomeDashboardParams.from_dict(obj["homeDashboard"]) if obj.get("homeDashboard") is not None else None,
            "customer_group_id": EntityGroupId.from_dict(obj["customerGroupId"]) if obj.get("customerGroupId") is not None else None,
            "custom_menu_id": CustomMenuId.from_dict(obj["customMenuId"]) if obj.get("customMenuId") is not None else None,
            "domain_id": DomainId.from_dict(obj["domainId"]) if obj.get("domainId") is not None else None,
            "privacy_policy": obj.get("privacyPolicy"),
            "terms_of_use": obj.get("termsOfUse")
        })
        return _obj


