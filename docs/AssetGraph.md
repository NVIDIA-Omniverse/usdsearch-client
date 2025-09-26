# AssetGraph


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[Asset]**](Asset.md) |  | 
**edges** | [**List[AssetRelationship]**](AssetRelationship.md) |  | 

## Example

```python
from usd_search_client.models.asset_graph import AssetGraph

# TODO update the JSON string below
json = "{}"
# create an instance of AssetGraph from a JSON string
asset_graph_instance = AssetGraph.from_json(json)
# print the JSON string representation of the object
print(AssetGraph.to_json())

# convert the object into a dict
asset_graph_dict = asset_graph_instance.to_dict()
# create an instance of AssetGraph from a dict
asset_graph_from_dict = AssetGraph.from_dict(asset_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


