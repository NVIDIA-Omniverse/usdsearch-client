# StatusResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the asset | 
**plugins_statuses** | [**Dict[str, PluginInfo]**](PluginInfo.md) | Indexing status of the asset for each plugin | 
**storage_backend_info** | [**StorageBackendInfo**](StorageBackendInfo.md) | Status of the asset on the storage backend | 

## Example

```python
from usd_search_client.models.status_result import StatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResult from a JSON string
status_result_instance = StatusResult.from_json(json)
# print the JSON string representation of the object
print(StatusResult.to_json())

# convert the object into a dict
status_result_dict = status_result_instance.to_dict()
# create an instance of StatusResult from a dict
status_result_from_dict = StatusResult.from_dict(status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


