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

from aries_cloudcontroller.models.indy_proof_proof_aggregated_proof import (
    IndyProofProofAggregatedProof,
)
from aries_cloudcontroller.models.indy_proof_proof_proofs_proof import (
    IndyProofProofProofsProof,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyProofProof(BaseModel):
    """
    IndyProofProof
    """  # noqa: E501

    aggregated_proof: Optional[IndyProofProofAggregatedProof] = None
    proofs: Optional[List[IndyProofProofProofsProof]] = Field(
        default=None, description="Indy proof proofs"
    )
    __properties: ClassVar[List[str]] = ["aggregated_proof", "proofs"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyProofProof from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregated_proof
        if self.aggregated_proof:
            _dict["aggregated_proof"] = self.aggregated_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in proofs (list)
        _items = []
        if self.proofs:
            for _item in self.proofs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["proofs"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyProofProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "aggregated_proof": (
                    IndyProofProofAggregatedProof.from_dict(obj["aggregated_proof"])
                    if obj.get("aggregated_proof") is not None
                    else None
                ),
                "proofs": (
                    [
                        IndyProofProofProofsProof.from_dict(_item)
                        for _item in obj["proofs"]
                    ]
                    if obj.get("proofs") is not None
                    else None
                ),
            }
        )
        return _obj
