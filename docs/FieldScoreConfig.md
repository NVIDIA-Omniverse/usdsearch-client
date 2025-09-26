# FieldScoreConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**enabled** | **bool** | Enable scoring for this field | [optional] [default to True]
**weight** | **float** | Weight for this field&#39;s score | [optional] [default to 1]
**match_type** | [**TextMatchType**](TextMatchType.md) |  | [optional] 
**fuzzy_max_expansions** | **int** |  | [optional] 
**nested** | **bool** | Field is nested | [optional] [default to False]
**wildcard** | **bool** | Run a wildcard query on this field | [optional] [default to True]
**match** | **bool** | Run a match query on this field | [optional] [default to True]
**case_insensitive** | **bool** | Case insensitive wildcard queries | [optional] [default to True]

## Example

```python
from usd_search_client.models.field_score_config import FieldScoreConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FieldScoreConfig from a JSON string
field_score_config_instance = FieldScoreConfig.from_json(json)
# print the JSON string representation of the object
print(FieldScoreConfig.to_json())

# convert the object into a dict
field_score_config_dict = field_score_config_instance.to_dict()
# create an instance of FieldScoreConfig from a dict
field_score_config_from_dict = FieldScoreConfig.from_dict(field_score_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


