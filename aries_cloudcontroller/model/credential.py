# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.linked_data_proof import LinkedDataProof


class Credential(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Credential - a model defined in OpenAPI
        context: The JSON-LD context of the credential.
        credential_subject: The credential_subject of this Credential.
        issuance_date: The issuance date.
        issuer: The JSON-LD Verifiable Credential Issuer. Either string of object with id field..
        type: The JSON-LD type of the credential.
        expiration_date: The expiration date [Optional].
        id: The id of this Credential [Optional].
        proof: The proof of the credential [Optional].
    """

    context: List[Dict] = Field(..., alias="@context")
    credential_subject: Dict[str, Any] = Field(..., alias="credentialSubject")
    issuance_date: str = Field(..., alias="issuanceDate")
    issuer: Dict[str, Any]
    type: List[str]
    expiration_date: Optional[str] = Field(None, alias="expirationDate")
    id: Optional[str] = None
    proof: Optional[LinkedDataProof] = None

    def __init__(
        self,
        *,
        context: List[Dict] = None,
        credential_subject: Dict[str, Any] = None,
        issuance_date: str = None,
        issuer: Dict[str, Any] = None,
        type: List[str] = None,
        expiration_date: Optional[str] = None,
        id: Optional[str] = None,
        proof: Optional[LinkedDataProof] = None,
        **kwargs,
    ):
        super().__init__(
            context=context,
            credential_subject=credential_subject,
            expiration_date=expiration_date,
            id=id,
            issuance_date=issuance_date,
            issuer=issuer,
            proof=proof,
            type=type,
            **kwargs,
        )

    @validator("expiration_date")
    def expiration_date_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of expiration_date does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("id")
    def id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"\w+:(\\/?\\/?)[^\s]+"
        if not re.match(pattern, value):
            raise ValueError(f"Value of id does not match regex pattern ('{pattern}')")
        return value

    @validator("issuance_date")
    def issuance_date_pattern(cls, value):

        pattern = r"^([0-9]{4})-([0-9]{2})-([0-9]{2})([Tt ]([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?)?(([Zz]|([+-])([0-9]{2}):([0-9]{2})))?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of issuance_date does not match regex pattern ('{pattern}')"
            )
        return value


Credential.update_forward_refs()