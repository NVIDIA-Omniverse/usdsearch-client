# PluginDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**data_types** | **List[str]** |  | 
**requires_rendering** | **bool** |  | 
**active** | **bool** |  | 
**config** | **object** |  | 

## Example

```python
from usd_search_client.models.plugin_description import PluginDescription

# TODO update the JSON string below
json = "{}"
# create an instance of PluginDescription from a JSON string
plugin_description_instance = PluginDescription.from_json(json)
# print the JSON string representation of the object
print(PluginDescription.to_json())

# convert the object into a dict
plugin_description_dict = plugin_description_instance.to_dict()
# create an instance of PluginDescription from a dict
plugin_description_from_dict = PluginDescription.from_dict(plugin_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


