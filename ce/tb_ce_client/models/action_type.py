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


class ActionType(str, Enum):
    """
    ActionType
    """

    """
    allowed enum values
    """
    ADDED = 'ADDED'
    DELETED = 'DELETED'
    UPDATED = 'UPDATED'
    ATTRIBUTES_UPDATED = 'ATTRIBUTES_UPDATED'
    ATTRIBUTES_DELETED = 'ATTRIBUTES_DELETED'
    TIMESERIES_UPDATED = 'TIMESERIES_UPDATED'
    TIMESERIES_DELETED = 'TIMESERIES_DELETED'
    RPC_CALL = 'RPC_CALL'
    CREDENTIALS_UPDATED = 'CREDENTIALS_UPDATED'
    ASSIGNED_TO_CUSTOMER = 'ASSIGNED_TO_CUSTOMER'
    UNASSIGNED_FROM_CUSTOMER = 'UNASSIGNED_FROM_CUSTOMER'
    ACTIVATED = 'ACTIVATED'
    SUSPENDED = 'SUSPENDED'
    CREDENTIALS_READ = 'CREDENTIALS_READ'
    ATTRIBUTES_READ = 'ATTRIBUTES_READ'
    RELATION_ADD_OR_UPDATE = 'RELATION_ADD_OR_UPDATE'
    RELATION_DELETED = 'RELATION_DELETED'
    RELATIONS_DELETED = 'RELATIONS_DELETED'
    REST_API_RULE_ENGINE_CALL = 'REST_API_RULE_ENGINE_CALL'
    ALARM_ACK = 'ALARM_ACK'
    ALARM_CLEAR = 'ALARM_CLEAR'
    ALARM_DELETE = 'ALARM_DELETE'
    ALARM_ASSIGNED = 'ALARM_ASSIGNED'
    ALARM_UNASSIGNED = 'ALARM_UNASSIGNED'
    LOGIN = 'LOGIN'
    LOGOUT = 'LOGOUT'
    LOCKOUT = 'LOCKOUT'
    ASSIGNED_FROM_TENANT = 'ASSIGNED_FROM_TENANT'
    ASSIGNED_TO_TENANT = 'ASSIGNED_TO_TENANT'
    PROVISION_SUCCESS = 'PROVISION_SUCCESS'
    PROVISION_FAILURE = 'PROVISION_FAILURE'
    ASSIGNED_TO_EDGE = 'ASSIGNED_TO_EDGE'
    UNASSIGNED_FROM_EDGE = 'UNASSIGNED_FROM_EDGE'
    ADDED_COMMENT = 'ADDED_COMMENT'
    UPDATED_COMMENT = 'UPDATED_COMMENT'
    DELETED_COMMENT = 'DELETED_COMMENT'
    SMS_SENT = 'SMS_SENT'
    COMMUNITY_GRANT_OFFLINE_CHECKER_RUN = 'COMMUNITY_GRANT_OFFLINE_CHECKER_RUN'
    COMMUNITY_GRANT_REQUEST_ACCESS = 'COMMUNITY_GRANT_REQUEST_ACCESS'
    COMMUNITY_GRANT_ENROLLMENT = 'COMMUNITY_GRANT_ENROLLMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionType from a JSON string"""
        return cls(json.loads(json_str))


