# PrimType

Retrieve prims of the specified types. Can provide either a single type or a list of types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from usd_search_client.models.prim_type import PrimType

# TODO update the JSON string below
json = "{}"
# create an instance of PrimType from a JSON string
prim_type_instance = PrimType.from_json(json)
# print the JSON string representation of the object
print(PrimType.to_json())

# convert the object into a dict
prim_type_dict = prim_type_instance.to_dict()
# create an instance of PrimType from a dict
prim_type_from_dict = PrimType.from_dict(prim_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


