# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401


class VCRecord(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    VCRecord - a model defined in OpenAPI
        contexts: The contexts of this VCRecord [Optional].
        cred_tags: The cred_tags of this VCRecord [Optional].
        cred_value: (JSON-serializable) credential value [Optional].
        expanded_types: The expanded_types of this VCRecord [Optional].
        given_id: Credential identifier [Optional].
        issuer_id: Issuer identifier [Optional].
        proof_types: The proof_types of this VCRecord [Optional].
        record_id: Record identifier [Optional].
        schema_ids: The schema_ids of this VCRecord [Optional].
        subject_ids: The subject_ids of this VCRecord [Optional].
    """

    contexts: Optional[List[str]] = None
    cred_tags: Optional[Dict[str, str]] = None
    cred_value: Optional[Dict[str, Any]] = None
    expanded_types: Optional[List[str]] = None
    given_id: Optional[str] = None
    issuer_id: Optional[str] = None
    proof_types: Optional[List[str]] = None
    record_id: Optional[str] = None
    schema_ids: Optional[List[str]] = None
    subject_ids: Optional[List[str]] = None

    class Config:
        allow_population_by_field_name = True


VCRecord.update_forward_refs()
