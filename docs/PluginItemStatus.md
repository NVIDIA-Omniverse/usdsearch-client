# PluginItemStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | asset status | 
**hash_value** | [**HashValue**](HashValue.md) |  | [optional] 
**processing_timestamp** | [**ProcessingTimestamp**](ProcessingTimestamp.md) |  | 
**exception** | **str** | reason for the Non Ok status | [optional] 

## Example

```python
from usd_search_client.models.plugin_item_status import PluginItemStatus

# update the JSON string below
json = "{}"
# create an instance of PluginItemStatus from a JSON string
plugin_item_status_instance = PluginItemStatus.from_json(json)
# print the JSON string representation of the object
print(PluginItemStatus.to_json())

# convert the object into a dict
plugin_item_status_dict = plugin_item_status_instance.to_dict()
# create an instance of PluginItemStatus from a dict
plugin_item_status_from_dict = PluginItemStatus.from_dict(plugin_item_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


