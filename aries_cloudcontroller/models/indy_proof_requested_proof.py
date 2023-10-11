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

from pydantic import BaseModel, Field

from aries_cloudcontroller.models.indy_proof_requested_proof_predicate import (
    IndyProofRequestedProofPredicate,
)
from aries_cloudcontroller.models.indy_proof_requested_proof_revealed_attr import (
    IndyProofRequestedProofRevealedAttr,
)
from aries_cloudcontroller.models.indy_proof_requested_proof_revealed_attr_group import (
    IndyProofRequestedProofRevealedAttrGroup,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyProofRequestedProof(BaseModel):
    """
    IndyProofRequestedProof
    """

    predicates: Optional[Dict[str, IndyProofRequestedProofPredicate]] = Field(
        default=None, description="Proof requested proof predicates."
    )
    revealed_attr_groups: Optional[
        Dict[str, IndyProofRequestedProofRevealedAttrGroup]
    ] = Field(
        default=None, description="Proof requested proof revealed attribute groups"
    )
    revealed_attrs: Optional[Dict[str, IndyProofRequestedProofRevealedAttr]] = Field(
        default=None, description="Proof requested proof revealed attributes"
    )
    self_attested_attrs: Optional[Union[str, Any]] = Field(
        default=None, description="Proof requested proof self-attested attributes"
    )
    unrevealed_attrs: Optional[Union[str, Any]] = Field(
        default=None, description="Unrevealed attributes"
    )
    __properties: ClassVar[List[str]] = [
        "predicates",
        "revealed_attr_groups",
        "revealed_attrs",
        "self_attested_attrs",
        "unrevealed_attrs",
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
        """Create an instance of IndyProofRequestedProof from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in predicates (dict)
        _field_dict = {}
        if self.predicates:
            for _key in self.predicates:
                if self.predicates[_key]:
                    _field_dict[_key] = self.predicates[_key].to_dict()
            _dict["predicates"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in revealed_attr_groups (dict)
        _field_dict = {}
        if self.revealed_attr_groups:
            for _key in self.revealed_attr_groups:
                if self.revealed_attr_groups[_key]:
                    _field_dict[_key] = self.revealed_attr_groups[_key].to_dict()
            _dict["revealed_attr_groups"] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in revealed_attrs (dict)
        _field_dict = {}
        if self.revealed_attrs:
            for _key in self.revealed_attrs:
                if self.revealed_attrs[_key]:
                    _field_dict[_key] = self.revealed_attrs[_key].to_dict()
            _dict["revealed_attrs"] = _field_dict
        # set to None if revealed_attr_groups (nullable) is None
        # and model_fields_set contains the field
        if (
            self.revealed_attr_groups is None
            and "revealed_attr_groups" in self.model_fields_set
        ):
            _dict["revealed_attr_groups"] = None

        # set to None if revealed_attrs (nullable) is None
        # and model_fields_set contains the field
        if self.revealed_attrs is None and "revealed_attrs" in self.model_fields_set:
            _dict["revealed_attrs"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyProofRequestedProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "predicates": dict(
                    (_k, IndyProofRequestedProofPredicate.from_dict(_v))
                    for _k, _v in obj.get("predicates").items()
                )
                if obj.get("predicates") is not None
                else None,
                "revealed_attr_groups": dict(
                    (_k, IndyProofRequestedProofRevealedAttrGroup.from_dict(_v))
                    for _k, _v in obj.get("revealed_attr_groups").items()
                )
                if obj.get("revealed_attr_groups") is not None
                else None,
                "revealed_attrs": dict(
                    (_k, IndyProofRequestedProofRevealedAttr.from_dict(_v))
                    for _k, _v in obj.get("revealed_attrs").items()
                )
                if obj.get("revealed_attrs") is not None
                else None,
                "self_attested_attrs": obj.get("self_attested_attrs"),
                "unrevealed_attrs": obj.get("unrevealed_attrs"),
            }
        )
        return _obj
