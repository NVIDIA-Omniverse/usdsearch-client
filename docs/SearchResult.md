# SearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the asset | 
**score** | **float** |  | 
**embed** | **str** |  | [optional] 
**root_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 
**default_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 
**image** | **str** |  | [optional] 
**predictions** | [**List[Prediction]**](Prediction.md) |  | [optional] 
**vision_generated_metadata** | **Dict[str, str]** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**in_scene_instance_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 

## Example

```python
from usd_search_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print(SearchResult.to_json())

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_from_dict = SearchResult.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

