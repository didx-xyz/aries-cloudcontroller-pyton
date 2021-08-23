# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator import AttachDecorator
from aries_cloudcontroller.model.v20_cred_format import V20CredFormat


class V20CredIssue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredIssue - a model defined in OpenAPI
        credentialsattach: Credential attachments.
        formats: Acceptable attachment formats.
        id: Message identifier [Optional].
        type: Message type [Optional].
        comment: Human-readable comment [Optional].
        replacement_id: Issuer-unique identifier to coordinate credential replacement [Optional].
    """

    credentialsattach: List[AttachDecorator] = Field(..., alias="credentials~attach")
    formats: List[V20CredFormat]
    id: Optional[str] = Field(None, alias="@id")
    type: Optional[str] = Field(None, alias="@type")
    comment: Optional[str] = None
    replacement_id: Optional[str] = None

    def __init__(
        self,
        *,
        credentialsattach: List[AttachDecorator] = None,
        formats: List[V20CredFormat] = None,
        id: Optional[str] = None,
        type: Optional[str] = None,
        comment: Optional[str] = None,
        replacement_id: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            type=type,
            comment=comment,
            credentialsattach=credentialsattach,
            formats=formats,
            replacement_id=replacement_id,
            **kwargs,
        )


V20CredIssue.update_forward_refs()
