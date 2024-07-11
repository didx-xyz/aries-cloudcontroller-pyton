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

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.models.indy_non_revocation_interval import (
    IndyNonRevocationInterval,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyCredPrecis(BaseModel):
    """
    IndyCredPrecis
    """  # noqa: E501

    cred_info: IndyCredInfo = Field(description="Credential info")
    interval: Optional[IndyNonRevocationInterval] = Field(
        default=None, description="Non-revocation interval from presentation request"
    )
    presentation_referents: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "cred_info",
        "interval",
        "presentation_referents",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyCredPrecis from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cred_info
        if self.cred_info:
            _dict["cred_info"] = self.cred_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interval
        if self.interval:
            _dict["interval"] = self.interval.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyCredPrecis from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cred_info": (
                    IndyCredInfo.from_dict(obj["cred_info"])
                    if obj.get("cred_info") is not None
                    else None
                ),
                "interval": (
                    IndyNonRevocationInterval.from_dict(obj["interval"])
                    if obj.get("interval") is not None
                    else None
                ),
                "presentation_referents": obj.get("presentation_referents"),
            }
        )
        return _obj
