# VectorQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Vector field to search in | 
**query_type** | [**VectorQueryType**](VectorQueryType.md) |  | 
**query** | [**Query**](Query.md) |  | 

## Example

```python
from usd_search_client.models.vector_query import VectorQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VectorQuery from a JSON string
vector_query_instance = VectorQuery.from_json(json)
# print the JSON string representation of the object
print(VectorQuery.to_json())

# convert the object into a dict
vector_query_dict = vector_query_instance.to_dict()
# create an instance of VectorQuery from a dict
vector_query_from_dict = VectorQuery.from_dict(vector_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


