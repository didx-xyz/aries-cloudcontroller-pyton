# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator


class PresentationRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PresentationRequest - a model defined in OpenAPI
        request_presentationsattach: The request_presentationsattach of this PresentationRequest.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
    """

    request_presentationsattach: List[AttachDecorator] = Field(
        ..., alias="request_presentations~attach"
    )
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None

    def __init__(
        self,
        *,
        request_presentationsattach: List[AttachDecorator],
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            request_presentationsattach=request_presentationsattach,
            **kwargs,
        )


PresentationRequest.update_forward_refs()
