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

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SubmissionRequirements(BaseModel):
    """
    SubmissionRequirements
    """  # noqa: E501

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

        if value not in set(["all", "pick"]):
            raise ValueError("must be one of enum values ('all', 'pick')")
        return value

    model_config = DEFAULT_PYDANTIC_MODEL_CONFIG

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SubmissionRequirements from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in from_nested (list)
        _items = []
        if self.from_nested:
            for _item in self.from_nested:
                if _item:
                    _items.append(_item.to_dict())
            _dict["from_nested"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubmissionRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "count": obj.get("count"),
                "from": obj.get("from"),
                "from_nested": (
                    [
                        SubmissionRequirements.from_dict(_item)
                        for _item in obj["from_nested"]
                    ]
                    if obj.get("from_nested") is not None
                    else None
                ),
                "max": obj.get("max"),
                "min": obj.get("min"),
                "name": obj.get("name"),
                "purpose": obj.get("purpose"),
                "rule": obj.get("rule"),
            }
        )
        return _obj


# TODO: Rewrite to not use raise_errors
SubmissionRequirements.model_rebuild(raise_errors=False)
