# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.v20_pres_format import V20PresFormat


class V20PresProposal(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresProposal - a model defined in OpenAPI
        formats: The formats of this V20PresProposal.
        proposalsattach: Attachment per acceptable format on corresponding identifier.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
    """

    formats: List[V20PresFormat]
    proposalsattach: List[AttachDecorator] = Field(..., alias="proposals~attach")
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None

    def __init__(
        self,
        *,
        formats: List[V20PresFormat] = None,
        proposalsattach: List[AttachDecorator] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            formats=formats,
            proposalsattach=proposalsattach,
            **kwargs,
        )


V20PresProposal.update_forward_refs()
