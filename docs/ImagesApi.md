# usd_search_client.ImagesApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**_images_get**](ImagesApi.md#_images_get) | **GET** /images | Get Image


# **_images_get**
> object _images_get(asset_url=asset_url, image_key=image_key, img_offset=img_offset)

Get Image

Fetch image data for a particular asset by asset URL or directly by image key. Includes access control validation - only returns images for assets the user has access to.  Args:     asset_url: The asset URL to fetch the image for (optional)     image_key: The image key to fetch directly from OpenSearch (optional)     img_offset: Which image to fetch from the asset's clip-embeddings (0-based index, default: 0)     request: FastAPI request object     token_auth: Bearer token authentication     basic_auth: Basic authentication credentials     api_key_auth: API key authentication     image_loader: Image loader dependency     search_backend_v2: Search backend client for finding image ID     storage_client: Storage client for access verification  Returns:     Binary image data as Response  Raises:     HTTPException: 400 if neither asset_url nor image_key provided, 404 if image not found, 403 if access denied

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.my-usd-search-instance.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = usd_search_client.Configuration(
    host = "http://api.my-usd-search-instance.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure HTTP basic authorization: HTTPBasic
configuration = usd_search_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = usd_search_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with usd_search_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usd_search_client.ImagesApi(api_client)
    asset_url = 'asset_url_example' # str | The asset URL to fetch the image for (optional)
    image_key = 'image_key_example' # str | The image key to fetch directly from OS (optional)
    img_offset = 0 # int | Which image to fetch from the asset's clip-embeddings (0-based index) (optional) (default to 0)

    try:
        # Get Image
        api_response = await api_instance._images_get(asset_url=asset_url, image_key=image_key, img_offset=img_offset)
        print("The response of ImagesApi->_images_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->_images_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_url** | **str**| The asset URL to fetch the image for | [optional] 
 **image_key** | **str**| The image key to fetch directly from OS | [optional] 
 **img_offset** | **int**| Which image to fetch from the asset&#39;s clip-embeddings (0-based index) | [optional] [default to 0]

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, image/jpeg, image/png, image/gif

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image binary data |  -  |
**400** | Bad request - missing or invalid parameters |  -  |
**403** | Access denied |  -  |
**404** | Image not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

