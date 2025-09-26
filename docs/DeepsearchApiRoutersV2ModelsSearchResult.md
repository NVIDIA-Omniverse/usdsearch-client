# DeepsearchApiRoutersV2ModelsSearchResult


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
**vision_generated_metadata** | **object** |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**in_scene_instance_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 
**usd_dimensions** | **object** |  | [optional] 

## Example

```python
from usd_search_client.models.deepsearch_api_routers_v2_models_search_result import DeepsearchApiRoutersV2ModelsSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeepsearchApiRoutersV2ModelsSearchResult from a JSON string
deepsearch_api_routers_v2_models_search_result_instance = DeepsearchApiRoutersV2ModelsSearchResult.from_json(json)
# print the JSON string representation of the object
print(DeepsearchApiRoutersV2ModelsSearchResult.to_json())

# convert the object into a dict
deepsearch_api_routers_v2_models_search_result_dict = deepsearch_api_routers_v2_models_search_result_instance.to_dict()
# create an instance of DeepsearchApiRoutersV2ModelsSearchResult from a dict
deepsearch_api_routers_v2_models_search_result_from_dict = DeepsearchApiRoutersV2ModelsSearchResult.from_dict(deepsearch_api_routers_v2_models_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


