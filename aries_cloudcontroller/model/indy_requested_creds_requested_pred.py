# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class IndyRequestedCredsRequestedPred(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyRequestedCredsRequestedPred - a model defined in OpenAPI
        cred_id: Wallet credential identifier (typically but not necessarily a UUID).
        timestamp: Epoch timestamp of interest for non-revocation proof [Optional].
    """

    cred_id: str
    timestamp: Optional[int] = None

    def __init__(
        self,
        *,
        cred_id: str = None,
        timestamp: Optional[int] = None,
        **kwargs,
    ):
        super().__init__(
            cred_id=cred_id,
            timestamp=timestamp,
            **kwargs,
        )

    @validator("timestamp")
    def timestamp_max(cls, value):
        # Property is optional
        if value is None:
            return

        if value > -1:
            raise ValueError(f"timestamp must be less than -1, currently {value}")
        return value

    @validator("timestamp")
    def timestamp_min(cls, value):
        # Property is optional
        if value is None:
            return

        if value < 0:
            raise ValueError(f"timestamp must be greater than 0, currently {value}")
        return value


IndyRequestedCredsRequestedPred.update_forward_refs()