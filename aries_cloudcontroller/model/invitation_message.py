# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator


class InvitationMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InvitationMessage - a model defined in OpenAPI
        id: Message identifier [Optional].
        type: Message type [Optional].
        handshake_protocols: The handshake_protocols of this InvitationMessage [Optional].
        label: Optional label [Optional].
        requestsattach: Optional request attachment [Optional].
        services: The services of this InvitationMessage [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    handshake_protocols: Optional[List[str]] = None
    label: Optional[str] = None
    requestsattach: Optional[List[AttachDecorator]] = Field(
        None, alias="requests~attach"
    )
    services: Optional[List[Dict]] = None

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        handshake_protocols: Optional[List[str]] = None,
        label: Optional[str] = None,
        requestsattach: Optional[List[AttachDecorator]] = None,
        services: Optional[List[Dict]] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            handshake_protocols=handshake_protocols,
            label=label,
            requestsattach=requestsattach,
            services=services,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


InvitationMessage.update_forward_refs()
