# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.schema_input_descriptor import SchemaInputDescriptor


class SchemasInputDescriptorFilter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SchemasInputDescriptorFilter - a model defined in OpenAPI
        oneof_filter: oneOf [Optional].
        uri_groups: The uri_groups of this SchemasInputDescriptorFilter [Optional].
    """

    oneof_filter: Optional[bool] = None
    uri_groups: Optional[List[List[SchemaInputDescriptor]]] = None

    class Config:
        allow_population_by_field_name = True


SchemasInputDescriptorFilter.update_forward_refs()
