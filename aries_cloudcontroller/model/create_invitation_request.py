# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class CreateInvitationRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateInvitationRequest - a model defined in OpenAPI
        mediation_id: Identifier for active mediation record to be used [Optional].
        metadata: Optional metadata to attach to the connection created with the invitation [Optional].
        my_label: Optional label for connection invitation [Optional].
        recipient_keys: List of recipient keys [Optional].
        routing_keys: List of routing keys [Optional].
        service_endpoint: Connection endpoint [Optional].
    """

    mediation_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    my_label: Optional[str] = None
    recipient_keys: Optional[List[str]] = None
    routing_keys: Optional[List[str]] = None
    service_endpoint: Optional[str] = None

    def __init__(
        self,
        *,
        mediation_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        my_label: Optional[str] = None,
        recipient_keys: Optional[List[str]] = None,
        routing_keys: Optional[List[str]] = None,
        service_endpoint: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            mediation_id=mediation_id,
            metadata=metadata,
            my_label=my_label,
            recipient_keys=recipient_keys,
            routing_keys=routing_keys,
            service_endpoint=service_endpoint,
            **kwargs,
        )

    @validator("mediation_id")
    def mediation_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of mediation_id does not match regex pattern ('{pattern}')"
            )
        return value


CreateInvitationRequest.update_forward_refs()