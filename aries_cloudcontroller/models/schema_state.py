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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Self

from aries_cloudcontroller.models.anon_creds_schema import AnonCredsSchema
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class SchemaState(BaseModel):
    """
    SchemaState
    """  # noqa: E501

    var_schema: Optional[AnonCredsSchema] = Field(default=None, alias="schema")
    schema_id: Optional[StrictStr] = Field(
        default=None, description="Schema identifier"
    )
    state: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["schema", "schema_id", "state"]

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["finished", "failed", "action", "wait"]):
            raise ValueError(
                "must be one of enum values ('finished', 'failed', 'action', 'wait')"
            )
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
        """Create an instance of SchemaState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict["schema"] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SchemaState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "schema": (
                    AnonCredsSchema.from_dict(obj["schema"])
                    if obj.get("schema") is not None
                    else None
                ),
                "schema_id": obj.get("schema_id"),
                "state": obj.get("state"),
            }
        )
        return _obj
