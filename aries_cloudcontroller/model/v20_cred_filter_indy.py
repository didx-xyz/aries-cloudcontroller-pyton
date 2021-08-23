# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class V20CredFilterIndy(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    V20CredFilterIndy - a model defined in OpenAPI
        cred_def_id: Credential definition identifier [Optional].
        issuer_did: Credential issuer DID [Optional].
        schema_id: Schema identifier [Optional].
        schema_issuer_did: Schema issuer DID [Optional].
        schema_name: Schema name [Optional].
        schema_version: Schema version [Optional].
    """

    cred_def_id: Optional[str] = None
    issuer_did: Optional[str] = None
    schema_id: Optional[str] = None
    schema_issuer_did: Optional[str] = None
    schema_name: Optional[str] = None
    schema_version: Optional[str] = None

    def __init__(
        self,
        *,
        cred_def_id: Optional[str] = None,
        issuer_did: Optional[str] = None,
        schema_id: Optional[str] = None,
        schema_issuer_did: Optional[str] = None,
        schema_name: Optional[str] = None,
        schema_version: Optional[str] = None,
        **kwargs,
    ):
        super().__init__(
            cred_def_id=cred_def_id,
            issuer_did=issuer_did,
            schema_id=schema_id,
            schema_issuer_did=schema_issuer_did,
            schema_name=schema_name,
            schema_version=schema_version,
            **kwargs,
        )

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("issuer_did")
    def issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_issuer_did")
    def schema_issuer_did_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_issuer_did does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_version")
    def schema_version_pattern(cls, value):
        # Property is optional
        if value is None:
            return

        pattern = r"^[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_version does not match regex pattern ('{pattern}')"
            )
        return value


V20CredFilterIndy.update_forward_refs()
