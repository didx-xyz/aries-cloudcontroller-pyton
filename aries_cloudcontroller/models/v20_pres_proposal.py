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
from typing import List, Optional

from pydantic import BaseModel, Field, StrictStr

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_pres_format import V20PresFormat

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class V20PresProposal(BaseModel):
    """
    V20PresProposal
    """

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    formats: List[V20PresFormat]
    proposalsattach: List[AttachDecorator] = Field(
        description="Attachment per acceptable format on corresponding identifier",
        alias="proposals~attach",
    )
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "comment",
        "formats",
        "proposals~attach",
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V20PresProposal from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in formats (list)
        _items = []
        if self.formats:
            for _item in self.formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict["formats"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in proposalsattach (list)
        _items = []
        if self.proposalsattach:
            for _item in self.proposalsattach:
                if _item:
                    _items.append(_item.to_dict())
            _dict["proposals~attach"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V20PresProposal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "comment": obj.get("comment"),
                "formats": [
                    V20PresFormat.from_dict(_item) for _item in obj.get("formats")
                ]
                if obj.get("formats") is not None
                else None,
                "proposals~attach": [
                    AttachDecorator.from_dict(_item)
                    for _item in obj.get("proposals~attach")
                ]
                if obj.get("proposals~attach") is not None
                else None,
            }
        )
        return _obj
