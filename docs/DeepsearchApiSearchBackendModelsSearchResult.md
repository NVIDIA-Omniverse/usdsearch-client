# DeepsearchApiSearchBackendModelsSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**score** | **float** |  | 
**rrf_score** | **float** |  | 
**metadata** | [**SearchResultMetadata**](SearchResultMetadata.md) |  | 
**source** | **object** |  | 
**inner_hits** | **object** |  | [optional] 
**ags_data** | [**AGSAssetData**](AGSAssetData.md) |  | [optional] 
**thumbnail_exists** | **bool** |  | [optional] 

## Example

```python
from usd_search_client.models.deepsearch_api_search_backend_models_search_result import DeepsearchApiSearchBackendModelsSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeepsearchApiSearchBackendModelsSearchResult from a JSON string
deepsearch_api_search_backend_models_search_result_instance = DeepsearchApiSearchBackendModelsSearchResult.from_json(json)
# print the JSON string representation of the object
print(DeepsearchApiSearchBackendModelsSearchResult.to_json())

# convert the object into a dict
deepsearch_api_search_backend_models_search_result_dict = deepsearch_api_search_backend_models_search_result_instance.to_dict()
# create an instance of DeepsearchApiSearchBackendModelsSearchResult from a dict
deepsearch_api_search_backend_models_search_result_from_dict = DeepsearchApiSearchBackendModelsSearchResult.from_dict(deepsearch_api_search_backend_models_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


