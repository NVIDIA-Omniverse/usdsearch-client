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

from typing import Optional, List, Union
from usd_search_client.api_client import ApiClient
from usd_search_client.api.ai_search_api import AISearchApi
from usd_search_client.api.images_api import ImagesApi
from usd_search_client.main.models import BasicSearchRequest, BasicSearchResponse, HybridSearchResponse
from usd_search_client.api.ags_asset_graph_api import AGSAssetGraphApi
from usd_search_client.models.asset import Asset
from usd_search_client.models.asset_graph import AssetGraph
from usd_search_client.api.ags_scene_graph_api import AGSSceneGraphApi
from usd_search_client.models.scene_summary_response import SceneSummaryResponse


async def search(search_request: BasicSearchRequest, api_client: Optional[ApiClient] = None) -> List[BasicSearchResponse]:
    """
    Search for items in the database.

    Args:
        search_request (BasicSearchRequest): The search request.

    Examples:
        >>> import usd_search_client
        >>> config = usd_search_client.Configuration(host = "http://api.my-usd-search-instance.example.com")
        >>> async with usd_search_client.ApiClient(config) as api_client:
        ...     search_request = usd_search_client.BasicSearchRequest(
        ...         description="box",
        ...         return_metadata=True,
        ...         return_images=True,
        ...         limit=10
        ...     )
        ...     response = await usd_search_client.search(search_request, api_client=api_client)
        ...     print(response)

    Returns:
        List[BasicSearchResponse]: The search response.
    """
    return await AISearchApi(api_client=api_client).search_post_v2_deepsearch_search_post(search_request)

async def search_hybrid(search_request: BasicSearchRequest, api_client: Optional[ApiClient] = None) -> List[HybridSearchResponse]:
    """
    Hybrid search for items in the database.

    Args:
        search_request (BasicSearchRequest): The search request.

    Examples:
        >>> import usd_search_client
        >>> config = usd_search_client.Configuration(host = "http://api.my-usd-search-instance.example.com")
        >>> async with usd_search_client.ApiClient(config) as api_client:
        ...     search_request = usd_search_client.BasicSearchRequest(
        ...         hybrid_text_query="red car",
        ...         vector_queries=[
        ...             usd_search_client.VectorQuery(
        ...                 field_name="clip-embedding.embedding",
        ...                 query_type=usd_search_client.VectorQueryType.TEXT,
        ...                 query=usd_search_client.Query(actual_instance="red car")
        ...             )
        ...         ],
        ...         return_metadata=True,
        ...         return_images=True,
        ...         limit=10
        ...     )
        ...     response = await usd_search_client.search_hybrid(search_request, api_client=api_client)
        ...     print(response)

    Returns:
        List[HybridSearchResponse]: The search response.
    """
    return await AISearchApi(api_client=api_client)._search_hybrid_post(search_request)

async def get_images(asset_url: Optional[str] = None, image_key: Optional[str] = None, img_offset: Optional[int] = None, api_client: Optional[ApiClient] = None) -> bytes:
    """
    Get images of an asset.

    Args:
        asset_url (Optional[str]): The URL of the asset.
        image_key (Optional[str]): The key of the image.
        img_offset (Optional[int]): The offset of the image.

    Examples:

        >>> import usd_search_client
        >>> import io
        >>> from PIL import Image
        >>> config = usd_search_client.Configuration(host = "http://api.my-usd-search-instance.example.com")
        >>> async with usd_search_client.ApiClient(config) as api_client:
        ...    response = await usd_search_client.get_images(asset_url="https://api.my-usd-search-instance.example.com/assets/123.usd", api_client=api_client)
        ...    with io.BytesIO(response) as image_file:
        ...        image = Image.open(image_file)
        ...        image.show()

    Returns:
        bytes: The image data.
    """
    return await ImagesApi(api_client=api_client)._images_get(
        asset_url=asset_url,
        image_key=image_key,
        img_offset=img_offset,
    )

async def get_dependencies(root_node_url: str, max_level: Optional[int] = None, limit: Optional[int] = None, flat: Optional[bool] = None, inverse: Optional[bool] = None, api_client: Optional[ApiClient] = None) -> Union[List[Asset], AssetGraph]:
    """
    Get dependencies of an asset.

    Args:
        root_node_url (str): The URL of the root asset.
        max_level (Optional[int]): The maximum level of the dependency graph.
        limit (Optional[int]): The maximum number of dependencies to return.
        flat (Optional[bool]): Whether to return the dependencies in a flat list. If True, the dependencies will be returned as a list of assets. If False, the dependencies will be returned as an asset graph.
        inverse (Optional[bool]): Whether to return the inverse dependencies. If True, the inverse dependencies will be returned. If False, the dependencies will be returned.

    Examples:

        >>> import usd_search_client
        >>> config = usd_search_client.Configuration(host = "http://api.my-usd-search-instance.example.com")
        >>> async with usd_search_client.ApiClient(config) as api_client:
        ...    response = await usd_search_client.get_dependencies(root_node_url="https://api.my-usd-search-instance.example.com/assets/123.usd", api_client=api_client)
        ...    print(response)

    Returns:
        Union[List[Asset], AssetGraph]: A list of assets or an asset graph.
    """
    ags_api = AGSAssetGraphApi(api_client=api_client)

    if flat:
        if inverse:
            return await ags_api.get_dependencies_inverse_dependency_graph_inverse_flat_get(
                root_node_url=root_node_url,
                max_level=max_level,
                limit=limit,
            )
        else:
            return await ags_api.get_dependencies_flat_dependency_graph_flat_get(
            root_node_url=root_node_url,
            max_level=max_level,
            limit=limit,
        )
    else:
        if inverse:
            return await ags_api.get_inverse_dependencies_graph_dependency_graph_inverse_graph_get(
                root_node_url=root_node_url,
                max_level=max_level,
                limit=limit,
            )
        else:
            return await ags_api.get_dependencies_graph_dependency_graph_graph_get(
                root_node_url=root_node_url,
                max_level=max_level,
                limit=limit,
            )

async def get_scene_summary(scene_url: str, api_client: Optional[ApiClient] = None) -> SceneSummaryResponse:
    """
    Get the summary of a scene.

    Args:
        scene_url (str): The URL of the scene.

    Examples:

        >>> import usd_search_client
        >>> config = usd_search_client.Configuration(host = "http://api.my-usd-search-instance.example.com")
        >>> async with usd_search_client.ApiClient(config) as api_client:
        ...    response = await usd_search_client.get_scene_summary(scene_url="https://api.my-usd-search-instance.example.com/assets/123.usd", api_client=api_client)
        ...    print(response)

    Returns:
        SceneSummaryResponse: The summary of the scene.
    """
    return await AGSSceneGraphApi(api_client=api_client).scene_summary_asset_graph_usd_scene_summary_get(scene_url=scene_url)