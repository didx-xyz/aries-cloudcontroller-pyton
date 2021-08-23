# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.signature_options import SignatureOptions


class SignedDoc(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SignedDoc - a model defined in OpenAPI
        proof: Linked data proof.
    """

    proof: SignatureOptions

    def __init__(
        self,
        *,
        proof: SignatureOptions = None,
        **kwargs,
    ):
        super().__init__(
            proof=proof,
            **kwargs,
        )


SignedDoc.update_forward_refs()
