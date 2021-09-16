# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class MenuFormParam(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MenuFormParam - a model defined in OpenAPI
        name: Menu parameter name.
        title: Menu parameter title.
        default: Default parameter value [Optional].
        description: Additional descriptive text for menu form parameter [Optional].
        required: Whether parameter is required [Optional].
        type: Menu form parameter input type [Optional].
    """

    name: str
    title: str
    default: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    type: Optional[str] = None

    def __init__(
        self,
        *,
        name: str = None,
        title: str = None,
        default: Optional[str] = None,
        description: Optional[str] = None,
        required: Optional[bool] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            default=default,
            description=description,
            name=name,
            required=required,
            title=title,
            type=type,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


MenuFormParam.update_forward_refs()
