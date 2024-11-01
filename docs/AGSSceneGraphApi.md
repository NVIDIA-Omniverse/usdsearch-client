# usd_search_client.AGSSceneGraphApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prims_asset_graph_usd_prims_get**](AGSSceneGraphApi.md#get_prims_asset_graph_usd_prims_get) | **GET** /asset_graph/usd/prims | Get Prims
[**scene_summary_asset_graph_usd_scene_summary_get**](AGSSceneGraphApi.md#scene_summary_asset_graph_usd_scene_summary_get) | **GET** /asset_graph/usd/scene_summary/ | Scene Summary


# **get_prims_asset_graph_usd_prims_get**
> List[Prim] get_prims_asset_graph_usd_prims_get(scene_url=scene_url, usd_path=usd_path, root_prim=root_prim, default_prim=default_prim, source_asset_url=source_asset_url, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)

Get Prims

Retrieve prims from a USD scene.  This API can be used for scene understanding, returns all objects in a scene together with their locations and dimensions.  NOTE: Calling without any parameters will return ALL prims. `scene_url` must be provided to fetch prims from the specified scene.  A globally unique prim id consists of (`scene_url`, `usd_path`) tuple. `usd_path` is unique only within a single scene. To retrieve prims from a specified scene, `scene_url` must be set. To retrieve a single prim from a specified scene, provide both `scene_url` and `usd_path`.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.prim import Prim
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
    api_instance = usd_search_client.AGSSceneGraphApi(api_client)
    scene_url = 'scene_url_example' # str | Retrieve prims from the scene at specified URL. (optional)
    usd_path = usd_search_client.UsdPath() # UsdPath | Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths. (optional)
    root_prim = True # bool | Retrieve root prims. Note: combined with default_prim returns both root and default prims. (optional)
    default_prim = True # bool | Retrieve default prims. Note: combined with root_prim returns both root and default prims. (optional)
    source_asset_url = 'source_asset_url_example' # str | Filter prims based on their source asset URL, i.e. the asset they have a reference to (optional)
    limit = 1000 # int | Page size (optional) (default to 1000)
    prim_type = usd_search_client.PrimType() # PrimType | Retrieve prims of the specified types. Can provide either a single type or a list of types. (optional)
    usd_path_prefix = 'usd_path_prefix_example' # str | Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path). (optional)
    properties_filter = 'properties_filter_example' # str | Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: `attribute1=abc,attribute2=456` (optional)
    min_bbox_dimension_x = 3.4 # float | Minimum bounding box X dimension (optional)
    min_bbox_dimension_y = 3.4 # float | Minimum bounding box Y dimension (optional)
    min_bbox_dimension_z = 3.4 # float | Minimum bounding box Z dimension (optional)
    max_bbox_dimension_x = 3.4 # float | Max bounding box X dimension (optional)
    max_bbox_dimension_y = 3.4 # float | Max bounding box Y dimension (optional)
    max_bbox_dimension_z = 3.4 # float | Max bounding box Z dimension (optional)

    try:
        # Get Prims
        api_response = await api_instance.get_prims_asset_graph_usd_prims_get(scene_url=scene_url, usd_path=usd_path, root_prim=root_prim, default_prim=default_prim, source_asset_url=source_asset_url, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)
        print("The response of AGSSceneGraphApi->get_prims_asset_graph_usd_prims_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSSceneGraphApi->get_prims_asset_graph_usd_prims_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_url** | **str**| Retrieve prims from the scene at specified URL. | [optional] 
 **usd_path** | [**UsdPath**](.md)| Retrieve prims from the specified USD paths. Can provide either a single path or a list of paths. | [optional] 
 **root_prim** | **bool**| Retrieve root prims. Note: combined with default_prim returns both root and default prims. | [optional] 
 **default_prim** | **bool**| Retrieve default prims. Note: combined with root_prim returns both root and default prims. | [optional] 
 **source_asset_url** | **str**| Filter prims based on their source asset URL, i.e. the asset they have a reference to | [optional] 
 **limit** | **int**| Page size | [optional] [default to 1000]
 **prim_type** | [**PrimType**](.md)| Retrieve prims of the specified types. Can provide either a single type or a list of types. | [optional] 
 **usd_path_prefix** | **str**| Retrieve prims with USD paths that begin with this prefix (i.e., the children of the prim at the specified path). | [optional] 
 **properties_filter** | **str**| Filter prims based on USD attributes (note: only a subset of attributes configured in the indexing service is available). Format: &#x60;attribute1&#x3D;abc,attribute2&#x3D;456&#x60; | [optional] 
 **min_bbox_dimension_x** | **float**| Minimum bounding box X dimension | [optional] 
 **min_bbox_dimension_y** | **float**| Minimum bounding box Y dimension | [optional] 
 **min_bbox_dimension_z** | **float**| Minimum bounding box Z dimension | [optional] 
 **max_bbox_dimension_x** | **float**| Max bounding box X dimension | [optional] 
 **max_bbox_dimension_y** | **float**| Max bounding box Y dimension | [optional] 
 **max_bbox_dimension_z** | **float**| Max bounding box Z dimension | [optional] 

### Return type

[**List[Prim]**](Prim.md)

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

# **scene_summary_asset_graph_usd_scene_summary_get**
> SceneSummaryResponse scene_summary_asset_graph_usd_scene_summary_get(scene_url)

Scene Summary

Retrieve summary info about a USD scene.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.scene_summary_response import SceneSummaryResponse
from usd_search_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.staging.deepsearch-cloud.nvidia.com
# See configuration.py for a list of all supported configuration parameters.
configuration = usd_search_client.Configuration(
    host = "http://api.staging.deepsearch-cloud.nvidia.com"
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
    api_instance = usd_search_client.AGSSceneGraphApi(api_client)
    scene_url = 'scene_url_example' # str | Scene summary.

    try:
        # Scene Summary
        api_response = await api_instance.scene_summary_asset_graph_usd_scene_summary_get(scene_url)
        print("The response of AGSSceneGraphApi->scene_summary_asset_graph_usd_scene_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSSceneGraphApi->scene_summary_asset_graph_usd_scene_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_url** | **str**| Scene summary. | 

### Return type

[**SceneSummaryResponse**](SceneSummaryResponse.md)

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

