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
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.indy_key_correctness_proof import (
    IndyKeyCorrectnessProof,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyCredAbstract(BaseModel):
    """
    IndyCredAbstract
    """  # noqa: E501

    cred_def_id: Annotated[str, Field(strict=True)] = Field(
        description="Credential definition identifier"
    )
    key_correctness_proof: IndyKeyCorrectnessProof = Field(
        description="Key correctness proof"
    )
    nonce: Annotated[str, Field(strict=True)] = Field(
        description="Nonce in credential abstract"
    )
    schema_id: Annotated[str, Field(strict=True)] = Field(
        description="Schema identifier"
    )
    __properties: ClassVar[List[str]] = [
        "cred_def_id",
        "key_correctness_proof",
        "nonce",
        "schema_id",
    ]

    @field_validator("cred_def_id")
    def cred_def_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/"
            )
        return value

    @field_validator("nonce")
    def nonce_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]*$/")
        return value

    @field_validator("schema_id")
    def schema_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/"
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
        """Create an instance of IndyCredAbstract from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of key_correctness_proof
        if self.key_correctness_proof:
            _dict["key_correctness_proof"] = self.key_correctness_proof.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyCredAbstract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cred_def_id": obj.get("cred_def_id"),
                "key_correctness_proof": (
                    IndyKeyCorrectnessProof.from_dict(obj["key_correctness_proof"])
                    if obj.get("key_correctness_proof") is not None
                    else None
                ),
                "nonce": obj.get("nonce"),
                "schema_id": obj.get("schema_id"),
            }
        )
        return _obj
