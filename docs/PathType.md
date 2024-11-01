# PathType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | Full asset URI | [optional] 
**etag** | **str** | unique asset ID | [optional] 
**status** | **str** | status of the operation | [optional] 
**event** | [**Event**](Event.md) |  | [optional] 
**type** | **str** | type of the asset | [optional] 
**ts** | **Dict[str, int]** | server timestamp | [optional] 
**transaction_id** | [**TransactionId**](TransactionId.md) |  | [optional] 
**acl** | **List[str]** | ACL list | [optional] 
**empty** | [**Empty**](Empty.md) |  | [optional] 
**mounted** | [**Mounted**](Mounted.md) |  | [optional] 
**size** | **int** | Size of the object in bytes | [optional] 
**created_by** | **str** | user ID who created the object | [optional] 
**created_date_seconds** | **int** | creation time (seconds) | [optional] 
**modified_by** | **str** | user ID who last modified the object | [optional] 
**modified_date_seconds** | **int** | last modification time (seconds) | [optional] 
**hash_type** | **str** | type of hashing function | [optional] 
**hash_value** | **str** | hash value (can be None for files on mounts) | [optional] 
**hash_bsize** | **str** | Hash block size | [optional] 
**is_deleted** | **bool** | flag to show that a file was deleted | [optional] 
**deleted_by** | **str** | user ID who last deleted the asset | [optional] 
**deleted_date_seconds** | **int** | time when the object was last deleted | [optional] 

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


