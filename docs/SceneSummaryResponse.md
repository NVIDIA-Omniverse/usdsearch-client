# SceneSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_url** | **str** |  | 
**scene_mpu** | **float** |  | 
**scene_up_axis** | [**AXIS**](AXIS.md) |  | 
**n_prims** | **int** | Number of prims in the scene. | 
**prim_types** | **Dict[str, int]** | Number of prims per type. | 
**unique_property_keys** | **Dict[str, int]** | Number of unique property keys. | 
**unique_properties** | **Dict[str, int]** | Number of unique property (key,value) pairs. | 
**referenced_assets** | **Dict[str, int]** | Number of unique assets referenced by the scene. | 
**default_prim** | [**Prim**](Prim.md) |  | [optional] 

## Example

```python
from usd_search_client.models.scene_summary_response import SceneSummaryResponse

# update the JSON string below
json = "{}"
# create an instance of SceneSummaryResponse from a JSON string
scene_summary_response_instance = SceneSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(SceneSummaryResponse.to_json())

# convert the object into a dict
scene_summary_response_dict = scene_summary_response_instance.to_dict()
# create an instance of SceneSummaryResponse from a dict
scene_summary_response_from_dict = SceneSummaryResponse.from_dict(scene_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


