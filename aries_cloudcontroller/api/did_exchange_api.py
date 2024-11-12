# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.1.1b3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from typing import Any, Dict, List, Optional, Tuple, Union

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient, RequestSerialized
from aries_cloudcontroller.models.conn_record import ConnRecord
from aries_cloudcontroller.models.didx_reject_request import DIDXRejectRequest
from aries_cloudcontroller.models.didx_request import DIDXRequest


class DidExchangeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def accept_invitation(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        use_did: Annotated[
            Optional[StrictStr],
            Field(description="The DID to use to for this connection"),
        ] = None,
        use_did_method: Annotated[
            Optional[StrictStr],
            Field(
                description="The DID method to use to generate a DID for this connection"
            ),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConnRecord:
        """Accept a stored connection invitation


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param use_did: The DID to use to for this connection
        :type use_did: str
        :param use_did_method: The DID method to use to generate a DID for this connection
        :type use_did_method: str
        ...
        """  # noqa: E501

        _param = self._accept_invitation_serialize(
            conn_id=conn_id,
            my_endpoint=my_endpoint,
            my_label=my_label,
            use_did=use_did,
            use_did_method=use_did_method,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _accept_invitation_serialize(
        self,
        conn_id,
        my_endpoint,
        my_label,
        use_did,
        use_did_method,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
        # process the query parameters
        if my_endpoint is not None:

            _query_params.append(("my_endpoint", my_endpoint))

        if my_label is not None:

            _query_params.append(("my_label", my_label))

        if use_did is not None:

            _query_params.append(("use_did", use_did))

        if use_did_method is not None:

            _query_params.append(("use_did_method", use_did_method))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/didexchange/{conn_id}/accept-invitation",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def accept_request(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        use_public_did: Annotated[
            Optional[StrictBool],
            Field(description="Use public DID for this connection"),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConnRecord:
        """Accept a stored connection request


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param use_public_did: Use public DID for this connection
        :type use_public_did: bool
        ...
        """  # noqa: E501

        _param = self._accept_request_serialize(
            conn_id=conn_id,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
            use_public_did=use_public_did,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _accept_request_serialize(
        self,
        conn_id,
        mediation_id,
        my_endpoint,
        use_public_did,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
        # process the query parameters
        if mediation_id is not None:

            _query_params.append(("mediation_id", mediation_id))

        if my_endpoint is not None:

            _query_params.append(("my_endpoint", my_endpoint))

        if use_public_did is not None:

            _query_params.append(("use_public_did", use_public_did))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/didexchange/{conn_id}/accept-request",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def create_request(
        self,
        their_public_did: Annotated[
            str,
            Field(
                strict=True,
                description="Qualified public DID to which to request connection",
            ),
        ],
        alias: Annotated[
            Optional[StrictStr], Field(description="Alias for connection")
        ] = None,
        auto_accept: Annotated[
            Optional[StrictBool],
            Field(description="Auto-accept connection (defaults to configuration)"),
        ] = None,
        goal: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message"
            ),
        ] = None,
        goal_code: Annotated[
            Optional[StrictStr],
            Field(
                description="A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message"
            ),
        ] = None,
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        my_label: Annotated[
            Optional[StrictStr], Field(description="Label for connection request")
        ] = None,
        protocol: Annotated[
            Optional[StrictStr],
            Field(description="Which DID Exchange Protocol version to use"),
        ] = None,
        use_did: Annotated[
            Optional[StrictStr],
            Field(description="The DID to use to for this connection"),
        ] = None,
        use_did_method: Annotated[
            Optional[StrictStr],
            Field(
                description="The DID method to use to generate a DID for this connection"
            ),
        ] = None,
        use_public_did: Annotated[
            Optional[StrictBool],
            Field(description="Use public DID for this connection"),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConnRecord:
        """Create and send a request against public DID's implicit invitation


        :param their_public_did: Qualified public DID to which to request connection (required)
        :type their_public_did: str
        :param alias: Alias for connection
        :type alias: str
        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param goal: A self-attested string that the receiver may want to display to the user about the context-specific goal of the out-of-band message
        :type goal: str
        :param goal_code: A self-attested code the receiver may want to display to the user or use in automatically deciding what to do with the out-of-band message
        :type goal_code: str
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param my_label: Label for connection request
        :type my_label: str
        :param protocol: Which DID Exchange Protocol version to use
        :type protocol: str
        :param use_did: The DID to use to for this connection
        :type use_did: str
        :param use_did_method: The DID method to use to generate a DID for this connection
        :type use_did_method: str
        :param use_public_did: Use public DID for this connection
        :type use_public_did: bool
        ...
        """  # noqa: E501

        _param = self._create_request_serialize(
            their_public_did=their_public_did,
            alias=alias,
            auto_accept=auto_accept,
            goal=goal,
            goal_code=goal_code,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
            my_label=my_label,
            protocol=protocol,
            use_did=use_did,
            use_did_method=use_did_method,
            use_public_did=use_public_did,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_request_serialize(
        self,
        their_public_did,
        alias,
        auto_accept,
        goal,
        goal_code,
        mediation_id,
        my_endpoint,
        my_label,
        protocol,
        use_did,
        use_did_method,
        use_public_did,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if their_public_did is not None:

            _query_params.append(("their_public_did", their_public_did))

        if alias is not None:

            _query_params.append(("alias", alias))

        if auto_accept is not None:

            _query_params.append(("auto_accept", auto_accept))

        if goal is not None:

            _query_params.append(("goal", goal))

        if goal_code is not None:

            _query_params.append(("goal_code", goal_code))

        if mediation_id is not None:

            _query_params.append(("mediation_id", mediation_id))

        if my_endpoint is not None:

            _query_params.append(("my_endpoint", my_endpoint))

        if my_label is not None:

            _query_params.append(("my_label", my_label))

        if protocol is not None:

            _query_params.append(("protocol", protocol))

        if use_did is not None:

            _query_params.append(("use_did", use_did))

        if use_did_method is not None:

            _query_params.append(("use_did_method", use_did_method))

        if use_public_did is not None:

            _query_params.append(("use_public_did", use_public_did))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/didexchange/create-request",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def receive_request(
        self,
        alias: Annotated[
            Optional[StrictStr], Field(description="Alias for connection")
        ] = None,
        auto_accept: Annotated[
            Optional[StrictBool],
            Field(description="Auto-accept connection (defaults to configuration)"),
        ] = None,
        mediation_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Identifier for active mediation record to be used"),
        ] = None,
        my_endpoint: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="My URL endpoint"),
        ] = None,
        body: Optional[DIDXRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConnRecord:
        """(Deprecated) Receive request against public DID's implicit invitation


        :param alias: Alias for connection
        :type alias: str
        :param auto_accept: Auto-accept connection (defaults to configuration)
        :type auto_accept: bool
        :param mediation_id: Identifier for active mediation record to be used
        :type mediation_id: str
        :param my_endpoint: My URL endpoint
        :type my_endpoint: str
        :param body:
        :type body: DIDXRequest
        ...
        """  # noqa: E501
        warnings.warn(
            "POST /didexchange/receive-request is deprecated.", DeprecationWarning
        )

        _param = self._receive_request_serialize(
            alias=alias,
            auto_accept=auto_accept,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _receive_request_serialize(
        self,
        alias,
        auto_accept,
        mediation_id,
        my_endpoint,
        body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if alias is not None:

            _query_params.append(("alias", alias))

        if auto_accept is not None:

            _query_params.append(("auto_accept", auto_accept))

        if mediation_id is not None:

            _query_params.append(("mediation_id", mediation_id))

        if my_endpoint is not None:

            _query_params.append(("my_endpoint", my_endpoint))

        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/didexchange/receive-request",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    async def reject(
        self,
        conn_id: Annotated[StrictStr, Field(description="Connection identifier")],
        body: Optional[DIDXRejectRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ConnRecord:
        """Abandon or reject a DID Exchange


        :param conn_id: Connection identifier (required)
        :type conn_id: str
        :param body:
        :type body: DIDXRejectRequest
        ...
        """  # noqa: E501

        _param = self._reject_serialize(
            conn_id=conn_id,
            body=body,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "ConnRecord",
        }
        response_data = await self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _reject_serialize(
        self,
        conn_id,
        body,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if conn_id is not None:
            _path_params["conn_id"] = conn_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if body is not None:
            _body_params = body

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                ["application/json"]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/didexchange/{conn_id}/reject",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
