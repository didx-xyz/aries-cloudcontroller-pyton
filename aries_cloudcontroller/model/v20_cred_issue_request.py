# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20CredIssueRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredIssueRequest - a model defined in OpenAPI
        comment: Human-readable comment [Optional].
    """

    comment: Optional[str] = None

    def __init__(
        self,
        *,
        comment: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            comment=comment,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20CredIssueRequest.update_forward_refs()
