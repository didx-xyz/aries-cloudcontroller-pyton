# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class KeylistUpdateRule(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    KeylistUpdateRule - a model defined in OpenAPI
        action: Action for specific key.
        recipient_key: Key to remove or add.
    """

    action: Literal["add", "remove"]
    recipient_key: str

    def __init__(
        self,
        *,
        action: Literal["add", "remove"] = None,
        recipient_key: str = None,
        **kwargs,
    ):
        super().__init__(
            action=action,
            recipient_key=recipient_key,
            **kwargs,
        )

    @validator("recipient_key")
    def recipient_key_pattern(cls, value):

        pattern = (
            r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{43,44}$"
        )
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of recipient_key does not match regex pattern ('{pattern}')"
            )
        return value


KeylistUpdateRule.update_forward_refs()
