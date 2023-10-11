# coding: utf-8

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0.9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from typing import Dict, List, Optional, Tuple

from pydantic import Field, StrictStr, validate_call
from typing_extensions import Annotated

from aries_cloudcontroller.api_client import ApiClient
from aries_cloudcontroller.api_response import ApiResponse
from aries_cloudcontroller.exceptions import ApiTypeError
from aries_cloudcontroller.models.create_wallet_request import CreateWalletRequest
from aries_cloudcontroller.models.create_wallet_response import CreateWalletResponse
from aries_cloudcontroller.models.create_wallet_token_request import (
    CreateWalletTokenRequest,
)
from aries_cloudcontroller.models.create_wallet_token_response import (
    CreateWalletTokenResponse,
)
from aries_cloudcontroller.models.remove_wallet_request import RemoveWalletRequest
from aries_cloudcontroller.models.update_wallet_request import UpdateWalletRequest
from aries_cloudcontroller.models.wallet_list import WalletList
from aries_cloudcontroller.models.wallet_record import WalletRecord


class MultitenancyApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def create_wallet(
        self,
        body: Optional[CreateWalletRequest] = None,
        **kwargs,
    ) -> CreateWalletResponse:
        """Create a subwallet  # noqa: E501


        :param body:
        :type body: CreateWalletRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateWalletResponse
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the create_wallet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.create_wallet_with_http_info.raw_function(
            body,
            **kwargs,
        )

    @validate_call
    async def create_wallet_with_http_info(
        self,
        body: Optional[CreateWalletRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Create a subwallet  # noqa: E501


        :param body:
        :type body: CreateWalletRequest
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
        :rtype: tuple(CreateWalletResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["body"]
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
                    " to method create_wallet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            "200": "CreateWalletResponse",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallet",
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
    async def delete_wallet(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        body: Optional[RemoveWalletRequest] = None,
        **kwargs,
    ) -> object:
        """Remove a subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
        :param body:
        :type body: RemoveWalletRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the delete_wallet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.delete_wallet_with_http_info.raw_function(
            wallet_id,
            body,
            **kwargs,
        )

    @validate_call
    async def delete_wallet_with_http_info(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        body: Optional[RemoveWalletRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Remove a subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
        :param body:
        :type body: RemoveWalletRequest
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
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["wallet_id", "body"]
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
                    " to method delete_wallet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["wallet_id"] is not None:
            _path_params["wallet_id"] = _params["wallet_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            "200": "object",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallet/{wallet_id}/remove",
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
    async def get_auth_token(
        self,
        wallet_id: StrictStr,
        body: Optional[CreateWalletTokenRequest] = None,
        **kwargs,
    ) -> CreateWalletTokenResponse:
        """Get auth token for a subwallet  # noqa: E501


        :param wallet_id: (required)
        :type wallet_id: str
        :param body:
        :type body: CreateWalletTokenRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateWalletTokenResponse
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_auth_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_auth_token_with_http_info.raw_function(
            wallet_id,
            body,
            **kwargs,
        )

    @validate_call
    async def get_auth_token_with_http_info(
        self,
        wallet_id: StrictStr,
        body: Optional[CreateWalletTokenRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Get auth token for a subwallet  # noqa: E501


        :param wallet_id: (required)
        :type wallet_id: str
        :param body:
        :type body: CreateWalletTokenRequest
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
        :rtype: tuple(CreateWalletTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["wallet_id", "body"]
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
                    " to method get_auth_token" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["wallet_id"] is not None:
            _path_params["wallet_id"] = _params["wallet_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            "200": "CreateWalletTokenResponse",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallet/{wallet_id}/token",
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
    async def get_wallet(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        **kwargs,
    ) -> WalletRecord:
        """Get a single subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WalletRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_wallet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_wallet_with_http_info.raw_function(
            wallet_id,
            **kwargs,
        )

    @validate_call
    async def get_wallet_with_http_info(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        **kwargs,
    ) -> ApiResponse:
        """Get a single subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
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
        :rtype: tuple(WalletRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["wallet_id"]
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
                    " to method get_wallet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["wallet_id"] is not None:
            _path_params["wallet_id"] = _params["wallet_id"]

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
            "200": "WalletRecord",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallet/{wallet_id}",
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
    async def get_wallets(
        self,
        wallet_name: Annotated[
            Optional[StrictStr], Field(description="Wallet name")
        ] = None,
        **kwargs,
    ) -> WalletList:
        """Query subwallets  # noqa: E501


        :param wallet_name: Wallet name
        :type wallet_name: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WalletList
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the get_wallets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_wallets_with_http_info.raw_function(
            wallet_name,
            **kwargs,
        )

    @validate_call
    async def get_wallets_with_http_info(
        self,
        wallet_name: Annotated[
            Optional[StrictStr], Field(description="Wallet name")
        ] = None,
        **kwargs,
    ) -> ApiResponse:
        """Query subwallets  # noqa: E501


        :param wallet_name: Wallet name
        :type wallet_name: str
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
        :rtype: tuple(WalletList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["wallet_name"]
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
                    " to method get_wallets" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        if _params.get("wallet_name") is not None:  # noqa: E501
            _query_params.append(("wallet_name", _params["wallet_name"]))

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
            "200": "WalletList",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallets",
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
    async def update_wallet(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        body: Optional[UpdateWalletRequest] = None,
        **kwargs,
    ) -> WalletRecord:
        """Update a subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
        :param body:
        :type body: UpdateWalletRequest
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: WalletRecord
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            message = "Error! Please call the update_wallet_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.update_wallet_with_http_info.raw_function(
            wallet_id,
            body,
            **kwargs,
        )

    @validate_call
    async def update_wallet_with_http_info(
        self,
        wallet_id: Annotated[StrictStr, Field(description="Subwallet identifier")],
        body: Optional[UpdateWalletRequest] = None,
        **kwargs,
    ) -> ApiResponse:
        """Update a subwallet  # noqa: E501


        :param wallet_id: Subwallet identifier (required)
        :type wallet_id: str
        :param body:
        :type body: UpdateWalletRequest
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
        :rtype: tuple(WalletRecord, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["wallet_id", "body"]
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
                    " to method update_wallet" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params["wallet_id"] is not None:
            _path_params["wallet_id"] = _params["wallet_id"]

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
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
            "200": "WalletRecord",
        }

        return await self.api_client.call_api(
            "/multitenancy/wallet/{wallet_id}",
            "PUT",
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