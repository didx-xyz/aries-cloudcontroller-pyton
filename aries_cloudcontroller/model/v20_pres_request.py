# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.v20_pres_format import V20PresFormat


class V20PresRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresRequest - a model defined in OpenAPI
        formats: The formats of this V20PresRequest.
        request_presentationsattach: Attachment per acceptable format on corresponding identifier.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        will_confirm: Whether verifier will send confirmation ack [Optional].
    """

    formats: List[V20PresFormat]
    request_presentationsattach: List[AttachDecorator] = Field(
        ..., alias="request_presentations~attach"
    )
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    will_confirm: Optional[bool] = None

    def __init__(
        self,
        *,
        formats: List[V20PresFormat] = None,
        request_presentationsattach: List[AttachDecorator] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        will_confirm: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            formats=formats,
            request_presentationsattach=request_presentationsattach,
            will_confirm=will_confirm,
            **kwargs,
        )


V20PresRequest.update_forward_refs()