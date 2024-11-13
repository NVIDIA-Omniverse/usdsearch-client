# Prim1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_url** | **str** |  | 
**usd_path** | **str** |  | 
**prim_type** | **str** |  | 
**bbox_max** | **List[float]** |  | 
**bbox_min** | **List[float]** |  | 
**bbox_midpoint** | **List[float]** |  | 
**bbox_dimension_x** | **float** |  | 
**bbox_dimension_y** | **float** |  | 
**bbox_dimension_z** | **float** |  | 
**source_asset_url** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**root_prim** | **bool** |  | [optional] 
**default_prim** | **bool** |  | [optional] 

## Example

```python
from usd_search_client.models.prim1 import Prim1

# update the JSON string below
json = "{}"
# create an instance of Prim1 from a JSON string
prim1_instance = Prim1.from_json(json)
# print the JSON string representation of the object
print(Prim1.to_json())

# convert the object into a dict
prim1_dict = prim1_instance.to_dict()
# create an instance of Prim1 from a dict
prim1_from_dict = Prim1.from_dict(prim1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


