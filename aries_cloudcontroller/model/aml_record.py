# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class AMLRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AMLRecord - a model defined in OpenAPI
        aml: The aml of this AMLRecord [Optional].
        aml_context: The aml_context of this AMLRecord [Optional].
        version: The version of this AMLRecord [Optional].
    """

    aml: Optional[Dict[str, str]] = None
    aml_context: Optional[str] = Field(None, alias="amlContext")
    version: Optional[str] = None

    def __init__(
        self,
        *,
        aml: Optional[Dict[str, str]] = None,
        aml_context: Optional[str] = None,
        version: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            aml=aml,
            aml_context=aml_context,
            version=version,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


AMLRecord.update_forward_refs()
