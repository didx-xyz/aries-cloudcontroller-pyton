# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_proof_req_attr_spec import IndyProofReqAttrSpec
from aries_cloudcontroller.model.indy_proof_req_pred_spec import IndyProofReqPredSpec
from aries_cloudcontroller.model.indy_proof_request_non_revoked import (
    IndyProofRequestNonRevoked,
)


class IndyProofRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofRequest - a model defined in OpenAPI
        name: Proof request name [Optional].
        non_revoked: The non_revoked of this IndyProofRequest [Optional].
        nonce: Nonce [Optional].
        requested_attributes: Requested attribute specifications of proof request [Optional].
        requested_predicates: Requested predicate specifications of proof request [Optional].
        version: Proof request version [Optional].
    """

    name: Optional[str] = None
    non_revoked: Optional[IndyProofRequestNonRevoked] = None
    nonce: Optional[str] = None
    requested_attributes: Optional[Dict[str, IndyProofReqAttrSpec]] = None
    requested_predicates: Optional[Dict[str, IndyProofReqPredSpec]] = None
    version: Optional[str] = None

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        non_revoked: Optional[IndyProofRequestNonRevoked] = None,
        nonce: Optional[str] = None,
        requested_attributes: Optional[Dict[str, IndyProofReqAttrSpec]] = None,
        requested_predicates: Optional[Dict[str, IndyProofReqPredSpec]] = None,
        version: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            non_revoked=non_revoked,
            nonce=nonce,
            requested_attributes=requested_attributes,
            requested_predicates=requested_predicates,
            version=version,
            **kwargs,
        )

    @validator("nonce")
    def nonce_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[1-9][0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of nonce does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("version")
    def version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of version does not match regex pattern ('{pattern}')"
            )
        return value


IndyProofRequest.update_forward_refs()