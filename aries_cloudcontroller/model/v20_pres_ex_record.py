# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_pres import V20Pres
from aries_cloudcontroller.model.v20_pres_ex_record_by_format import (
    V20PresExRecordByFormat,
)
from aries_cloudcontroller.model.v20_pres_proposal import V20PresProposal
from aries_cloudcontroller.model.v20_pres_request import V20PresRequest


class V20PresExRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresExRecord - a model defined in OpenAPI
        auto_present: Prover choice to auto-present proof as verifier requests [Optional].
        auto_verify: Verifier choice to auto-verify proof presentation [Optional].
        by_format: Attachment content by format for proposal, request, and presentation [Optional].
        connection_id: Connection identifier [Optional].
        created_at: Time of record creation [Optional].
        error_msg: Error message [Optional].
        initiator: Present-proof exchange initiator: self or external [Optional].
        pres: Presentation message [Optional].
        pres_ex_id: Presentation exchange identifier [Optional].
        pres_proposal: Presentation proposal message [Optional].
        pres_request: Presentation request message [Optional].
        role: Present-proof exchange role: prover or verifier [Optional].
        state: Present-proof exchange state [Optional].
        thread_id: Thread identifier [Optional].
        trace: Record trace information, based on agent configuration [Optional].
        updated_at: Time of last record update [Optional].
        verified: Whether presentation is verified: &#39;true&#39; or &#39;false&#39; [Optional].
        verified_msgs: The verified_msgs of this V20PresExRecord [Optional].
    """

    auto_present: Optional[bool] = None
    auto_verify: Optional[bool] = None
    by_format: Optional[V20PresExRecordByFormat] = None
    connection_id: Optional[str] = None
    created_at: Optional[str] = None
    error_msg: Optional[str] = None
    initiator: Optional[Literal["self", "external"]] = None
    pres: Optional[V20Pres] = None
    pres_ex_id: Optional[str] = None
    pres_proposal: Optional[V20PresProposal] = None
    pres_request: Optional[V20PresRequest] = None
    role: Optional[Literal["prover", "verifier"]] = None
    state: Optional[
        Literal[
            "proposal-sent",
            "proposal-received",
            "request-sent",
            "request-received",
            "presentation-sent",
            "presentation-received",
            "done",
            "abandoned",
        ]
    ] = None
    thread_id: Optional[str] = None
    trace: Optional[bool] = None
    updated_at: Optional[str] = None
    verified: Optional[Literal["true", "false"]] = None
    verified_msgs: Optional[List[str]] = None

    def __init__(
        self,
        *,
        auto_present: Optional[bool] = None,
        auto_verify: Optional[bool] = None,
        by_format: Optional[V20PresExRecordByFormat] = None,
        connection_id: Optional[str] = None,
        created_at: Optional[str] = None,
        error_msg: Optional[str] = None,
        initiator: Optional[Literal["self", "external"]] = None,
        pres: Optional[V20Pres] = None,
        pres_ex_id: Optional[str] = None,
        pres_proposal: Optional[V20PresProposal] = None,
        pres_request: Optional[V20PresRequest] = None,
        role: Optional[Literal["prover", "verifier"]] = None,
        state: Optional[
            Literal[
                "proposal-sent",
                "proposal-received",
                "request-sent",
                "request-received",
                "presentation-sent",
                "presentation-received",
                "done",
                "abandoned",
            ]
        ] = None,
        thread_id: Optional[str] = None,
        trace: Optional[bool] = None,
        updated_at: Optional[str] = None,
        verified: Optional[Literal["true", "false"]] = None,
        verified_msgs: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(
            auto_present=auto_present,
            auto_verify=auto_verify,
            by_format=by_format,
            connection_id=connection_id,
            created_at=created_at,
            error_msg=error_msg,
            initiator=initiator,
            pres=pres,
            pres_ex_id=pres_ex_id,
            pres_proposal=pres_proposal,
            pres_request=pres_request,
            role=role,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
            verified=verified,
            verified_msgs=verified_msgs,
            **kwargs,
        )

    @validator("created_at")
    def created_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of created_at does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("updated_at")
    def updated_at_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of updated_at does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


V20PresExRecord.update_forward_refs()
