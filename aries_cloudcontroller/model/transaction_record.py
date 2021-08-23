# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class TransactionRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TransactionRecord - a model defined in OpenAPI
        type: Transaction type [Optional].
        connection_id: The connection identifier for thie particular transaction record [Optional].
        created_at: Time of record creation [Optional].
        endorser_write_txn: If True, Endorser will write the transaction after endorsing it [Optional].
        formats: The formats of this TransactionRecord [Optional].
        messages_attach: The messages_attach of this TransactionRecord [Optional].
        signature_request: The signature_request of this TransactionRecord [Optional].
        signature_response: The signature_response of this TransactionRecord [Optional].
        state: Current record state [Optional].
        thread_id: Thread Identifier [Optional].
        timing: The timing of this TransactionRecord [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        transaction_id: Transaction identifier [Optional].
        updated_at: Time of last record update [Optional].
    """

    type: Optional[str] = Field(None, alias="_type")
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    endorser_write_txn: Optional[bool] = None
    formats: Optional[List[Dict[str, str]]] = None
    messages_attach: Optional[List[Dict]] = None
    signature_request: Optional[List[Dict]] = None
    signature_response: Optional[List[Dict]] = None
    state: Optional[str] = None
    thread_id: Optional[str] = None
    timing: Optional[Dict[str, Any]] = None
    trace: Optional[bool] = None
    transaction_id: Optional[str] = None
    updated_at: Optional[str] = None

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        connection_id: Optional[str] = None,
        created_at: Optional[str] = None,
        endorser_write_txn: Optional[bool] = None,
        formats: Optional[List[Dict[str, str]]] = None,
        messages_attach: Optional[List[Dict]] = None,
        signature_request: Optional[List[Dict]] = None,
        signature_response: Optional[List[Dict]] = None,
        state: Optional[str] = None,
        thread_id: Optional[str] = None,
        timing: Optional[Dict[str, Any]] = None,
        trace: Optional[bool] = None,
        transaction_id: Optional[str] = None,
        updated_at: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            type=type,
            connection_id=connection_id,
            created_at=created_at,
            endorser_write_txn=endorser_write_txn,
            formats=formats,
            messages_attach=messages_attach,
            signature_request=signature_request,
            signature_response=signature_response,
            state=state,
            thread_id=thread_id,
            timing=timing,
            trace=trace,
            transaction_id=transaction_id,
            updated_at=updated_at,
            **kwargs,
        )

    @validator("created_at")
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value


TransactionRecord.update_forward_refs()
