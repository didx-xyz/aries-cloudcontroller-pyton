# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0rc4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.cred_def_value_primary import CredDefValuePrimary
from aries_cloudcontroller.models.cred_def_value_revocation import (
    CredDefValueRevocation,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class CredDefValue(BaseModel):
    """
    CredDefValue
    """  # noqa: E501

    primary: Optional[CredDefValuePrimary] = Field(
        default=None, description="Primary value for credential definition"
    )
    revocation: Optional[CredDefValueRevocation] = Field(
        default=None, description="Revocation value for credential definition"
    )
    __properties: ClassVar[List[str]] = ["primary", "revocation"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CredDefValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of primary
        if self.primary:
            _dict["primary"] = self.primary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of revocation
        if self.revocation:
            _dict["revocation"] = self.revocation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CredDefValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "primary": (
                    CredDefValuePrimary.from_dict(obj["primary"])
                    if obj.get("primary") is not None
                    else None
                ),
                "revocation": (
                    CredDefValueRevocation.from_dict(obj["revocation"])
                    if obj.get("revocation") is not None
                    else None
                ),
            }
        )
        return _obj
