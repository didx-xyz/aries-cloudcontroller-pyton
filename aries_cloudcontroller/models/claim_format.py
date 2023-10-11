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
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ClaimFormat(BaseModel):
    """
    ClaimFormat
    """

    jwt: Optional[Union[str, Any]] = None
    jwt_vc: Optional[Union[str, Any]] = None
    jwt_vp: Optional[Union[str, Any]] = None
    ldp: Optional[Union[str, Any]] = None
    ldp_vc: Optional[Union[str, Any]] = None
    ldp_vp: Optional[Union[str, Any]] = None
    __properties: ClassVar[List[str]] = [
        "jwt",
        "jwt_vc",
        "jwt_vp",
        "ldp",
        "ldp_vc",
        "ldp_vp",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClaimFormat from a JSON string"""
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
        """Create an instance of ClaimFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "jwt": obj.get("jwt"),
                "jwt_vc": obj.get("jwt_vc"),
                "jwt_vp": obj.get("jwt_vp"),
                "ldp": obj.get("ldp"),
                "ldp_vc": obj.get("ldp_vc"),
                "ldp_vp": obj.get("ldp_vp"),
            }
        )
        return _obj
