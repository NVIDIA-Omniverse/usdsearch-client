# VerifyAccessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** | List of URLs to check access for | 

## Example

```python
from usd_search_client.models.verify_access_request import VerifyAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAccessRequest from a JSON string
verify_access_request_instance = VerifyAccessRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyAccessRequest.to_json())

# convert the object into a dict
verify_access_request_dict = verify_access_request_instance.to_dict()
# create an instance of VerifyAccessRequest from a dict
verify_access_request_from_dict = VerifyAccessRequest.from_dict(verify_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


