# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class SubmissionRequirements(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubmissionRequirements - a model defined in OpenAPI
        count: Count Value [Optional].
        from_: From [Optional].
        from_nested: The from_nested of this SubmissionRequirements [Optional].
        max: Max Value [Optional].
        min: Min Value [Optional].
        name: Name [Optional].
        purpose: Purpose [Optional].
        rule: Selection [Optional].
    """

    count: Optional[int] = None
    from_: Optional[str] = Field(None, alias="from")
    from_nested: Optional[List[SubmissionRequirements]] = None
    max: Optional[int] = None
    min: Optional[int] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    rule: Optional[Literal["all", "pick"]] = None

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        from_: Optional[str] = None,
        from_nested: Optional[List[SubmissionRequirements]] = None,
        max: Optional[int] = None,
        min: Optional[int] = None,
        name: Optional[str] = None,
        purpose: Optional[str] = None,
        rule: Optional[Literal["all", "pick"]] = None,
        **kwargs,
    ):
        super().__init__(
            count=count,
            from_=from_,
            from_nested=from_nested,
            max=max,
            min=min,
            name=name,
            purpose=purpose,
            rule=rule,
            **kwargs,
        )


SubmissionRequirements.update_forward_refs()