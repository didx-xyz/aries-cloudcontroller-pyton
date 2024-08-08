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

from pydantic import BaseModel, Field, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.models.menu_form_param import MenuFormParam
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class MenuForm(BaseModel):
    """
    MenuForm
    """  # noqa: E501

    description: Optional[StrictStr] = Field(
        default=None, description="Additional descriptive text for menu form"
    )
    params: Optional[List[MenuFormParam]] = Field(
        default=None, description="List of form parameters"
    )
    submit_label: Optional[StrictStr] = Field(
        default=None,
        description="Alternative label for form submit button",
        alias="submit-label",
    )
    title: Optional[StrictStr] = Field(default=None, description="Menu form title")
    __properties: ClassVar[List[str]] = [
        "description",
        "params",
        "submit-label",
        "title",
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
        """Create an instance of MenuForm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item in self.params:
                if _item:
                    _items.append(_item.to_dict())
            _dict["params"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MenuForm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "description": obj.get("description"),
                "params": (
                    [MenuFormParam.from_dict(_item) for _item in obj["params"]]
                    if obj.get("params") is not None
                    else None
                ),
                "submit-label": obj.get("submit-label"),
                "title": obj.get("title"),
            }
        )
        return _obj
