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

# flake8: noqa
"""
    USD Search and Asset Graph Search APIs

    # USD Search API Overview **USD Search API** is a collection of cloud-native microservices that enable developers, creators, and workflow specialists to efficiently search through vast collections of OpenUSD data, images, and other assets using natural language or image-based inputs. With these production-ready microservices, developers can deploy USD Search API onto their own infrastructure.  With USD Search API’s artificial intelligence (AI) features, you can quickly locate untagged and unstructured 3D data and digital assets, saving time navigating unstructured, untagged 3D data. USD Search API is capable of searching and indexing 3D asset databases, as well as navigating complex 3D scenes to perform spatial searches, without requiring manual tagging of assets. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from usd_search_client.models.axis import AXIS
from usd_search_client.models.asset import Asset
from usd_search_client.models.asset_graph import AssetGraph
from usd_search_client.models.asset_graph1 import AssetGraph1
from usd_search_client.models.asset_relationship import AssetRelationship
from usd_search_client.models.backend_status_type import BackendStatusType
from usd_search_client.models.deep_search_search_request import DeepSearchSearchRequest
from usd_search_client.models.edge_type import EdgeType
from usd_search_client.models.edge_type1 import EdgeType1
from usd_search_client.models.empty import Empty
from usd_search_client.models.event import Event
from usd_search_client.models.event_mapping import EventMapping
from usd_search_client.models.http_validation_error import HTTPValidationError
from usd_search_client.models.hash_value import HashValue
from usd_search_client.models.location_inner import LocationInner
from usd_search_client.models.metadata import Metadata
from usd_search_client.models.mounted import Mounted
from usd_search_client.models.path_type import PathType
from usd_search_client.models.plugin_info import PluginInfo
from usd_search_client.models.plugin_item_status import PluginItemStatus
from usd_search_client.models.plugin_status_type import PluginStatusType
from usd_search_client.models.prediction import Prediction
from usd_search_client.models.prim import Prim
from usd_search_client.models.prim1 import Prim1
from usd_search_client.models.prim_type import PrimType
from usd_search_client.models.processing_timestamp import ProcessingTimestamp
from usd_search_client.models.scene_summary_response import SceneSummaryResponse
from usd_search_client.models.search_method import SearchMethod
from usd_search_client.models.search_result import SearchResult
from usd_search_client.models.spatial_query_response_item import SpatialQueryResponseItem
from usd_search_client.models.status_result import StatusResult
from usd_search_client.models.storage_backend_info import StorageBackendInfo
from usd_search_client.models.transaction_id import TransactionId
from usd_search_client.models.usd_path import UsdPath
from usd_search_client.models.validation_error import ValidationError
from usd_search_client.models.verify_access_request import VerifyAccessRequest
