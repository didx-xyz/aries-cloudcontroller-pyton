# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.wallet_record import WalletRecord


class WalletList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    WalletList - a model defined in OpenAPI
        results: List of wallet records [Optional].
    """

    results: Optional[List[WalletRecord]] = None

    class Config:
        allow_population_by_field_name = True


WalletList.update_forward_refs()
