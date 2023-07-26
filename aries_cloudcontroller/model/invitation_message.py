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
        accept: List of mime type in order of preference [Optional].
        goal: A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message [Optional].
        goal_code: A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message [Optional].
        handshake_protocols: The handshake_protocols of this InvitationMessage [Optional].
        image_url: Optional image URL for out-of-band invitation [Optional].
        label: Optional label [Optional].
        requestsattach: Optional request attachment [Optional].
        services: The services of this InvitationMessage [Optional].
    """

    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    accept: Optional[List[str]] = None
    goal: Optional[str] = None
    goal_code: Optional[str] = None
    handshake_protocols: Optional[List[str]] = None
    image_url: Optional[str] = Field(None, alias="imageUrl")
    label: Optional[str] = None
    requestsattach: Optional[List[AttachDecorator]] = Field(
        None, alias="requests~attach"
    )
    services: Optional[List[Union[Dict, str]]] = None

    class Config:
        allow_population_by_field_name = True


InvitationMessage.update_forward_refs()
