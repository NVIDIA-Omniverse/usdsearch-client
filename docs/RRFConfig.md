# RRFConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_constant** | **int** | RRF constant factor (k). This value determines how much influence documents in individual result sets per query have over the final ranked result set. A higher value indicates that lower ranked documents have more influence. This value must be greater than or equal to 1. | [optional] [default to 60]
**window_size** | **int** |  | [optional] 
**query_rank_constants** | **Dict[str, int]** | Specific rank constants for different search types | [optional] 

## Example

```python
from usd_search_client.models.rrf_config import RRFConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RRFConfig from a JSON string
rrf_config_instance = RRFConfig.from_json(json)
# print the JSON string representation of the object
print(RRFConfig.to_json())

# convert the object into a dict
rrf_config_dict = rrf_config_instance.to_dict()
# create an instance of RRFConfig from a dict
rrf_config_from_dict = RRFConfig.from_dict(rrf_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


