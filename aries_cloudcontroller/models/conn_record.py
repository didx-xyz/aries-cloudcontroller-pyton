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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ConnRecord(BaseModel):
    """
    ConnRecord
    """  # noqa: E501

    accept: Optional[StrictStr] = Field(
        default=None, description="Connection acceptance: manual or auto"
    )
    alias: Optional[StrictStr] = Field(
        default=None, description="Optional alias to apply to connection for later use"
    )
    connection_id: Optional[StrictStr] = Field(
        default=None, description="Connection identifier"
    )
    connection_protocol: Optional[StrictStr] = Field(
        default=None, description="Connection protocol used"
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    error_msg: Optional[StrictStr] = Field(default=None, description="Error message")
    inbound_connection_id: Optional[StrictStr] = Field(
        default=None, description="Inbound routing connection id to use"
    )
    invitation_key: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Public key for connection"
    )
    invitation_mode: Optional[StrictStr] = Field(
        default=None, description="Invitation mode"
    )
    invitation_msg_id: Optional[StrictStr] = Field(
        default=None, description="ID of out-of-band invitation message"
    )
    my_did: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Our DID for connection"
    )
    request_id: Optional[StrictStr] = Field(
        default=None, description="Connection request identifier"
    )
    rfc23_state: Optional[StrictStr] = Field(
        default=None, description="State per RFC 23"
    )
    routing_state: Optional[StrictStr] = Field(
        default=None, description="Routing state of connection"
    )
    state: Optional[StrictStr] = Field(default=None, description="Current record state")
    their_did: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Their DID for connection"
    )
    their_label: Optional[StrictStr] = Field(
        default=None, description="Their label for connection"
    )
    their_public_did: Optional[StrictStr] = Field(
        default=None, description="Other agent's public DID for connection"
    )
    their_role: Optional[StrictStr] = Field(
        default=None, description="Their role in the connection protocol"
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "accept",
        "alias",
        "connection_id",
        "connection_protocol",
        "created_at",
        "error_msg",
        "inbound_connection_id",
        "invitation_key",
        "invitation_mode",
        "invitation_msg_id",
        "my_did",
        "request_id",
        "rfc23_state",
        "routing_state",
        "state",
        "their_did",
        "their_label",
        "their_public_did",
        "their_role",
        "updated_at",
    ]

    @field_validator("accept")
    def accept_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("manual", "auto"):
            raise ValueError("must be one of enum values ('manual', 'auto')")
        return value

    @field_validator("connection_protocol")
    def connection_protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("connections/1.0", "didexchange/1.0"):
            raise ValueError(
                "must be one of enum values ('connections/1.0', 'didexchange/1.0')"
            )
        return value

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

    @field_validator("invitation_key")
    def invitation_key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$/"
            )
        return value

    @field_validator("invitation_mode")
    def invitation_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("once", "multi", "static"):
            raise ValueError("must be one of enum values ('once', 'multi', 'static')")
        return value

    @field_validator("my_did")
    def my_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("routing_state")
    def routing_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("none", "request", "active", "error"):
            raise ValueError(
                "must be one of enum values ('none', 'request', 'active', 'error')"
            )
        return value

    @field_validator("their_did")
    def their_did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$/"
            )
        return value

    @field_validator("their_role")
    def their_role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("invitee", "requester", "inviter", "responder"):
            raise ValueError(
                "must be one of enum values ('invitee', 'requester', 'inviter', 'responder')"
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

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConnRecord from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "rfc23_state",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConnRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "accept": obj.get("accept"),
                "alias": obj.get("alias"),
                "connection_id": obj.get("connection_id"),
                "connection_protocol": obj.get("connection_protocol"),
                "created_at": obj.get("created_at"),
                "error_msg": obj.get("error_msg"),
                "inbound_connection_id": obj.get("inbound_connection_id"),
                "invitation_key": obj.get("invitation_key"),
                "invitation_mode": obj.get("invitation_mode"),
                "invitation_msg_id": obj.get("invitation_msg_id"),
                "my_did": obj.get("my_did"),
                "request_id": obj.get("request_id"),
                "rfc23_state": obj.get("rfc23_state"),
                "routing_state": obj.get("routing_state"),
                "state": obj.get("state"),
                "their_did": obj.get("their_did"),
                "their_label": obj.get("their_label"),
                "their_public_did": obj.get("their_public_did"),
                "their_role": obj.get("their_role"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
