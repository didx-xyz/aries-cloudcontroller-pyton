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

from pydantic import BaseModel, Field, StrictBool, StrictStr

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class MenuFormParam(BaseModel):
    """
    MenuFormParam
    """

    default: Optional[StrictStr] = Field(
        default=None, description="Default parameter value"
    )
    description: Optional[StrictStr] = Field(
        default=None, description="Additional descriptive text for menu form parameter"
    )
    name: StrictStr = Field(description="Menu parameter name")
    required: Optional[StrictBool] = Field(
        default=None, description="Whether parameter is required"
    )
    title: StrictStr = Field(description="Menu parameter title")
    type: Optional[StrictStr] = Field(
        default=None, description="Menu form parameter input type"
    )
    __properties: ClassVar[List[str]] = [
        "default",
        "description",
        "name",
        "required",
        "title",
        "type",
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
        """Create an instance of MenuFormParam from a JSON string"""
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
        """Create an instance of MenuFormParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "default": obj.get("default"),
                "description": obj.get("description"),
                "name": obj.get("name"),
                "required": obj.get("required"),
                "title": obj.get("title"),
                "type": obj.get("type"),
            }
        )
        return _obj
