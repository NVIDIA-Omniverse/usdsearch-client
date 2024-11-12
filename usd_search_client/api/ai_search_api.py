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

    # USD Search API Overview **USD Search** is a versatile AI-powered search engine designed to enable comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (AWS S3 and Omniverse Nucleus server). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Search, USD Search extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional, Union
from typing_extensions import Annotated
from usd_search_client.models.deep_search_search_request import DeepSearchSearchRequest
from usd_search_client.models.search_result import SearchResult

from usd_search_client.api_client import ApiClient, RequestSerialized
from usd_search_client.api_response import ApiResponse
from usd_search_client.rest import RESTResponseType


class AISearchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def search_post_v2_deepsearch_search_post(
        self,
        deep_search_search_request: DeepSearchSearchRequest,
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
    ) -> List[SearchResult]:
        """Search Post

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as body parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param deep_search_search_request: (required)
        :type deep_search_search_request: DeepSearchSearchRequest
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

        _param = self._search_post_v2_deepsearch_search_post_serialize(
            deep_search_search_request=deep_search_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
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
    async def search_post_v2_deepsearch_search_post_with_http_info(
        self,
        deep_search_search_request: DeepSearchSearchRequest,
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
    ) -> ApiResponse[List[SearchResult]]:
        """Search Post

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as body parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param deep_search_search_request: (required)
        :type deep_search_search_request: DeepSearchSearchRequest
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

        _param = self._search_post_v2_deepsearch_search_post_serialize(
            deep_search_search_request=deep_search_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
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
    async def search_post_v2_deepsearch_search_post_without_preload_content(
        self,
        deep_search_search_request: DeepSearchSearchRequest,
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
        """Search Post

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as body parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param deep_search_search_request: (required)
        :type deep_search_search_request: DeepSearchSearchRequest
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

        _param = self._search_post_v2_deepsearch_search_post_serialize(
            deep_search_search_request=deep_search_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_post_v2_deepsearch_search_post_serialize(
        self,
        deep_search_search_request,
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
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if deep_search_search_request is not None:
            _body_params = deep_search_search_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'APIKeyHeader', 
            'HTTPBasic', 
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/search',
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




    @validate_call
    async def search_v2_deepsearch_search_get(
        self,
        description: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1024)]], Field(description="Conduct text-based searches powered by AI")] = None,
        image_similarity_search: Annotated[Optional[List[StrictStr]], Field(description="Perform similarity searches based on a list of images")] = None,
        file_name: Annotated[Optional[StrictStr], Field(description="Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_file_name: Annotated[Optional[StrictStr], Field(description="Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_include: Annotated[Optional[StrictStr], Field(description="Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_exclude: Annotated[Optional[StrictStr], Field(description="Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        created_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created after a specified date")] = None,
        created_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created before a specified date")] = None,
        modified_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified after a specified date")] = None,
        modified_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified before a specified date")] = None,
        file_size_greater_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files larger than a specific size")] = None,
        file_size_less_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files smaller than a specific size")] = None,
        created_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_created_by: Annotated[Optional[StrictStr], Field(description="Exclude assets created by a specific user from the results")] = None,
        modified_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_modified_by: Annotated[Optional[StrictStr], Field(description="Exclude assets modified by a specific user from the results")] = None,
        similarity_threshold: Annotated[Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]], Field(description="Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.")] = None,
        cutoff_threshold: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Set the cutoff threshold for embedding-based searches")] = None,
        search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        search_in_scene: Annotated[Optional[StrictStr], Field(description="Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.")] = None,
        filter_by_properties: Annotated[Optional[StrictStr], Field(description="Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_x: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum X axis dimension of the asset's bounding box")] = None,
        min_bbox_y: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Y axis dimension of the asset's bounding box")] = None,
        min_bbox_z: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Z axis dimension of the asset's bounding box")] = None,
        max_bbox_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum X axis dimension of the asset's bounding box")] = None,
        max_bbox_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Y axis dimension of the asset's bounding box")] = None,
        max_bbox_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Z axis dimension of the asset's bounding box")] = None,
        return_images: Annotated[Optional[StrictBool], Field(description="Return images if set to True")] = None,
        return_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata if set to True")] = None,
        return_root_prims: Annotated[Optional[StrictBool], Field(description="Return root prims if set to True")] = None,
        return_default_prims: Annotated[Optional[StrictBool], Field(description="Return default prims if set to True")] = None,
        return_predictions: Annotated[Optional[StrictBool], Field(description="Return predictions if set to True")] = None,
        return_in_scene_instances_prims: Annotated[Optional[StrictBool], Field(description="[in-scene search only] Return prims of instances of objects found in the scene")] = None,
        embedding_knn_search_method: Annotated[Optional[Any], Field(description="Search method, approximate should be faster but is less accurate. Default is exact")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="Set the maximum number of results to return from the search, default is 32")] = None,
        vision_metadata: Annotated[Optional[StrictStr], Field(description="Uses a keyword match query on metadata fields that were generated using Vision Language Models")] = None,
        return_vision_generated_metadata: Annotated[Optional[StrictBool], Field(description="Returns the metadata fields that were generated using Vision Language Models")] = None,
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
    ) -> List[SearchResult]:
        """Search

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as query parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param description: Conduct text-based searches powered by AI
        :type description: str
        :param image_similarity_search: Perform similarity searches based on a list of images
        :type image_similarity_search: List[str]
        :param file_name: Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_name: str
        :param exclude_file_name: Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_file_name: str
        :param file_extension_include: Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_include: str
        :param file_extension_exclude: Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_exclude: str
        :param created_after: Filter results to only include assets created after a specified date
        :type created_after: str
        :param created_before: Filter results to only include assets created before a specified date
        :type created_before: str
        :param modified_after: Filter results to only include assets modified after a specified date
        :type modified_after: str
        :param modified_before: Filter results to only include assets modified before a specified date
        :type modified_before: str
        :param file_size_greater_than: Filter results to only include files larger than a specific size
        :type file_size_greater_than: str
        :param file_size_less_than: Filter results to only include files smaller than a specific size
        :type file_size_less_than: str
        :param created_by: Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type created_by: str
        :param exclude_created_by: Exclude assets created by a specific user from the results
        :type exclude_created_by: str
        :param modified_by: Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type modified_by: str
        :param exclude_modified_by: Exclude assets modified by a specific user from the results
        :type exclude_modified_by: str
        :param similarity_threshold: Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.
        :type similarity_threshold: float
        :param cutoff_threshold: Set the cutoff threshold for embedding-based searches
        :type cutoff_threshold: float
        :param search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type search_path: str
        :param exclude_search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_search_path: str
        :param search_in_scene: Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.
        :type search_in_scene: str
        :param filter_by_properties: Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`
        :type filter_by_properties: str
        :param min_bbox_x: Filter by minimum X axis dimension of the asset's bounding box
        :type min_bbox_x: float
        :param min_bbox_y: Filter by minimum Y axis dimension of the asset's bounding box
        :type min_bbox_y: float
        :param min_bbox_z: Filter by minimum Z axis dimension of the asset's bounding box
        :type min_bbox_z: float
        :param max_bbox_x: Filter by maximum X axis dimension of the asset's bounding box
        :type max_bbox_x: float
        :param max_bbox_y: Filter by maximum Y axis dimension of the asset's bounding box
        :type max_bbox_y: float
        :param max_bbox_z: Filter by maximum Z axis dimension of the asset's bounding box
        :type max_bbox_z: float
        :param return_images: Return images if set to True
        :type return_images: bool
        :param return_metadata: Return metadata if set to True
        :type return_metadata: bool
        :param return_root_prims: Return root prims if set to True
        :type return_root_prims: bool
        :param return_default_prims: Return default prims if set to True
        :type return_default_prims: bool
        :param return_predictions: Return predictions if set to True
        :type return_predictions: bool
        :param return_in_scene_instances_prims: [in-scene search only] Return prims of instances of objects found in the scene
        :type return_in_scene_instances_prims: bool
        :param embedding_knn_search_method: Search method, approximate should be faster but is less accurate. Default is exact
        :type embedding_knn_search_method: SearchMethod
        :param limit: Set the maximum number of results to return from the search, default is 32
        :type limit: int
        :param vision_metadata: Uses a keyword match query on metadata fields that were generated using Vision Language Models
        :type vision_metadata: str
        :param return_vision_generated_metadata: Returns the metadata fields that were generated using Vision Language Models
        :type return_vision_generated_metadata: bool
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

        _param = self._search_v2_deepsearch_search_get_serialize(
            description=description,
            image_similarity_search=image_similarity_search,
            file_name=file_name,
            exclude_file_name=exclude_file_name,
            file_extension_include=file_extension_include,
            file_extension_exclude=file_extension_exclude,
            created_after=created_after,
            created_before=created_before,
            modified_after=modified_after,
            modified_before=modified_before,
            file_size_greater_than=file_size_greater_than,
            file_size_less_than=file_size_less_than,
            created_by=created_by,
            exclude_created_by=exclude_created_by,
            modified_by=modified_by,
            exclude_modified_by=exclude_modified_by,
            similarity_threshold=similarity_threshold,
            cutoff_threshold=cutoff_threshold,
            search_path=search_path,
            exclude_search_path=exclude_search_path,
            search_in_scene=search_in_scene,
            filter_by_properties=filter_by_properties,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            return_images=return_images,
            return_metadata=return_metadata,
            return_root_prims=return_root_prims,
            return_default_prims=return_default_prims,
            return_predictions=return_predictions,
            return_in_scene_instances_prims=return_in_scene_instances_prims,
            embedding_knn_search_method=embedding_knn_search_method,
            limit=limit,
            vision_metadata=vision_metadata,
            return_vision_generated_metadata=return_vision_generated_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
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
    async def search_v2_deepsearch_search_get_with_http_info(
        self,
        description: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1024)]], Field(description="Conduct text-based searches powered by AI")] = None,
        image_similarity_search: Annotated[Optional[List[StrictStr]], Field(description="Perform similarity searches based on a list of images")] = None,
        file_name: Annotated[Optional[StrictStr], Field(description="Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_file_name: Annotated[Optional[StrictStr], Field(description="Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_include: Annotated[Optional[StrictStr], Field(description="Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_exclude: Annotated[Optional[StrictStr], Field(description="Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        created_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created after a specified date")] = None,
        created_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created before a specified date")] = None,
        modified_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified after a specified date")] = None,
        modified_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified before a specified date")] = None,
        file_size_greater_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files larger than a specific size")] = None,
        file_size_less_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files smaller than a specific size")] = None,
        created_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_created_by: Annotated[Optional[StrictStr], Field(description="Exclude assets created by a specific user from the results")] = None,
        modified_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_modified_by: Annotated[Optional[StrictStr], Field(description="Exclude assets modified by a specific user from the results")] = None,
        similarity_threshold: Annotated[Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]], Field(description="Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.")] = None,
        cutoff_threshold: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Set the cutoff threshold for embedding-based searches")] = None,
        search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        search_in_scene: Annotated[Optional[StrictStr], Field(description="Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.")] = None,
        filter_by_properties: Annotated[Optional[StrictStr], Field(description="Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_x: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum X axis dimension of the asset's bounding box")] = None,
        min_bbox_y: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Y axis dimension of the asset's bounding box")] = None,
        min_bbox_z: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Z axis dimension of the asset's bounding box")] = None,
        max_bbox_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum X axis dimension of the asset's bounding box")] = None,
        max_bbox_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Y axis dimension of the asset's bounding box")] = None,
        max_bbox_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Z axis dimension of the asset's bounding box")] = None,
        return_images: Annotated[Optional[StrictBool], Field(description="Return images if set to True")] = None,
        return_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata if set to True")] = None,
        return_root_prims: Annotated[Optional[StrictBool], Field(description="Return root prims if set to True")] = None,
        return_default_prims: Annotated[Optional[StrictBool], Field(description="Return default prims if set to True")] = None,
        return_predictions: Annotated[Optional[StrictBool], Field(description="Return predictions if set to True")] = None,
        return_in_scene_instances_prims: Annotated[Optional[StrictBool], Field(description="[in-scene search only] Return prims of instances of objects found in the scene")] = None,
        embedding_knn_search_method: Annotated[Optional[Any], Field(description="Search method, approximate should be faster but is less accurate. Default is exact")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="Set the maximum number of results to return from the search, default is 32")] = None,
        vision_metadata: Annotated[Optional[StrictStr], Field(description="Uses a keyword match query on metadata fields that were generated using Vision Language Models")] = None,
        return_vision_generated_metadata: Annotated[Optional[StrictBool], Field(description="Returns the metadata fields that were generated using Vision Language Models")] = None,
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
    ) -> ApiResponse[List[SearchResult]]:
        """Search

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as query parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param description: Conduct text-based searches powered by AI
        :type description: str
        :param image_similarity_search: Perform similarity searches based on a list of images
        :type image_similarity_search: List[str]
        :param file_name: Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_name: str
        :param exclude_file_name: Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_file_name: str
        :param file_extension_include: Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_include: str
        :param file_extension_exclude: Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_exclude: str
        :param created_after: Filter results to only include assets created after a specified date
        :type created_after: str
        :param created_before: Filter results to only include assets created before a specified date
        :type created_before: str
        :param modified_after: Filter results to only include assets modified after a specified date
        :type modified_after: str
        :param modified_before: Filter results to only include assets modified before a specified date
        :type modified_before: str
        :param file_size_greater_than: Filter results to only include files larger than a specific size
        :type file_size_greater_than: str
        :param file_size_less_than: Filter results to only include files smaller than a specific size
        :type file_size_less_than: str
        :param created_by: Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type created_by: str
        :param exclude_created_by: Exclude assets created by a specific user from the results
        :type exclude_created_by: str
        :param modified_by: Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type modified_by: str
        :param exclude_modified_by: Exclude assets modified by a specific user from the results
        :type exclude_modified_by: str
        :param similarity_threshold: Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.
        :type similarity_threshold: float
        :param cutoff_threshold: Set the cutoff threshold for embedding-based searches
        :type cutoff_threshold: float
        :param search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type search_path: str
        :param exclude_search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_search_path: str
        :param search_in_scene: Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.
        :type search_in_scene: str
        :param filter_by_properties: Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`
        :type filter_by_properties: str
        :param min_bbox_x: Filter by minimum X axis dimension of the asset's bounding box
        :type min_bbox_x: float
        :param min_bbox_y: Filter by minimum Y axis dimension of the asset's bounding box
        :type min_bbox_y: float
        :param min_bbox_z: Filter by minimum Z axis dimension of the asset's bounding box
        :type min_bbox_z: float
        :param max_bbox_x: Filter by maximum X axis dimension of the asset's bounding box
        :type max_bbox_x: float
        :param max_bbox_y: Filter by maximum Y axis dimension of the asset's bounding box
        :type max_bbox_y: float
        :param max_bbox_z: Filter by maximum Z axis dimension of the asset's bounding box
        :type max_bbox_z: float
        :param return_images: Return images if set to True
        :type return_images: bool
        :param return_metadata: Return metadata if set to True
        :type return_metadata: bool
        :param return_root_prims: Return root prims if set to True
        :type return_root_prims: bool
        :param return_default_prims: Return default prims if set to True
        :type return_default_prims: bool
        :param return_predictions: Return predictions if set to True
        :type return_predictions: bool
        :param return_in_scene_instances_prims: [in-scene search only] Return prims of instances of objects found in the scene
        :type return_in_scene_instances_prims: bool
        :param embedding_knn_search_method: Search method, approximate should be faster but is less accurate. Default is exact
        :type embedding_knn_search_method: SearchMethod
        :param limit: Set the maximum number of results to return from the search, default is 32
        :type limit: int
        :param vision_metadata: Uses a keyword match query on metadata fields that were generated using Vision Language Models
        :type vision_metadata: str
        :param return_vision_generated_metadata: Returns the metadata fields that were generated using Vision Language Models
        :type return_vision_generated_metadata: bool
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

        _param = self._search_v2_deepsearch_search_get_serialize(
            description=description,
            image_similarity_search=image_similarity_search,
            file_name=file_name,
            exclude_file_name=exclude_file_name,
            file_extension_include=file_extension_include,
            file_extension_exclude=file_extension_exclude,
            created_after=created_after,
            created_before=created_before,
            modified_after=modified_after,
            modified_before=modified_before,
            file_size_greater_than=file_size_greater_than,
            file_size_less_than=file_size_less_than,
            created_by=created_by,
            exclude_created_by=exclude_created_by,
            modified_by=modified_by,
            exclude_modified_by=exclude_modified_by,
            similarity_threshold=similarity_threshold,
            cutoff_threshold=cutoff_threshold,
            search_path=search_path,
            exclude_search_path=exclude_search_path,
            search_in_scene=search_in_scene,
            filter_by_properties=filter_by_properties,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            return_images=return_images,
            return_metadata=return_metadata,
            return_root_prims=return_root_prims,
            return_default_prims=return_default_prims,
            return_predictions=return_predictions,
            return_in_scene_instances_prims=return_in_scene_instances_prims,
            embedding_knn_search_method=embedding_knn_search_method,
            limit=limit,
            vision_metadata=vision_metadata,
            return_vision_generated_metadata=return_vision_generated_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
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
    async def search_v2_deepsearch_search_get_without_preload_content(
        self,
        description: Annotated[Optional[Annotated[str, Field(strict=True, max_length=1024)]], Field(description="Conduct text-based searches powered by AI")] = None,
        image_similarity_search: Annotated[Optional[List[StrictStr]], Field(description="Perform similarity searches based on a list of images")] = None,
        file_name: Annotated[Optional[StrictStr], Field(description="Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_file_name: Annotated[Optional[StrictStr], Field(description="Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_include: Annotated[Optional[StrictStr], Field(description="Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        file_extension_exclude: Annotated[Optional[StrictStr], Field(description="Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        created_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created after a specified date")] = None,
        created_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets created before a specified date")] = None,
        modified_after: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified after a specified date")] = None,
        modified_before: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include assets modified before a specified date")] = None,
        file_size_greater_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files larger than a specific size")] = None,
        file_size_less_than: Annotated[Optional[Annotated[str, Field(strict=True)]], Field(description="Filter results to only include files smaller than a specific size")] = None,
        created_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_created_by: Annotated[Optional[StrictStr], Field(description="Exclude assets created by a specific user from the results")] = None,
        modified_by: Annotated[Optional[StrictStr], Field(description="Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")] = None,
        exclude_modified_by: Annotated[Optional[StrictStr], Field(description="Exclude assets modified by a specific user from the results")] = None,
        similarity_threshold: Annotated[Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]], Field(description="Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.")] = None,
        cutoff_threshold: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Set the cutoff threshold for embedding-based searches")] = None,
        search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        exclude_search_path: Annotated[Optional[StrictStr], Field(description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")] = None,
        search_in_scene: Annotated[Optional[StrictStr], Field(description="Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.")] = None,
        filter_by_properties: Annotated[Optional[StrictStr], Field(description="Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_x: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum X axis dimension of the asset's bounding box")] = None,
        min_bbox_y: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Y axis dimension of the asset's bounding box")] = None,
        min_bbox_z: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Filter by minimum Z axis dimension of the asset's bounding box")] = None,
        max_bbox_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum X axis dimension of the asset's bounding box")] = None,
        max_bbox_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Y axis dimension of the asset's bounding box")] = None,
        max_bbox_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Filter by maximum Z axis dimension of the asset's bounding box")] = None,
        return_images: Annotated[Optional[StrictBool], Field(description="Return images if set to True")] = None,
        return_metadata: Annotated[Optional[StrictBool], Field(description="Return metadata if set to True")] = None,
        return_root_prims: Annotated[Optional[StrictBool], Field(description="Return root prims if set to True")] = None,
        return_default_prims: Annotated[Optional[StrictBool], Field(description="Return default prims if set to True")] = None,
        return_predictions: Annotated[Optional[StrictBool], Field(description="Return predictions if set to True")] = None,
        return_in_scene_instances_prims: Annotated[Optional[StrictBool], Field(description="[in-scene search only] Return prims of instances of objects found in the scene")] = None,
        embedding_knn_search_method: Annotated[Optional[Any], Field(description="Search method, approximate should be faster but is less accurate. Default is exact")] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="Set the maximum number of results to return from the search, default is 32")] = None,
        vision_metadata: Annotated[Optional[StrictStr], Field(description="Uses a keyword match query on metadata fields that were generated using Vision Language Models")] = None,
        return_vision_generated_metadata: Annotated[Optional[StrictBool], Field(description="Returns the metadata fields that were generated using Vision Language Models")] = None,
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
        """Search

        Version 2 of the DeepSearch API search endpoint. All supported search parameters are available as query parameters. It *does not* support DeepSearch query language.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, DeepSearch extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

        :param description: Conduct text-based searches powered by AI
        :type description: str
        :param image_similarity_search: Perform similarity searches based on a list of images
        :type image_similarity_search: List[str]
        :param file_name: Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_name: str
        :param exclude_file_name: Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_file_name: str
        :param file_extension_include: Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_include: str
        :param file_extension_exclude: Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type file_extension_exclude: str
        :param created_after: Filter results to only include assets created after a specified date
        :type created_after: str
        :param created_before: Filter results to only include assets created before a specified date
        :type created_before: str
        :param modified_after: Filter results to only include assets modified after a specified date
        :type modified_after: str
        :param modified_before: Filter results to only include assets modified before a specified date
        :type modified_before: str
        :param file_size_greater_than: Filter results to only include files larger than a specific size
        :type file_size_greater_than: str
        :param file_size_less_than: Filter results to only include files smaller than a specific size
        :type file_size_less_than: str
        :param created_by: Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type created_by: str
        :param exclude_created_by: Exclude assets created by a specific user from the results
        :type exclude_created_by: str
        :param modified_by: Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.
        :type modified_by: str
        :param exclude_modified_by: Exclude assets modified by a specific user from the results
        :type exclude_modified_by: str
        :param similarity_threshold: Set the similarity threshold for embedding-based searches. This functionality allows filterring duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.
        :type similarity_threshold: float
        :param cutoff_threshold: Set the cutoff threshold for embedding-based searches
        :type cutoff_threshold: float
        :param search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type search_path: str
        :param exclude_search_path: Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.
        :type exclude_search_path: str
        :param search_in_scene: Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.
        :type search_in_scene: str
        :param filter_by_properties: Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`
        :type filter_by_properties: str
        :param min_bbox_x: Filter by minimum X axis dimension of the asset's bounding box
        :type min_bbox_x: float
        :param min_bbox_y: Filter by minimum Y axis dimension of the asset's bounding box
        :type min_bbox_y: float
        :param min_bbox_z: Filter by minimum Z axis dimension of the asset's bounding box
        :type min_bbox_z: float
        :param max_bbox_x: Filter by maximum X axis dimension of the asset's bounding box
        :type max_bbox_x: float
        :param max_bbox_y: Filter by maximum Y axis dimension of the asset's bounding box
        :type max_bbox_y: float
        :param max_bbox_z: Filter by maximum Z axis dimension of the asset's bounding box
        :type max_bbox_z: float
        :param return_images: Return images if set to True
        :type return_images: bool
        :param return_metadata: Return metadata if set to True
        :type return_metadata: bool
        :param return_root_prims: Return root prims if set to True
        :type return_root_prims: bool
        :param return_default_prims: Return default prims if set to True
        :type return_default_prims: bool
        :param return_predictions: Return predictions if set to True
        :type return_predictions: bool
        :param return_in_scene_instances_prims: [in-scene search only] Return prims of instances of objects found in the scene
        :type return_in_scene_instances_prims: bool
        :param embedding_knn_search_method: Search method, approximate should be faster but is less accurate. Default is exact
        :type embedding_knn_search_method: SearchMethod
        :param limit: Set the maximum number of results to return from the search, default is 32
        :type limit: int
        :param vision_metadata: Uses a keyword match query on metadata fields that were generated using Vision Language Models
        :type vision_metadata: str
        :param return_vision_generated_metadata: Returns the metadata fields that were generated using Vision Language Models
        :type return_vision_generated_metadata: bool
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

        _param = self._search_v2_deepsearch_search_get_serialize(
            description=description,
            image_similarity_search=image_similarity_search,
            file_name=file_name,
            exclude_file_name=exclude_file_name,
            file_extension_include=file_extension_include,
            file_extension_exclude=file_extension_exclude,
            created_after=created_after,
            created_before=created_before,
            modified_after=modified_after,
            modified_before=modified_before,
            file_size_greater_than=file_size_greater_than,
            file_size_less_than=file_size_less_than,
            created_by=created_by,
            exclude_created_by=exclude_created_by,
            modified_by=modified_by,
            exclude_modified_by=exclude_modified_by,
            similarity_threshold=similarity_threshold,
            cutoff_threshold=cutoff_threshold,
            search_path=search_path,
            exclude_search_path=exclude_search_path,
            search_in_scene=search_in_scene,
            filter_by_properties=filter_by_properties,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            return_images=return_images,
            return_metadata=return_metadata,
            return_root_prims=return_root_prims,
            return_default_prims=return_default_prims,
            return_predictions=return_predictions,
            return_in_scene_instances_prims=return_in_scene_instances_prims,
            embedding_knn_search_method=embedding_knn_search_method,
            limit=limit,
            vision_metadata=vision_metadata,
            return_vision_generated_metadata=return_vision_generated_metadata,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SearchResult]",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _search_v2_deepsearch_search_get_serialize(
        self,
        description,
        image_similarity_search,
        file_name,
        exclude_file_name,
        file_extension_include,
        file_extension_exclude,
        created_after,
        created_before,
        modified_after,
        modified_before,
        file_size_greater_than,
        file_size_less_than,
        created_by,
        exclude_created_by,
        modified_by,
        exclude_modified_by,
        similarity_threshold,
        cutoff_threshold,
        search_path,
        exclude_search_path,
        search_in_scene,
        filter_by_properties,
        min_bbox_x,
        min_bbox_y,
        min_bbox_z,
        max_bbox_x,
        max_bbox_y,
        max_bbox_z,
        return_images,
        return_metadata,
        return_root_prims,
        return_default_prims,
        return_predictions,
        return_in_scene_instances_prims,
        embedding_knn_search_method,
        limit,
        vision_metadata,
        return_vision_generated_metadata,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'image_similarity_search': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if description is not None:
            
            _query_params.append(('description', description))
            
        if image_similarity_search is not None:
            
            _query_params.append(('image_similarity_search', image_similarity_search))
            
        if file_name is not None:
            
            _query_params.append(('file_name', file_name))
            
        if exclude_file_name is not None:
            
            _query_params.append(('exclude_file_name', exclude_file_name))
            
        if file_extension_include is not None:
            
            _query_params.append(('file_extension_include', file_extension_include))
            
        if file_extension_exclude is not None:
            
            _query_params.append(('file_extension_exclude', file_extension_exclude))
            
        if created_after is not None:
            
            _query_params.append(('created_after', created_after))
            
        if created_before is not None:
            
            _query_params.append(('created_before', created_before))
            
        if modified_after is not None:
            
            _query_params.append(('modified_after', modified_after))
            
        if modified_before is not None:
            
            _query_params.append(('modified_before', modified_before))
            
        if file_size_greater_than is not None:
            
            _query_params.append(('file_size_greater_than', file_size_greater_than))
            
        if file_size_less_than is not None:
            
            _query_params.append(('file_size_less_than', file_size_less_than))
            
        if created_by is not None:
            
            _query_params.append(('created_by', created_by))
            
        if exclude_created_by is not None:
            
            _query_params.append(('exclude_created_by', exclude_created_by))
            
        if modified_by is not None:
            
            _query_params.append(('modified_by', modified_by))
            
        if exclude_modified_by is not None:
            
            _query_params.append(('exclude_modified_by', exclude_modified_by))
            
        if similarity_threshold is not None:
            
            _query_params.append(('similarity_threshold', similarity_threshold))
            
        if cutoff_threshold is not None:
            
            _query_params.append(('cutoff_threshold', cutoff_threshold))
            
        if search_path is not None:
            
            _query_params.append(('search_path', search_path))
            
        if exclude_search_path is not None:
            
            _query_params.append(('exclude_search_path', exclude_search_path))
            
        if search_in_scene is not None:
            
            _query_params.append(('search_in_scene', search_in_scene))
            
        if filter_by_properties is not None:
            
            _query_params.append(('filter_by_properties', filter_by_properties))
            
        if min_bbox_x is not None:
            
            _query_params.append(('min_bbox_x', min_bbox_x))
            
        if min_bbox_y is not None:
            
            _query_params.append(('min_bbox_y', min_bbox_y))
            
        if min_bbox_z is not None:
            
            _query_params.append(('min_bbox_z', min_bbox_z))
            
        if max_bbox_x is not None:
            
            _query_params.append(('max_bbox_x', max_bbox_x))
            
        if max_bbox_y is not None:
            
            _query_params.append(('max_bbox_y', max_bbox_y))
            
        if max_bbox_z is not None:
            
            _query_params.append(('max_bbox_z', max_bbox_z))
            
        if return_images is not None:
            
            _query_params.append(('return_images', return_images))
            
        if return_metadata is not None:
            
            _query_params.append(('return_metadata', return_metadata))
            
        if return_root_prims is not None:
            
            _query_params.append(('return_root_prims', return_root_prims))
            
        if return_default_prims is not None:
            
            _query_params.append(('return_default_prims', return_default_prims))
            
        if return_predictions is not None:
            
            _query_params.append(('return_predictions', return_predictions))
            
        if return_in_scene_instances_prims is not None:
            
            _query_params.append(('return_in_scene_instances_prims', return_in_scene_instances_prims))
            
        if embedding_knn_search_method is not None:
            
            _query_params.append(('embedding_knn_search_method', embedding_knn_search_method.value))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if vision_metadata is not None:
            
            _query_params.append(('vision_metadata', vision_metadata))
            
        if return_vision_generated_metadata is not None:
            
            _query_params.append(('return_vision_generated_metadata', return_vision_generated_metadata))
            
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
            'APIKeyHeader', 
            'HTTPBasic', 
            'HTTPBearer'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/search',
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


