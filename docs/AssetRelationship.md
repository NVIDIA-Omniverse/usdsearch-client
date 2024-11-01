# AssetRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_1_url** | **str** |  | 
**node_2_url** | **str** |  | 
**type** | [**EdgeType1**](EdgeType1.md) |  | 

## Example

```python
from usd_search_client.models.asset_relationship import AssetRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRelationship from a JSON string
asset_relationship_instance = AssetRelationship.from_json(json)
# print the JSON string representation of the object
print(AssetRelationship.to_json())

# convert the object into a dict
asset_relationship_dict = asset_relationship_instance.to_dict()
# create an instance of AssetRelationship from a dict
asset_relationship_from_dict = AssetRelationship.from_dict(asset_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


