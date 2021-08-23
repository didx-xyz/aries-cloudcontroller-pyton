# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attach_decorator_data1_jws import (
    AttachDecoratorData1JWS,
)
from aries_cloudcontroller.model.attach_decorator_data_jws_header import (
    AttachDecoratorDataJWSHeader,
)


class AttachDecoratorDataJWS(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AttachDecoratorDataJWS - a model defined in OpenAPI
        header: The header of this AttachDecoratorDataJWS [Optional].
        protected: protected JWS header [Optional].
        signature: signature [Optional].
        signatures: List of signatures [Optional].
    """

    header: Optional[AttachDecoratorDataJWSHeader] = None
    protected: Optional[str] = None
    signature: Optional[str] = None
    signatures: Optional[List[AttachDecoratorData1JWS]] = None

    def __init__(
        self,
        *,
        header: Optional[AttachDecoratorDataJWSHeader] = None,
        protected: Optional[str] = None,
        signature: Optional[str] = None,
        signatures: Optional[List[AttachDecoratorData1JWS]] = None,
        **kwargs,
    ):
        super().__init__(
            header=header,
            protected=protected,
            signature=signature,
            signatures=signatures,
            **kwargs,
        )

    @validator("protected")
    def protected_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[-_a-zA-Z0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of protected does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("signature")
    def signature_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[-_a-zA-Z0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of signature does not match regex pattern ('{pattern}')"
            )
        return value


AttachDecoratorDataJWS.update_forward_refs()