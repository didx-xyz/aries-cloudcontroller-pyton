# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.attachment_def import AttachmentDef


class InvitationCreateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InvitationCreateRequest - a model defined in OpenAPI
        alias: Alias for connection [Optional].
        attachments: Optional invitation attachments [Optional].
        handshake_protocols: The handshake_protocols of this InvitationCreateRequest [Optional].
        mediation_id: Identifier for active mediation record to be used [Optional].
        metadata: Optional metadata to attach to the connection created with the invitation [Optional].
        my_label: Label for connection invitation [Optional].
        use_public_did: Whether to use public DID in invitation [Optional].
    """

    alias: Optional[str] = None
    attachments: Optional[List[AttachmentDef]] = None
    handshake_protocols: Optional[List[str]] = None
    mediation_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    my_label: Optional[str] = None
    use_public_did: Optional[bool] = None

    def __init__(
        self,
        *,
        alias: Optional[str] = None,
        attachments: Optional[List[AttachmentDef]] = None,
        handshake_protocols: Optional[List[str]] = None,
        mediation_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        my_label: Optional[str] = None,
        use_public_did: Optional[bool] = None,
        **kwargs,
    ):
        super().__init__(
            alias=alias,
            attachments=attachments,
            handshake_protocols=handshake_protocols,
            mediation_id=mediation_id,
            metadata=metadata,
            my_label=my_label,
            use_public_did=use_public_did,
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


InvitationCreateRequest.update_forward_refs()