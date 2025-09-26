# PathType

This class is used to store the information about the path of the asset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**etag** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**type** | **str** |  | [optional] 
**ts** | **Dict[str, int]** |  | [optional] 
**transaction_id** | [**TransactionId**](TransactionId.md) |  | [optional] 
**acl** | **List[str]** |  | [optional] 
**empty** | [**Empty**](Empty.md) |  | [optional] 
**mounted** | [**Mounted**](Mounted.md) |  | [optional] 
**size** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**created_date_seconds** | [**CreatedDateSeconds**](CreatedDateSeconds.md) |  | [optional] 
**modified_by** | **str** |  | [optional] 
**modified_date_seconds** | [**ModifiedDateSeconds**](ModifiedDateSeconds.md) |  | [optional] 
**hash_type** | [**HashType**](HashType.md) |  | [optional] 
**hash_value** | **str** |  | [optional] 
**hash_bsize** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**deleted_by** | **str** |  | [optional] 
**deleted_date_seconds** | [**DeletedDateSeconds**](DeletedDateSeconds.md) |  | [optional] 

## Example

```python
from usd_search_client.models.path_type import PathType

# TODO update the JSON string below
json = "{}"
# create an instance of PathType from a JSON string
path_type_instance = PathType.from_json(json)
# print the JSON string representation of the object
print(PathType.to_json())

# convert the object into a dict
path_type_dict = path_type_instance.to_dict()
# create an instance of PathType from a dict
path_type_from_dict = PathType.from_dict(path_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


