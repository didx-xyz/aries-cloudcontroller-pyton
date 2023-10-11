# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Tuple

from pydantic import Field, StrictBool, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient
from aries_cloudcontroller.api_response import ApiResponse
from aries_cloudcontroller.exceptions import ApiTypeError
from aries_cloudcontroller.models.schema_get_result import SchemaGetResult
from aries_cloudcontroller.models.schema_send_request import SchemaSendRequest
from aries_cloudcontroller.models.schemas_created_result import SchemasCreatedResult
from aries_cloudcontroller.models.txn_or_schema_send_result import TxnOrSchemaSendResult


class SchemaApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def get_created_schemas(
        self,
        schema_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema identifier"),
        ] = None,
        schema_issuer_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema issuer DID"),
        ] = None,
        schema_name: Annotated[
            Optional[StrictStr], Field(description="Schema name")
        ] = None,
        schema_version: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema version"),
        ] = None,
        **kwargs,
    ) -> SchemasCreatedResult:
        """Search for matching schema that agent originated  # noqa: E501


        :param schema_id: Schema identifier
        :type schema_id: str
        :param schema_issuer_did: Schema issuer DID
        :type schema_issuer_did: str
        :param schema_name: Schema name
        :type schema_name: str
        :param schema_version: Schema version
        :type schema_version: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SchemasCreatedResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_created_schemas_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_created_schemas_with_http_info.raw_function(
            schema_id,
            schema_issuer_did,
            schema_name,
            schema_version,
            **kwargs,
        )

    @validate_call
    async def get_created_schemas_with_http_info(
        self,
        schema_id: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema identifier"),
        ] = None,
        schema_issuer_did: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema issuer DID"),
        ] = None,
        schema_name: Annotated[
            Optional[StrictStr], Field(description="Schema name")
        ] = None,
        schema_version: Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(description="Schema version"),
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        """Search for matching schema that agent originated  # noqa: E501


        :param schema_id: Schema identifier
        :type schema_id: str
        :param schema_issuer_did: Schema issuer DID
        :type schema_issuer_did: str
        :param schema_name: Schema name
        :type schema_name: str
        :param schema_version: Schema version
        :type schema_version: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SchemasCreatedResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            "schema_id",
            "schema_issuer_did",
            "schema_name",
            "schema_version",
        ]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_created_schemas" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("schema_id") is not None:  # noqa: E501
            _query_params.append(("schema_id", _params["schema_id"]))

        if _params.get("schema_issuer_did") is not None:  # noqa: E501
            _query_params.append(("schema_issuer_did", _params["schema_issuer_did"]))

        if _params.get("schema_name") is not None:  # noqa: E501
            _query_params.append(("schema_name", _params["schema_name"]))

        if _params.get("schema_version") is not None:  # noqa: E501
            _query_params.append(("schema_version", _params["schema_version"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "SchemasCreatedResult",
        }

        return await self.api_client.call_api(
            "/schemas/created",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def get_schema(
        self,
        schema_id: Annotated[str, Field(strict=True, description="Schema identifier")],
        **kwargs,
    ) -> SchemaGetResult:
        """Gets a schema from the ledger  # noqa: E501


        :param schema_id: Schema identifier (required)
        :type schema_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SchemaGetResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_schema_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_schema_with_http_info.raw_function(
            schema_id,
            **kwargs,
        )

    @validate_call
    async def get_schema_with_http_info(
        self,
        schema_id: Annotated[str, Field(strict=True, description="Schema identifier")],
        **kwargs,
    ) -> ApiResponse:
        """Gets a schema from the ledger  # noqa: E501


        :param schema_id: Schema identifier (required)
        :type schema_id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SchemaGetResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["schema_id"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schema" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["schema_id"] is not None:
            _path_params["schema_id"] = _params["schema_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "SchemaGetResult",
        }

        return await self.api_client.call_api(
            "/schemas/{schema_id}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def publish_schema(
        self,
        conn_id: Annotated[
            Optional[StrictStr], Field(description="Connection identifier")
        ] = None,
        create_transaction_for_endorser: Annotated[
            Optional[StrictBool],
            Field(description="Create Transaction For Endorser's signature"),
        ] = None,
        body: Optional[SchemaSendRequest] = None,
        **kwargs,
    ) -> TxnOrSchemaSendResult:
        """Sends a schema to the ledger  # noqa: E501


        :param conn_id: Connection identifier
        :type conn_id: str
        :param create_transaction_for_endorser: Create Transaction For Endorser's signature
        :type create_transaction_for_endorser: bool
        :param body:
        :type body: SchemaSendRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TxnOrSchemaSendResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the publish_schema_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.publish_schema_with_http_info.raw_function(
            conn_id,
            create_transaction_for_endorser,
            body,
            **kwargs,
        )

    @validate_call
    async def publish_schema_with_http_info(
        self,
        conn_id: Annotated[
            Optional[StrictStr], Field(description="Connection identifier")
        ] = None,
        create_transaction_for_endorser: Annotated[
            Optional[StrictBool],
            Field(description="Create Transaction For Endorser's signature"),
        ] = None,
        body: Optional[SchemaSendRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Sends a schema to the ledger  # noqa: E501


        :param conn_id: Connection identifier
        :type conn_id: str
        :param create_transaction_for_endorser: Create Transaction For Endorser's signature
        :type create_transaction_for_endorser: bool
        :param body:
        :type body: SchemaSendRequest
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TxnOrSchemaSendResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["conn_id", "create_transaction_for_endorser", "body"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_schema" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("conn_id") is not None:  # noqa: E501
            _query_params.append(("conn_id", _params["conn_id"]))

        if _params.get("create_transaction_for_endorser") is not None:  # noqa: E501
            _query_params.append(
                (
                    "create_transaction_for_endorser",
                    _params["create_transaction_for_endorser"],
                )
            )

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params["body"] is not None:
            _body_params = _params["body"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "TxnOrSchemaSendResult",
        }

        return await self.api_client.call_api(
            "/schemas",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_call
    async def write_record(
        self,
        schema_id: Annotated[str, Field(strict=True, description="Schema identifier")],
        **kwargs,
    ) -> SchemaGetResult:
        """Writes a schema non-secret record to the wallet  # noqa: E501


        :param schema_id: Schema identifier (required)
        :type schema_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SchemaGetResult
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the write_record_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.write_record_with_http_info.raw_function(
            schema_id,
            **kwargs,
        )

    @validate_call
    async def write_record_with_http_info(
        self,
        schema_id: Annotated[str, Field(strict=True, description="Schema identifier")],
        **kwargs,
    ) -> ApiResponse:
        """Writes a schema non-secret record to the wallet  # noqa: E501


        :param schema_id: Schema identifier (required)
        :type schema_id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(SchemaGetResult, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["schema_id"]
        _all_params.extend(
            [
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method write_record" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["schema_id"] is not None:
            _path_params["schema_id"] = _params["schema_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ["AuthorizationHeader"]  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "SchemaGetResult",
        }

        return await self.api_client.call_api(
            "/schemas/{schema_id}/write_record",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )