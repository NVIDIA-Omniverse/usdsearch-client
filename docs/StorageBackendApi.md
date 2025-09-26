# usd_search_client.StorageBackendApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_backend_info_info_backend_storage_get**](StorageBackendApi.md#get_storage_backend_info_info_backend_storage_get) | **GET** /info/backend/storage | Get Storage Backend Info


# **get_storage_backend_info_info_backend_storage_get**
> StorageBackendInfo get_storage_backend_info_info_backend_storage_get(check_availability=check_availability)

Get Storage Backend Info

Display some information about the storage backend, to which the USD Search API instance is connected to.

### Example


```python
import usd_search_client
from usd_search_client.models.storage_backend_info import StorageBackendInfo
from usd_search_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.my-usd-search-instance.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = usd_search_client.Configuration(
    host = "http://api.my-usd-search-instance.example.com"
)


# Enter a context with an instance of the API client
async with usd_search_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usd_search_client.StorageBackendApi(api_client)
    check_availability = False # bool | Check if storage backend is available (optional) (default to False)

    try:
        # Get Storage Backend Info
        api_response = await api_instance.get_storage_backend_info_info_backend_storage_get(check_availability=check_availability)
        print("The response of StorageBackendApi->get_storage_backend_info_info_backend_storage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageBackendApi->get_storage_backend_info_info_backend_storage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_availability** | **bool**| Check if storage backend is available | [optional] [default to False]

### Return type

[**StorageBackendInfo**](StorageBackendInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

