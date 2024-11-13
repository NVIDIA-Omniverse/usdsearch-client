# usd_search_client.AGSSpatialGraphApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get**](AGSSpatialGraphApi.md#get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get) | **GET** /asset_graph/usd/prims/spatial_bbox | Get Prims Within Bounding Box
[**get_prims_within_radius_asset_graph_usd_prims_spatial_get**](AGSSpatialGraphApi.md#get_prims_within_radius_asset_graph_usd_prims_spatial_get) | **GET** /asset_graph/usd/prims/spatial | Get Prims Within Radius


# **get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get**
> List[Prim] get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get(scene_url, min_bbox_x, min_bbox_y, min_bbox_z, max_bbox_x, max_bbox_y, max_bbox_z, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)

Get Prims Within Bounding Box

Perform a spatial search within a scene to retrieve prims from a USD scene that fall within a specified bounding box. The bounding box is defined by two points: [min_bbox_x, min_bbox_y, min_bbox_z] and [max_bbox_x, max_bbox_y, max_bbox_z].  A prim is considered to be within the bounding box if its bounding box midpoint falls within the specified query bounding box.

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
    api_instance = usd_search_client.AGSSpatialGraphApi(api_client)
    scene_url = 'scene_url_example' # str | Retrieve prims from the scene at specified URL.
    min_bbox_x = 3.4 # float | Query bounding box minimum X
    min_bbox_y = 3.4 # float | Query bounding box minimum Y
    min_bbox_z = 3.4 # float | Query bounding box minimum Z
    max_bbox_x = 3.4 # float | Query bounding box maximum X
    max_bbox_y = 3.4 # float | Query bounding box maximum Y
    max_bbox_z = 3.4 # float | Query bounding box maximum Z
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
        # Get Prims Within Bounding Box
        api_response = await api_instance.get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get(scene_url, min_bbox_x, min_bbox_y, min_bbox_z, max_bbox_x, max_bbox_y, max_bbox_z, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)
        print("The response of AGSSpatialGraphApi->get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSSpatialGraphApi->get_prims_within_bounding_box_asset_graph_usd_prims_spatial_bbox_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_url** | **str**| Retrieve prims from the scene at specified URL. | 
 **min_bbox_x** | **float**| Query bounding box minimum X | 
 **min_bbox_y** | **float**| Query bounding box minimum Y | 
 **min_bbox_z** | **float**| Query bounding box minimum Z | 
 **max_bbox_x** | **float**| Query bounding box maximum X | 
 **max_bbox_y** | **float**| Query bounding box maximum Y | 
 **max_bbox_z** | **float**| Query bounding box maximum Z | 
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

# **get_prims_within_radius_asset_graph_usd_prims_spatial_get**
> List[SpatialQueryResponseItem] get_prims_within_radius_asset_graph_usd_prims_spatial_get(scene_url, radius, center_prim_usd_path=center_prim_usd_path, center_x=center_x, center_y=center_y, center_z=center_z, transformation_matrix=transformation_matrix, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)

Get Prims Within Radius

Perform a spatial search within a scene to retrieve prims from a USD scene based on their proximity to a reference prim `center_prim_usd_path` or specific coordinates `[center_x, center_y, center_z]` within a specified `radius`.  **Note:** You must specify either `center_prim_usd_path` or the coordinates `[center_x, center_y, center_z]`.  Returns prim objects including: attributes, dimensions, and min, max, midpoint coordinates of the bounding box, distance from the query center, vector from the query center to the prim midpoint.  If searching using `center_prim_usd_path` the center prim at `center_prim_usd_path` is included in the results (unless excluded by filters used).

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.spatial_query_response_item import SpatialQueryResponseItem
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
    api_instance = usd_search_client.AGSSpatialGraphApi(api_client)
    scene_url = 'scene_url_example' # str | URL of the scene to search.
    radius = 3.4 # float | Radius of the proximity query
    center_prim_usd_path = 'center_prim_usd_path_example' # str | USD path of the reference Prim. (Returned in results unless excluded by filters) (optional)
    center_x = 3.4 # float | X coordinate of the query center. (optional)
    center_y = 3.4 # float | Y coordinate of the query center. (optional)
    center_z = 3.4 # float | Z coordinate of the query center. (optional)
    transformation_matrix = '1,0,0;0,1,0;0,0,1' # str | Transformation matrix for the vector space. By default does not apply any transformation. (optional) (default to '1,0,0;0,1,0;0,0,1')
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
        # Get Prims Within Radius
        api_response = await api_instance.get_prims_within_radius_asset_graph_usd_prims_spatial_get(scene_url, radius, center_prim_usd_path=center_prim_usd_path, center_x=center_x, center_y=center_y, center_z=center_z, transformation_matrix=transformation_matrix, limit=limit, prim_type=prim_type, usd_path_prefix=usd_path_prefix, properties_filter=properties_filter, min_bbox_dimension_x=min_bbox_dimension_x, min_bbox_dimension_y=min_bbox_dimension_y, min_bbox_dimension_z=min_bbox_dimension_z, max_bbox_dimension_x=max_bbox_dimension_x, max_bbox_dimension_y=max_bbox_dimension_y, max_bbox_dimension_z=max_bbox_dimension_z)
        print("The response of AGSSpatialGraphApi->get_prims_within_radius_asset_graph_usd_prims_spatial_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AGSSpatialGraphApi->get_prims_within_radius_asset_graph_usd_prims_spatial_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scene_url** | **str**| URL of the scene to search. | 
 **radius** | **float**| Radius of the proximity query | 
 **center_prim_usd_path** | **str**| USD path of the reference Prim. (Returned in results unless excluded by filters) | [optional] 
 **center_x** | **float**| X coordinate of the query center. | [optional] 
 **center_y** | **float**| Y coordinate of the query center. | [optional] 
 **center_z** | **float**| Z coordinate of the query center. | [optional] 
 **transformation_matrix** | **str**| Transformation matrix for the vector space. By default does not apply any transformation. | [optional] [default to &#39;1,0,0;0,1,0;0,0,1&#39;]
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

[**List[SpatialQueryResponseItem]**](SpatialQueryResponseItem.md)

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

