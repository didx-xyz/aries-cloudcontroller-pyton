# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional, Set

import orjson
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated, Self

from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG


class ConnectionInvitation(BaseModel):
    """
    ConnectionInvitation
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    did: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="DID for connection invitation"
    )
    image_url: Optional[StrictStr] = Field(
        default=None,
        description="Optional image URL for connection invitation",
        alias="imageUrl",
    )
    label: Optional[StrictStr] = Field(
        default=None, description="Optional label for connection invitation"
    )
    recipient_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of recipient keys", alias="recipientKeys"
    )
    routing_keys: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None, description="List of routing keys", alias="routingKeys"
    )
    service_endpoint: Optional[StrictStr] = Field(
        default=None,
        description="Service endpoint at which to reach this agent",
        alias="serviceEndpoint",
    )
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "did",
        "imageUrl",
        "label",
        "recipientKeys",
        "routingKeys",
        "serviceEndpoint",
    ]

    @field_validator("did")
    def did_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+=[a-zA-Z0-9_.:%-]*)*)(\/[^#?]*)?([?][^#]*)?(\#.*)?$$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+=[a-zA-Z0-9_.:%-]*)*)(\/[^#?]*)?([?][^#]*)?(\#.*)?$$/"
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
        """Create an instance of ConnectionInvitation from a JSON string"""
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
        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict["imageUrl"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionInvitation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "did": obj.get("did"),
                "imageUrl": obj.get("imageUrl"),
                "label": obj.get("label"),
                "recipientKeys": obj.get("recipientKeys"),
                "routingKeys": obj.get("routingKeys"),
                "serviceEndpoint": obj.get("serviceEndpoint"),
            }
        )
        return _obj
