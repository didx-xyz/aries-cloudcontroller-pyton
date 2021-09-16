# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.model.v20_cred_ex_record_indy import V20CredExRecordIndy
from aries_cloudcontroller.model.v20_cred_ex_record_ld_proof import (
    V20CredExRecordLDProof,
)


class V20CredExRecordDetail(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredExRecordDetail - a model defined in OpenAPI
        cred_ex_record: Credential exchange record [Optional].
        indy: The indy of this V20CredExRecordDetail [Optional].
        ld_proof: The ld_proof of this V20CredExRecordDetail [Optional].
    """

    cred_ex_record: Optional[V20CredExRecord] = None
    indy: Optional[V20CredExRecordIndy] = None
    ld_proof: Optional[V20CredExRecordLDProof] = None

    def __init__(
        self,
        *,
        cred_ex_record: Optional[V20CredExRecord] = None,
        indy: Optional[V20CredExRecordIndy] = None,
        ld_proof: Optional[V20CredExRecordLDProof] = None,
        **kwargs,
    ):
        super().__init__(
            cred_ex_record=cred_ex_record,
            indy=indy,
            ld_proof=ld_proof,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20CredExRecordDetail.update_forward_refs()
