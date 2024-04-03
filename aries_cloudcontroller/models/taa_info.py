# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, StrictBool

from aries_cloudcontroller.models.aml_record import AMLRecord
from aries_cloudcontroller.models.taa_acceptance import TAAAcceptance
from aries_cloudcontroller.models.taa_record import TAARecord
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TAAInfo(BaseModel):
    """
    TAAInfo
    """  # noqa: E501

    aml_record: Optional[AMLRecord] = None
    taa_accepted: Optional[TAAAcceptance] = None
    taa_record: Optional[TAARecord] = None
    taa_required: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = [
        "aml_record",
        "taa_accepted",
        "taa_record",
        "taa_required",
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
        """Create an instance of TAAInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aml_record
        if self.aml_record:
            _dict["aml_record"] = self.aml_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taa_accepted
        if self.taa_accepted:
            _dict["taa_accepted"] = self.taa_accepted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taa_record
        if self.taa_record:
            _dict["taa_record"] = self.taa_record.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TAAInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "aml_record": (
                    AMLRecord.from_dict(obj.get("aml_record"))
                    if obj.get("aml_record") is not None
                    else None
                ),
                "taa_accepted": (
                    TAAAcceptance.from_dict(obj.get("taa_accepted"))
                    if obj.get("taa_accepted") is not None
                    else None
                ),
                "taa_record": (
                    TAARecord.from_dict(obj.get("taa_record"))
                    if obj.get("taa_record") is not None
                    else None
                ),
                "taa_required": obj.get("taa_required"),
            }
        )
        return _obj
