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

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class LinkedDataProof(BaseModel):
    """
    LinkedDataProof
    """  # noqa: E501

    challenge: Optional[StrictStr] = Field(
        default=None,
        description="Associates a challenge with a proof, for use with a proofPurpose such as authentication",
    )
    created: Annotated[str, Field(strict=True)] = Field(
        description="The string value of an ISO8601 combined date and time string generated by the Signature Algorithm"
    )
    domain: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="A string value specifying the restricted domain of the signature.",
    )
    jws: Optional[StrictStr] = Field(
        default=None,
        description="Associates a Detached Json Web Signature with a proof",
    )
    nonce: Optional[StrictStr] = Field(default=None, description="The nonce")
    proof_purpose: StrictStr = Field(description="Proof purpose", alias="proofPurpose")
    proof_value: Optional[StrictStr] = Field(
        default=None, description="The proof value of a proof", alias="proofValue"
    )
    type: StrictStr = Field(
        description="Identifies the digital signature suite that was used to create the signature"
    )
    verification_method: Annotated[str, Field(strict=True)] = Field(
        description="Information used for proof verification",
        alias="verificationMethod",
    )
    __properties: ClassVar[List[str]] = [
        "challenge",
        "created",
        "domain",
        "jws",
        "nonce",
        "proofPurpose",
        "proofValue",
        "type",
        "verificationMethod",
    ]

    @field_validator("created")
    def created_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
            )
        return value

    @field_validator("domain")
    def domain_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\w+:(\/?\/?)[^\s]+", value):
            raise ValueError(
                r"must validate the regular expression /\w+:(\/?\/?)[^\s]+/"
            )
        return value

    @field_validator("verification_method")
    def verification_method_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"\w+:(\/?\/?)[^\s]+", value):
            raise ValueError(
                r"must validate the regular expression /\w+:(\/?\/?)[^\s]+/"
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
        """Create an instance of LinkedDataProof from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LinkedDataProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "challenge": obj.get("challenge"),
                "created": obj.get("created"),
                "domain": obj.get("domain"),
                "jws": obj.get("jws"),
                "nonce": obj.get("nonce"),
                "proofPurpose": obj.get("proofPurpose"),
                "proofValue": obj.get("proofValue"),
                "type": obj.get("type"),
                "verificationMethod": obj.get("verificationMethod"),
            }
        )
        return _obj
