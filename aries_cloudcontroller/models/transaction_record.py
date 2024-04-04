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
from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class TransactionRecord(BaseModel):
    """
    TransactionRecord
    """  # noqa: E501

    type: Optional[StrictStr] = Field(
        default=None, description="Transaction type", alias="_type"
    )
    connection_id: Optional[StrictStr] = Field(
        default=None,
        description="The connection identifier for this particular transaction record",
    )
    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    endorser_write_txn: Optional[StrictBool] = Field(
        default=None,
        description="If True, Endorser will write the transaction after endorsing it",
    )
    formats: Optional[List[Dict[str, StrictStr]]] = None
    messages_attach: Optional[List[Union[str, Any]]] = None
    meta_data: Optional[Union[str, Any]] = None
    signature_request: Optional[List[Union[str, Any]]] = None
    signature_response: Optional[List[Union[str, Any]]] = None
    state: Optional[StrictStr] = Field(default=None, description="Current record state")
    thread_id: Optional[StrictStr] = Field(
        default=None, description="Thread Identifier"
    )
    timing: Optional[Union[str, Any]] = None
    trace: Optional[StrictBool] = Field(
        default=None,
        description="Record trace information, based on agent configuration",
    )
    transaction_id: Optional[StrictStr] = Field(
        default=None, description="Transaction identifier"
    )
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "_type",
        "connection_id",
        "created_at",
        "endorser_write_txn",
        "formats",
        "messages_attach",
        "meta_data",
        "signature_request",
        "signature_response",
        "state",
        "thread_id",
        "timing",
        "trace",
        "transaction_id",
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
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionRecord from a JSON string"""
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
        """Create an instance of TransactionRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "_type": obj.get("_type"),
                "connection_id": obj.get("connection_id"),
                "created_at": obj.get("created_at"),
                "endorser_write_txn": obj.get("endorser_write_txn"),
                "formats": obj.get("formats"),
                "messages_attach": obj.get("messages_attach"),
                "meta_data": obj.get("meta_data"),
                "signature_request": obj.get("signature_request"),
                "signature_response": obj.get("signature_response"),
                "state": obj.get("state"),
                "thread_id": obj.get("thread_id"),
                "timing": obj.get("timing"),
                "trace": obj.get("trace"),
                "transaction_id": obj.get("transaction_id"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
