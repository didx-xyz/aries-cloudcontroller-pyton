# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional, Union, Literal  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator, Field, Extra  # noqa: F401
from aries_cloudcontroller.model.indy_proof_req_pred_spec_non_revoked import (
    IndyProofReqPredSpecNonRevoked,
)


class IndyProofReqPredSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IndyProofReqPredSpec - a model defined in OpenAPI
        name: Attribute name.
        p_type: Predicate type (&#39;&lt;&#39;, &#39;&lt;&#x3D;&#39;, &#39;&gt;&#x3D;&#39;, or &#39;&gt;&#39;).
        p_value: Threshold value.
        non_revoked: The non_revoked of this IndyProofReqPredSpec [Optional].
        restrictions: If present, credential must satisfy one of given restrictions: specify schema_id, schema_issuer_did, schema_name, schema_version, issuer_did, cred_def_id, and/or attr::&lt;attribute-name&gt;::value where &lt;attribute-name&gt; represents a credential attribute name [Optional].
    """

    name: str
    p_type: Literal["&lt;", "&lt;&#x3D;", "&gt;&#x3D;", "&gt;"]
    p_value: int
    non_revoked: Optional[IndyProofReqPredSpecNonRevoked] = None
    restrictions: Optional[List[Dict[str, str]]] = None

    def __init__(
        self,
        *,
        name: str = None,
        p_type: Literal["&lt;", "&lt;&#x3D;", "&gt;&#x3D;", "&gt;"] = None,
        p_value: int = None,
        non_revoked: Optional[IndyProofReqPredSpecNonRevoked] = None,
        restrictions: Optional[List[Dict[str, str]]] = None,
        **kwargs,
    ):
        super().__init__(
            name=name,
            non_revoked=non_revoked,
            p_type=p_type,
            p_value=p_value,
            restrictions=restrictions,
            **kwargs,
        )


IndyProofReqPredSpec.update_forward_refs()