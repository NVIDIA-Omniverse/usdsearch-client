# AssetGraph1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[Asset]**](Asset.md) |  | 
**edges** | [**List[AssetRelationship]**](AssetRelationship.md) |  | 

## Example

```python
from usd_search_client.models.asset_graph1 import AssetGraph1

# TODO update the JSON string below
json = "{}"
# create an instance of AssetGraph1 from a JSON string
asset_graph1_instance = AssetGraph1.from_json(json)
# print the JSON string representation of the object
print(AssetGraph1.to_json())

# convert the object into a dict
asset_graph1_dict = asset_graph1_instance.to_dict()
# create an instance of AssetGraph1 from a dict
asset_graph1_from_dict = AssetGraph1.from_dict(asset_graph1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


