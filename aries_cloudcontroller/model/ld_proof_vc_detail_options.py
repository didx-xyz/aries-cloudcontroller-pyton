# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.credential_status_options import (
    CredentialStatusOptions,
)


class LDProofVCDetailOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LDProofVCDetailOptions - a model defined in OpenAPI
        proof_type: The proof type used for the proof. Should match suites registered in the Linked Data Cryptographic Suite Registry.
        challenge: A challenge to include in the proof. SHOULD be provided by the requesting party of the credential (&#x3D;holder) [Optional].
        created: The date and time of the proof (with a maximum accuracy in seconds). Defaults to current system time [Optional].
        credential_status: The credential status mechanism to use for the credential. Omitting the property indicates the issued credential will not include a credential status [Optional].
        domain: The intended domain of validity for the proof [Optional].
        proof_purpose: The proof purpose used for the proof. Should match proof purposes registered in the Linked Data Proofs Specification [Optional].
    """

    proof_type: str = Field(..., alias="proofType")
    challenge: Optional[str] = None
    created: Optional[str] = None
    credential_status: Optional[CredentialStatusOptions] = Field(
        None, alias="credentialStatus"
    )
    domain: Optional[str] = None
    proof_purpose: Optional[str] = Field(None, alias="proofPurpose")

    def __init__(
        self,
        *,
        proof_type: str,
        challenge: Optional[str] = None,
        created: Optional[str] = None,
        credential_status: Optional[CredentialStatusOptions] = None,
        domain: Optional[str] = None,
        proof_purpose: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            challenge=challenge,
            created=created,
            credential_status=credential_status,
            domain=domain,
            proof_purpose=proof_purpose,
            proof_type=proof_type,
            **kwargs,
        )

    @validator("created")
    def created_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created does not match regex pattern ('{pattern}')"
            )
        return value


LDProofVCDetailOptions.update_forward_refs()
