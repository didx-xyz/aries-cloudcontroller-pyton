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
from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.credential_offer import CredentialOffer
from aries_cloudcontroller.models.credential_proposal import CredentialProposal
from aries_cloudcontroller.models.indy_cred_abstract import IndyCredAbstract
from aries_cloudcontroller.models.indy_cred_info import IndyCredInfo
from aries_cloudcontroller.models.indy_cred_request import IndyCredRequest
from aries_cloudcontroller.models.indy_credential import IndyCredential

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V10CredentialExchange(BaseModel):
    """
    V10CredentialExchange
    """

    auto_issue: Optional[StrictBool] = Field(
        default=None,
        description="Issuer choice to issue to request in this credential exchange",
    )
    auto_offer: Optional[StrictBool] = Field(
        default=None,
        description="Holder choice to accept offer in this credential exchange",
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Issuer choice to remove this credential exchange record when complete",
    )
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection identifier"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    credential: Optional[IndyCredInfo] = None
    credential_definition_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Credential definition identifier"
    )
    credential_exchange_id: Optional[StrictStr] = Field(
        default=None, description="Credential exchange identifier"
    )
    credential_id: Optional[StrictStr] = Field(
        default=None, description="Credential identifier"
    )
    credential_offer: Optional[IndyCredAbstract] = None
    credential_offer_dict: Optional[CredentialOffer] = None
    credential_proposal_dict: Optional[CredentialProposal] = None
    credential_request: Optional[IndyCredRequest] = None
    credential_request_metadata: Optional[Union[str, Any]] = Field(
        default=None, description="(Indy) credential request metadata"
    )
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    initiator: Optional[StrictStr] = Field(
        default=None,
        description="Issue-credential exchange initiator: self or external",
    )
    parent_thread_id: Optional[StrictStr] = Field(
        default=None, description="Parent thread identifier"
    )
    raw_credential: Optional[IndyCredential] = None
    revoc_reg_id: Optional[StrictStr] = Field(
        default=None, description="Revocation registry identifier"
    )
    revocation_id: Optional[StrictStr] = Field(
        default=None, description="Credential identifier within revocation registry"
    )
    role: Optional[StrictStr] = Field(
        default=None, description="Issue-credential exchange role: holder or issuer"
    )
    schema_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Schema identifier"
    )
    state: Optional[StrictStr] = Field(
        default=None, description="Issue-credential exchange state"
    )
    thread_id: Optional[StrictStr] = Field(
        default=None, description="Thread identifier"
    )
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "auto_issue",
        "auto_offer",
        "auto_remove",
        "connection_id",
        "created_at",
        "credential",
        "credential_definition_id",
        "credential_exchange_id",
        "credential_id",
        "credential_offer",
        "credential_offer_dict",
        "credential_proposal_dict",
        "credential_request",
        "credential_request_metadata",
        "error_msg",
        "initiator",
        "parent_thread_id",
        "raw_credential",
        "revoc_reg_id",
        "revocation_id",
        "role",
        "schema_id",
        "state",
        "thread_id",
        "trace",
        "updated_at",
    ]

    @field_validator("created_at")
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
            )
        return value

    @field_validator("credential_definition_id")
    def credential_definition_id_validate_regular_expression(cls, value):
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

    @field_validator("initiator")
    def initiator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("self", "external"):
            raise ValueError("must be one of enum values ('self', 'external')")
        return value

    @field_validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("holder", "issuer"):
            raise ValueError("must be one of enum values ('holder', 'issuer')")
        return value

    @field_validator("schema_id")
    def schema_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$/"
            )
        return value

    @field_validator("updated_at")
    def updated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
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
        """Create an instance of V10CredentialExchange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credential
        if self.credential:
            _dict["credential"] = self.credential.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_offer
        if self.credential_offer:
            _dict["credential_offer"] = self.credential_offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_offer_dict
        if self.credential_offer_dict:
            _dict["credential_offer_dict"] = self.credential_offer_dict.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_proposal_dict
        if self.credential_proposal_dict:
            _dict["credential_proposal_dict"] = self.credential_proposal_dict.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credential_request
        if self.credential_request:
            _dict["credential_request"] = self.credential_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of raw_credential
        if self.raw_credential:
            _dict["raw_credential"] = self.raw_credential.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V10CredentialExchange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_issue": obj.get("auto_issue"),
                "auto_offer": obj.get("auto_offer"),
                "auto_remove": obj.get("auto_remove"),
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "credential": IndyCredInfo.from_dict(obj.get("credential"))
                if obj.get("credential") is not None
                else None,
                "credential_definition_id": obj.get("credential_definition_id"),
                "credential_exchange_id": obj.get("credential_exchange_id"),
                "credential_id": obj.get("credential_id"),
                "credential_offer": IndyCredAbstract.from_dict(
                    obj.get("credential_offer")
                )
                if obj.get("credential_offer") is not None
                else None,
                "credential_offer_dict": CredentialOffer.from_dict(
                    obj.get("credential_offer_dict")
                )
                if obj.get("credential_offer_dict") is not None
                else None,
                "credential_proposal_dict": CredentialProposal.from_dict(
                    obj.get("credential_proposal_dict")
                )
                if obj.get("credential_proposal_dict") is not None
                else None,
                "credential_request": IndyCredRequest.from_dict(
                    obj.get("credential_request")
                )
                if obj.get("credential_request") is not None
                else None,
                "credential_request_metadata": obj.get("credential_request_metadata"),
                "error_msg": obj.get("error_msg"),
                "initiator": obj.get("initiator"),
                "parent_thread_id": obj.get("parent_thread_id"),
                "raw_credential": IndyCredential.from_dict(obj.get("raw_credential"))
                if obj.get("raw_credential") is not None
                else None,
                "revoc_reg_id": obj.get("revoc_reg_id"),
                "revocation_id": obj.get("revocation_id"),
                "role": obj.get("role"),
                "schema_id": obj.get("schema_id"),
                "state": obj.get("state"),
                "thread_id": obj.get("thread_id"),
                "trace": obj.get("trace"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj