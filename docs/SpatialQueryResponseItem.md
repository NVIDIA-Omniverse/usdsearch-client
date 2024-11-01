# SpatialQueryResponseItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prim** | [**Prim**](Prim.md) |  | 
**distance** | **float** | Distance from the query center to the bounding box midpoint of the result. | 
**vector** | **List[float]** | Vector from the query center to the result. If the &#x60;transformation_matrix&#x60; argument is provided, the vector is transformed using the given matrix. | 

## Example

```python
from usd_search_client.models.spatial_query_response_item import SpatialQueryResponseItem

# TODO update the JSON string below
json = "{}"
# create an instance of SpatialQueryResponseItem from a JSON string
spatial_query_response_item_instance = SpatialQueryResponseItem.from_json(json)
# print the JSON string representation of the object
print(SpatialQueryResponseItem.to_json())

# convert the object into a dict
spatial_query_response_item_dict = spatial_query_response_item_instance.to_dict()
# create an instance of SpatialQueryResponseItem from a dict
spatial_query_response_item_from_dict = SpatialQueryResponseItem.from_dict(spatial_query_response_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


