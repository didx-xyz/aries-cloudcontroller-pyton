# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v10_presentation_exchange import (
    V10PresentationExchange,
)


class V10PresentationExchangeList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V10PresentationExchangeList - a model defined in OpenAPI
        results: Aries RFC 37 v1.0 presentation exchange records [Optional].
    """

    results: Optional[List[V10PresentationExchange]] = None

    def __init__(
        self,
        *,
        results: Optional[List[V10PresentationExchange]] = None,
        **kwargs,
    ):
        super().__init__(
            results=results,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V10PresentationExchangeList.update_forward_refs()
