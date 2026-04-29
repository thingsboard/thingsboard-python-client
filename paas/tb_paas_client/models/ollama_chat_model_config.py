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

from pydantic import ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from tb_paas_client.models.ai_model_config import AiModelConfig
from tb_paas_client.models.ai_model_type import AiModelType
from tb_paas_client.models.ollama_provider_config import OllamaProviderConfig
from typing import Optional, Set
from typing_extensions import Self

class OllamaChatModelConfig(AiModelConfig):
    """
    OllamaChatModelConfig
    """ # noqa: E501
    provider_config: OllamaProviderConfig = Field(serialization_alias="providerConfig")
    model_id: Annotated[str, Field(min_length=1, strict=True)] = Field(serialization_alias="modelId")
    temperature: Optional[Union[StrictFloat, StrictInt]] = None
    top_p: Optional[Union[Annotated[float, Field(le=1, strict=True)], Annotated[int, Field(le=1, strict=True)]]] = Field(default=None, serialization_alias="topP")
    top_k: Optional[StrictInt] = Field(default=None, serialization_alias="topK")
    context_length: Optional[StrictInt] = Field(default=None, serialization_alias="contextLength")
    max_output_tokens: Optional[StrictInt] = Field(default=None, serialization_alias="maxOutputTokens")
    timeout_seconds: Optional[StrictInt] = Field(default=None, serialization_alias="timeoutSeconds")
    max_retries: Optional[StrictInt] = Field(default=None, serialization_alias="maxRetries")
    model_type: Optional[AiModelType] = Field(default=None, serialization_alias="modelType")
    __properties: ClassVar[List[str]] = ["provider", "providerConfig", "modelId", "temperature", "topP", "topK", "contextLength", "maxOutputTokens", "timeoutSeconds", "maxRetries", "modelType"]

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
        """Create an instance of OllamaChatModelConfig from a JSON string"""
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
            "model_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of provider_config
        if self.provider_config:
            _dict['providerConfig'] = self.provider_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OllamaChatModelConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider"),
            "provider_config": OllamaProviderConfig.from_dict(obj["providerConfig"]) if obj.get("providerConfig") is not None else None,
            "model_id": obj.get("modelId"),
            "temperature": obj.get("temperature"),
            "top_p": obj.get("topP"),
            "top_k": obj.get("topK"),
            "context_length": obj.get("contextLength"),
            "max_output_tokens": obj.get("maxOutputTokens"),
            "timeout_seconds": obj.get("timeoutSeconds"),
            "max_retries": obj.get("maxRetries"),
            "model_type": obj.get("modelType")
        })
        return _obj


