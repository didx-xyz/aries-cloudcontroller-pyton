# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictBool, StrictStr

from aries_cloudcontroller.models.indy_proof_request import IndyProofRequest
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V10PresentationCreateRequestRequest(BaseModel):
    """
    V10PresentationCreateRequestRequest
    """  # noqa: E501

    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Whether to remove the presentation exchange record on completion (overrides --preserve-exchange-records configuration setting)",
    )
    auto_verify: Optional[StrictBool] = Field(
        default=None, description="Verifier choice to auto-verify proof presentation"
    )
    comment: Optional[StrictStr] = None
    proof_request: IndyProofRequest
    trace: Optional[StrictBool] = Field(
        default=None, description="Whether to trace event (default false)"
    )
    __properties: ClassVar[List[str]] = [
        "auto_remove",
        "auto_verify",
        "comment",
        "proof_request",
        "trace",
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
        """Create an instance of V10PresentationCreateRequestRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of proof_request
        if self.proof_request:
            _dict["proof_request"] = self.proof_request.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V10PresentationCreateRequestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_remove": obj.get("auto_remove"),
                "auto_verify": obj.get("auto_verify"),
                "comment": obj.get("comment"),
                "proof_request": IndyProofRequest.from_dict(obj.get("proof_request"))
                if obj.get("proof_request") is not None
                else None,
                "trace": obj.get("trace"),
            }
        )
        return _obj
