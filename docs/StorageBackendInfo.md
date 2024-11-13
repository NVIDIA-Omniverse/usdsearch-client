# StorageBackendInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_status** | [**BackendStatusType**](BackendStatusType.md) | Status of the asset in the storage backend | 
**storage_asset_hash** | **str** | Current hash value of the asset in storage | [optional] 
**metadata** | [**PathType**](PathType.md) | asset metadata | [optional] 

## Example

```python
from usd_search_client.models.storage_backend_info import StorageBackendInfo

# update the JSON string below
json = "{}"
# create an instance of StorageBackendInfo from a JSON string
storage_backend_info_instance = StorageBackendInfo.from_json(json)
# print the JSON string representation of the object
print(StorageBackendInfo.to_json())

# convert the object into a dict
storage_backend_info_dict = storage_backend_info_instance.to_dict()
# create an instance of StorageBackendInfo from a dict
storage_backend_info_from_dict = StorageBackendInfo.from_dict(storage_backend_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


