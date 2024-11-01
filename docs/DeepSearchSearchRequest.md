# DeepSearchSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Conduct text-based searches powered by AI | [optional] 
**image_similarity_search** | **List[str]** | Perform similarity searches based on images | [optional] 
**file_name** | **str** | Filter results by asset file name, allowing partial matches. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**exclude_file_name** | **str** | Exclude results by asset file name, allowing partial matches. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**file_extension_include** | **str** | Filter results by file extension. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**file_extension_exclude** | **str** | Exclude results by file extension. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**created_after** | **str** | Filter results to only include assets created after a specified date | [optional] 
**created_before** | **str** | Filter results to only include assets created before a specified date | [optional] 
**modified_after** | **str** | Filter results to only include assets modified after a specified date | [optional] 
**modified_before** | **str** | Filter results to only include assets modified before a specified date | [optional] 
**file_size_greater_than** | **str** | Filter results to only include files larger than a specific size | [optional] 
**file_size_less_than** | **str** | Filter results to only include files smaller than a specific size | [optional] 
**created_by** | **str** | Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner&#39;s ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. | [optional] 
**exclude_created_by** | **str** | Exclude assets created by a specific user from the results | [optional] 
**modified_by** | **str** | Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner&#39;s ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. | [optional] 
**exclude_modified_by** | **str** | Exclude assets modified by a specific user from the results | [optional] 
**similarity_threshold** | **float** | Set the similarity threshold for embedding-based searches. This functionality allows filtering duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range. | [optional] 
**cutoff_threshold** | **float** | Set the cutoff threshold for embedding-based searches | [optional] 
**search_path** | **str** | Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**exclude_search_path** | **str** | Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] 
**search_in_scene** | **str** | Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix. | [optional] 
**filter_by_properties** | **str** | Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: &#x60;attribute1&#x3D;abc,attribute2&#x3D;456&#x60; | [optional] 
**min_bbox_x** | **float** | Filter by minimum X axis dimension of the asset&#39;s bounding box | [optional] 
**min_bbox_y** | **float** | Filter by minimum Y axis dimension of the asset&#39;s bounding box | [optional] 
**min_bbox_z** | **float** | Filter by minimum Z axis dimension of the asset&#39;s bounding box | [optional] 
**max_bbox_x** | **float** | Filter by maximum X axis dimension of the asset&#39;s bounding box | [optional] 
**max_bbox_y** | **float** | Filter by maximum Y axis dimension of the asset&#39;s bounding box | [optional] 
**max_bbox_z** | **float** | Filter by maximum Z axis dimension of the asset&#39;s bounding box | [optional] 
**return_images** | **bool** | Return images if set to True | [optional] [default to False]
**return_metadata** | **bool** | Return metadata if set to True | [optional] [default to False]
**return_root_prims** | **bool** | Return root prims if set to True | [optional] [default to False]
**return_predictions** | **bool** | Return predictions if set to True | [optional] [default to False]
**return_in_scene_instances_prims** | **bool** | [in-scene search only] Return prims of instances of objects found in the scene | [optional] [default to False]
**embedding_knn_search_method** | [**SearchMethod**](SearchMethod.md) | Search method, approximate should be faster but is less accurate. Default is exact | [optional] 
**limit** | **int** | Set the maximum number of results to return from the search, default is 32 | [optional] 
**vision_metadata** | **str** | Uses a keyword match query on metadata fields that were generated using Vision Language Models | [optional] 
**return_vision_generated_metadata** | **bool** | Returns the metadata fields that were generated using Vision Language Models | [optional] [default to False]

## Example

```python
from usd_search_client.models.deep_search_search_request import DeepSearchSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeepSearchSearchRequest from a JSON string
deep_search_search_request_instance = DeepSearchSearchRequest.from_json(json)
# print the JSON string representation of the object
print(DeepSearchSearchRequest.to_json())

# convert the object into a dict
deep_search_search_request_dict = deep_search_search_request_instance.to_dict()
# create an instance of DeepSearchSearchRequest from a dict
deep_search_search_request_from_dict = DeepSearchSearchRequest.from_dict(deep_search_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


