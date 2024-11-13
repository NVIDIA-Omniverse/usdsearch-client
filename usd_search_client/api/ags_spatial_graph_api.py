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

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing import Any, List, Optional, Union
from typing_extensions import Annotated
from usd_search_client.models.prim import Prim
from usd_search_client.models.spatial_query_response_item import SpatialQueryResponseItem

from usd_search_client.api_client import ApiClient, RequestSerialized
from usd_search_client.api_response import ApiResponse
from usd_search_client.rest import RESTResponseType


class AGSSpatialGraphApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get(
        self,
        scene_url: Annotated[StrictStr, Field(description="Retrieve prims from the scene at specified URL.")],
        min_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum X")],
        min_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Y")],
        min_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Z")],
        max_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum X")],
        max_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Y")],
        max_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Z")],
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
    ) -> List[Prim]:
        """Get Prims Within Bounding Box

        Perform a spatial search within a scene to retrieve prims from a USD scene that fall within a specified bounding box. The bounding box is defined by two points: [min_bbox_x, min_bbox_y, min_bbox_z] and [max_bbox_x, max_bbox_y, max_bbox_z].  A prim is considered to be within the bounding box if its bounding box midpoint falls within the specified query bounding box.

        :param scene_url: Retrieve prims from the scene at specified URL. (required)
        :type scene_url: str
        :param min_bbox_x: Query bounding box minimum X (required)
        :type min_bbox_x: float
        :param min_bbox_y: Query bounding box minimum Y (required)
        :type min_bbox_y: float
        :param min_bbox_z: Query bounding box minimum Z (required)
        :type min_bbox_z: float
        :param max_bbox_x: Query bounding box maximum X (required)
        :type max_bbox_x: float
        :param max_bbox_y: Query bounding box maximum Y (required)
        :type max_bbox_y: float
        :param max_bbox_z: Query bounding box maximum Z (required)
        :type max_bbox_z: float
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_serialize(
            scene_url=scene_url,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Prim]",
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
    async def get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_with_http_info(
        self,
        scene_url: Annotated[StrictStr, Field(description="Retrieve prims from the scene at specified URL.")],
        min_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum X")],
        min_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Y")],
        min_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Z")],
        max_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum X")],
        max_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Y")],
        max_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Z")],
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
    ) -> ApiResponse[List[Prim]]:
        """Get Prims Within Bounding Box

        Perform a spatial search within a scene to retrieve prims from a USD scene that fall within a specified bounding box. The bounding box is defined by two points: [min_bbox_x, min_bbox_y, min_bbox_z] and [max_bbox_x, max_bbox_y, max_bbox_z].  A prim is considered to be within the bounding box if its bounding box midpoint falls within the specified query bounding box.

        :param scene_url: Retrieve prims from the scene at specified URL. (required)
        :type scene_url: str
        :param min_bbox_x: Query bounding box minimum X (required)
        :type min_bbox_x: float
        :param min_bbox_y: Query bounding box minimum Y (required)
        :type min_bbox_y: float
        :param min_bbox_z: Query bounding box minimum Z (required)
        :type min_bbox_z: float
        :param max_bbox_x: Query bounding box maximum X (required)
        :type max_bbox_x: float
        :param max_bbox_y: Query bounding box maximum Y (required)
        :type max_bbox_y: float
        :param max_bbox_z: Query bounding box maximum Z (required)
        :type max_bbox_z: float
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_serialize(
            scene_url=scene_url,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Prim]",
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
    async def get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_without_preload_content(
        self,
        scene_url: Annotated[StrictStr, Field(description="Retrieve prims from the scene at specified URL.")],
        min_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum X")],
        min_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Y")],
        min_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box minimum Z")],
        max_bbox_x: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum X")],
        max_bbox_y: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Y")],
        max_bbox_z: Annotated[Union[StrictFloat, StrictInt], Field(description="Query bounding box maximum Z")],
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
        """Get Prims Within Bounding Box

        Perform a spatial search within a scene to retrieve prims from a USD scene that fall within a specified bounding box. The bounding box is defined by two points: [min_bbox_x, min_bbox_y, min_bbox_z] and [max_bbox_x, max_bbox_y, max_bbox_z].  A prim is considered to be within the bounding box if its bounding box midpoint falls within the specified query bounding box.

        :param scene_url: Retrieve prims from the scene at specified URL. (required)
        :type scene_url: str
        :param min_bbox_x: Query bounding box minimum X (required)
        :type min_bbox_x: float
        :param min_bbox_y: Query bounding box minimum Y (required)
        :type min_bbox_y: float
        :param min_bbox_z: Query bounding box minimum Z (required)
        :type min_bbox_z: float
        :param max_bbox_x: Query bounding box maximum X (required)
        :type max_bbox_x: float
        :param max_bbox_y: Query bounding box maximum Y (required)
        :type max_bbox_y: float
        :param max_bbox_z: Query bounding box maximum Z (required)
        :type max_bbox_z: float
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_serialize(
            scene_url=scene_url,
            min_bbox_x=min_bbox_x,
            min_bbox_y=min_bbox_y,
            min_bbox_z=min_bbox_z,
            max_bbox_x=max_bbox_x,
            max_bbox_y=max_bbox_y,
            max_bbox_z=max_bbox_z,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Prim]",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get_serialize(
        self,
        scene_url,
        min_bbox_x,
        min_bbox_y,
        min_bbox_z,
        max_bbox_x,
        max_bbox_y,
        max_bbox_z,
        limit,
        prim_type,
        usd_path_prefix,
        properties_filter,
        min_bbox_dimension_x,
        min_bbox_dimension_y,
        min_bbox_dimension_z,
        max_bbox_dimension_x,
        max_bbox_dimension_y,
        max_bbox_dimension_z,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            "prim_type": "multi",
            "usd_path_prefix": "multi"
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if scene_url is not None:
            
            _query_params.append(('scene_url', scene_url))
            
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
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if prim_type is not None:
            
            _query_params.append(('prim_type', prim_type))
            
        if usd_path_prefix is not None:
            
            _query_params.append(('usd_path_prefix', usd_path_prefix))
            
        if properties_filter is not None:
            
            _query_params.append(('properties_filter', properties_filter))
            
        if min_bbox_dimension_x is not None:
            
            _query_params.append(('min_bbox_dimension_x', min_bbox_dimension_x))
            
        if min_bbox_dimension_y is not None:
            
            _query_params.append(('min_bbox_dimension_y', min_bbox_dimension_y))
            
        if min_bbox_dimension_z is not None:
            
            _query_params.append(('min_bbox_dimension_z', min_bbox_dimension_z))
            
        if max_bbox_dimension_x is not None:
            
            _query_params.append(('max_bbox_dimension_x', max_bbox_dimension_x))
            
        if max_bbox_dimension_y is not None:
            
            _query_params.append(('max_bbox_dimension_y', max_bbox_dimension_y))
            
        if max_bbox_dimension_z is not None:
            
            _query_params.append(('max_bbox_dimension_z', max_bbox_dimension_z))
            
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
            resource_path='/asset_graph/usd/prims/spatial_bbox',
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
    async def get_prims_within_radius_asset_graph_usd_prims_spatial_get(
        self,
        scene_url: Annotated[StrictStr, Field(description="URL of the scene to search.")],
        radius: Annotated[Union[StrictFloat, StrictInt], Field(description="Radius of the proximity query")],
        center_prim_usd_path: Annotated[Optional[StrictStr], Field(description="USD path of the reference Prim. (Returned in results unless excluded by filters)")] = None,
        center_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="X coordinate of the query center.")] = None,
        center_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Y coordinate of the query center.")] = None,
        center_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Z coordinate of the query center.")] = None,
        transformation_matrix: Annotated[Optional[StrictStr], Field(description="Transformation matrix for the vector space. By default does not apply any transformation.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
    ) -> List[SpatialQueryResponseItem]:
        """Get Prims Within Radius

        Perform a spatial search within a scene to retrieve prims from a USD scene based on their proximity to a reference prim `center_prim_usd_path` or specific coordinates `[center_x, center_y, center_z]` within a specified `radius`.  **Note:** You must specify either `center_prim_usd_path` or the coordinates `[center_x, center_y, center_z]`.  Returns prim objects including: attributes, dimensions, and min, max, midpoint coordinates of the bounding box, distance from the query center, vector from the query center to the prim midpoint.  If searching using `center_prim_usd_path` the center prim at `center_prim_usd_path` is included in the results (unless excluded by filters used).

        :param scene_url: URL of the scene to search. (required)
        :type scene_url: str
        :param radius: Radius of the proximity query (required)
        :type radius: float
        :param center_prim_usd_path: USD path of the reference Prim. (Returned in results unless excluded by filters)
        :type center_prim_usd_path: str
        :param center_x: X coordinate of the query center.
        :type center_x: float
        :param center_y: Y coordinate of the query center.
        :type center_y: float
        :param center_z: Z coordinate of the query center.
        :type center_z: float
        :param transformation_matrix: Transformation matrix for the vector space. By default does not apply any transformation.
        :type transformation_matrix: str
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_radius_asset_graph_usd_prims_spatial_get_serialize(
            scene_url=scene_url,
            radius=radius,
            center_prim_usd_path=center_prim_usd_path,
            center_x=center_x,
            center_y=center_y,
            center_z=center_z,
            transformation_matrix=transformation_matrix,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SpatialQueryResponseItem]",
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
    async def get_prims_within_radius_asset_graph_usd_prims_spatial_get_with_http_info(
        self,
        scene_url: Annotated[StrictStr, Field(description="URL of the scene to search.")],
        radius: Annotated[Union[StrictFloat, StrictInt], Field(description="Radius of the proximity query")],
        center_prim_usd_path: Annotated[Optional[StrictStr], Field(description="USD path of the reference Prim. (Returned in results unless excluded by filters)")] = None,
        center_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="X coordinate of the query center.")] = None,
        center_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Y coordinate of the query center.")] = None,
        center_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Z coordinate of the query center.")] = None,
        transformation_matrix: Annotated[Optional[StrictStr], Field(description="Transformation matrix for the vector space. By default does not apply any transformation.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
    ) -> ApiResponse[List[SpatialQueryResponseItem]]:
        """Get Prims Within Radius

        Perform a spatial search within a scene to retrieve prims from a USD scene based on their proximity to a reference prim `center_prim_usd_path` or specific coordinates `[center_x, center_y, center_z]` within a specified `radius`.  **Note:** You must specify either `center_prim_usd_path` or the coordinates `[center_x, center_y, center_z]`.  Returns prim objects including: attributes, dimensions, and min, max, midpoint coordinates of the bounding box, distance from the query center, vector from the query center to the prim midpoint.  If searching using `center_prim_usd_path` the center prim at `center_prim_usd_path` is included in the results (unless excluded by filters used).

        :param scene_url: URL of the scene to search. (required)
        :type scene_url: str
        :param radius: Radius of the proximity query (required)
        :type radius: float
        :param center_prim_usd_path: USD path of the reference Prim. (Returned in results unless excluded by filters)
        :type center_prim_usd_path: str
        :param center_x: X coordinate of the query center.
        :type center_x: float
        :param center_y: Y coordinate of the query center.
        :type center_y: float
        :param center_z: Z coordinate of the query center.
        :type center_z: float
        :param transformation_matrix: Transformation matrix for the vector space. By default does not apply any transformation.
        :type transformation_matrix: str
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_radius_asset_graph_usd_prims_spatial_get_serialize(
            scene_url=scene_url,
            radius=radius,
            center_prim_usd_path=center_prim_usd_path,
            center_x=center_x,
            center_y=center_y,
            center_z=center_z,
            transformation_matrix=transformation_matrix,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SpatialQueryResponseItem]",
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
    async def get_prims_within_radius_asset_graph_usd_prims_spatial_get_without_preload_content(
        self,
        scene_url: Annotated[StrictStr, Field(description="URL of the scene to search.")],
        radius: Annotated[Union[StrictFloat, StrictInt], Field(description="Radius of the proximity query")],
        center_prim_usd_path: Annotated[Optional[StrictStr], Field(description="USD path of the reference Prim. (Returned in results unless excluded by filters)")] = None,
        center_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="X coordinate of the query center.")] = None,
        center_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Y coordinate of the query center.")] = None,
        center_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Z coordinate of the query center.")] = None,
        transformation_matrix: Annotated[Optional[StrictStr], Field(description="Transformation matrix for the vector space. By default does not apply any transformation.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Page size")] = None,
        prim_type: Annotated[Optional[Any], Field(description="Retrieve prims of the specified types. Can provide either a single type or a list of types.")] = None,
        usd_path_prefix: Annotated[Optional[StrictStr], Field(description="Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).")] = None,
        properties_filter: Annotated[Optional[StrictStr], Field(description="Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`")] = None,
        min_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box X dimension")] = None,
        min_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Y dimension")] = None,
        min_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Minimum bounding box Z dimension")] = None,
        max_bbox_dimension_x: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box X dimension")] = None,
        max_bbox_dimension_y: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Y dimension")] = None,
        max_bbox_dimension_z: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Max bounding box Z dimension")] = None,
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
        """Get Prims Within Radius

        Perform a spatial search within a scene to retrieve prims from a USD scene based on their proximity to a reference prim `center_prim_usd_path` or specific coordinates `[center_x, center_y, center_z]` within a specified `radius`.  **Note:** You must specify either `center_prim_usd_path` or the coordinates `[center_x, center_y, center_z]`.  Returns prim objects including: attributes, dimensions, and min, max, midpoint coordinates of the bounding box, distance from the query center, vector from the query center to the prim midpoint.  If searching using `center_prim_usd_path` the center prim at `center_prim_usd_path` is included in the results (unless excluded by filters used).

        :param scene_url: URL of the scene to search. (required)
        :type scene_url: str
        :param radius: Radius of the proximity query (required)
        :type radius: float
        :param center_prim_usd_path: USD path of the reference Prim. (Returned in results unless excluded by filters)
        :type center_prim_usd_path: str
        :param center_x: X coordinate of the query center.
        :type center_x: float
        :param center_y: Y coordinate of the query center.
        :type center_y: float
        :param center_z: Z coordinate of the query center.
        :type center_z: float
        :param transformation_matrix: Transformation matrix for the vector space. By default does not apply any transformation.
        :type transformation_matrix: str
        :param limit: Page size
        :type limit: int
        :param prim_type: Retrieve prims of the specified types. Can provide either a single type or a list of types.
        :type prim_type: PrimType
        :param usd_path_prefix: Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path).
        :type usd_path_prefix: str
        :param properties_filter: Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456`
        :type properties_filter: str
        :param min_bbox_dimension_x: Minimum bounding box X dimension
        :type min_bbox_dimension_x: float
        :param min_bbox_dimension_y: Minimum bounding box Y dimension
        :type min_bbox_dimension_y: float
        :param min_bbox_dimension_z: Minimum bounding box Z dimension
        :type min_bbox_dimension_z: float
        :param max_bbox_dimension_x: Max bounding box X dimension
        :type max_bbox_dimension_x: float
        :param max_bbox_dimension_y: Max bounding box Y dimension
        :type max_bbox_dimension_y: float
        :param max_bbox_dimension_z: Max bounding box Z dimension
        :type max_bbox_dimension_z: float
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

        _param = self._get_prims_within_radius_asset_graph_usd_prims_spatial_get_serialize(
            scene_url=scene_url,
            radius=radius,
            center_prim_usd_path=center_prim_usd_path,
            center_x=center_x,
            center_y=center_y,
            center_z=center_z,
            transformation_matrix=transformation_matrix,
            limit=limit,
            prim_type=prim_type,
            usd_path_prefix=usd_path_prefix,
            properties_filter=properties_filter,
            min_bbox_dimension_x=min_bbox_dimension_x,
            min_bbox_dimension_y=min_bbox_dimension_y,
            min_bbox_dimension_z=min_bbox_dimension_z,
            max_bbox_dimension_x=max_bbox_dimension_x,
            max_bbox_dimension_y=max_bbox_dimension_y,
            max_bbox_dimension_z=max_bbox_dimension_z,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[SpatialQueryResponseItem]",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_prims_within_radius_asset_graph_usd_prims_spatial_get_serialize(
        self,
        scene_url,
        radius,
        center_prim_usd_path,
        center_x,
        center_y,
        center_z,
        transformation_matrix,
        limit,
        prim_type,
        usd_path_prefix,
        properties_filter,
        min_bbox_dimension_x,
        min_bbox_dimension_y,
        min_bbox_dimension_z,
        max_bbox_dimension_x,
        max_bbox_dimension_y,
        max_bbox_dimension_z,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            "prim_type": "multi",
            "usd_path_prefix": "multi"
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if scene_url is not None:
            
            _query_params.append(('scene_url', scene_url))
            
        if radius is not None:
            
            _query_params.append(('radius', radius))
            
        if center_prim_usd_path is not None:
            
            _query_params.append(('center_prim_usd_path', center_prim_usd_path))
            
        if center_x is not None:
            
            _query_params.append(('center_x', center_x))
            
        if center_y is not None:
            
            _query_params.append(('center_y', center_y))
            
        if center_z is not None:
            
            _query_params.append(('center_z', center_z))
            
        if transformation_matrix is not None:
            
            _query_params.append(('transformation_matrix', transformation_matrix))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if prim_type is not None:
            
            _query_params.append(('prim_type', prim_type))
            
        if usd_path_prefix is not None:
            
            _query_params.append(('usd_path_prefix', usd_path_prefix))
            
        if properties_filter is not None:
            
            _query_params.append(('properties_filter', properties_filter))
            
        if min_bbox_dimension_x is not None:
            
            _query_params.append(('min_bbox_dimension_x', min_bbox_dimension_x))
            
        if min_bbox_dimension_y is not None:
            
            _query_params.append(('min_bbox_dimension_y', min_bbox_dimension_y))
            
        if min_bbox_dimension_z is not None:
            
            _query_params.append(('min_bbox_dimension_z', min_bbox_dimension_z))
            
        if max_bbox_dimension_x is not None:
            
            _query_params.append(('max_bbox_dimension_x', max_bbox_dimension_x))
            
        if max_bbox_dimension_y is not None:
            
            _query_params.append(('max_bbox_dimension_y', max_bbox_dimension_y))
            
        if max_bbox_dimension_z is not None:
            
            _query_params.append(('max_bbox_dimension_z', max_bbox_dimension_z))
            
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
            resource_path='/asset_graph/usd/prims/spatial',
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


