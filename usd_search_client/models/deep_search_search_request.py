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


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from usd_search_client.models.search_method import SearchMethod
from typing import Optional, Set
from typing_extensions import Self

class DeepSearchSearchRequest(BaseModel):
    """
    DeepSearchSearchRequest
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Conduct text-based searches powered by AI")
    image_similarity_search: Optional[List[StrictStr]] = Field(default=None, description="Perform similarity searches based on images")
    file_name: Optional[StrictStr] = Field(default=None, description="Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    exclude_file_name: Optional[StrictStr] = Field(default=None, description="Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    file_extension_include: Optional[StrictStr] = Field(default=None, description="Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    file_extension_exclude: Optional[StrictStr] = Field(default=None, description="Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    created_after: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include assets created after a specified date")
    created_before: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include assets created before a specified date")
    modified_after: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include assets modified after a specified date")
    modified_before: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include assets modified before a specified date")
    file_size_greater_than: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include files larger than a specific size")
    file_size_less_than: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Filter results to only include files smaller than a specific size")
    created_by: Optional[StrictStr] = Field(default=None, description="Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")
    exclude_created_by: Optional[StrictStr] = Field(default=None, description="Exclude assets created by a specific user from the results")
    modified_by: Optional[StrictStr] = Field(default=None, description="Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email.")
    exclude_modified_by: Optional[StrictStr] = Field(default=None, description="Exclude assets modified by a specific user from the results")
    similarity_threshold: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = Field(default=None, description="Set the similarity threshold for embedding-based searches. This functionality allows filtering duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range.")
    cutoff_threshold: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Set the cutoff threshold for embedding-based searches")
    search_path: Optional[StrictStr] = Field(default=None, description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    exclude_search_path: Optional[StrictStr] = Field(default=None, description="Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND.")
    search_in_scene: Optional[StrictStr] = Field(default=None, description="Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix.")
    filter_by_properties: Optional[StrictStr] = Field(default=None, description="Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`")
    min_bbox_x: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by minimum X axis dimension of the asset's bounding box")
    min_bbox_y: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by minimum Y axis dimension of the asset's bounding box")
    min_bbox_z: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by minimum Z axis dimension of the asset's bounding box")
    max_bbox_x: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by maximum X axis dimension of the asset's bounding box")
    max_bbox_y: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by maximum Y axis dimension of the asset's bounding box")
    max_bbox_z: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Filter by maximum Z axis dimension of the asset's bounding box")
    return_images: Optional[StrictBool] = Field(default=False, description="Return images if set to True")
    return_metadata: Optional[StrictBool] = Field(default=False, description="Return metadata if set to True")
    return_root_prims: Optional[StrictBool] = Field(default=False, description="Return root prims if set to True")
    return_predictions: Optional[StrictBool] = Field(default=False, description="Return predictions if set to True")
    return_in_scene_instances_prims: Optional[StrictBool] = Field(default=False, description="[in-scene search only] Return prims of instances of objects found in the scene")
    embedding_knn_search_method: Optional[SearchMethod] = Field(default=None, description="Search method, approximate should be faster but is less accurate. Default is exact")
    limit: Optional[Annotated[int, Field(le=10000, strict=True)]] = Field(default=None, description="Set the maximum number of results to return from the search, default is 32")
    vision_metadata: Optional[StrictStr] = Field(default=None, description="Uses a keyword match query on metadata fields that were generated using Vision Language Models")
    return_vision_generated_metadata: Optional[StrictBool] = Field(default=False, description="Returns the metadata fields that were generated using Vision Language Models")
    __properties: ClassVar[List[str]] = ["description", "image_similarity_search", "file_name", "exclude_file_name", "file_extension_include", "file_extension_exclude", "created_after", "created_before", "modified_after", "modified_before", "file_size_greater_than", "file_size_less_than", "created_by", "exclude_created_by", "modified_by", "exclude_modified_by", "similarity_threshold", "cutoff_threshold", "search_path", "exclude_search_path", "search_in_scene", "filter_by_properties", "min_bbox_x", "min_bbox_y", "min_bbox_z", "max_bbox_x", "max_bbox_y", "max_bbox_z", "return_images", "return_metadata", "return_root_prims", "return_predictions", "return_in_scene_instances_prims", "embedding_knn_search_method", "limit", "vision_metadata", "return_vision_generated_metadata"]

    @field_validator('created_after')
    def created_after_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(r"must validate the regular expression /\d{4}-\d{2}-\d{2}/")
        return value

    @field_validator('created_before')
    def created_before_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(r"must validate the regular expression /\d{4}-\d{2}-\d{2}/")
        return value

    @field_validator('modified_after')
    def modified_after_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(r"must validate the regular expression /\d{4}-\d{2}-\d{2}/")
        return value

    @field_validator('modified_before')
    def modified_before_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(r"must validate the regular expression /\d{4}-\d{2}-\d{2}/")
        return value

    @field_validator('file_size_greater_than')
    def file_size_greater_than_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d+[KMGT]B", value):
            raise ValueError(r"must validate the regular expression /\d+[KMGT]B/")
        return value

    @field_validator('file_size_less_than')
    def file_size_less_than_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"\d+[KMGT]B", value):
            raise ValueError(r"must validate the regular expression /\d+[KMGT]B/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DeepSearchSearchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeepSearchSearchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "image_similarity_search": obj.get("image_similarity_search"),
            "file_name": obj.get("file_name"),
            "exclude_file_name": obj.get("exclude_file_name"),
            "file_extension_include": obj.get("file_extension_include"),
            "file_extension_exclude": obj.get("file_extension_exclude"),
            "created_after": obj.get("created_after"),
            "created_before": obj.get("created_before"),
            "modified_after": obj.get("modified_after"),
            "modified_before": obj.get("modified_before"),
            "file_size_greater_than": obj.get("file_size_greater_than"),
            "file_size_less_than": obj.get("file_size_less_than"),
            "created_by": obj.get("created_by"),
            "exclude_created_by": obj.get("exclude_created_by"),
            "modified_by": obj.get("modified_by"),
            "exclude_modified_by": obj.get("exclude_modified_by"),
            "similarity_threshold": obj.get("similarity_threshold"),
            "cutoff_threshold": obj.get("cutoff_threshold"),
            "search_path": obj.get("search_path"),
            "exclude_search_path": obj.get("exclude_search_path"),
            "search_in_scene": obj.get("search_in_scene"),
            "filter_by_properties": obj.get("filter_by_properties"),
            "min_bbox_x": obj.get("min_bbox_x"),
            "min_bbox_y": obj.get("min_bbox_y"),
            "min_bbox_z": obj.get("min_bbox_z"),
            "max_bbox_x": obj.get("max_bbox_x"),
            "max_bbox_y": obj.get("max_bbox_y"),
            "max_bbox_z": obj.get("max_bbox_z"),
            "return_images": obj.get("return_images") if obj.get("return_images") is not None else False,
            "return_metadata": obj.get("return_metadata") if obj.get("return_metadata") is not None else False,
            "return_root_prims": obj.get("return_root_prims") if obj.get("return_root_prims") is not None else False,
            "return_predictions": obj.get("return_predictions") if obj.get("return_predictions") is not None else False,
            "return_in_scene_instances_prims": obj.get("return_in_scene_instances_prims") if obj.get("return_in_scene_instances_prims") is not None else False,
            "embedding_knn_search_method": obj.get("embedding_knn_search_method"),
            "limit": obj.get("limit"),
            "vision_metadata": obj.get("vision_metadata"),
            "return_vision_generated_metadata": obj.get("return_vision_generated_metadata") if obj.get("return_vision_generated_metadata") is not None else False
        })
        return _obj


