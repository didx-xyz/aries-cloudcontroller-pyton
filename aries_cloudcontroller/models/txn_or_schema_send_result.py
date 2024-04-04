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
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel
from typing_extensions import Self

from aries_cloudcontroller.models.schema_send_result import SchemaSendResult
from aries_cloudcontroller.models.transaction_record import TransactionRecord
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class TxnOrSchemaSendResult(BaseModel):
    """
    TxnOrSchemaSendResult
    """  # noqa: E501

    sent: Optional[SchemaSendResult] = None
    txn: Optional[TransactionRecord] = None
    __properties: ClassVar[List[str]] = ["sent", "txn"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TxnOrSchemaSendResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sent
        if self.sent:
            _dict["sent"] = self.sent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of txn
        if self.txn:
            _dict["txn"] = self.txn.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TxnOrSchemaSendResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "sent": (
                    SchemaSendResult.from_dict(obj.get("sent"))
                    if obj.get("sent") is not None
                    else None
                ),
                "txn": (
                    TransactionRecord.from_dict(obj.get("txn"))
                    if obj.get("txn") is not None
                    else None
                ),
            }
        )
        return _obj
