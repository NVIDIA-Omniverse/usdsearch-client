# UsdPath

Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from usd_search_client.models.usd_path import UsdPath

# TODO update the JSON string below
json = "{}"
# create an instance of UsdPath from a JSON string
usd_path_instance = UsdPath.from_json(json)
# print the JSON string representation of the object
print(UsdPath.to_json())

# convert the object into a dict
usd_path_dict = usd_path_instance.to_dict()
# create an instance of UsdPath from a dict
usd_path_from_dict = UsdPath.from_dict(usd_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


