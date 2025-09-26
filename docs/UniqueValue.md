# UniqueValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**asset_count** | **int** |  | 

## Example

```python
from usd_search_client.models.unique_value import UniqueValue

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueValue from a JSON string
unique_value_instance = UniqueValue.from_json(json)
# print the JSON string representation of the object
print(UniqueValue.to_json())

# convert the object into a dict
unique_value_dict = unique_value_instance.to_dict()
# create an instance of UniqueValue from a dict
unique_value_from_dict = UniqueValue.from_dict(unique_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


