# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_attr_spec import V20CredAttrSpec


class V20CredPreview(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredPreview - a model defined in OpenAPI
        attributes: The attributes of this V20CredPreview.
        type: Message type identifier [Optional].
    """

    attributes: List[V20CredAttrSpec]
    type: Optional[str] = Field(None, alias="@type")

    def __init__(
        self,
        *,
        attributes: List[V20CredAttrSpec] = None,
        type: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            type=type,
            attributes=attributes,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20CredPreview.update_forward_refs()
