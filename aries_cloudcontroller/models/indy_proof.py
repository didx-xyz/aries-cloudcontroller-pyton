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
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.indy_proof_identifier import IndyProofIdentifier
from aries_cloudcontroller.models.indy_proof_proof import IndyProofProof
from aries_cloudcontroller.models.indy_proof_requested_proof import (
    IndyProofRequestedProof,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyProof(BaseModel):
    """
    IndyProof
    """  # noqa: E501

    identifiers: Optional[List[IndyProofIdentifier]] = Field(
        default=None, description="Indy proof.identifiers content"
    )
    proof: Optional[IndyProofProof] = None
    requested_proof: Optional[IndyProofRequestedProof] = None
    __properties: ClassVar[List[str]] = ["identifiers", "proof", "requested_proof"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyProof from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in identifiers (list)
        _items = []
        if self.identifiers:
            for _item in self.identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["identifiers"] = _items
        # override the default output from pydantic by calling `to_dict()` of proof
        if self.proof:
            _dict["proof"] = self.proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_proof
        if self.requested_proof:
            _dict["requested_proof"] = self.requested_proof.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IndyProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "identifiers": (
                    [
                        IndyProofIdentifier.from_dict(_item)
                        for _item in obj.get("identifiers")
                    ]
                    if obj.get("identifiers") is not None
                    else None
                ),
                "proof": (
                    IndyProofProof.from_dict(obj.get("proof"))
                    if obj.get("proof") is not None
                    else None
                ),
                "requested_proof": (
                    IndyProofRequestedProof.from_dict(obj.get("requested_proof"))
                    if obj.get("requested_proof") is not None
                    else None
                ),
            }
        )
        return _obj
