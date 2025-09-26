# ScoringConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rrf_config** | [**RRFConfig**](RRFConfig.md) |  | [optional] 
**hybrid_text** | [**HybridTextConfig**](HybridTextConfig.md) |  | [optional] 
**vector_fields** | [**Dict[str, VectorFieldConfig]**](VectorFieldConfig.md) | Configuration for vector search fields | [optional] 

## Example

```python
from usd_search_client.models.scoring_config import ScoringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScoringConfig from a JSON string
scoring_config_instance = ScoringConfig.from_json(json)
# print the JSON string representation of the object
print(ScoringConfig.to_json())

# convert the object into a dict
scoring_config_dict = scoring_config_instance.to_dict()
# create an instance of ScoringConfig from a dict
scoring_config_from_dict = ScoringConfig.from_dict(scoring_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


