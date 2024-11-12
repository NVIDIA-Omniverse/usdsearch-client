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

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, List, Optional, Union
from typing_extensions import Annotated
from usd_search_client.models.prim import Prim
from usd_search_client.models.scene_summary_response import SceneSummaryResponse

from usd_search_client.api_client import ApiClient, RequestSerialized
from usd_search_client.api_response import ApiResponse
from usd_search_client.rest import RESTResponseType


class AGSSceneGraphApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    async def get_prims_asset_graph_usd_prims_get(
        self,
        scene_url: Annotated[Optional[StrictStr], Field(description="Retrieve prims from the scene at specified URL.")] = None,
        usd_path: Annotated[Optional[Any], Field(description="Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.")] = None,
        root_prim: Annotated[Optional[StrictBool], Field(description="Retrieve root prims. Note: combined with default_prim returns both root and default prims.")] = None,
        default_prim: Annotated[Optional[StrictBool], Field(description="Retrieve default prims. Note: combined with root_prim returns both root and default prims.")] = None,
        source_asset_url: Annotated[Optional[StrictStr], Field(description="Filter prims based on their source asset URL, i.e. the asset they have a reference to")] = None,
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
        """Get Prims

        Retrieve prims from a USD scene.  This API can be used for scene understanding, returns all objects in a scene together with their locations and dimensions.  NOTE: Calling without any parameters will return ALL prims. `scene_url` must be provided to fetch prims from the specified scene.  A globally unique prim id consists of (`scene_url`, `usd_path`) tuple. `usd_path` is unique only within a single scene. To retrieve prims from a specified scene, `scene_url` must be set. To retrieve a single prim from a specified scene, provide both `scene_url` and `usd_path`.

        :param scene_url: Retrieve prims from the scene at specified URL.
        :type scene_url: str
        :param usd_path: Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.
        :type usd_path: UsdPath
        :param root_prim: Retrieve root prims. Note: combined with default_prim returns both root and default prims.
        :type root_prim: bool
        :param default_prim: Retrieve default prims. Note: combined with root_prim returns both root and default prims.
        :type default_prim: bool
        :param source_asset_url: Filter prims based on their source asset URL, i.e. the asset they have a reference to
        :type source_asset_url: str
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

        _param = self._get_prims_asset_graph_usd_prims_get_serialize(
            scene_url=scene_url,
            usd_path=usd_path,
            root_prim=root_prim,
            default_prim=default_prim,
            source_asset_url=source_asset_url,
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
    async def get_prims_asset_graph_usd_prims_get_with_http_info(
        self,
        scene_url: Annotated[Optional[StrictStr], Field(description="Retrieve prims from the scene at specified URL.")] = None,
        usd_path: Annotated[Optional[Any], Field(description="Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.")] = None,
        root_prim: Annotated[Optional[StrictBool], Field(description="Retrieve root prims. Note: combined with default_prim returns both root and default prims.")] = None,
        default_prim: Annotated[Optional[StrictBool], Field(description="Retrieve default prims. Note: combined with root_prim returns both root and default prims.")] = None,
        source_asset_url: Annotated[Optional[StrictStr], Field(description="Filter prims based on their source asset URL, i.e. the asset they have a reference to")] = None,
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
        """Get Prims

        Retrieve prims from a USD scene.  This API can be used for scene understanding, returns all objects in a scene together with their locations and dimensions.  NOTE: Calling without any parameters will return ALL prims. `scene_url` must be provided to fetch prims from the specified scene.  A globally unique prim id consists of (`scene_url`, `usd_path`) tuple. `usd_path` is unique only within a single scene. To retrieve prims from a specified scene, `scene_url` must be set. To retrieve a single prim from a specified scene, provide both `scene_url` and `usd_path`.

        :param scene_url: Retrieve prims from the scene at specified URL.
        :type scene_url: str
        :param usd_path: Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.
        :type usd_path: UsdPath
        :param root_prim: Retrieve root prims. Note: combined with default_prim returns both root and default prims.
        :type root_prim: bool
        :param default_prim: Retrieve default prims. Note: combined with root_prim returns both root and default prims.
        :type default_prim: bool
        :param source_asset_url: Filter prims based on their source asset URL, i.e. the asset they have a reference to
        :type source_asset_url: str
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

        _param = self._get_prims_asset_graph_usd_prims_get_serialize(
            scene_url=scene_url,
            usd_path=usd_path,
            root_prim=root_prim,
            default_prim=default_prim,
            source_asset_url=source_asset_url,
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
    async def get_prims_asset_graph_usd_prims_get_without_preload_content(
        self,
        scene_url: Annotated[Optional[StrictStr], Field(description="Retrieve prims from the scene at specified URL.")] = None,
        usd_path: Annotated[Optional[Any], Field(description="Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.")] = None,
        root_prim: Annotated[Optional[StrictBool], Field(description="Retrieve root prims. Note: combined with default_prim returns both root and default prims.")] = None,
        default_prim: Annotated[Optional[StrictBool], Field(description="Retrieve default prims. Note: combined with root_prim returns both root and default prims.")] = None,
        source_asset_url: Annotated[Optional[StrictStr], Field(description="Filter prims based on their source asset URL, i.e. the asset they have a reference to")] = None,
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
        """Get Prims

        Retrieve prims from a USD scene.  This API can be used for scene understanding, returns all objects in a scene together with their locations and dimensions.  NOTE: Calling without any parameters will return ALL prims. `scene_url` must be provided to fetch prims from the specified scene.  A globally unique prim id consists of (`scene_url`, `usd_path`) tuple. `usd_path` is unique only within a single scene. To retrieve prims from a specified scene, `scene_url` must be set. To retrieve a single prim from a specified scene, provide both `scene_url` and `usd_path`.

        :param scene_url: Retrieve prims from the scene at specified URL.
        :type scene_url: str
        :param usd_path: Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.
        :type usd_path: UsdPath
        :param root_prim: Retrieve root prims. Note: combined with default_prim returns both root and default prims.
        :type root_prim: bool
        :param default_prim: Retrieve default prims. Note: combined with root_prim returns both root and default prims.
        :type default_prim: bool
        :param source_asset_url: Filter prims based on their source asset URL, i.e. the asset they have a reference to
        :type source_asset_url: str
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

        _param = self._get_prims_asset_graph_usd_prims_get_serialize(
            scene_url=scene_url,
            usd_path=usd_path,
            root_prim=root_prim,
            default_prim=default_prim,
            source_asset_url=source_asset_url,
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


    def _get_prims_asset_graph_usd_prims_get_serialize(
        self,
        scene_url,
        usd_path,
        root_prim,
        default_prim,
        source_asset_url,
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

        # We add parameters that should be formatted as multi-dict. For some reason the OpenAPI generator doesn't do this.
        _collection_formats: Dict[str, str] = {
            "prim_type": "multi",
            "usd_path": "multi"
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
            
        if usd_path is not None:
            
            _query_params.append(('usd_path', usd_path))
            
        if root_prim is not None:
            
            _query_params.append(('root_prim', root_prim))
            
        if default_prim is not None:
            
            _query_params.append(('default_prim', default_prim))
            
        if source_asset_url is not None:
            
            _query_params.append(('source_asset_url', source_asset_url))
            
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
            resource_path='/asset_graph/usd/prims',
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
    async def scene_summary_asset_graph_usd_scene_summary_get(
        self,
        scene_url: Annotated[StrictStr, Field(description="Scene summary.")],
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
    ) -> SceneSummaryResponse:
        """Scene Summary

        Retrieve summary info about a USD scene.

        :param scene_url: Scene summary. (required)
        :type scene_url: str
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

        _param = self._scene_summary_asset_graph_usd_scene_summary_get_serialize(
            scene_url=scene_url,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SceneSummaryResponse",
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
    async def scene_summary_asset_graph_usd_scene_summary_get_with_http_info(
        self,
        scene_url: Annotated[StrictStr, Field(description="Scene summary.")],
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
    ) -> ApiResponse[SceneSummaryResponse]:
        """Scene Summary

        Retrieve summary info about a USD scene.

        :param scene_url: Scene summary. (required)
        :type scene_url: str
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

        _param = self._scene_summary_asset_graph_usd_scene_summary_get_serialize(
            scene_url=scene_url,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SceneSummaryResponse",
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
    async def scene_summary_asset_graph_usd_scene_summary_get_without_preload_content(
        self,
        scene_url: Annotated[StrictStr, Field(description="Scene summary.")],
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
        """Scene Summary

        Retrieve summary info about a USD scene.

        :param scene_url: Scene summary. (required)
        :type scene_url: str
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

        _param = self._scene_summary_asset_graph_usd_scene_summary_get_serialize(
            scene_url=scene_url,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SceneSummaryResponse",
            '422': "HTTPValidationError",
        }
        response_data = await self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _scene_summary_asset_graph_usd_scene_summary_get_serialize(
        self,
        scene_url,
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
        if scene_url is not None:
            
            _query_params.append(('scene_url', scene_url))
            
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
            resource_path='/asset_graph/usd/scene_summary/',
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


