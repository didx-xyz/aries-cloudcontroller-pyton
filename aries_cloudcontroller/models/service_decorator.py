# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Annotated

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ServiceDecorator(BaseModel):
    """
    ServiceDecorator
    """  # noqa: E501

    recipient_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of recipient keys", alias="recipientKeys"
    )
    routing_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of routing keys", alias="routingKeys"
    )
    service_endpoint: Optional[StrictStr] = Field(
        default=None,
        description="Service endpoint at which to reach this agent",
        alias="serviceEndpoint",
    )
    __properties: ClassVar[List[str]] = [
        "recipientKeys",
        "routingKeys",
        "serviceEndpoint",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServiceDecorator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of ServiceDecorator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "recipientKeys": obj.get("recipientKeys"),
                "routingKeys": obj.get("routingKeys"),
                "serviceEndpoint": obj.get("serviceEndpoint"),
            }
        )
        return _obj
