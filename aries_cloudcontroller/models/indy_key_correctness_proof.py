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
from typing import Any, Dict, List

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyKeyCorrectnessProof(BaseModel):
    """
    IndyKeyCorrectnessProof
    """

    c: Annotated[str, Field(strict=True)] = Field(
        description="c in key correctness proof"
    )
    xr_cap: List[List[StrictStr]] = Field(description="xr_cap in key correctness proof")
    xz_cap: Annotated[str, Field(strict=True)] = Field(
        description="xz_cap in key correctness proof"
    )
    __properties: ClassVar[List[str]] = ["c", "xr_cap", "xz_cap"]

    @field_validator("c")
    def c_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("xz_cap")
    def xz_cap_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
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
        """Create an instance of IndyKeyCorrectnessProof from a JSON string"""
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
        """Create an instance of IndyKeyCorrectnessProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "c": obj.get("c"),
                "xr_cap": obj.get("xr_cap"),
                "xz_cap": obj.get("xz_cap"),
            }
        )
        return _obj
