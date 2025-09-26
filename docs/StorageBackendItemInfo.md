# StorageBackendItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_backend_type** | [**AvailableStorageClients**](AvailableStorageClients.md) |  | 
**base_url** | **str** |  | 
**s3_endpoint_url** | **str** |  | [optional] 
**available** | **bool** |  | [optional] 

## Example

```python
from usd_search_client.models.storage_backend_item_info import StorageBackendItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorageBackendItemInfo from a JSON string
storage_backend_item_info_instance = StorageBackendItemInfo.from_json(json)
# print the JSON string representation of the object
print(StorageBackendItemInfo.to_json())

# convert the object into a dict
storage_backend_item_info_dict = storage_backend_item_info_instance.to_dict()
# create an instance of StorageBackendItemInfo from a dict
storage_backend_item_info_from_dict = StorageBackendItemInfo.from_dict(storage_backend_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


