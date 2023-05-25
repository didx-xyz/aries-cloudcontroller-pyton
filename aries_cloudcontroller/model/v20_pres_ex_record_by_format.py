# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20PresExRecordByFormat(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresExRecordByFormat - a model defined in OpenAPI
        pres: The pres of this V20PresExRecordByFormat [Optional].
        pres_proposal: The pres_proposal of this V20PresExRecordByFormat [Optional].
        pres_request: The pres_request of this V20PresExRecordByFormat [Optional].
    """

    pres: Optional[Dict[str, Any]] = None
    pres_proposal: Optional[Dict[str, Any]] = None
    pres_request: Optional[Dict[str, Any]] = None

    class Config:
        allow_population_by_field_name = True


V20PresExRecordByFormat.update_forward_refs()
