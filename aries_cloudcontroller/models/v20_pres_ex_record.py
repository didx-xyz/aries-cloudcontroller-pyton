# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.models.v20_pres import V20Pres
from aries_cloudcontroller.models.v20_pres_ex_record_by_format import (
    V20PresExRecordByFormat,
)
from aries_cloudcontroller.models.v20_pres_proposal import V20PresProposal
from aries_cloudcontroller.models.v20_pres_request import V20PresRequest
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20PresExRecord(BaseModel):
    """
    V20PresExRecord
    """  # noqa: E501

    auto_present: Optional[StrictBool] = Field(
        default=None,
        description="Prover choice to auto-present proof as verifier requests",
    )
    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Verifier choice to remove this presentation exchange record when complete",
    )
    auto_verify: Optional[StrictBool] = Field(
        default=None, description="Verifier choice to auto-verify proof presentation"
    )
    by_format: Optional[V20PresExRecordByFormat] = Field(
        default=None,
        description="Attachment content by format for proposal, request, and presentation",
    )
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection identifier"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    initiator: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange initiator: self or external"
    )
    pres: Optional[V20Pres] = Field(default=None, description="Presentation message")
    pres_ex_id: Optional[StrictStr] = Field(
        default=None, description="Presentation exchange identifier"
    )
    pres_proposal: Optional[V20PresProposal] = Field(
        default=None, description="Presentation proposal message"
    )
    pres_request: Optional[V20PresRequest] = Field(
        default=None, description="Presentation request message"
    )
    role: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange role: prover or verifier"
    )
    state: Optional[StrictStr] = Field(
        default=None, description="Present-proof exchange state"
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
    verified: Optional[StrictStr] = Field(
        default=None, description="Whether presentation is verified: 'true' or 'false'"
    )
    verified_msgs: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "auto_present",
        "auto_remove",
        "auto_verify",
        "by_format",
        "connection_id",
        "created_at",
        "error_msg",
        "initiator",
        "pres",
        "pres_ex_id",
        "pres_proposal",
        "pres_request",
        "role",
        "state",
        "thread_id",
        "trace",
        "updated_at",
        "verified",
        "verified_msgs",
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

    @field_validator("initiator")
    def initiator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["self", "external"]):
            raise ValueError("must be one of enum values ('self', 'external')")
        return value

    @field_validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["prover", "verifier"]):
            raise ValueError("must be one of enum values ('prover', 'verifier')")
        return value

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "proposal-sent",
                "proposal-received",
                "request-sent",
                "request-received",
                "presentation-sent",
                "presentation-received",
                "done",
                "abandoned",
                "deleted",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('proposal-sent', 'proposal-received', 'request-sent', 'request-received', 'presentation-sent', 'presentation-received', 'done', 'abandoned', 'deleted')"
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

    @field_validator("verified")
    def verified_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["true", "false"]):
            raise ValueError("must be one of enum values ('true', 'false')")
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
        """Create an instance of V20PresExRecord from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

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
        # override the default output from pydantic by calling `to_dict()` of by_format
        if self.by_format:
            _dict["by_format"] = self.by_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pres
        if self.pres:
            _dict["pres"] = self.pres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pres_proposal
        if self.pres_proposal:
            _dict["pres_proposal"] = self.pres_proposal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pres_request
        if self.pres_request:
            _dict["pres_request"] = self.pres_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20PresExRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_present": obj.get("auto_present"),
                "auto_remove": obj.get("auto_remove"),
                "auto_verify": obj.get("auto_verify"),
                "by_format": (
                    V20PresExRecordByFormat.from_dict(obj["by_format"])
                    if obj.get("by_format") is not None
                    else None
                ),
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "error_msg": obj.get("error_msg"),
                "initiator": obj.get("initiator"),
                "pres": (
                    V20Pres.from_dict(obj["pres"])
                    if obj.get("pres") is not None
                    else None
                ),
                "pres_ex_id": obj.get("pres_ex_id"),
                "pres_proposal": (
                    V20PresProposal.from_dict(obj["pres_proposal"])
                    if obj.get("pres_proposal") is not None
                    else None
                ),
                "pres_request": (
                    V20PresRequest.from_dict(obj["pres_request"])
                    if obj.get("pres_request") is not None
                    else None
                ),
                "role": obj.get("role"),
                "state": obj.get("state"),
                "thread_id": obj.get("thread_id"),
                "trace": obj.get("trace"),
                "updated_at": obj.get("updated_at"),
                "verified": obj.get("verified"),
                "verified_msgs": obj.get("verified_msgs"),
            }
        )
        return _obj
