# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.indy_eq_proof import IndyEQProof
from aries_cloudcontroller.models.indy_ge_proof import IndyGEProof
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyPrimaryProof(BaseModel):
    """
    IndyPrimaryProof
    """  # noqa: E501

    eq_proof: Optional[IndyEQProof] = Field(
        default=None, description="Indy equality proof"
    )
    ge_proofs: Optional[List[IndyGEProof]] = Field(
        default=None, description="Indy GE proofs"
    )
    __properties: ClassVar[List[str]] = ["eq_proof", "ge_proofs"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyPrimaryProof from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of eq_proof
        if self.eq_proof:
            _dict["eq_proof"] = self.eq_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ge_proofs (list)
        _items = []
        if self.ge_proofs:
            for _item in self.ge_proofs:
                if _item:
                    _items.append(_item.to_dict())
            _dict["ge_proofs"] = _items
        # set to None if eq_proof (nullable) is None
        # and model_fields_set contains the field
        if self.eq_proof is None and "eq_proof" in self.model_fields_set:
            _dict["eq_proof"] = None

        # set to None if ge_proofs (nullable) is None
        # and model_fields_set contains the field
        if self.ge_proofs is None and "ge_proofs" in self.model_fields_set:
            _dict["ge_proofs"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyPrimaryProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "eq_proof": (
                    IndyEQProof.from_dict(obj["eq_proof"])
                    if obj.get("eq_proof") is not None
                    else None
                ),
                "ge_proofs": (
                    [IndyGEProof.from_dict(_item) for _item in obj["ge_proofs"]]
                    if obj.get("ge_proofs") is not None
                    else None
                ),
            }
        )
        return _obj
