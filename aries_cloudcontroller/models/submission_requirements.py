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

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SubmissionRequirements(BaseModel):
    """
    SubmissionRequirements
    """

    count: Optional[StrictInt] = Field(default=None, description="Count Value")
    var_from: Optional[StrictStr] = Field(
        default=None, description="From", alias="from"
    )
    from_nested: Optional[List[SubmissionRequirements]] = None
    max: Optional[StrictInt] = Field(default=None, description="Max Value")
    min: Optional[StrictInt] = Field(default=None, description="Min Value")
    name: Optional[StrictStr] = Field(default=None, description="Name")
    purpose: Optional[StrictStr] = Field(default=None, description="Purpose")
    rule: Optional[StrictStr] = Field(default=None, description="Selection")
    __properties: ClassVar[List[str]] = [
        "count",
        "from",
        "from_nested",
        "max",
        "min",
        "name",
        "purpose",
        "rule",
    ]

    @field_validator("rule")
    def rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("all", "pick"):
            raise ValueError("must be one of enum values ('all', 'pick')")
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SubmissionRequirements from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in from_nested (list)
        _items = []
        if self.from_nested:
            for _item in self.from_nested:
                if _item:
                    _items.append(_item.to_dict())
            _dict["from_nested"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of SubmissionRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "count": obj.get("count"),
                "from": obj.get("from"),
                "from_nested": [
                    SubmissionRequirements.from_dict(_item)
                    for _item in obj.get("from_nested")
                ]
                if obj.get("from_nested") is not None
                else None,
                "max": obj.get("max"),
                "min": obj.get("min"),
                "name": obj.get("name"),
                "purpose": obj.get("purpose"),
                "rule": obj.get("rule"),
            }
        )
        return _obj


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # TODO: pydantic v2
    # SubmissionRequirements.model_rebuild()
    pass
