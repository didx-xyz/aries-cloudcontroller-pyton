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
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.indy_proof_req_attr_spec import IndyProofReqAttrSpec
from aries_cloudcontroller.models.indy_proof_req_pred_spec import IndyProofReqPredSpec
from aries_cloudcontroller.models.indy_proof_request_non_revoked import (
    IndyProofRequestNonRevoked,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyProofRequest(BaseModel):
    """
    IndyProofRequest
    """  # noqa: E501

    name: Optional[StrictStr] = Field(default=None, description="Proof request name")
    non_revoked: Optional[IndyProofRequestNonRevoked] = None
    nonce: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Nonce"
    )
    requested_attributes: Dict[str, IndyProofReqAttrSpec] = Field(
        description="Requested attribute specifications of proof request"
    )
    requested_predicates: Dict[str, IndyProofReqPredSpec] = Field(
        description="Requested predicate specifications of proof request"
    )
    version: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Proof request version"
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "non_revoked",
        "nonce",
        "requested_attributes",
        "requested_predicates",
        "version",
    ]

    @field_validator("nonce")
    def nonce_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[1-9][0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[1-9][0-9]*$/")
        return value

    @field_validator("version")
    def version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9.]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9.]+$/")
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyProofRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of non_revoked
        if self.non_revoked:
            _dict["non_revoked"] = self.non_revoked.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in requested_attributes (dict)
        _field_dict = {}
        if self.requested_attributes:
            for _key in self.requested_attributes:
                if self.requested_attributes[_key]:
                    _field_dict[_key] = self.requested_attributes[_key].to_dict()
            _dict["requested_attributes"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in requested_predicates (dict)
        _field_dict = {}
        if self.requested_predicates:
            for _key in self.requested_predicates:
                if self.requested_predicates[_key]:
                    _field_dict[_key] = self.requested_predicates[_key].to_dict()
            _dict["requested_predicates"] = _field_dict
        # set to None if non_revoked (nullable) is None
        # and model_fields_set contains the field
        if self.non_revoked is None and "non_revoked" in self.model_fields_set:
            _dict["non_revoked"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IndyProofRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "non_revoked": (
                    IndyProofRequestNonRevoked.from_dict(obj.get("non_revoked"))
                    if obj.get("non_revoked") is not None
                    else None
                ),
                "nonce": obj.get("nonce"),
                "requested_attributes": (
                    dict(
                        (_k, IndyProofReqAttrSpec.from_dict(_v))
                        for _k, _v in obj.get("requested_attributes").items()
                    )
                    if obj.get("requested_attributes") is not None
                    else None
                ),
                "requested_predicates": (
                    dict(
                        (_k, IndyProofReqPredSpec.from_dict(_v))
                        for _k, _v in obj.get("requested_predicates").items()
                    )
                    if obj.get("requested_predicates") is not None
                    else None
                ),
                "version": obj.get("version"),
            }
        )
        return _obj
