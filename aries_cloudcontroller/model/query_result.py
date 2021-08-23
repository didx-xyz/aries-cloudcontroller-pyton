# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class QueryResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    QueryResult - a model defined in OpenAPI
        results: Query results keyed by protocol [Optional].
    """

    results: Optional[Dict[str, Any]] = None

    def __init__(
        self,
        *,
        results: Optional[Dict[str, Any]] = None,
        **kwargs,
    ):
        super().__init__(
            results=results,
            **kwargs,
        )


QueryResult.update_forward_refs()