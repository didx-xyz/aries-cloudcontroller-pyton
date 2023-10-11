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
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.attach_decorator_data1_jws import (
    AttachDecoratorData1JWS,
)
from aries_cloudcontroller.models.attach_decorator_data_jws_header import (
    AttachDecoratorDataJWSHeader,
)

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AttachDecoratorDataJWS(BaseModel):
    """
    AttachDecoratorDataJWS
    """

    header: Optional[AttachDecoratorDataJWSHeader] = None
    protected: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="protected JWS header"
    )
    signature: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="signature"
    )
    signatures: Optional[List[AttachDecoratorData1JWS]] = Field(
        default=None, description="List of signatures"
    )
    __properties: ClassVar[List[str]] = [
        "header",
        "protected",
        "signature",
        "signatures",
    ]

    @field_validator("protected")
    def protected_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-_a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[-_a-zA-Z0-9]*$/")
        return value

    @field_validator("signature")
    def signature_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-_a-zA-Z0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[-_a-zA-Z0-9]*$/")
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
        """Create an instance of AttachDecoratorDataJWS from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of header
        if self.header:
            _dict["header"] = self.header.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in signatures (list)
        _items = []
        if self.signatures:
            for _item in self.signatures:
                if _item:
                    _items.append(_item.to_dict())
            _dict["signatures"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of AttachDecoratorDataJWS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "header": AttachDecoratorDataJWSHeader.from_dict(obj.get("header"))
                if obj.get("header") is not None
                else None,
                "protected": obj.get("protected"),
                "signature": obj.get("signature"),
                "signatures": [
                    AttachDecoratorData1JWS.from_dict(_item)
                    for _item in obj.get("signatures")
                ]
                if obj.get("signatures") is not None
                else None,
            }
        )
        return _obj
