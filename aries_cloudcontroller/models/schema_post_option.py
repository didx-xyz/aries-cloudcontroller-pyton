# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SchemaPostOption(BaseModel):
    """
    SchemaPostOption
    """  # noqa: E501

    create_transaction_for_endorser: Optional[StrictBool] = Field(
        default=None,
        description="Create transaction for endorser (optional, default false). Use this for agents who don't specify an author role but want to create a transaction for an endorser to sign.",
    )
    endorser_connection_id: Optional[StrictStr] = Field(
        default=None,
        description="Connection identifier (optional) (this is an example). You can set this if you know the endorser's connection id you want to use. If not specified then the agent will attempt to find an endorser connection.",
    )
    __properties: ClassVar[List[str]] = [
        "create_transaction_for_endorser",
        "endorser_connection_id",
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
        """Create an instance of SchemaPostOption from a JSON string"""
        return cls.from_dict(orjson.loads(json_str))

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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaPostOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "create_transaction_for_endorser": obj.get(
                    "create_transaction_for_endorser"
                ),
                "endorser_connection_id": obj.get("endorser_connection_id"),
            }
        )
        return _obj
