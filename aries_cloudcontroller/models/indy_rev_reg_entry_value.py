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
from typing import List, Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyRevRegEntryValue(BaseModel):
    """
    IndyRevRegEntryValue
    """

    accum: Optional[StrictStr] = Field(default=None, description="Accumulator value")
    prev_accum: Optional[StrictStr] = Field(
        default=None, description="Previous accumulator value", alias="prevAccum"
    )
    revoked: Optional[List[StrictInt]] = Field(
        default=None, description="Revoked credential revocation identifiers"
    )
    __properties: ClassVar[List[str]] = ["accum", "prevAccum", "revoked"]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndyRevRegEntryValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyRevRegEntryValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "accum": obj.get("accum"),
                "prevAccum": obj.get("prevAccum"),
                "revoked": obj.get("revoked"),
            }
        )
        return _obj
