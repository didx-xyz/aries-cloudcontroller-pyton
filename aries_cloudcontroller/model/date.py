# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class Date(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Date - a model defined in OpenAPI
        expires_time: Expiry Date.
    """

    expires_time: datetime

    def __init__(
        self,
        *,
        expires_time: datetime = None,
        **kwargs,
    ):
        super().__init__(
            expires_time=expires_time,
            **kwargs,
        )


Date.update_forward_refs()