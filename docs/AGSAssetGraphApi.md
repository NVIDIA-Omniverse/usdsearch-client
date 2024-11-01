# usd_search_client.AGSAssetGraphApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dependencies_flat_dependency_graph_flat_get**](AGSAssetGraphApi.md#get_dependencies_flat_dependency_graph_flat_get) | **GET** /dependency_graph/flat | Get Dependencies Flat
[**get_dependencies_graph_dependency_graph_graph_get**](AGSAssetGraphApi.md#get_dependencies_graph_dependency_graph_graph_get) | **GET** /dependency_graph/graph | Get Dependencies Graph
[**get_dependencies_inverse_dependency_graph_inverse_flat_get**](AGSAssetGraphApi.md#get_dependencies_inverse_dependency_graph_inverse_flat_get) | **GET** /dependency_graph/inverse/flat | Get Dependencies Inverse
[**get_inverse_dependencies_graph_dependency_graph_inverse_graph_get**](AGSAssetGraphApi.md#get_inverse_dependencies_graph_dependency_graph_inverse_graph_get) | **GET** /dependency_graph/inverse/graph | Get Inverse Dependencies Graph


# **get_dependencies_flat_dependency_graph_flat_get**
> List[Asset] get_dependencies_flat_dependency_graph_flat_get(root_node_url, max_level=max_level, limit=limit)

Get Dependencies Flat

Get a flat list of dependencies (unique files) for the specified asset.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.asset import Asset
from usd_search_client.rest import ApiException
from pprint import pprint


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
    api_instance = usd_search_client.AGSAssetGraphApi(api_client)
    root_node_url = 'root_node_url_example' # str | URL of the asset
    max_level = 56 # int | Max level of dependency tree traversal (by default unlimited) (optional)
    limit = 1000 # int | Page size (optional) (default to 1000)

    try:
        # Get Dependencies Flat
        api_response = await api_instance.get_dependencies_flat_dependency_graph_flat_get(root_node_url, max_level=max_level, limit=limit)
        print("The response of AGSAssetGraphApi->get_dependencies_flat_dependency_graph_flat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSAssetGraphApi->get_dependencies_flat_dependency_graph_flat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_node_url** | **str**| URL of the asset | 
 **max_level** | **int**| Max level of dependency tree traversal (by default unlimited) | [optional] 
 **limit** | **int**| Page size | [optional] [default to 1000]

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependencies_graph_dependency_graph_graph_get**
> AssetGraph get_dependencies_graph_dependency_graph_graph_get(root_node_url, max_level=max_level, limit=limit)

Get Dependencies Graph

Get a graph of dependencies (unique files) for the specified asset.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.asset_graph import AssetGraph
from usd_search_client.rest import ApiException
from pprint import pprint


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
    api_instance = usd_search_client.AGSAssetGraphApi(api_client)
    root_node_url = 'root_node_url_example' # str | URL of the asset
    max_level = 56 # int | Max level of dependency tree traversal (by default unlimited) (optional)
    limit = 1000 # int | Page size (optional) (default to 1000)

    try:
        # Get Dependencies Graph
        api_response = await api_instance.get_dependencies_graph_dependency_graph_graph_get(root_node_url, max_level=max_level, limit=limit)
        print("The response of AGSAssetGraphApi->get_dependencies_graph_dependency_graph_graph_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSAssetGraphApi->get_dependencies_graph_dependency_graph_graph_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_node_url** | **str**| URL of the asset | 
 **max_level** | **int**| Max level of dependency tree traversal (by default unlimited) | [optional] 
 **limit** | **int**| Page size | [optional] [default to 1000]

### Return type

[**AssetGraph**](AssetGraph.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependencies_inverse_dependency_graph_inverse_flat_get**
> List[Asset] get_dependencies_inverse_dependency_graph_inverse_flat_get(root_node_url, max_level=max_level, limit=limit)

Get Dependencies Inverse

Get a flat list of all assets (unique files) that depend on the specified asset.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.asset import Asset
from usd_search_client.rest import ApiException
from pprint import pprint


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
    api_instance = usd_search_client.AGSAssetGraphApi(api_client)
    root_node_url = 'root_node_url_example' # str | URL of the asset
    max_level = 56 # int | Max level of dependency tree traversal (by default unlimited) (optional)
    limit = 1000 # int | Page size (optional) (default to 1000)

    try:
        # Get Dependencies Inverse
        api_response = await api_instance.get_dependencies_inverse_dependency_graph_inverse_flat_get(root_node_url, max_level=max_level, limit=limit)
        print("The response of AGSAssetGraphApi->get_dependencies_inverse_dependency_graph_inverse_flat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSAssetGraphApi->get_dependencies_inverse_dependency_graph_inverse_flat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_node_url** | **str**| URL of the asset | 
 **max_level** | **int**| Max level of dependency tree traversal (by default unlimited) | [optional] 
 **limit** | **int**| Page size | [optional] [default to 1000]

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inverse_dependencies_graph_dependency_graph_inverse_graph_get**
> AssetGraph get_inverse_dependencies_graph_dependency_graph_inverse_graph_get(root_node_url, max_level=max_level, limit=limit)

Get Inverse Dependencies Graph

Get a graph of all assets (unique files) that depend on the specified asset.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.asset_graph import AssetGraph
from usd_search_client.rest import ApiException
from pprint import pprint


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
    api_instance = usd_search_client.AGSAssetGraphApi(api_client)
    root_node_url = 'root_node_url_example' # str | URL of the asset
    max_level = 56 # int | Max level of dependency tree traversal (by default unlimited) (optional)
    limit = 1000 # int | Page size (optional) (default to 1000)

    try:
        # Get Inverse Dependencies Graph
        api_response = await api_instance.get_inverse_dependencies_graph_dependency_graph_inverse_graph_get(root_node_url, max_level=max_level, limit=limit)
        print("The response of AGSAssetGraphApi->get_inverse_dependencies_graph_dependency_graph_inverse_graph_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSAssetGraphApi->get_inverse_dependencies_graph_dependency_graph_inverse_graph_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_node_url** | **str**| URL of the asset | 
 **max_level** | **int**| Max level of dependency tree traversal (by default unlimited) | [optional] 
 **limit** | **int**| Page size | [optional] [default to 1000]

### Return type

[**AssetGraph**](AssetGraph.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

