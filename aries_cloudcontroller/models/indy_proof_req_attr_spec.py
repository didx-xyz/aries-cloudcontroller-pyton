# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.indy_proof_req_attr_spec_non_revoked import (
    IndyProofReqAttrSpecNonRevoked,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class IndyProofReqAttrSpec(BaseModel):
    """
    IndyProofReqAttrSpec
    """  # noqa: E501

    name: Optional[StrictStr] = Field(default=None, description="Attribute name")
    names: Optional[List[StrictStr]] = Field(
        default=None, description="Attribute name group"
    )
    non_revoked: Optional[IndyProofReqAttrSpecNonRevoked] = None
    restrictions: Optional[List[Dict[str, StrictStr]]] = Field(
        default=None,
        description="If present, credential must satisfy one of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did, cred_def_id, and/or attr::<attribute-name>::value where <attribute-name> represents a credential attribute name",
    )
    __properties: ClassVar[List[str]] = ["name", "names", "non_revoked", "restrictions"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IndyProofReqAttrSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of non_revoked
        if self.non_revoked:
            _dict["non_revoked"] = self.non_revoked.to_dict()
        # set to None if non_revoked (nullable) is None
        # and model_fields_set contains the field
        if self.non_revoked is None and "non_revoked" in self.model_fields_set:
            _dict["non_revoked"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IndyProofReqAttrSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "names": obj.get("names"),
                "non_revoked": (
                    IndyProofReqAttrSpecNonRevoked.from_dict(obj["non_revoked"])
                    if obj.get("non_revoked") is not None
                    else None
                ),
                "restrictions": obj.get("restrictions"),
            }
        )
        return _obj
