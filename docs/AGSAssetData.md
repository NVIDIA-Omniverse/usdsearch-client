# AGSAssetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 
**root_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 
**default_prims** | [**List[Prim1]**](Prim1.md) |  | [optional] 

## Example

```python
from usd_search_client.models.ags_asset_data import AGSAssetData

# TODO update the JSON string below
json = "{}"
# create an instance of AGSAssetData from a JSON string
ags_asset_data_instance = AGSAssetData.from_json(json)
# print the JSON string representation of the object
print(AGSAssetData.to_json())

# convert the object into a dict
ags_asset_data_dict = ags_asset_data_instance.to_dict()
# create an instance of AGSAssetData from a dict
ags_asset_data_from_dict = AGSAssetData.from_dict(ags_asset_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


