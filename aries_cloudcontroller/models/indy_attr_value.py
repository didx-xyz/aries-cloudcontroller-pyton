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
import re

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyAttrValue(BaseModel):
    """
    IndyAttrValue
    """

    encoded: Annotated[str, Field(strict=True)] = Field(
        description="Attribute encoded value"
    )
    raw: StrictStr = Field(description="Attribute raw value")
    __properties: ClassVar[List[str]] = ["encoded", "raw"]

    @field_validator("encoded")
    def encoded_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-?[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^-?[0-9]*$/")
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndyAttrValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyAttrValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {"encoded": obj.get("encoded"), "raw": obj.get("raw")}
        )
        return _obj
