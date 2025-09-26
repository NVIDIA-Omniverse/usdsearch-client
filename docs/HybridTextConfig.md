# HybridTextConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable hybrid text search | [optional] [default to True]
**weight** | **float** | Weight for hybrid text search | [optional] [default to 1]
**fields** | [**List[FieldScoreConfig]**](FieldScoreConfig.md) | Fields to search in | [optional] 
**cross_field_operator** | **str** | How to combine field matches | [optional] [default to 'or']

## Example

```python
from usd_search_client.models.hybrid_text_config import HybridTextConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HybridTextConfig from a JSON string
hybrid_text_config_instance = HybridTextConfig.from_json(json)
# print the JSON string representation of the object
print(HybridTextConfig.to_json())

# convert the object into a dict
hybrid_text_config_dict = hybrid_text_config_instance.to_dict()
# create an instance of HybridTextConfig from a dict
hybrid_text_config_from_dict = HybridTextConfig.from_dict(hybrid_text_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


