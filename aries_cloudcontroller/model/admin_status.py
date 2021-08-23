# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class AdminStatus(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AdminStatus - a model defined in OpenAPI
        conductor: Conductor statistics [Optional].
        label: Default label [Optional].
        timing: Timing results [Optional].
        version: Version code [Optional].
    """

    conductor: Optional[Dict[str, Any]] = None
    label: Optional[str] = None
    timing: Optional[Dict[str, Any]] = None
    version: Optional[str] = None

    def __init__(
        self,
        *,
        conductor: Optional[Dict[str, Any]] = None,
        label: Optional[str] = None,
        timing: Optional[Dict[str, Any]] = None,
        version: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            conductor=conductor,
            label=label,
            timing=timing,
            version=version,
            **kwargs,
        )


AdminStatus.update_forward_refs()