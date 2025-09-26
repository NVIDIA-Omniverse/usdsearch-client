# usd_search_client.AISearchApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**_search_hybrid_post**](AISearchApi.md#_search_hybrid_post) | **POST** /search_hybrid | Search Post
[**search_post_v2_deepsearch_search_post**](AISearchApi.md#search_post_v2_deepsearch_search_post) | **POST** /search | Search Post
[**search_v2_deepsearch_search_get**](AISearchApi.md#search_v2_deepsearch_search_get) | **GET** /search | Search
[**stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get**](AISearchApi.md#stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get) | **GET** /search/stats/usd_properties | Stats Usd Properties


# **_search_hybrid_post**
> SearchResponse _search_hybrid_post(deep_search_search_request_v2)

Search Post

Hybrid Search endpoint is an evolution of basic /search endpoint that supports the same filters but returns data in a new format and adds support for the following features: - **Enhanced Response Format**: Returns SearchResponse with detailed explanations and metadata - **Hybrid Search Support**: Combines text and vector search methods with configurable weights - **Advanced Explanations**: Provides detailed scoring explanations including RRF (Reciprocal Rank Fusion) scores - **Configurable Scoring**: Supports field-specific scoring configurations and weights - **Search Result Metadata**: Includes explanations, RRF ranks, and original ranks for transparency

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.deep_search_search_request_v2 import DeepSearchSearchRequestV2
from usd_search_client.models.search_response import SearchResponse
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
    api_instance = usd_search_client.AISearchApi(api_client)
    deep_search_search_request_v2 = {"hybrid_text_query":"red car vehicle","vector_queries":[{"field_name":"clip-embedding.embedding","query_type":"text","query":"red car vehicle"}],"return_metadata":true,"return_images":true,"limit":10} # DeepSearchSearchRequestV2 | 

    try:
        # Search Post
        api_response = await api_instance._search_hybrid_post(deep_search_search_request_v2)
        print("The response of AISearchApi->_search_hybrid_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISearchApi->_search_hybrid_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep_search_search_request_v2** | [**DeepSearchSearchRequestV2**](DeepSearchSearchRequestV2.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_post_v2_deepsearch_search_post**
> List[DeepsearchApiRoutersV2ModelsSearchResult] search_post_v2_deepsearch_search_post(deep_search_search_request_v2)

Search Post

All supported search parameters are available as body parameters.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, USD Search API extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.deep_search_search_request_v2 import DeepSearchSearchRequestV2
from usd_search_client.models.deepsearch_api_routers_v2_models_search_result import DeepsearchApiRoutersV2ModelsSearchResult
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
    api_instance = usd_search_client.AISearchApi(api_client)
    deep_search_search_request_v2 = usd_search_client.DeepSearchSearchRequestV2() # DeepSearchSearchRequestV2 | 

    try:
        # Search Post
        api_response = await api_instance.search_post_v2_deepsearch_search_post(deep_search_search_request_v2)
        print("The response of AISearchApi->search_post_v2_deepsearch_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISearchApi->search_post_v2_deepsearch_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deep_search_search_request_v2** | [**DeepSearchSearchRequestV2**](DeepSearchSearchRequestV2.md)|  | 

### Return type

[**List[DeepsearchApiRoutersV2ModelsSearchResult]**](DeepsearchApiRoutersV2ModelsSearchResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v2_deepsearch_search_get**
> List[DeepsearchApiRoutersV2ModelsSearchResult] search_v2_deepsearch_search_get(description=description, image_similarity_search=image_similarity_search, file_name=file_name, exclude_file_name=exclude_file_name, file_extension_include=file_extension_include, file_extension_exclude=file_extension_exclude, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, file_size_greater_than=file_size_greater_than, file_size_less_than=file_size_less_than, created_by=created_by, exclude_created_by=exclude_created_by, modified_by=modified_by, exclude_modified_by=exclude_modified_by, similarity_threshold=similarity_threshold, cutoff_threshold=cutoff_threshold, search_path=search_path, exclude_search_path=exclude_search_path, filter_url_regexp=filter_url_regexp, search_in_scene=search_in_scene, filter_by_properties=filter_by_properties, exclude_filter_by_properties=exclude_filter_by_properties, min_bbox_x=min_bbox_x, min_bbox_y=min_bbox_y, min_bbox_z=min_bbox_z, max_bbox_x=max_bbox_x, max_bbox_y=max_bbox_y, max_bbox_z=max_bbox_z, return_images=return_images, return_metadata=return_metadata, return_root_prims=return_root_prims, return_default_prims=return_default_prims, return_predictions=return_predictions, return_in_scene_instances_prims=return_in_scene_instances_prims, embedding_knn_search_method=embedding_knn_search_method, limit=limit, vision_metadata=vision_metadata, return_vision_generated_metadata=return_vision_generated_metadata, return_inner_hits=return_inner_hits)

Search

All supported search parameters are available as query parameters.  Search endpoint enables comprehensive searches across images (e.g., .jpg, .png) and USD-based 3D models within various storage backends (Nucleus, S3, etc.). It enables users to use natural language, image similarity, and precise metadata criteria (file name, type, date, size, creator, etc.) to locate relevant content efficiently. Furthermore, when integrated with the Asset Graph Service, USD Search API extends its capabilities to include searches based on USD properties and spatial dimensions of 3D model bounding boxes, enhancing the ability to find assets that meet specific requirements.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.deepsearch_api_routers_v2_models_search_result import DeepsearchApiRoutersV2ModelsSearchResult
from usd_search_client.models.search_method import SearchMethod
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
    api_instance = usd_search_client.AISearchApi(api_client)
    description = '' # str | Conduct text-based searches powered by AI (optional) (default to '')
    image_similarity_search = ['[]'] # List[str] | Perform similarity searches based on a list of images (optional)
    file_name = '' # str | Filter results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    exclude_file_name = '' # str | Exclude results by asset file name, allowing partial matches. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    file_extension_include = '' # str | Filter results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    file_extension_exclude = '' # str | Exclude results by file extension. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    created_after = 'created_after_example' # str | Filter results to only include assets created after a specified date (optional)
    created_before = 'created_before_example' # str | Filter results to only include assets created before a specified date (optional)
    modified_after = 'modified_after_example' # str | Filter results to only include assets modified after a specified date (optional)
    modified_before = 'modified_before_example' # str | Filter results to only include assets modified before a specified date (optional)
    file_size_greater_than = 'file_size_greater_than_example' # str | Filter results to only include files larger than a specific size (optional)
    file_size_less_than = 'file_size_less_than_example' # str | Filter results to only include files smaller than a specific size (optional)
    created_by = '' # str | Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. (optional) (default to '')
    exclude_created_by = '' # str | Exclude assets created by a specific user from the results (optional) (default to '')
    modified_by = '' # str | Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner's ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. (optional) (default to '')
    exclude_modified_by = '' # str | Exclude assets modified by a specific user from the results (optional) (default to '')
    similarity_threshold = 0 # float | Set the similarity threshold for embedding-based searches. This functionality allows filtering duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range. (optional)
    cutoff_threshold = 3.4 # float | Set the cutoff threshold for embedding-based searches (optional)
    search_path = '' # str | Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    exclude_search_path = '' # str | Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: `*` for any number of characters, `?` for a single character. Separate terms with `,` for OR and `;` for AND. (optional) (default to '')
    filter_url_regexp = 'filter_url_regexp_example' # str | Specify an asset URL filter in the [Lucene Regexp format](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/query-dsl-regexp-query.html#regexp-syntax). (optional)
    search_in_scene = '' # str | Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix. (optional) (default to '')
    filter_by_properties = '' # str | Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456`, to search for key only use `key=`, and to search for value only `=value` (optional) (default to '')
    exclude_filter_by_properties = '' # str | Exclude assets by USD attributes (note: only supported for a subset of attributes indexed). Format: `attribute1=abc,attribute2=456` (optional) (default to '')
    min_bbox_x = 3.4 # float | Filter by minimum X axis dimension of the asset's bounding box (optional)
    min_bbox_y = 3.4 # float | Filter by minimum Y axis dimension of the asset's bounding box (optional)
    min_bbox_z = 3.4 # float | Filter by minimum Z axis dimension of the asset's bounding box (optional)
    max_bbox_x = 3.4 # float | Filter by maximum X axis dimension of the asset's bounding box (optional)
    max_bbox_y = 3.4 # float | Filter by maximum Y axis dimension of the asset's bounding box (optional)
    max_bbox_z = 3.4 # float | Filter by maximum Z axis dimension of the asset's bounding box (optional)
    return_images = False # bool | Return images if set to True (optional) (default to False)
    return_metadata = False # bool | Return metadata if set to True (optional) (default to False)
    return_root_prims = False # bool | Return root prims if set to True (optional) (default to False)
    return_default_prims = False # bool | Return default prims if set to True (optional) (default to False)
    return_predictions = False # bool | Return predictions if set to True (optional) (default to False)
    return_in_scene_instances_prims = False # bool | [in-scene search only] Return prims of instances of objects found in the scene (optional) (default to False)
    embedding_knn_search_method = usd_search_client.SearchMethod() # SearchMethod | Search method, approximate should be faster but is less accurate. Default is exact (optional)
    limit = 56 # int | Set the maximum number of results to return from the search, default is 32 (optional)
    vision_metadata = 'vision_metadata_example' # str | Uses a keyword match query on metadata fields that were generated using Vision Language Models (optional)
    return_vision_generated_metadata = False # bool | Returns the metadata fields that were generated using Vision Language Models (optional) (default to False)
    return_inner_hits = False # bool | Return inner hits from nested queries for debugging and detailed scoring (optional) (default to False)

    try:
        # Search
        api_response = await api_instance.search_v2_deepsearch_search_get(description=description, image_similarity_search=image_similarity_search, file_name=file_name, exclude_file_name=exclude_file_name, file_extension_include=file_extension_include, file_extension_exclude=file_extension_exclude, created_after=created_after, created_before=created_before, modified_after=modified_after, modified_before=modified_before, file_size_greater_than=file_size_greater_than, file_size_less_than=file_size_less_than, created_by=created_by, exclude_created_by=exclude_created_by, modified_by=modified_by, exclude_modified_by=exclude_modified_by, similarity_threshold=similarity_threshold, cutoff_threshold=cutoff_threshold, search_path=search_path, exclude_search_path=exclude_search_path, filter_url_regexp=filter_url_regexp, search_in_scene=search_in_scene, filter_by_properties=filter_by_properties, exclude_filter_by_properties=exclude_filter_by_properties, min_bbox_x=min_bbox_x, min_bbox_y=min_bbox_y, min_bbox_z=min_bbox_z, max_bbox_x=max_bbox_x, max_bbox_y=max_bbox_y, max_bbox_z=max_bbox_z, return_images=return_images, return_metadata=return_metadata, return_root_prims=return_root_prims, return_default_prims=return_default_prims, return_predictions=return_predictions, return_in_scene_instances_prims=return_in_scene_instances_prims, embedding_knn_search_method=embedding_knn_search_method, limit=limit, vision_metadata=vision_metadata, return_vision_generated_metadata=return_vision_generated_metadata, return_inner_hits=return_inner_hits)
        print("The response of AISearchApi->search_v2_deepsearch_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISearchApi->search_v2_deepsearch_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| Conduct text-based searches powered by AI | [optional] [default to &#39;&#39;]
 **image_similarity_search** | [**List[str]**](str.md)| Perform similarity searches based on a list of images | [optional] 
 **file_name** | **str**| Filter results by asset file name, allowing partial matches. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **exclude_file_name** | **str**| Exclude results by asset file name, allowing partial matches. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **file_extension_include** | **str**| Filter results by file extension. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **file_extension_exclude** | **str**| Exclude results by file extension. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **created_after** | **str**| Filter results to only include assets created after a specified date | [optional] 
 **created_before** | **str**| Filter results to only include assets created before a specified date | [optional] 
 **modified_after** | **str**| Filter results to only include assets modified after a specified date | [optional] 
 **modified_before** | **str**| Filter results to only include assets modified before a specified date | [optional] 
 **file_size_greater_than** | **str**| Filter results to only include files larger than a specific size | [optional] 
 **file_size_less_than** | **str**| Filter results to only include files smaller than a specific size | [optional] 
 **created_by** | **str**| Filter results to only include assets created by a specific user. In case AWS S3 bucket is used as a storage backend, this field corresponds to the owner&#39;s ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. | [optional] [default to &#39;&#39;]
 **exclude_created_by** | **str**| Exclude assets created by a specific user from the results | [optional] [default to &#39;&#39;]
 **modified_by** | **str**| Filter results to only include assets modified by a specific user. In the case, when AWS S3 bucket is used as a storage backend, this field corresponds to the owner&#39;s ID. In case of an Omniverse Nucleus server, this field may depend on the configuration, but typically corresponds to user email. | [optional] [default to &#39;&#39;]
 **exclude_modified_by** | **str**| Exclude assets modified by a specific user from the results | [optional] [default to &#39;&#39;]
 **similarity_threshold** | **float**| Set the similarity threshold for embedding-based searches. This functionality allows filtering duplicates and returning only those results that are different from each other. Assets are considered to be duplicates if the cosine distance betwen the embeddings a smaller than the similarity_threshold value, which could be in the [0, 2] range. | [optional] 
 **cutoff_threshold** | **float**| Set the cutoff threshold for embedding-based searches | [optional] 
 **search_path** | **str**| Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **exclude_search_path** | **str**| Specify the search path within the storage backend. This path should not contain the storage backend URL, just the asset path on the storage backend. Use wildcards: &#x60;*&#x60; for any number of characters, &#x60;?&#x60; for a single character. Separate terms with &#x60;,&#x60; for OR and &#x60;;&#x60; for AND. | [optional] [default to &#39;&#39;]
 **filter_url_regexp** | **str**| Specify an asset URL filter in the [Lucene Regexp format](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/query-dsl-regexp-query.html#regexp-syntax). | [optional] 
 **search_in_scene** | **str**| Conduct the search within a specific scene. Provide the full URL for the asset including the storage backend URL prefix. | [optional] [default to &#39;&#39;]
 **filter_by_properties** | **str**| Filter assets by USD attributes where at least one root prim matches (note: only supported for a subset of attributes indexed). Format: &#x60;attribute1&#x3D;abc,attribute2&#x3D;456&#x60;, to search for key only use &#x60;key&#x3D;&#x60;, and to search for value only &#x60;&#x3D;value&#x60; | [optional] [default to &#39;&#39;]
 **exclude_filter_by_properties** | **str**| Exclude assets by USD attributes (note: only supported for a subset of attributes indexed). Format: &#x60;attribute1&#x3D;abc,attribute2&#x3D;456&#x60; | [optional] [default to &#39;&#39;]
 **min_bbox_x** | **float**| Filter by minimum X axis dimension of the asset&#39;s bounding box | [optional] 
 **min_bbox_y** | **float**| Filter by minimum Y axis dimension of the asset&#39;s bounding box | [optional] 
 **min_bbox_z** | **float**| Filter by minimum Z axis dimension of the asset&#39;s bounding box | [optional] 
 **max_bbox_x** | **float**| Filter by maximum X axis dimension of the asset&#39;s bounding box | [optional] 
 **max_bbox_y** | **float**| Filter by maximum Y axis dimension of the asset&#39;s bounding box | [optional] 
 **max_bbox_z** | **float**| Filter by maximum Z axis dimension of the asset&#39;s bounding box | [optional] 
 **return_images** | **bool**| Return images if set to True | [optional] [default to False]
 **return_metadata** | **bool**| Return metadata if set to True | [optional] [default to False]
 **return_root_prims** | **bool**| Return root prims if set to True | [optional] [default to False]
 **return_default_prims** | **bool**| Return default prims if set to True | [optional] [default to False]
 **return_predictions** | **bool**| Return predictions if set to True | [optional] [default to False]
 **return_in_scene_instances_prims** | **bool**| [in-scene search only] Return prims of instances of objects found in the scene | [optional] [default to False]
 **embedding_knn_search_method** | [**SearchMethod**](.md)| Search method, approximate should be faster but is less accurate. Default is exact | [optional] 
 **limit** | **int**| Set the maximum number of results to return from the search, default is 32 | [optional] 
 **vision_metadata** | **str**| Uses a keyword match query on metadata fields that were generated using Vision Language Models | [optional] 
 **return_vision_generated_metadata** | **bool**| Returns the metadata fields that were generated using Vision Language Models | [optional] [default to False]
 **return_inner_hits** | **bool**| Return inner hits from nested queries for debugging and detailed scoring | [optional] [default to False]

### Return type

[**List[DeepsearchApiRoutersV2ModelsSearchResult]**](DeepsearchApiRoutersV2ModelsSearchResult.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get**
> StatsResponse stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get()

Stats Usd Properties

Get statistics for USD properties: count of unique properties, count of unique values, and count of unique kv pairs.

### Example

* Api Key Authentication (APIKeyHeader):
* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import usd_search_client
from usd_search_client.models.stats_response import StatsResponse
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
    api_instance = usd_search_client.AISearchApi(api_client)

    try:
        # Stats Usd Properties
        api_response = await api_instance.stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get()
        print("The response of AISearchApi->stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISearchApi->stats_usd_properties_v2_deepsearch_search_stats_usd_properties_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatsResponse**](StatsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

