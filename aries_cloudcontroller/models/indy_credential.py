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
import re
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.indy_attr_value import IndyAttrValue

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class IndyCredential(BaseModel):
    """
    IndyCredential
    """

    cred_def_id: Annotated[str, Field(strict=True)] = Field(
        description="Credential definition identifier"
    )
    rev_reg: Optional[Union[str, Any]] = Field(
        default=None, description="Revocation registry state"
    )
    rev_reg_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Revocation registry identifier"
    )
    schema_id: Annotated[str, Field(strict=True)] = Field(
        description="Schema identifier"
    )
    signature: Union[str, Any] = Field(description="Credential signature")
    signature_correctness_proof: Union[str, Any] = Field(
        description="Credential signature correctness proof"
    )
    values: Dict[str, IndyAttrValue] = Field(description="Credential attributes")
    witness: Optional[Union[str, Any]] = Field(
        default=None, description="Witness for revocation proof"
    )
    __properties: ClassVar[List[str]] = [
        "cred_def_id",
        "rev_reg",
        "rev_reg_id",
        "schema_id",
        "signature",
        "signature_correctness_proof",
        "values",
        "witness",
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

    @field_validator("rev_reg_id")
    def rev_reg_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/"
            )
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

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IndyCredential from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in values (dict)
        _field_dict = {}
        if self.values:
            for _key in self.values:
                if self.values[_key]:
                    _field_dict[_key] = self.values[_key].to_dict()
            _dict["values"] = _field_dict
        # set to None if rev_reg (nullable) is None
        # and model_fields_set contains the field
        if self.rev_reg is None and "rev_reg" in self.model_fields_set:
            _dict["rev_reg"] = None

        # set to None if rev_reg_id (nullable) is None
        # and model_fields_set contains the field
        if self.rev_reg_id is None and "rev_reg_id" in self.model_fields_set:
            _dict["rev_reg_id"] = None

        # set to None if witness (nullable) is None
        # and model_fields_set contains the field
        if self.witness is None and "witness" in self.model_fields_set:
            _dict["witness"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of IndyCredential from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cred_def_id": obj.get("cred_def_id"),
                "rev_reg": obj.get("rev_reg"),
                "rev_reg_id": obj.get("rev_reg_id"),
                "schema_id": obj.get("schema_id"),
                "signature": obj.get("signature"),
                "signature_correctness_proof": obj.get("signature_correctness_proof"),
                "values": dict(
                    (_k, IndyAttrValue.from_dict(_v))
                    for _k, _v in obj.get("values").items()
                )
                if obj.get("values") is not None
                else None,
                "witness": obj.get("witness"),
            }
        )
        return _obj
