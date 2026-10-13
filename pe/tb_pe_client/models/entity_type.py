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


class EntityType(str, Enum):
    """
    EntityType
    """

    """
    allowed enum values
    """
    TENANT = 'TENANT'
    CUSTOMER = 'CUSTOMER'
    USER = 'USER'
    DASHBOARD = 'DASHBOARD'
    ASSET = 'ASSET'
    DEVICE = 'DEVICE'
    ALARM = 'ALARM'
    ENTITY_GROUP = 'ENTITY_GROUP'
    CONVERTER = 'CONVERTER'
    INTEGRATION = 'INTEGRATION'
    RULE_CHAIN = 'RULE_CHAIN'
    RULE_NODE = 'RULE_NODE'
    SCHEDULER_EVENT = 'SCHEDULER_EVENT'
    BLOB_ENTITY = 'BLOB_ENTITY'
    REPORT_TEMPLATE = 'REPORT_TEMPLATE'
    REPORT = 'REPORT'
    ENTITY_VIEW = 'ENTITY_VIEW'
    WIDGETS_BUNDLE = 'WIDGETS_BUNDLE'
    WIDGET_TYPE = 'WIDGET_TYPE'
    ROLE = 'ROLE'
    GROUP_PERMISSION = 'GROUP_PERMISSION'
    TENANT_PROFILE = 'TENANT_PROFILE'
    DEVICE_PROFILE = 'DEVICE_PROFILE'
    ASSET_PROFILE = 'ASSET_PROFILE'
    API_USAGE_STATE = 'API_USAGE_STATE'
    TB_RESOURCE = 'TB_RESOURCE'
    OTA_PACKAGE = 'OTA_PACKAGE'
    EDGE = 'EDGE'
    RPC = 'RPC'
    QUEUE = 'QUEUE'
    NOTIFICATION_TARGET = 'NOTIFICATION_TARGET'
    NOTIFICATION_TEMPLATE = 'NOTIFICATION_TEMPLATE'
    NOTIFICATION_REQUEST = 'NOTIFICATION_REQUEST'
    NOTIFICATION = 'NOTIFICATION'
    NOTIFICATION_RULE = 'NOTIFICATION_RULE'
    QUEUE_STATS = 'QUEUE_STATS'
    OAUTH2_CLIENT = 'OAUTH2_CLIENT'
    DOMAIN = 'DOMAIN'
    MOBILE_APP = 'MOBILE_APP'
    MOBILE_APP_BUNDLE = 'MOBILE_APP_BUNDLE'
    CALCULATED_FIELD = 'CALCULATED_FIELD'
    JOB = 'JOB'
    SECRET = 'SECRET'
    ADMIN_SETTINGS = 'ADMIN_SETTINGS'
    AI_MODEL = 'AI_MODEL'
    API_KEY = 'API_KEY'
    AGENT = 'AGENT'
    AGENT_APPLICATION = 'AGENT_APPLICATION'
    AGENT_APP_EVENT = 'AGENT_APP_EVENT'
    AGENT_APP_UNIT = 'AGENT_APP_UNIT'
    AGENT_APP_PROFILE = 'AGENT_APP_PROFILE'
    AGENT_PROFILE = 'AGENT_PROFILE'
    AGENT_BULK_ACTION = 'AGENT_BULK_ACTION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EntityType from a JSON string"""
        return cls(json.loads(json_str))


