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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.cred_def_value import CredDefValue

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CredentialDefinition(BaseModel):
    """
    CredentialDefinition
    """

    id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential definition identifier"
    )
    schema_id: Optional[StrictStr] = Field(
        default=None,
        description="Schema identifier within credential definition identifier",
        alias="schemaId",
    )
    tag: Optional[StrictStr] = Field(
        default=None, description="Tag within credential definition identifier"
    )
    type: Optional[Union[str, Any]] = Field(
        default=None, description="Signature type: CL for Camenisch-Lysyanskaya"
    )
    value: Optional[CredDefValue] = None
    ver: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Node protocol version"
    )
    __properties: ClassVar[List[str]] = [
        "id",
        "schemaId",
        "tag",
        "type",
        "value",
        "ver",
    ]

    @field_validator("id")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$/"
            )
        return value

    @field_validator("ver")
    def ver_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9.]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9.]+$/")
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
        """Create an instance of CredentialDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict["value"] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of CredentialDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "schemaId": obj.get("schemaId"),
                "tag": obj.get("tag"),
                "type": obj.get("type"),
                "value": CredDefValue.from_dict(obj.get("value"))
                if obj.get("value") is not None
                else None,
                "ver": obj.get("ver"),
            }
        )
        return _obj
