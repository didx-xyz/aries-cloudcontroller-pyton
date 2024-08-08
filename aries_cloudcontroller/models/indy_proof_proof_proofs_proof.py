# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0rc6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.indy_non_revoc_proof import IndyNonRevocProof
from aries_cloudcontroller.models.indy_primary_proof import IndyPrimaryProof
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyProofProofProofsProof(BaseModel):
    """
    IndyProofProofProofsProof
    """  # noqa: E501

    non_revoc_proof: Optional[IndyNonRevocProof] = Field(
        default=None, description="Indy non-revocation proof"
    )
    primary_proof: Optional[IndyPrimaryProof] = Field(
        default=None, description="Indy primary proof"
    )
    __properties: ClassVar[List[str]] = ["non_revoc_proof", "primary_proof"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyProofProofProofsProof from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of non_revoc_proof
        if self.non_revoc_proof:
            _dict["non_revoc_proof"] = self.non_revoc_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_proof
        if self.primary_proof:
            _dict["primary_proof"] = self.primary_proof.to_dict()
        # set to None if non_revoc_proof (nullable) is None
        # and model_fields_set contains the field
        if self.non_revoc_proof is None and "non_revoc_proof" in self.model_fields_set:
            _dict["non_revoc_proof"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyProofProofProofsProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "non_revoc_proof": (
                    IndyNonRevocProof.from_dict(obj["non_revoc_proof"])
                    if obj.get("non_revoc_proof") is not None
                    else None
                ),
                "primary_proof": (
                    IndyPrimaryProof.from_dict(obj["primary_proof"])
                    if obj.get("primary_proof") is not None
                    else None
                ),
            }
        )
        return _obj
