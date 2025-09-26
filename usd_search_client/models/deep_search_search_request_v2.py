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

    # USD Search API Overview **USD Search API** is a collection of cloud-native microservices that enable developers, creators, and workflow specialists to efficiently search through vast collections of OpenUSD data, images, and other assets using natural language or image-based inputs. With these production-ready microservices, developers can deploy USD Search API onto their own infrastructure. With USD Search API’s artificial intelligence (AI) features, you can quickly locate untagged and unstructured 3D data and digital assets, saving time navigating unstructured, untagged 3D data. USD Search API is capable of searching and indexing 3D asset databases, as well as navigating complex 3D scenes to perform spatial searches, without requiring manual tagging of assets. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from usd_search_client.models.scoring_config import ScoringConfig
from usd_search_client.models.search_method import SearchMethod
from usd_search_client.models.vector_query import VectorQuery
from typing import Optional, Set
from typing_extensions import Self

class DeepSearchSearchRequestV2(BaseModel):
    """
    DeepSearchSearchRequestV2
    """ # noqa: E501
    description: Optional[StrictStr] = None
    image_similarity_search: Optional[Annotated[List[StrictStr], Field(max_length=10)]] = None
    file_name: Optional[StrictStr] = None
    exclude_file_name: Optional[StrictStr] = None
    file_extension_include: Optional[StrictStr] = None
    file_extension_exclude: Optional[StrictStr] = None
    created_after: Optional[StrictStr] = None
    created_before: Optional[StrictStr] = None
    modified_after: Optional[StrictStr] = None
    modified_before: Optional[StrictStr] = None
    file_size_greater_than: Optional[Annotated[str, Field(strict=True)]] = None
    file_size_less_than: Optional[Annotated[str, Field(strict=True)]] = None
    created_by: Optional[StrictStr] = None
    exclude_created_by: Optional[StrictStr] = None
    modified_by: Optional[StrictStr] = None
    exclude_modified_by: Optional[StrictStr] = None
    similarity_threshold: Optional[Union[Annotated[float, Field(le=2, strict=True, ge=0)], Annotated[int, Field(le=2, strict=True, ge=0)]]] = None
    cutoff_threshold: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    search_path: Optional[StrictStr] = None
    exclude_search_path: Optional[StrictStr] = None
    filter_url_regexp: Optional[StrictStr] = None
    search_in_scene: Optional[StrictStr] = None
    filter_by_properties: Optional[StrictStr] = None
    min_bbox_x: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    min_bbox_y: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    min_bbox_z: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    max_bbox_x: Optional[Union[StrictFloat, StrictInt]] = None
    max_bbox_y: Optional[Union[StrictFloat, StrictInt]] = None
    max_bbox_z: Optional[Union[StrictFloat, StrictInt]] = None
    bbox_use_scaled_dimensions: Optional[StrictBool] = Field(default=True, description="Use scaled dimensions for bounding box filtering")
    return_images: Optional[StrictBool] = Field(default=False, description="Return images if set to True")
    return_metadata: Optional[StrictBool] = Field(default=False, description="Return metadata if set to True")
    return_root_prims: Optional[StrictBool] = Field(default=False, description="Return root prims if set to True")
    return_default_prims: Optional[StrictBool] = Field(default=False, description="Return default prims if set to True")
    return_predictions: Optional[StrictBool] = Field(default=False, description="Return predictions if set to True")
    return_in_scene_instances_prims: Optional[StrictBool] = Field(default=False, description="[in-scene search only] Return prims of instances of objects found in the scene")
    embedding_knn_search_method: Optional[SearchMethod] = None
    limit: Optional[Annotated[int, Field(le=10000, strict=True)]] = None
    vision_metadata: Optional[StrictStr] = None
    return_vision_generated_metadata: Optional[StrictBool] = Field(default=False, description="Returns the metadata fields that were generated using Vision Language Models")
    return_inner_hits: Optional[StrictBool] = Field(default=False, description="Return inner hits from nested queries")
    scoring_config: Optional[ScoringConfig] = None
    hybrid_text_query: Optional[StrictStr] = None
    vector_queries: Optional[List[VectorQuery]] = Field(default=None, description="Generic vector queries for different fields")
    return_embeddings: Optional[StrictBool] = Field(default=False, description="Return embeddings for search results")
    return_tags: Optional[StrictBool] = Field(default=False, description="Return tags for search results")
    return_usd_properties: Optional[StrictBool] = Field(default=False, description="Return USD properties for search results")
    return_usd_dimensions: Optional[StrictBool] = Field(default=False, description="Return USD dimensions for search results")
    deduplicate_by_hash: Optional[StrictBool] = Field(default=False, description="Return only items with unique hash_value using OpenSearch collapse")
    __properties: ClassVar[List[str]] = ["description", "image_similarity_search", "file_name", "exclude_file_name", "file_extension_include", "file_extension_exclude", "created_after", "created_before", "modified_after", "modified_before", "file_size_greater_than", "file_size_less_than", "created_by", "exclude_created_by", "modified_by", "exclude_modified_by", "similarity_threshold", "cutoff_threshold", "search_path", "exclude_search_path", "filter_url_regexp", "search_in_scene", "filter_by_properties", "min_bbox_x", "min_bbox_y", "min_bbox_z", "max_bbox_x", "max_bbox_y", "max_bbox_z", "bbox_use_scaled_dimensions", "return_images", "return_metadata", "return_root_prims", "return_default_prims", "return_predictions", "return_in_scene_instances_prims", "embedding_knn_search_method", "limit", "vision_metadata", "return_vision_generated_metadata", "return_inner_hits", "scoring_config", "hybrid_text_query", "vector_queries", "return_embeddings", "return_tags", "return_usd_properties", "return_usd_dimensions", "deduplicate_by_hash"]

    @field_validator('file_size_greater_than')
    def file_size_greater_than_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+[KMGT]B$", value):
            raise ValueError(r"must validate the regular expression /^\d+[KMGT]B$/")
        return value

    @field_validator('file_size_less_than')
    def file_size_less_than_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+[KMGT]B$", value):
            raise ValueError(r"must validate the regular expression /^\d+[KMGT]B$/")
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
        """Create an instance of DeepSearchSearchRequestV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scoring_config
        if self.scoring_config:
            _dict['scoring_config'] = self.scoring_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vector_queries (list)
        _items = []
        if self.vector_queries:
            for _item_vector_queries in self.vector_queries:
                if _item_vector_queries:
                    _items.append(_item_vector_queries.to_dict())
            _dict['vector_queries'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if image_similarity_search (nullable) is None
        # and model_fields_set contains the field
        if self.image_similarity_search is None and "image_similarity_search" in self.model_fields_set:
            _dict['image_similarity_search'] = None

        # set to None if file_name (nullable) is None
        # and model_fields_set contains the field
        if self.file_name is None and "file_name" in self.model_fields_set:
            _dict['file_name'] = None

        # set to None if exclude_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_file_name is None and "exclude_file_name" in self.model_fields_set:
            _dict['exclude_file_name'] = None

        # set to None if file_extension_include (nullable) is None
        # and model_fields_set contains the field
        if self.file_extension_include is None and "file_extension_include" in self.model_fields_set:
            _dict['file_extension_include'] = None

        # set to None if file_extension_exclude (nullable) is None
        # and model_fields_set contains the field
        if self.file_extension_exclude is None and "file_extension_exclude" in self.model_fields_set:
            _dict['file_extension_exclude'] = None

        # set to None if created_after (nullable) is None
        # and model_fields_set contains the field
        if self.created_after is None and "created_after" in self.model_fields_set:
            _dict['created_after'] = None

        # set to None if created_before (nullable) is None
        # and model_fields_set contains the field
        if self.created_before is None and "created_before" in self.model_fields_set:
            _dict['created_before'] = None

        # set to None if modified_after (nullable) is None
        # and model_fields_set contains the field
        if self.modified_after is None and "modified_after" in self.model_fields_set:
            _dict['modified_after'] = None

        # set to None if modified_before (nullable) is None
        # and model_fields_set contains the field
        if self.modified_before is None and "modified_before" in self.model_fields_set:
            _dict['modified_before'] = None

        # set to None if file_size_greater_than (nullable) is None
        # and model_fields_set contains the field
        if self.file_size_greater_than is None and "file_size_greater_than" in self.model_fields_set:
            _dict['file_size_greater_than'] = None

        # set to None if file_size_less_than (nullable) is None
        # and model_fields_set contains the field
        if self.file_size_less_than is None and "file_size_less_than" in self.model_fields_set:
            _dict['file_size_less_than'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if exclude_created_by (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_created_by is None and "exclude_created_by" in self.model_fields_set:
            _dict['exclude_created_by'] = None

        # set to None if modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by is None and "modified_by" in self.model_fields_set:
            _dict['modified_by'] = None

        # set to None if exclude_modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_modified_by is None and "exclude_modified_by" in self.model_fields_set:
            _dict['exclude_modified_by'] = None

        # set to None if similarity_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.similarity_threshold is None and "similarity_threshold" in self.model_fields_set:
            _dict['similarity_threshold'] = None

        # set to None if cutoff_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.cutoff_threshold is None and "cutoff_threshold" in self.model_fields_set:
            _dict['cutoff_threshold'] = None

        # set to None if search_path (nullable) is None
        # and model_fields_set contains the field
        if self.search_path is None and "search_path" in self.model_fields_set:
            _dict['search_path'] = None

        # set to None if exclude_search_path (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_search_path is None and "exclude_search_path" in self.model_fields_set:
            _dict['exclude_search_path'] = None

        # set to None if filter_url_regexp (nullable) is None
        # and model_fields_set contains the field
        if self.filter_url_regexp is None and "filter_url_regexp" in self.model_fields_set:
            _dict['filter_url_regexp'] = None

        # set to None if search_in_scene (nullable) is None
        # and model_fields_set contains the field
        if self.search_in_scene is None and "search_in_scene" in self.model_fields_set:
            _dict['search_in_scene'] = None

        # set to None if filter_by_properties (nullable) is None
        # and model_fields_set contains the field
        if self.filter_by_properties is None and "filter_by_properties" in self.model_fields_set:
            _dict['filter_by_properties'] = None

        # set to None if min_bbox_x (nullable) is None
        # and model_fields_set contains the field
        if self.min_bbox_x is None and "min_bbox_x" in self.model_fields_set:
            _dict['min_bbox_x'] = None

        # set to None if min_bbox_y (nullable) is None
        # and model_fields_set contains the field
        if self.min_bbox_y is None and "min_bbox_y" in self.model_fields_set:
            _dict['min_bbox_y'] = None

        # set to None if min_bbox_z (nullable) is None
        # and model_fields_set contains the field
        if self.min_bbox_z is None and "min_bbox_z" in self.model_fields_set:
            _dict['min_bbox_z'] = None

        # set to None if max_bbox_x (nullable) is None
        # and model_fields_set contains the field
        if self.max_bbox_x is None and "max_bbox_x" in self.model_fields_set:
            _dict['max_bbox_x'] = None

        # set to None if max_bbox_y (nullable) is None
        # and model_fields_set contains the field
        if self.max_bbox_y is None and "max_bbox_y" in self.model_fields_set:
            _dict['max_bbox_y'] = None

        # set to None if max_bbox_z (nullable) is None
        # and model_fields_set contains the field
        if self.max_bbox_z is None and "max_bbox_z" in self.model_fields_set:
            _dict['max_bbox_z'] = None

        # set to None if embedding_knn_search_method (nullable) is None
        # and model_fields_set contains the field
        if self.embedding_knn_search_method is None and "embedding_knn_search_method" in self.model_fields_set:
            _dict['embedding_knn_search_method'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if vision_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.vision_metadata is None and "vision_metadata" in self.model_fields_set:
            _dict['vision_metadata'] = None

        # set to None if scoring_config (nullable) is None
        # and model_fields_set contains the field
        if self.scoring_config is None and "scoring_config" in self.model_fields_set:
            _dict['scoring_config'] = None

        # set to None if hybrid_text_query (nullable) is None
        # and model_fields_set contains the field
        if self.hybrid_text_query is None and "hybrid_text_query" in self.model_fields_set:
            _dict['hybrid_text_query'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeepSearchSearchRequestV2 from a dict"""
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
            "filter_url_regexp": obj.get("filter_url_regexp"),
            "search_in_scene": obj.get("search_in_scene"),
            "filter_by_properties": obj.get("filter_by_properties"),
            "min_bbox_x": obj.get("min_bbox_x"),
            "min_bbox_y": obj.get("min_bbox_y"),
            "min_bbox_z": obj.get("min_bbox_z"),
            "max_bbox_x": obj.get("max_bbox_x"),
            "max_bbox_y": obj.get("max_bbox_y"),
            "max_bbox_z": obj.get("max_bbox_z"),
            "bbox_use_scaled_dimensions": obj.get("bbox_use_scaled_dimensions") if obj.get("bbox_use_scaled_dimensions") is not None else True,
            "return_images": obj.get("return_images") if obj.get("return_images") is not None else False,
            "return_metadata": obj.get("return_metadata") if obj.get("return_metadata") is not None else False,
            "return_root_prims": obj.get("return_root_prims") if obj.get("return_root_prims") is not None else False,
            "return_default_prims": obj.get("return_default_prims") if obj.get("return_default_prims") is not None else False,
            "return_predictions": obj.get("return_predictions") if obj.get("return_predictions") is not None else False,
            "return_in_scene_instances_prims": obj.get("return_in_scene_instances_prims") if obj.get("return_in_scene_instances_prims") is not None else False,
            "embedding_knn_search_method": obj.get("embedding_knn_search_method"),
            "limit": obj.get("limit"),
            "vision_metadata": obj.get("vision_metadata"),
            "return_vision_generated_metadata": obj.get("return_vision_generated_metadata") if obj.get("return_vision_generated_metadata") is not None else False,
            "return_inner_hits": obj.get("return_inner_hits") if obj.get("return_inner_hits") is not None else False,
            "scoring_config": ScoringConfig.from_dict(obj["scoring_config"]) if obj.get("scoring_config") is not None else None,
            "hybrid_text_query": obj.get("hybrid_text_query"),
            "vector_queries": [VectorQuery.from_dict(_item) for _item in obj["vector_queries"]] if obj.get("vector_queries") is not None else None,
            "return_embeddings": obj.get("return_embeddings") if obj.get("return_embeddings") is not None else False,
            "return_tags": obj.get("return_tags") if obj.get("return_tags") is not None else False,
            "return_usd_properties": obj.get("return_usd_properties") if obj.get("return_usd_properties") is not None else False,
            "return_usd_dimensions": obj.get("return_usd_dimensions") if obj.get("return_usd_dimensions") is not None else False,
            "deduplicate_by_hash": obj.get("deduplicate_by_hash") if obj.get("deduplicate_by_hash") is not None else False
        })
        return _obj


