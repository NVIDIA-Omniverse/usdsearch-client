# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# coding: utf-8

"""
    USD Search and Asset Graph Search APIs

    # USD Search API Overview **USD Search API** is a collection of cloud-native microservices that enable developers, creators, and workflow specialists to efficiently search through vast collections of OpenUSD data, images, and other assets using natural language or image-based inputs. With these production-ready microservices, developers can deploy USD Search API onto their own infrastructure.  With USD Search API’s artificial intelligence (AI) features, you can quickly locate untagged and unstructured 3D data and digital assets, saving time navigating unstructured, untagged 3D data. USD Search API is capable of searching and indexing 3D asset databases, as well as navigating complex 3D scenes to perform spatial searches, without requiring manual tagging of assets. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr
from typing import Optional
from typing_extensions import Annotated
from usd_search_client.models.status_result import StatusResult

from usd_search_client.api_client import ApiClient, RequestSerialized
from usd_search_client.api_response import ApiResponse
from usd_search_client.rest import RESTResponseType


class IndexingStatusApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def get_asset_status_info_indexing_asset_status_get(
        self,
        url: Annotated[StrictStr, Field(description="Asset URL for which processing status needs to be retrieved")],
        return_asset_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata for the asset if set to True")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StatusResult:
        """Get Asset Status

        For each URL the service checks caches of all plugins that support processing this asset and reports the following information: * **indexing_status** [*not_found* / *in_sync* / *out_of_sync* ] - this parameter checks the difference between cached value of asset hash and the actual (up-to-date) asset hash from the storage backend.     * if these two values match - then the asset is considered to be up-to-date, in other words *in_sync*     * otherwise, the final version of the asset has not be processed yet.     * The *not_found* status is assigned in case the asset has never been processed. * **plugin_status_history** - is a list of last statuses that were assigned to the asset, while it was being processed. Each item of this list has the following structure:     * **status** [*ok* / *processing* / *failed_retries_exhausted* / other string] - shows whether the asset was         * *ok* - successfully processed         * *processing* - processing for the asset has started         * *failed_retries_exhausted* - processing of the asset failed and reached the retry limit         * any other string - indicates that that processing has failed with this message.     * **processing_timestamp** - the moment when the status was assigned     * **exception** - optional exception explanation  The service could additionally report asset metadata from the storage backend if **return_asset_metadata** flag is set to *True*.

        :param url: Asset URL for which processing status needs to be retrieved (required)
        :type url: str
        :param return_asset_metadata: Return metadata for the asset if set to True
        :type return_asset_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_asset_status_info_indexing_asset_status_get_serialize(
            url=url,
            return_asset_metadata=return_asset_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatusResult",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    async def get_asset_status_info_indexing_asset_status_get_with_http_info(
        self,
        url: Annotated[StrictStr, Field(description="Asset URL for which processing status needs to be retrieved")],
        return_asset_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata for the asset if set to True")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StatusResult]:
        """Get Asset Status

        For each URL the service checks caches of all plugins that support processing this asset and reports the following information: * **indexing_status** [*not_found* / *in_sync* / *out_of_sync* ] - this parameter checks the difference between cached value of asset hash and the actual (up-to-date) asset hash from the storage backend.     * if these two values match - then the asset is considered to be up-to-date, in other words *in_sync*     * otherwise, the final version of the asset has not be processed yet.     * The *not_found* status is assigned in case the asset has never been processed. * **plugin_status_history** - is a list of last statuses that were assigned to the asset, while it was being processed. Each item of this list has the following structure:     * **status** [*ok* / *processing* / *failed_retries_exhausted* / other string] - shows whether the asset was         * *ok* - successfully processed         * *processing* - processing for the asset has started         * *failed_retries_exhausted* - processing of the asset failed and reached the retry limit         * any other string - indicates that that processing has failed with this message.     * **processing_timestamp** - the moment when the status was assigned     * **exception** - optional exception explanation  The service could additionally report asset metadata from the storage backend if **return_asset_metadata** flag is set to *True*.

        :param url: Asset URL for which processing status needs to be retrieved (required)
        :type url: str
        :param return_asset_metadata: Return metadata for the asset if set to True
        :type return_asset_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_asset_status_info_indexing_asset_status_get_serialize(
            url=url,
            return_asset_metadata=return_asset_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatusResult",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        await response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    async def get_asset_status_info_indexing_asset_status_get_without_preload_content(
        self,
        url: Annotated[StrictStr, Field(description="Asset URL for which processing status needs to be retrieved")],
        return_asset_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata for the asset if set to True")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Asset Status

        For each URL the service checks caches of all plugins that support processing this asset and reports the following information: * **indexing_status** [*not_found* / *in_sync* / *out_of_sync* ] - this parameter checks the difference between cached value of asset hash and the actual (up-to-date) asset hash from the storage backend.     * if these two values match - then the asset is considered to be up-to-date, in other words *in_sync*     * otherwise, the final version of the asset has not be processed yet.     * The *not_found* status is assigned in case the asset has never been processed. * **plugin_status_history** - is a list of last statuses that were assigned to the asset, while it was being processed. Each item of this list has the following structure:     * **status** [*ok* / *processing* / *failed_retries_exhausted* / other string] - shows whether the asset was         * *ok* - successfully processed         * *processing* - processing for the asset has started         * *failed_retries_exhausted* - processing of the asset failed and reached the retry limit         * any other string - indicates that that processing has failed with this message.     * **processing_timestamp** - the moment when the status was assigned     * **exception** - optional exception explanation  The service could additionally report asset metadata from the storage backend if **return_asset_metadata** flag is set to *True*.

        :param url: Asset URL for which processing status needs to be retrieved (required)
        :type url: str
        :param return_asset_metadata: Return metadata for the asset if set to True
        :type return_asset_metadata: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_asset_status_info_indexing_asset_status_get_serialize(
            url=url,
            return_asset_metadata=return_asset_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "StatusResult",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_asset_status_info_indexing_asset_status_get_serialize(
        self,
        url,
        return_asset_metadata,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if url is not None:
            
            _query_params.append(('url', url))
            
        if return_asset_metadata is not None:
            
            _query_params.append(('return_asset_metadata', return_asset_metadata))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/info/indexing/asset/status',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


