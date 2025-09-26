# SearchResultMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanations** | [**List[ScoreExplanation]**](ScoreExplanation.md) |  | 
**rrf_rank** | **int** |  | [optional] 
**original_ranks** | **Dict[str, int]** |  | [optional] 

## Example

```python
from usd_search_client.models.search_result_metadata import SearchResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultMetadata from a JSON string
search_result_metadata_instance = SearchResultMetadata.from_json(json)
# print the JSON string representation of the object
print(SearchResultMetadata.to_json())

# convert the object into a dict
search_result_metadata_dict = search_result_metadata_instance.to_dict()
# create an instance of SearchResultMetadata from a dict
search_result_metadata_from_dict = SearchResultMetadata.from_dict(search_result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


