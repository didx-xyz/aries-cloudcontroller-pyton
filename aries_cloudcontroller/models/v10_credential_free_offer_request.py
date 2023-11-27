# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.credential_preview import CredentialPreview
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V10CredentialFreeOfferRequest(BaseModel):
    """
    V10CredentialFreeOfferRequest
    """  # noqa: E501

    auto_issue: Optional[StrictBool] = Field(
        default=None,
        description="Whether to respond automatically to credential requests, creating and issuing requested credentials",
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)",
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    connection_id: StrictStr = Field(description="Connection identifier")
    cred_def_id: Annotated[str, Field(strict=True)] = Field(
        description="Credential definition identifier"
    )
    credential_preview: CredentialPreview
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    __properties: ClassVar[List[str]] = [
        "auto_issue",
        "auto_remove",
        "comment",
        "connection_id",
        "cred_def_id",
        "credential_preview",
        "trace",
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

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V10CredentialFreeOfferRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential_preview
        if self.credential_preview:
            _dict["credential_preview"] = self.credential_preview.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V10CredentialFreeOfferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_issue": obj.get("auto_issue"),
                "auto_remove": obj.get("auto_remove"),
                "comment": obj.get("comment"),
                "connection_id": obj.get("connection_id"),
                "cred_def_id": obj.get("cred_def_id"),
                "credential_preview": CredentialPreview.from_dict(
                    obj.get("credential_preview")
                )
                if obj.get("credential_preview") is not None
                else None,
                "trace": obj.get("trace"),
            }
        )
        return _obj
