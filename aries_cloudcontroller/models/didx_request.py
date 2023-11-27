# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re
from typing import Any, ClassVar, Dict, List, Optional

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing_extensions import Annotated

from aries_cloudcontroller.models.attach_decorator import AttachDecorator
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class DIDXRequest(BaseModel):
    """
    DIDXRequest
    """  # noqa: E501

    id: Optional[StrictStr] = Field(
        default=None, description="Message identifier", alias="@id"
    )
    type: Optional[StrictStr] = Field(
        default=None, description="Message type", alias="@type"
    )
    did: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="DID of exchange"
    )
    did_docattach: Optional[AttachDecorator] = Field(
        default=None, alias="did_doc~attach"
    )
    goal: Optional[StrictStr] = Field(
        default=None,
        description="A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message",
    )
    goal_code: Optional[StrictStr] = Field(
        default=None,
        description="A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message",
    )
    label: StrictStr = Field(description="Label for DID exchange request")
    __properties: ClassVar[List[str]] = [
        "@id",
        "@type",
        "did",
        "did_doc~attach",
        "goal",
        "goal_code",
        "label",
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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DIDXRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "type",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of did_docattach
        if self.did_docattach:
            _dict["did_doc~attach"] = self.did_docattach.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DIDXRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "@id": obj.get("@id"),
                "@type": obj.get("@type"),
                "did": obj.get("did"),
                "did_doc~attach": AttachDecorator.from_dict(obj.get("did_doc~attach"))
                if obj.get("did_doc~attach") is not None
                else None,
                "goal": obj.get("goal"),
                "goal_code": obj.get("goal_code"),
                "label": obj.get("label"),
            }
        )
        return _obj
