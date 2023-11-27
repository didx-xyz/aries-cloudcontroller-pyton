# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictBool, StrictStr

from aries_cloudcontroller.models.v20_cred_filter_ld_proof import V20CredFilterLDProof
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V20CredRequestFree(BaseModel):
    """
    V20CredRequestFree
    """  # noqa: E501

    auto_remove: Optional[StrictBool] = Field(
        default=None,
        description="Whether to remove the credential exchange record on completion (overrides --preserve-exchange-records configuration setting)",
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    connection_id: StrictStr = Field(description="Connection identifier")
    filter: V20CredFilterLDProof
    holder_did: Optional[StrictStr] = Field(
        default=None,
        description="Holder DID to substitute for the credentialSubject.id",
    )
    trace: Optional[StrictBool] = Field(
        default=None, description="Whether to trace event (default false)"
    )
    __properties: ClassVar[List[str]] = [
        "auto_remove",
        "comment",
        "connection_id",
        "filter",
        "holder_did",
        "trace",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V20CredRequestFree from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict["filter"] = self.filter.to_dict()
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict["comment"] = None

        # set to None if holder_did (nullable) is None
        # and model_fields_set contains the field
        if self.holder_did is None and "holder_did" in self.model_fields_set:
            _dict["holder_did"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V20CredRequestFree from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "auto_remove": obj.get("auto_remove"),
                "comment": obj.get("comment"),
                "connection_id": obj.get("connection_id"),
                "filter": V20CredFilterLDProof.from_dict(obj.get("filter"))
                if obj.get("filter") is not None
                else None,
                "holder_did": obj.get("holder_did"),
                "trace": obj.get("trace"),
            }
        )
        return _obj
