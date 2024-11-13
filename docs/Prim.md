# Prim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_url** | **str** | URL of the Prim&#39;s scene | 
**usd_path** | **str** | USD path of the prim withn scene &#x60;scene_url&#x60;. Unique within a single scene. | 
**prim_type** | **str** | Prim type | 
**source_asset_url** | **str** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**translate** | **List[float]** | Translate X, Y, Z world coordinates of the prim | [optional] [default to [0,0,0]]
**rotate_x** | **float** |  | [optional] 
**rotate_y** | **float** |  | [optional] 
**rotate_z** | **float** |  | [optional] 
**scale_x** | **float** |  | [optional] 
**scale_y** | **float** |  | [optional] 
**scale_z** | **float** |  | [optional] 
**bbox_max** | **List[float]** | Max X, Y, Z coordinates of the bounding box | 
**bbox_min** | **List[float]** | Min X, Y, Z coordinates of the bounding box | 
**bbox_midpoint** | **List[float]** | Midpoint X, Y, Z coordinates of the bounding box, i.e. Prim&#39;s location within the scene &#x60;scene_url&#x60;. | 
**root_prim** | **bool** |  | [optional] 
**default_prim** | **bool** |  | [optional] 
**bbox_dimension_x** | **float** | X axis dimension of prim&#39;s bounding box | [readonly] 
**bbox_dimension_y** | **float** | Y axis dimension of prim&#39;s bounding box | [readonly] 
**bbox_dimension_z** | **float** | Z axis dimension of prim&#39;s bounding box | [readonly] 

## Example

```python
from usd_search_client.models.prim import Prim

# update the JSON string below
json = "{}"
# create an instance of Prim from a JSON string
prim_instance = Prim.from_json(json)
# print the JSON string representation of the object
print(Prim.to_json())

# convert the object into a dict
prim_dict = prim_instance.to_dict()
# create an instance of Prim from a dict
prim_from_dict = Prim.from_dict(prim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


