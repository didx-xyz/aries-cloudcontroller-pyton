# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_pres_ex_record import V20PresExRecord


class V20PresExRecordList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresExRecordList - a model defined in OpenAPI
        results: Presentation exchange records [Optional].
    """

    results: Optional[List[V20PresExRecord]] = None

    def __init__(
        self,
        *,
        results: Optional[List[V20PresExRecord]] = None,
        **kwargs,
    ):
        super().__init__(
            results=results,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20PresExRecordList.update_forward_refs()
