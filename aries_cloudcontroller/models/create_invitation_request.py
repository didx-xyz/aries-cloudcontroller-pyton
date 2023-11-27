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
import re
from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CreateInvitationRequest(BaseModel):
    """
    CreateInvitationRequest
    """  # noqa: E501

    mediation_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Identifier for active mediation record to be used"
    )
    metadata: Optional[Union[str, Any]] = Field(
        default=None,
        description="Optional metadata to attach to the connection created with the invitation",
    )
    my_label: Optional[StrictStr] = Field(
        default=None, description="Optional label for connection invitation"
    )
    recipient_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of recipient keys"
    )
    routing_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of routing keys"
    )
    service_endpoint: Optional[StrictStr] = Field(
        default=None, description="Connection endpoint"
    )
    __properties: ClassVar[List[str]] = [
        "mediation_id",
        "metadata",
        "my_label",
        "recipient_keys",
        "routing_keys",
        "service_endpoint",
    ]

    @field_validator("mediation_id")
    def mediation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-4[a-fA-F0-9]{3}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}/"
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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CreateInvitationRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateInvitationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "mediation_id": obj.get("mediation_id"),
                "metadata": obj.get("metadata"),
                "my_label": obj.get("my_label"),
                "recipient_keys": obj.get("recipient_keys"),
                "routing_keys": obj.get("routing_keys"),
                "service_endpoint": obj.get("service_endpoint"),
            }
        )
        return _obj
