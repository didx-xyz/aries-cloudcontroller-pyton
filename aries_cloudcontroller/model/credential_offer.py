# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.credential_preview import CredentialPreview


class CredentialOffer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CredentialOffer - a model defined in OpenAPI
        offersattach: The offersattach of this CredentialOffer.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        credential_preview: The credential_preview of this CredentialOffer [Optional].
    """

    offersattach: List[AttachDecorator] = Field(..., alias="offers~attach")
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    credential_preview: Optional[CredentialPreview] = None

    def __init__(
        self,
        *,
        offersattach: List[AttachDecorator] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        credential_preview: Optional[CredentialPreview] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            credential_preview=credential_preview,
            offersattach=offersattach,
            **kwargs,
        )


CredentialOffer.update_forward_refs()
