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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from usd_search_client.models.created_date_seconds import CreatedDateSeconds
from usd_search_client.models.deleted_date_seconds import DeletedDateSeconds
from usd_search_client.models.empty import Empty
from usd_search_client.models.event import Event
from usd_search_client.models.hash_type import HashType
from usd_search_client.models.modified_date_seconds import ModifiedDateSeconds
from usd_search_client.models.mounted import Mounted
from usd_search_client.models.transaction_id import TransactionId
from typing import Optional, Set
from typing_extensions import Self

class PathType(BaseModel):
    """
    This class is used to store the information about the path of the asset.
    """ # noqa: E501
    uri: Optional[StrictStr] = None
    etag: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    event: Optional[Event] = None
    type: Optional[StrictStr] = None
    ts: Optional[Dict[str, StrictInt]] = None
    transaction_id: Optional[TransactionId] = None
    acl: Optional[List[StrictStr]] = None
    empty: Optional[Empty] = None
    mounted: Optional[Mounted] = None
    size: Optional[StrictInt] = None
    created_by: Optional[StrictStr] = None
    created_date_seconds: Optional[CreatedDateSeconds] = None
    modified_by: Optional[StrictStr] = None
    modified_date_seconds: Optional[ModifiedDateSeconds] = None
    hash_type: Optional[HashType] = None
    hash_value: Optional[StrictStr] = None
    hash_bsize: Optional[StrictInt] = None
    is_deleted: Optional[StrictBool] = None
    deleted_by: Optional[StrictStr] = None
    deleted_date_seconds: Optional[DeletedDateSeconds] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["uri", "etag", "status", "event", "type", "ts", "transaction_id", "acl", "empty", "mounted", "size", "created_by", "created_date_seconds", "modified_by", "modified_date_seconds", "hash_type", "hash_value", "hash_bsize", "is_deleted", "deleted_by", "deleted_date_seconds"]

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
        """Create an instance of PathType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction_id
        if self.transaction_id:
            _dict['transaction_id'] = self.transaction_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of empty
        if self.empty:
            _dict['empty'] = self.empty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mounted
        if self.mounted:
            _dict['mounted'] = self.mounted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_date_seconds
        if self.created_date_seconds:
            _dict['created_date_seconds'] = self.created_date_seconds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_date_seconds
        if self.modified_date_seconds:
            _dict['modified_date_seconds'] = self.modified_date_seconds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hash_type
        if self.hash_type:
            _dict['hash_type'] = self.hash_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleted_date_seconds
        if self.deleted_date_seconds:
            _dict['deleted_date_seconds'] = self.deleted_date_seconds.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict['uri'] = None

        # set to None if etag (nullable) is None
        # and model_fields_set contains the field
        if self.etag is None and "etag" in self.model_fields_set:
            _dict['etag'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if event (nullable) is None
        # and model_fields_set contains the field
        if self.event is None and "event" in self.model_fields_set:
            _dict['event'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if ts (nullable) is None
        # and model_fields_set contains the field
        if self.ts is None and "ts" in self.model_fields_set:
            _dict['ts'] = None

        # set to None if transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_id is None and "transaction_id" in self.model_fields_set:
            _dict['transaction_id'] = None

        # set to None if acl (nullable) is None
        # and model_fields_set contains the field
        if self.acl is None and "acl" in self.model_fields_set:
            _dict['acl'] = None

        # set to None if empty (nullable) is None
        # and model_fields_set contains the field
        if self.empty is None and "empty" in self.model_fields_set:
            _dict['empty'] = None

        # set to None if mounted (nullable) is None
        # and model_fields_set contains the field
        if self.mounted is None and "mounted" in self.model_fields_set:
            _dict['mounted'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if created_date_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.created_date_seconds is None and "created_date_seconds" in self.model_fields_set:
            _dict['created_date_seconds'] = None

        # set to None if modified_by (nullable) is None
        # and model_fields_set contains the field
        if self.modified_by is None and "modified_by" in self.model_fields_set:
            _dict['modified_by'] = None

        # set to None if modified_date_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.modified_date_seconds is None and "modified_date_seconds" in self.model_fields_set:
            _dict['modified_date_seconds'] = None

        # set to None if hash_type (nullable) is None
        # and model_fields_set contains the field
        if self.hash_type is None and "hash_type" in self.model_fields_set:
            _dict['hash_type'] = None

        # set to None if hash_value (nullable) is None
        # and model_fields_set contains the field
        if self.hash_value is None and "hash_value" in self.model_fields_set:
            _dict['hash_value'] = None

        # set to None if hash_bsize (nullable) is None
        # and model_fields_set contains the field
        if self.hash_bsize is None and "hash_bsize" in self.model_fields_set:
            _dict['hash_bsize'] = None

        # set to None if is_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_deleted is None and "is_deleted" in self.model_fields_set:
            _dict['is_deleted'] = None

        # set to None if deleted_by (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_by is None and "deleted_by" in self.model_fields_set:
            _dict['deleted_by'] = None

        # set to None if deleted_date_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_date_seconds is None and "deleted_date_seconds" in self.model_fields_set:
            _dict['deleted_date_seconds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "etag": obj.get("etag"),
            "status": obj.get("status"),
            "event": Event.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "type": obj.get("type"),
            "ts": obj.get("ts"),
            "transaction_id": TransactionId.from_dict(obj["transaction_id"]) if obj.get("transaction_id") is not None else None,
            "acl": obj.get("acl"),
            "empty": Empty.from_dict(obj["empty"]) if obj.get("empty") is not None else None,
            "mounted": Mounted.from_dict(obj["mounted"]) if obj.get("mounted") is not None else None,
            "size": obj.get("size"),
            "created_by": obj.get("created_by"),
            "created_date_seconds": CreatedDateSeconds.from_dict(obj["created_date_seconds"]) if obj.get("created_date_seconds") is not None else None,
            "modified_by": obj.get("modified_by"),
            "modified_date_seconds": ModifiedDateSeconds.from_dict(obj["modified_date_seconds"]) if obj.get("modified_date_seconds") is not None else None,
            "hash_type": HashType.from_dict(obj["hash_type"]) if obj.get("hash_type") is not None else None,
            "hash_value": obj.get("hash_value"),
            "hash_bsize": obj.get("hash_bsize"),
            "is_deleted": obj.get("is_deleted"),
            "deleted_by": obj.get("deleted_by"),
            "deleted_date_seconds": DeletedDateSeconds.from_dict(obj["deleted_date_seconds"]) if obj.get("deleted_date_seconds") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


