# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.rev_reg_result import RevRegResult
from aries_cloudcontroller.model.transaction_record import TransactionRecord


class TxnOrRevRegResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TxnOrRevRegResult - a model defined in OpenAPI
        sent: The sent of this TxnOrRevRegResult [Optional].
        txn: Revocation registry definition transaction to endorse [Optional].
    """

    sent: Optional[RevRegResult] = None
    txn: Optional[TransactionRecord] = None

    class Config:
        allow_population_by_field_name = True


TxnOrRevRegResult.update_forward_refs()
