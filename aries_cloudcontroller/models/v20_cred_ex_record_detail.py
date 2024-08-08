# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0rc6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field
from typing_extensions import Self

from aries_cloudcontroller.models.v20_cred_ex_record import V20CredExRecord
from aries_cloudcontroller.models.v20_cred_ex_record_indy import V20CredExRecordIndy
from aries_cloudcontroller.models.v20_cred_ex_record_ld_proof import (
    V20CredExRecordLDProof,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20CredExRecordDetail(BaseModel):
    """
    V20CredExRecordDetail
    """  # noqa: E501

    cred_ex_record: Optional[V20CredExRecord] = Field(
        default=None, description="Credential exchange record"
    )
    indy: Optional[V20CredExRecordIndy] = None
    ld_proof: Optional[V20CredExRecordLDProof] = None
    vc_di: Optional[V20CredExRecord] = None
    __properties: ClassVar[List[str]] = ["cred_ex_record", "indy", "ld_proof", "vc_di"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V20CredExRecordDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cred_ex_record
        if self.cred_ex_record:
            _dict["cred_ex_record"] = self.cred_ex_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indy
        if self.indy:
            _dict["indy"] = self.indy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ld_proof
        if self.ld_proof:
            _dict["ld_proof"] = self.ld_proof.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vc_di
        if self.vc_di:
            _dict["vc_di"] = self.vc_di.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20CredExRecordDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cred_ex_record": (
                    V20CredExRecord.from_dict(obj["cred_ex_record"])
                    if obj.get("cred_ex_record") is not None
                    else None
                ),
                "indy": (
                    V20CredExRecordIndy.from_dict(obj["indy"])
                    if obj.get("indy") is not None
                    else None
                ),
                "ld_proof": (
                    V20CredExRecordLDProof.from_dict(obj["ld_proof"])
                    if obj.get("ld_proof") is not None
                    else None
                ),
                "vc_di": (
                    V20CredExRecord.from_dict(obj["vc_di"])
                    if obj.get("vc_di") is not None
                    else None
                ),
            }
        )
        return _obj
