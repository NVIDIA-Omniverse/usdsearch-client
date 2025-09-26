# UniqueKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**asset_count** | **int** |  | 

## Example

```python
from usd_search_client.models.unique_key import UniqueKey

# TODO update the JSON string below
json = "{}"
# create an instance of UniqueKey from a JSON string
unique_key_instance = UniqueKey.from_json(json)
# print the JSON string representation of the object
print(UniqueKey.to_json())

# convert the object into a dict
unique_key_dict = unique_key_instance.to_dict()
# create an instance of UniqueKey from a dict
unique_key_from_dict = UniqueKey.from_dict(unique_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


