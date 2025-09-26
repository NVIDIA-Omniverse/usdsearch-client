# DeepSearchSearchRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**image_similarity_search** | **List[str]** |  | [optional] 
**file_name** | **str** |  | [optional] 
**exclude_file_name** | **str** |  | [optional] 
**file_extension_include** | **str** |  | [optional] 
**file_extension_exclude** | **str** |  | [optional] 
**created_after** | **str** |  | [optional] 
**created_before** | **str** |  | [optional] 
**modified_after** | **str** |  | [optional] 
**modified_before** | **str** |  | [optional] 
**file_size_greater_than** | **str** |  | [optional] 
**file_size_less_than** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**exclude_created_by** | **str** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**exclude_modified_by** | **str** |  | [optional] 
**similarity_threshold** | **float** |  | [optional] 
**cutoff_threshold** | **float** |  | [optional] 
**search_path** | **str** |  | [optional] 
**exclude_search_path** | **str** |  | [optional] 
**filter_url_regexp** | **str** |  | [optional] 
**search_in_scene** | **str** |  | [optional] 
**filter_by_properties** | **str** |  | [optional] 
**min_bbox_x** | **float** |  | [optional] 
**min_bbox_y** | **float** |  | [optional] 
**min_bbox_z** | **float** |  | [optional] 
**max_bbox_x** | **float** |  | [optional] 
**max_bbox_y** | **float** |  | [optional] 
**max_bbox_z** | **float** |  | [optional] 
**bbox_use_scaled_dimensions** | **bool** | Use scaled dimensions for bounding box filtering | [optional] [default to True]
**return_images** | **bool** | Return images if set to True | [optional] [default to False]
**return_metadata** | **bool** | Return metadata if set to True | [optional] [default to False]
**return_root_prims** | **bool** | Return root prims if set to True | [optional] [default to False]
**return_default_prims** | **bool** | Return default prims if set to True | [optional] [default to False]
**return_predictions** | **bool** | Return predictions if set to True | [optional] [default to False]
**return_in_scene_instances_prims** | **bool** | [in-scene search only] Return prims of instances of objects found in the scene | [optional] [default to False]
**embedding_knn_search_method** | [**SearchMethod**](SearchMethod.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**vision_metadata** | **str** |  | [optional] 
**return_vision_generated_metadata** | **bool** | Returns the metadata fields that were generated using Vision Language Models | [optional] [default to False]
**return_inner_hits** | **bool** | Return inner hits from nested queries | [optional] [default to False]
**scoring_config** | [**ScoringConfig**](ScoringConfig.md) |  | [optional] 
**hybrid_text_query** | **str** |  | [optional] 
**vector_queries** | [**List[VectorQuery]**](VectorQuery.md) | Generic vector queries for different fields | [optional] 
**return_embeddings** | **bool** | Return embeddings for search results | [optional] [default to False]
**return_tags** | **bool** | Return tags for search results | [optional] [default to False]
**return_usd_properties** | **bool** | Return USD properties for search results | [optional] [default to False]
**return_usd_dimensions** | **bool** | Return USD dimensions for search results | [optional] [default to False]
**deduplicate_by_hash** | **bool** | Return only items with unique hash_value using OpenSearch collapse | [optional] [default to False]

## Example

```python
from usd_search_client.models.deep_search_search_request_v2 import DeepSearchSearchRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of DeepSearchSearchRequestV2 from a JSON string
deep_search_search_request_v2_instance = DeepSearchSearchRequestV2.from_json(json)
# print the JSON string representation of the object
print(DeepSearchSearchRequestV2.to_json())

# convert the object into a dict
deep_search_search_request_v2_dict = deep_search_search_request_v2_instance.to_dict()
# create an instance of DeepSearchSearchRequestV2 from a dict
deep_search_search_request_v2_from_dict = DeepSearchSearchRequestV2.from_dict(deep_search_search_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


