# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_key_correctness_proof import (
    IndyKeyCorrectnessProof,
)


class IndyCredAbstract(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyCredAbstract - a model defined in OpenAPI
        cred_def_id: Credential definition identifier.
        key_correctness_proof: Key correctness proof.
        nonce: Nonce in credential abstract.
        schema_id: Schema identifier.
    """

    cred_def_id: str
    key_correctness_proof: IndyKeyCorrectnessProof
    nonce: str
    schema_id: str

    def __init__(
        self,
        *,
        cred_def_id: str = None,
        key_correctness_proof: IndyKeyCorrectnessProof = None,
        nonce: str = None,
        schema_id: str = None,
        **kwargs,
    ):
        super().__init__(
            cred_def_id=cred_def_id,
            key_correctness_proof=key_correctness_proof,
            nonce=nonce,
            schema_id=schema_id,
            **kwargs,
        )

    @validator("cred_def_id")
    def cred_def_id_pattern(cls, value):

        pattern = r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+)):(.+)?$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of cred_def_id does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("nonce")
    def nonce_pattern(cls, value):

        pattern = r"^[0-9]*$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of nonce does not match regex pattern ('{pattern}')"
            )
        return value

    @validator("schema_id")
    def schema_id_pattern(cls, value):

        pattern = r"^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+$"
        if not re.match(pattern, value):
            raise ValueError(
                f"Value of schema_id does not match regex pattern ('{pattern}')"
            )
        return value

    class Config:
        allow_population_by_field_name = True


IndyCredAbstract.update_forward_refs()
