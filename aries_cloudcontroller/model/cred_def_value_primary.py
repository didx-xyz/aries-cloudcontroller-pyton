# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.generated import Generated


class CredDefValuePrimary(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredDefValuePrimary - a model defined in OpenAPI
        n: The n of this CredDefValuePrimary [Optional].
        r: The r of this CredDefValuePrimary [Optional].
        rctxt: The rctxt of this CredDefValuePrimary [Optional].
        s: The s of this CredDefValuePrimary [Optional].
        z: The z of this CredDefValuePrimary [Optional].
    """

    n: Optional[str] = None
    r: Optional[Generated] = None
    rctxt: Optional[str] = None
    s: Optional[str] = None
    z: Optional[str] = None

    def __init__(
        self,
        *,
        n: Optional[str] = None,
        r: Optional[Generated] = None,
        rctxt: Optional[str] = None,
        s: Optional[str] = None,
        z: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            n=n,
            r=r,
            rctxt=rctxt,
            s=s,
            z=z,
            **kwargs,
        )

    @validator("n")
    def n_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of n does not match regex pattern ('{pattern}')")
        return value

    @validator("rctxt")
    def rctxt_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of rctxt does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("s")
    def s_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of s does not match regex pattern ('{pattern}')")
        return value

    @validator("z")
    def z_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(f"Value of z does not match regex pattern ('{pattern}')")
        return value

    class Config:
        allow_population_by_field_name = True


CredDefValuePrimary.update_forward_refs()
