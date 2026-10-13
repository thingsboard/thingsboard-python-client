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


class AgentAppStepType(str, Enum):
    """
    AgentAppStepType
    """

    """
    allowed enum values
    """
    COMPOSE_TEMPLATE = 'COMPOSE_TEMPLATE'
    COMPOSE = 'COMPOSE'
    COMPOSE_START = 'COMPOSE_START'
    COMPOSE_DOWN = 'COMPOSE_DOWN'
    ROLLBACK = 'ROLLBACK'
    BACKUP_VOLUME = 'BACKUP_VOLUME'
    BACKUP_VOLUME_REMOVE = 'BACKUP_VOLUME_REMOVE'
    COMPOSE_RESTART = 'COMPOSE_RESTART'
    RUN_JOB = 'RUN_JOB'
    AGENT_PREPARE = 'AGENT_PREPARE'
    AGENT_FINALIZE = 'AGENT_FINALIZE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentAppStepType from a JSON string"""
        return cls(json.loads(json_str))


