# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class PublishRevocations(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PublishRevocations - a model defined in OpenAPI
        rrid2crid: Credential revocation ids by revocation registry id [Optional].
    """

    rrid2crid: Optional[Dict[str, List[str]]] = None

    def __init__(
        self,
        *,
        rrid2crid: Optional[Dict[str, List[str]]] = None,
        **kwargs,
    ):
        super().__init__(
            rrid2crid=rrid2crid,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


PublishRevocations.update_forward_refs()
