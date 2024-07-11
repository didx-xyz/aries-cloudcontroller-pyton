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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.models.v20_pres_format import V20PresFormat
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class V20PresRequest(BaseModel):
    """
    V20PresRequest
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    comment: Optional[StrictStr] = Field(
        default=None, description="Human-readable comment"
    )
    formats: List[V20PresFormat] = Field(description="Acceptable attachment formats")
    request_presentationsattach: List[AttachDecorator] = Field(
        description="Attachment per acceptable format on corresponding identifier",
        alias="request_presentations~attach",
    )
    will_confirm: Optional[StrictBool] = Field(
        default=None, description="Whether verifier will send confirmation ack"
    )
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "comment",
        "formats",
        "request_presentations~attach",
        "will_confirm",
    ]

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V20PresRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in formats (list)
        _items = []
        if self.formats:
            for _item in self.formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict["formats"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in request_presentationsattach (list)
        _items = []
        if self.request_presentationsattach:
            for _item in self.request_presentationsattach:
                if _item:
                    _items.append(_item.to_dict())
            _dict["request_presentations~attach"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V20PresRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "comment": obj.get("comment"),
                "formats": (
                    [V20PresFormat.from_dict(_item) for _item in obj["formats"]]
                    if obj.get("formats") is not None
                    else None
                ),
                "request_presentations~attach": (
                    [
                        AttachDecorator.from_dict(_item)
                        for _item in obj["request_presentations~attach"]
                    ]
                    if obj.get("request_presentations~attach") is not None
                    else None
                ),
                "will_confirm": obj.get("will_confirm"),
            }
        )
        return _obj
