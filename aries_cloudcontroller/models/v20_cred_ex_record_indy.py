# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.10.2
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


class V20CredExRecordIndy(BaseModel):
    """
    V20CredExRecordIndy
    """  # noqa: E501

    created_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of record creation"
    )
    cred_ex_id: Optional[StrictStr] = Field(
        default=None,
        description="Corresponding v2.0 credential exchange record identifier",
    )
    cred_ex_indy_id: Optional[StrictStr] = Field(
        default=None, description="Record identifier"
    )
    cred_id_stored: Optional[StrictStr] = Field(
        default=None, description="Credential identifier stored in wallet"
    )
    cred_request_metadata: Optional[Union[str, Any]] = Field(
        default=None, description="Credential request metadata for indy holder"
    )
    cred_rev_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Credential revocation identifier within revocation registry",
    )
    rev_reg_id: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Revocation registry identifier"
    )
    state: Optional[StrictStr] = Field(default=None, description="Current record state")
    updated_at: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, description="Time of last record update"
    )
    __properties: ClassVar[List[str]] = [
        "created_at",
        "cred_ex_id",
        "cred_ex_indy_id",
        "cred_id_stored",
        "cred_request_metadata",
        "cred_rev_id",
        "rev_reg_id",
        "state",
        "updated_at",
    ]

    @field_validator("created_at")
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
            )
        return value

    @field_validator("cred_rev_id")
    def cred_rev_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[1-9][0-9]*$", value):
            raise ValueError(r"must validate the regular expression /^[1-9][0-9]*$/")
        return value

    @field_validator("rev_reg_id")
    def rev_reg_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):4:([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}):3:CL:(([1-9][0-9]*)|([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}:2:.+:[0-9.]+))(:.+)?:CL_ACCUM:(.+$)/"
            )
        return value

    @field_validator("updated_at")
    def updated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r"^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$",
            value,
        ):
            raise ValueError(
                r"must validate the regular expression /^\d{4}-\d\d-\d\d[T ]\d\d:\d\d(?:\:(?:\d\d(?:\.\d{1,6})?))?(?:[+-]\d\d:?\d\d|Z|)$/"
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
        """Create an instance of V20CredExRecordIndy from a JSON string"""
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
        """Create an instance of V20CredExRecordIndy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "created_at": obj.get("created_at"),
                "cred_ex_id": obj.get("cred_ex_id"),
                "cred_ex_indy_id": obj.get("cred_ex_indy_id"),
                "cred_id_stored": obj.get("cred_id_stored"),
                "cred_request_metadata": obj.get("cred_request_metadata"),
                "cred_rev_id": obj.get("cred_rev_id"),
                "rev_reg_id": obj.get("rev_reg_id"),
                "state": obj.get("state"),
                "updated_at": obj.get("updated_at"),
            }
        )
        return _obj
