# AssetStorageBackendInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_status** | [**BackendStatusType**](BackendStatusType.md) |  | 
**storage_asset_hash** | **str** |  | [optional] 
**metadata** | [**PathType**](PathType.md) |  | [optional] 

## Example

```python
from usd_search_client.models.asset_storage_backend_info import AssetStorageBackendInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AssetStorageBackendInfo from a JSON string
asset_storage_backend_info_instance = AssetStorageBackendInfo.from_json(json)
# print the JSON string representation of the object
print(AssetStorageBackendInfo.to_json())

# convert the object into a dict
asset_storage_backend_info_dict = asset_storage_backend_info_instance.to_dict()
# create an instance of AssetStorageBackendInfo from a dict
asset_storage_backend_info_from_dict = AssetStorageBackendInfo.from_dict(asset_storage_backend_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


