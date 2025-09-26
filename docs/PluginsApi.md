# usd_search_client.PluginsApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_plugins_info_plugins_get**](PluginsApi.md#list_plugins_info_plugins_get) | **GET** /info/plugins | List of supported plugins


# **list_plugins_info_plugins_get**
> List[PluginDescription] list_plugins_info_plugins_get(only_active=only_active)

List of supported plugins

Get the list of plugins that are supported by the USD Search instance

### Example


```python
import usd_search_client
from usd_search_client.models.plugin_description import PluginDescription
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
    api_instance = usd_search_client.PluginsApi(api_client)
    only_active = True # bool | show only active plugins (optional) (default to True)

    try:
        # List of supported plugins
        api_response = await api_instance.list_plugins_info_plugins_get(only_active=only_active)
        print("The response of PluginsApi->list_plugins_info_plugins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugins_info_plugins_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_active** | **bool**| show only active plugins | [optional] [default to True]

### Return type

[**List[PluginDescription]**](PluginDescription.md)

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

