# usd_search_client.IndexingStatusApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_status_info_indexing_asset_status_get**](IndexingStatusApi.md#get_asset_status_info_indexing_asset_status_get) | **GET** /info/indexing/asset/status | Get Asset Status


# **get_asset_status_info_indexing_asset_status_get**
> StatusResult get_asset_status_info_indexing_asset_status_get(url, return_asset_metadata=return_asset_metadata)

Get Asset Status

For each URL the service checks caches of all plugins that support processing this asset and reports the following information: * **indexing_status** [*not_found* / *in_sync* / *out_of_sync* ] - this parameter checks the difference between cached value of asset hash and the actual (up-to-date) asset hash from the storage backend.     * if these two values match - then the asset is considered to be up-to-date, in other words *in_sync*     * otherwise, the final version of the asset has not be processed yet.     * The *not_found* status is assigned in case the asset has never been processed. * **plugin_status_history** - is a list of last statuses that were assigned to the asset, while it was being processed. Each item of this list has the following structure:     * **status** [*ok* / *processing* / *failed_retries_exhausted* / other string] - shows whether the asset was         * *ok* - successfully processed         * *processing* - processing for the asset has started         * *failed_retries_exhausted* - processing of the asset failed and reached the retry limit         * any other string - indicates that that processing has failed with this message.     * **processing_timestamp** - the moment when the status was assigned     * **exception** - optional exception explanation  The service could additionally report asset metadata from the storage backend if **return_asset_metadata** flag is set to *True*.

### Example


```python
import usd_search_client
from usd_search_client.models.status_result import StatusResult
from usd_search_client.rest import ApiException
from pprint import pprint


# See configuration.py for a list of all supported configuration parameters.
configuration = usd_search_client.Configuration(
    host = "http://api.my-usd-search-instance.example.com"
)


# Enter a context with an instance of the API client
async with usd_search_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usd_search_client.IndexingStatusApi(api_client)
    url = 'url_example' # str | Asset URL for which processing status needs to be retrieved
    return_asset_metadata = False # bool | Return metadata for the asset if set to True (optional) (default to False)

    try:
        # Get Asset Status
        api_response = await api_instance.get_asset_status_info_indexing_asset_status_get(url, return_asset_metadata=return_asset_metadata)
        print("The response of IndexingStatusApi->get_asset_status_info_indexing_asset_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IndexingStatusApi->get_asset_status_info_indexing_asset_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Asset URL for which processing status needs to be retrieved | 
 **return_asset_metadata** | **bool**| Return metadata for the asset if set to True | [optional] [default to False]

### Return type

[**StatusResult**](StatusResult.md)

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

