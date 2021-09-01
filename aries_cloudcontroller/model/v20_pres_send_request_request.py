# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.v20_pres_request_by_format import (
    V20PresRequestByFormat,
)


class V20PresSendRequestRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20PresSendRequestRequest - a model defined in OpenAPI
        connection_id: Connection identifier.
        presentation_request: The presentation_request of this V20PresSendRequestRequest.
        comment: The comment of this V20PresSendRequestRequest [Optional].
        trace: Whether to trace event (default false) [Optional].
    """

    connection_id: str
    presentation_request: V20PresRequestByFormat
    comment: Optional[str] = None
    trace: Optional[bool] = None

    def __init__(
        self,
        *,
        connection_id: str = None,
        presentation_request: V20PresRequestByFormat = None,
        comment: Optional[str] = None,
        trace: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            comment=comment,
            connection_id=connection_id,
            presentation_request=presentation_request,
            trace=trace,
            **kwargs,
        )

    class Config:
        allow_population_by_field_name = True


V20PresSendRequestRequest.update_forward_refs()
