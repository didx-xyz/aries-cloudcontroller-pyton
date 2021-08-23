# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_cred_filter_ld_proof import V20CredFilterLDProof


class V20CredRequestFree(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredRequestFree - a model defined in OpenAPI
        connection_id: Connection identifier.
        filter: Credential specification criteria by format.
        auto_remove: Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting) [Optional].
        comment: Human-readable comment [Optional].
        holder_did: Holder DID to substitute for the credentialSubject.id [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    connection_id: str
    filter: V20CredFilterLDProof
    auto_remove: Optional[bool] = None
    comment: Optional[str] = None
    holder_did: Optional[str] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        connection_id: str = None,
        filter: V20CredFilterLDProof = None,
        auto_remove: Optional[bool] = None,
        comment: Optional[str] = None,
        holder_did: Optional[str] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            auto_remove=auto_remove,
            comment=comment,
            connection_id=connection_id,
            filter=filter,
            holder_did=holder_did,
            trace=trace,
            **kwargs,
        )


V20CredRequestFree.update_forward_refs()