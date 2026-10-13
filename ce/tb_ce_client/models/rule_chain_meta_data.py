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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from tb_ce_client.models.node_connection_info import NodeConnectionInfo
from tb_ce_client.models.rule_chain_connection_info import RuleChainConnectionInfo
from tb_ce_client.models.rule_chain_id import RuleChainId
from tb_ce_client.models.rule_chain_note import RuleChainNote
from tb_ce_client.models.rule_node import RuleNode
from typing import Optional, Set
from typing_extensions import Self

class RuleChainMetaData(BaseModel):
    """
    A JSON value representing the rule chain metadata.
    """ # noqa: E501
    rule_chain_id: RuleChainId = Field(description="JSON object with Rule Chain Id.", serialization_alias="ruleChainId")
    version: Optional[StrictInt] = Field(default=None, description="Version of the Rule Chain")
    first_node_index: StrictInt = Field(description="Index of the first rule node in the 'nodes' list", serialization_alias="firstNodeIndex")
    nodes: List[RuleNode] = Field(description="List of rule node JSON objects")
    connections: List[NodeConnectionInfo] = Field(description="List of JSON objects that represent connections between rule nodes")
    rule_chain_connections: List[RuleChainConnectionInfo] = Field(description="List of JSON objects that represent connections between rule nodes and other rule chains.", serialization_alias="ruleChainConnections")
    notes: Optional[List[RuleChainNote]] = Field(default=None, description="List of sticky notes placed on the rule chain canvas")
    __properties: ClassVar[List[str]] = ["ruleChainId", "version", "firstNodeIndex", "nodes", "connections", "ruleChainConnections", "notes"]

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
        """Create an instance of RuleChainMetaData from a JSON string"""
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
            "rule_chain_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of rule_chain_id
        if self.rule_chain_id:
            _dict['ruleChainId'] = self.rule_chain_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item_nodes in self.nodes:
                if _item_nodes:
                    _items.append(_item_nodes.to_dict())
            _dict['nodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict['connections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rule_chain_connections (list)
        _items = []
        if self.rule_chain_connections:
            for _item_rule_chain_connections in self.rule_chain_connections:
                if _item_rule_chain_connections:
                    _items.append(_item_rule_chain_connections.to_dict())
            _dict['ruleChainConnections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RuleChainMetaData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rule_chain_id": RuleChainId.from_dict(obj["ruleChainId"]) if obj.get("ruleChainId") is not None else None,
            "version": obj.get("version"),
            "first_node_index": obj.get("firstNodeIndex"),
            "nodes": [RuleNode.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "connections": [NodeConnectionInfo.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None,
            "rule_chain_connections": [RuleChainConnectionInfo.from_dict(_item) for _item in obj["ruleChainConnections"]] if obj.get("ruleChainConnections") is not None else None,
            "notes": [RuleChainNote.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None
        })
        return _obj


