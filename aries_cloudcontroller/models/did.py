# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Literal, Optional, Set

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG
from aries_cloudcontroller.util.regex_patterns import BBS_PATTERN, ED25519_PATTERN


class DID(BaseModel):
    """
    DID
    """  # noqa: E501

    # keep custom changes
    did: Annotated[str, Field(strict=True)] = Field(description="DID of interest")
    key_type: Literal[
        "ed25519", "x25519", "bls12381g1", "bls12381g2", "bls12381g1g2"
    ] = Field(description="Key type associated with the DID")
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional metadata associated with the DID"
    )
    method: Literal["sov", "key", "web", "did:peer:2", "did:peer:4"] = Field(
        description="Did method associated with the DID"
    )
    posture: Literal["public", "posted", "wallet_only"] = Field(
        description="Whether DID is current public DID, posted to ledger but not current public DID, or local to the wallet",
    )
    verkey: Annotated[str, Field(strict=True)] = Field(
        description="Public verification key"
    )
    __properties: ClassVar[List[str]] = [
        "did",
        "key_type",
        "metadata",
        "method",
        "posture",
        "verkey",
    ]

    @field_validator("did")
    def did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+=[a-zA-Z0-9_.:%-]*)*)(\/[^#?]*)?([?][^#]*)?(\#.*)?$$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+=[a-zA-Z0-9_.:%-]*)*)(\/[^#?]*)?([?][^#]*)?(\#.*)?$$/"
            )
        return value

    @field_validator("key_type")
    def key_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["ed25519", "bls12381g2"]):
            raise ValueError("must be one of enum values ('ed25519', 'bls12381g2')")
        return value

    @field_validator("posture")
    def posture_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["public", "posted", "wallet_only"]):
            raise ValueError(
                "must be one of enum values ('public', 'posted', 'wallet_only')"
            )
        return value

    @field_validator("verkey")
    def verkey_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(ED25519_PATTERN, value) and not re.match(BBS_PATTERN, value):
            raise ValueError(
                f"Invalid verkey format. Expected either an ED25519 format matching: {ED25519_PATTERN} or BBS+ format matching: {BBS_PATTERN}"
            )
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
        """Create an instance of DID from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DID from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "did": obj.get("did"),
                "key_type": obj.get("key_type"),
                "metadata": obj.get("metadata"),
                "method": obj.get("method"),
                "posture": obj.get("posture"),
                "verkey": obj.get("verkey"),
            }
        )
        return _obj
