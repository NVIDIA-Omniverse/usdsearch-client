# ScoreExplanation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_type** | [**SearchType**](SearchType.md) |  | 
**score** | **float** |  | 
**var_field** | **str** |  | 
**details** | **object** |  | [optional] 
**rrf_score** | **float** |  | [optional] 
**rrf_rank_constant** | **int** |  | [optional] 
**matched_terms** | **List[str]** |  | [optional] 
**vector_similarity** | **float** |  | [optional] 
**matched_vectors** | [**List[VectorScore]**](VectorScore.md) |  | [optional] 

## Example

```python
from usd_search_client.models.score_explanation import ScoreExplanation

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreExplanation from a JSON string
score_explanation_instance = ScoreExplanation.from_json(json)
# print the JSON string representation of the object
print(ScoreExplanation.to_json())

# convert the object into a dict
score_explanation_dict = score_explanation_instance.to_dict()
# create an instance of ScoreExplanation from a dict
score_explanation_from_dict = ScoreExplanation.from_dict(score_explanation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


