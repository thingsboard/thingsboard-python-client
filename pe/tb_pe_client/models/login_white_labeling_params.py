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
from tb_pe_client.models.domain_id import DomainId
from tb_pe_client.models.favicon import Favicon
from tb_pe_client.models.palette_settings import PaletteSettings
from typing import Optional, Set
from typing_extensions import Self

class LoginWhiteLabelingParams(BaseModel):
    """
    A JSON value representing the login white labeling configuration
    """ # noqa: E501
    logo_image_url: Optional[StrictStr] = Field(default=None, description="Logo image URL", serialization_alias="logoImageUrl")
    logo_image_height: Optional[StrictInt] = Field(default=None, description="The height of a logo container. Logo image will be automatically scaled.", serialization_alias="logoImageHeight")
    collapsed_logo_image_url: Optional[StrictStr] = Field(default=None, description="Logo shown when side menu is collapsed", serialization_alias="collapsedLogoImageUrl")
    app_title: Optional[StrictStr] = Field(default=None, description="White-labeled name of the platform", serialization_alias="appTitle")
    favicon: Optional[Favicon] = Field(default=None, description="JSON object that contains website icon url and type")
    palette_settings: Optional[PaletteSettings] = Field(default=None, description="Complex JSON that describes structure of the Angular Material Palette. See [theming](https://material.angular.io/guide/theming) for more details", serialization_alias="paletteSettings")
    primary_color_panels: Optional[StrictBool] = Field(default=None, description="Whether primary-color panels (top toolbar, side navigation, dialog and entity-details headers) use the primary palette color as background. When false, they render on a white background", serialization_alias="primaryColorPanels")
    help_link_base_url: Optional[StrictStr] = Field(default=None, description="Base URL for help link", serialization_alias="helpLinkBaseUrl")
    ui_help_base_url: Optional[StrictStr] = Field(default=None, description="Base URL for the repository with the UI help components (markdown)", serialization_alias="uiHelpBaseUrl")
    enable_help_links: Optional[StrictBool] = Field(default=None, description="Enable or Disable help links", serialization_alias="enableHelpLinks")
    white_labeling_enabled: Optional[StrictBool] = Field(default=None, description="Enable white-labeling", serialization_alias="whiteLabelingEnabled")
    show_name_version: Optional[StrictBool] = Field(default=None, description="Show platform name and version on UI and login screen", serialization_alias="showNameVersion")
    platform_name: Optional[StrictStr] = Field(default=None, description="White-labeled platform name", serialization_alias="platformName")
    platform_version: Optional[StrictStr] = Field(default=None, description="White-labeled platform version", serialization_alias="platformVersion")
    custom_css: Optional[StrictStr] = Field(default=None, description="Custom CSS content", serialization_alias="customCss")
    hide_connectivity_dialog: Optional[StrictBool] = Field(default=None, description="Hide device connectivity dialog", serialization_alias="hideConnectivityDialog")
    override_trendz_name: Optional[StrictBool] = Field(default=None, description="Override Trendz Add-on name", serialization_alias="overrideTrendzName")
    page_background_color: Optional[StrictStr] = Field(default=None, description="Login page background color", serialization_alias="pageBackgroundColor")
    dark_foreground: Optional[StrictBool] = Field(default=None, description="Enable/Disable dark foreground", serialization_alias="darkForeground")
    domain_id: Optional[DomainId] = Field(default=None, description="Domain id", serialization_alias="domainId")
    base_url: Optional[StrictStr] = Field(default=None, description="Base URL for the activation link, etc", serialization_alias="baseUrl")
    prohibit_different_url: Optional[StrictBool] = Field(default=None, description="Prohibit use of other URLs. It is recommended to enable this setting", serialization_alias="prohibitDifferentUrl")
    admin_settings_id: Optional[StrictStr] = Field(default=None, description="Id of the settings object that store this parameters", serialization_alias="adminSettingsId")
    show_name_bottom: Optional[StrictBool] = Field(default=None, description="Show platform name and version on login page", serialization_alias="showNameBottom")
    __properties: ClassVar[List[str]] = ["logoImageUrl", "logoImageHeight", "collapsedLogoImageUrl", "appTitle", "favicon", "paletteSettings", "primaryColorPanels", "helpLinkBaseUrl", "uiHelpBaseUrl", "enableHelpLinks", "whiteLabelingEnabled", "showNameVersion", "platformName", "platformVersion", "customCss", "hideConnectivityDialog", "overrideTrendzName", "pageBackgroundColor", "darkForeground", "domainId", "baseUrl", "prohibitDifferentUrl", "adminSettingsId", "showNameBottom"]

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
        """Create an instance of LoginWhiteLabelingParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "white_labeling_enabled",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of favicon
        if self.favicon:
            _dict['favicon'] = self.favicon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of palette_settings
        if self.palette_settings:
            _dict['paletteSettings'] = self.palette_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_id
        if self.domain_id:
            _dict['domainId'] = self.domain_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoginWhiteLabelingParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "logo_image_url": obj.get("logoImageUrl"),
            "logo_image_height": obj.get("logoImageHeight"),
            "collapsed_logo_image_url": obj.get("collapsedLogoImageUrl"),
            "app_title": obj.get("appTitle"),
            "favicon": Favicon.from_dict(obj["favicon"]) if obj.get("favicon") is not None else None,
            "palette_settings": PaletteSettings.from_dict(obj["paletteSettings"]) if obj.get("paletteSettings") is not None else None,
            "primary_color_panels": obj.get("primaryColorPanels"),
            "help_link_base_url": obj.get("helpLinkBaseUrl"),
            "ui_help_base_url": obj.get("uiHelpBaseUrl"),
            "enable_help_links": obj.get("enableHelpLinks"),
            "white_labeling_enabled": obj.get("whiteLabelingEnabled"),
            "show_name_version": obj.get("showNameVersion"),
            "platform_name": obj.get("platformName"),
            "platform_version": obj.get("platformVersion"),
            "custom_css": obj.get("customCss"),
            "hide_connectivity_dialog": obj.get("hideConnectivityDialog"),
            "override_trendz_name": obj.get("overrideTrendzName"),
            "page_background_color": obj.get("pageBackgroundColor"),
            "dark_foreground": obj.get("darkForeground"),
            "domain_id": DomainId.from_dict(obj["domainId"]) if obj.get("domainId") is not None else None,
            "base_url": obj.get("baseUrl"),
            "prohibit_different_url": obj.get("prohibitDifferentUrl"),
            "admin_settings_id": obj.get("adminSettingsId"),
            "show_name_bottom": obj.get("showNameBottom")
        })
        return _obj


