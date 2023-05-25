# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class SchemaInputDescriptor(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemaInputDescriptor - a model defined in OpenAPI
        required: Required [Optional].
        uri: URI [Optional].
    """

    required: Optional[bool] = None
    uri: Optional[str] = None

    class Config:
        allow_population_by_field_name = True


SchemaInputDescriptor.update_forward_refs()
