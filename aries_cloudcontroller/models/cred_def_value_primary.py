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
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, field_validator

from aries_cloudcontroller.models.generated import Generated
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CredDefValuePrimary(BaseModel):
    """
    CredDefValuePrimary
    """

    n: Optional[StrictStr] = None
    r: Optional[Generated] = None
    rctxt: Optional[StrictStr] = None
    s: Optional[StrictStr] = None
    z: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["n", "r", "rctxt", "s", "z"]

    @field_validator("n")
    def n_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("rctxt")
    def rctxt_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("s")
    def s_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("z")
    def z_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CredDefValuePrimary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of r
        if self.r:
            _dict["r"] = self.r.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CredDefValuePrimary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "n": obj.get("n"),
                "r": Generated.from_dict(obj.get("r"))
                if obj.get("r") is not None
                else None,
                "rctxt": obj.get("rctxt"),
                "s": obj.get("s"),
                "z": obj.get("z"),
            }
        )
        return _obj
