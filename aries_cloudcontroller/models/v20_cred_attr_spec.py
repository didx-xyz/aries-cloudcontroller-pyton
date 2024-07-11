# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0rc4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20CredAttrSpec(BaseModel):
    """
    V20CredAttrSpec
    """  # noqa: E501

    mime_type: Optional[StrictStr] = Field(
        default=None,
        description="MIME type: omit for (null) default",
        alias="mime-type",
    )
    name: StrictStr = Field(description="Attribute name")
    value: StrictStr = Field(
        description="Attribute value: base64-encode if MIME type is present"
    )
    __properties: ClassVar[List[str]] = ["mime-type", "name", "value"]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V20CredAttrSpec from a JSON string"""
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
        # set to None if mime_type (nullable) is None
        # and model_fields_set contains the field
        if self.mime_type is None and "mime_type" in self.model_fields_set:
            _dict["mime-type"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20CredAttrSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "mime-type": obj.get("mime-type"),
                "name": obj.get("name"),
                "value": obj.get("value"),
            }
        )
        return _obj
