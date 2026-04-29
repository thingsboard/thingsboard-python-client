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
import json
from enum import Enum
from typing_extensions import Self


class Resource(str, Enum):
    """
    Resource
    """

    """
    allowed enum values
    """
    ALL = 'ALL'
    PROFILE = 'PROFILE'
    ADMIN_SETTINGS = 'ADMIN_SETTINGS'
    ALARM = 'ALARM'
    DEVICE = 'DEVICE'
    ASSET = 'ASSET'
    CUSTOMER = 'CUSTOMER'
    DASHBOARD = 'DASHBOARD'
    ENTITY_VIEW = 'ENTITY_VIEW'
    EDGE = 'EDGE'
    TENANT = 'TENANT'
    RULE_CHAIN = 'RULE_CHAIN'
    USER = 'USER'
    WIDGETS_BUNDLE = 'WIDGETS_BUNDLE'
    WIDGET_TYPE = 'WIDGET_TYPE'
    OAUTH2_CLIENT = 'OAUTH2_CLIENT'
    DOMAIN = 'DOMAIN'
    MOBILE_APP = 'MOBILE_APP'
    MOBILE_APP_BUNDLE = 'MOBILE_APP_BUNDLE'
    OAUTH2_CONFIGURATION_TEMPLATE = 'OAUTH2_CONFIGURATION_TEMPLATE'
    TENANT_PROFILE = 'TENANT_PROFILE'
    DEVICE_PROFILE = 'DEVICE_PROFILE'
    ASSET_PROFILE = 'ASSET_PROFILE'
    CONVERTER = 'CONVERTER'
    INTEGRATION = 'INTEGRATION'
    SCHEDULER_EVENT = 'SCHEDULER_EVENT'
    BLOB_ENTITY = 'BLOB_ENTITY'
    CUSTOMER_GROUP = 'CUSTOMER_GROUP'
    DEVICE_GROUP = 'DEVICE_GROUP'
    ASSET_GROUP = 'ASSET_GROUP'
    USER_GROUP = 'USER_GROUP'
    ENTITY_VIEW_GROUP = 'ENTITY_VIEW_GROUP'
    EDGE_GROUP = 'EDGE_GROUP'
    DASHBOARD_GROUP = 'DASHBOARD_GROUP'
    ROLE = 'ROLE'
    GROUP_PERMISSION = 'GROUP_PERMISSION'
    WHITE_LABELING = 'WHITE_LABELING'
    AUDIT_LOG = 'AUDIT_LOG'
    API_USAGE_STATE = 'API_USAGE_STATE'
    TB_RESOURCE = 'TB_RESOURCE'
    OTA_PACKAGE = 'OTA_PACKAGE'
    QUEUE = 'QUEUE'
    QUEUE_STATS = 'QUEUE_STATS'
    VERSION_CONTROL = 'VERSION_CONTROL'
    NOTIFICATION = 'NOTIFICATION'
    MOBILE_APP_SETTINGS = 'MOBILE_APP_SETTINGS'
    CUSTOM_MENU = 'CUSTOM_MENU'
    JOB = 'JOB'
    SECRET = 'SECRET'
    REPORT_TEMPLATE = 'REPORT_TEMPLATE'
    REPORT = 'REPORT'
    AI_MODEL = 'AI_MODEL'
    AI = 'AI'
    API_KEY = 'API_KEY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Resource from a JSON string"""
        return cls(json.loads(json_str))


