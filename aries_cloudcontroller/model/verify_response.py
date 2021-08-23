# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class VerifyResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VerifyResponse - a model defined in OpenAPI
        valid: The valid of this VerifyResponse.
        error: Error text [Optional].
    """

    valid: bool
    error: Optional[str] = None

    def __init__(
        self,
        *,
        valid: bool = None,
        error: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            error=error,
            valid=valid,
            **kwargs,
        )


VerifyResponse.update_forward_refs()
