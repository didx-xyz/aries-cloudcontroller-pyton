# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field, StrictStr

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Disclosures(BaseModel):
    """
    Disclosures
    """

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    disclosures: List[Union[str, Any]] = Field(
        description="List of protocol or goal_code descriptors"
    )
    __properties: ClassVar[List[str]] = ["@id", "@type", "disclosures"]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Disclosures from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "type",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of Disclosures from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "disclosures": obj.get("disclosures"),
            }
        )
        return _obj
