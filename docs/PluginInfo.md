# PluginInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_status** | [**PluginStatusType**](PluginStatusType.md) | Indexing status of the asset for a given plugin | 
**indexed_asset_hash** | **str** | Hash of the indexed asset. If equal to the hash of the asset in storage, the indexed asset is up to date. | [optional] 
**plugin_status_history** | [**List[PluginItemStatus]**](PluginItemStatus.md) | status history for plugins | [optional] 

## Example

```python
from usd_search_client.models.plugin_info import PluginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PluginInfo from a JSON string
plugin_info_instance = PluginInfo.from_json(json)
# print the JSON string representation of the object
print(PluginInfo.to_json())

# convert the object into a dict
plugin_info_dict = plugin_info_instance.to_dict()
# create an instance of PluginInfo from a dict
plugin_info_from_dict = PluginInfo.from_dict(plugin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


