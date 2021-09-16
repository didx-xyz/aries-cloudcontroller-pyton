# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential import Credential
from aries_cloudcontroller.model.ld_proof_vc_detail_options import (
    LDProofVCDetailOptions,
)


class LDProofVCDetail(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LDProofVCDetail - a model defined in OpenAPI
        credential: Detail of the JSON-LD Credential to be issued.
        options: Options for specifying how the linked data proof is created..
    """

    credential: Credential
    options: LDProofVCDetailOptions

    def __init__(
        self,
        *,
        credential: Credential = None,
        options: LDProofVCDetailOptions = None,
        **kwargs,
    ):
        super().__init__(
            credential=credential,
            options=options,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


LDProofVCDetail.update_forward_refs()
