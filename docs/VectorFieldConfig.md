# VectorFieldConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable vector search for this field | [optional] [default to False]
**weight** | **float** | Weight for vector search | [optional] [default to 1]
**field_name** | **str** | Name of the vector field in the index | 
**dimension** | **int** | Dimension of the vector field | 
**model_name** | **str** |  | [optional] 

## Example

```python
from usd_search_client.models.vector_field_config import VectorFieldConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VectorFieldConfig from a JSON string
vector_field_config_instance = VectorFieldConfig.from_json(json)
# print the JSON string representation of the object
print(VectorFieldConfig.to_json())

# convert the object into a dict
vector_field_config_dict = vector_field_config_instance.to_dict()
# create an instance of VectorFieldConfig from a dict
vector_field_config_from_dict = VectorFieldConfig.from_dict(vector_field_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


