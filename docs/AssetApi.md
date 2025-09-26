# usd_search_client.AssetApi

All URIs are relative to *http://api.my-usd-search-instance.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_status_info_indexing_asset_status_get**](AssetApi.md#get_asset_status_info_indexing_asset_status_get) | **GET** /info/indexing/asset/status | Get Asset Status
[**submit_for_processing_process_asset_get**](AssetApi.md#submit_for_processing_process_asset_get) | **GET** /process/asset | On-demand asset processing


# **get_asset_status_info_indexing_asset_status_get**
> StatusResult get_asset_status_info_indexing_asset_status_get(url, return_asset_metadata=return_asset_metadata)

Get Asset Status

For each URL the service checks caches of all plugins that support processing this asset and reports the following information:  * **indexing_status** [*not_found* / *in_sync* / *out_of_sync* ] - this parameter checks the difference between cached value of asset hash and the actual (up-to-date) asset hash from the storage backend.      * if these two values match - then the asset is considered to be up-to-date, in other words *in_sync*     * otherwise, the final version of the asset has not be processed yet.     * The *not_found* status is assigned in case the asset has never been processed.  * **plugin_status_history** - is a list of last statuses that were assigned to the asset, while it was being processed. Each item of this list has the following structure:      * **status** [*ok* / *processing* / *failed_retries_exhausted* / other string] - shows whether the asset was          * *ok* - successfully processed         * *processing* - processing for the asset has started         * *failed_retries_exhausted* - processing of the asset failed and reached the retry limit         * any other string - indicates that that processing has failed with this message.      * **processing_timestamp** - the moment when the status was assigned     * **exception** - optional exception explanation  The service could additionally report asset metadata from the storage backend if **return_asset_metadata** flag is set to *True*.

### Example


```python
import usd_search_client
from usd_search_client.models.status_result import StatusResult
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
    api_instance = usd_search_client.AssetApi(api_client)
    url = 'url_example' # str | Asset URL for which processing status needs to be retrieved
    return_asset_metadata = False # bool | Return metadata for the asset if set to True (optional) (default to False)

    try:
        # Get Asset Status
        api_response = await api_instance.get_asset_status_info_indexing_asset_status_get(url, return_asset_metadata=return_asset_metadata)
        print("The response of AssetApi->get_asset_status_info_indexing_asset_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->get_asset_status_info_indexing_asset_status_get: %s\n" % e)
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

# **submit_for_processing_process_asset_get**
> object submit_for_processing_process_asset_get(url, plugins=plugins, refresh_metadata=refresh_metadata, refresh_tags=refresh_tags, priority=priority)

On-demand asset processing

USD Search processes all assets on the storage backend in the background. This, however, may take time depending on the amount of data on the storage backend and the amount of available resources, which could lead to delays in specific assets appearing in the search index. In order to address this and prioritize processing of specific assets, it is possible to use this endpoint to trigger indexing of a specific asset on demand.  When triggering processing of a specific asset URL the user could decide, with which plugin the asset needs to be processed. By default, when no plugin is selected - the service will trigger processing for all plugins that could work with this asset type. Please find below the list of supported plugins:  * **asset_graph_generation**:      Constructs several graphs based on the prim hierarchy of a USD file. This plugin is an essential component of Asset Graph Service (AGS).          * This plugin supports the following data types: *usda, usd, usdc, usdz*  * **image_to_embedding**:      Extracts CLIP embeddings from the images that are found on the storage backend.          * This plugin supports the following data types: *gif, jpe, icns, png, grib, exr, msp, dcx, fit, dib, tif, pcd, tga, hdf, jp2, jpf, pnm, fits, ps, sgi, dds, im, jpc, jpx, bw, pfm, webp, pcx, tiff, wmf, icb, eps, flc, ppm, vst, psd, rgba, h5, cur, bmp, xbm, ftc, jpeg, jpg, bufr, emf, j2c, j2k, apng, mpg, pxr, vda, jfif, gbr, pgm, fli, ftu, pbm, iim, ico, qoi, ras, xpm, rgb, blp, mpeg*  * **image_to_vision_metadata**:      Extracts VLM-generated metadata from the images that are found on the storage backend.          * This plugin supports the following data types: *gif, jpe, icns, png, grib, exr, msp, dcx, fit, dib, tif, pcd, tga, hdf, jp2, jpf, pnm, fits, ps, sgi, dds, im, jpc, jpx, bw, pfm, webp, pcx, tiff, wmf, icb, eps, flc, ppm, vst, psd, rgba, h5, cur, bmp, xbm, ftc, jpeg, jpg, bufr, emf, j2c, j2k, apng, mpg, pxr, vda, jfif, gbr, pgm, fli, ftu, pbm, iim, ico, qoi, ras, xpm, rgb, blp, mpeg*  * **rendering_to_embedding**:      Renders the asset and extracts CLIP embeddings from the generated preview images.          * This plugin supports the following data types: *usda, usd, usdc, usdz*  * **rendering_to_vision_metadata**:      Renders the asset and extracts VLM-generated metadata using the generated preview images.          * This plugin supports the following data types: *usda, usd, usdc, usdz*  * **thumbnail_generation**:      Renders the asset uploads one of the rendered images to the storage backend to serve as a thumbnail for this asset.          * This plugin supports the following data types: *usda, usd, usdc, usdz*  * **thumbnail_to_embedding**:      For any asset stored on the storage backend this plugin relies on the thumbnail of this asset to extract CLIP embeddings.          * This plugin supports the following data types: *any*  * **thumbnail_to_vision_metadata**:      For any asset stored on the storage backend this plugin relies on the thumbnail of this asset to extract VLM-generated metadata.          * This plugin supports the following data types: *any*   **NOTE**: If some of the plugins are not enabled for the USD Search instance, selecting them for the *plugins* parameter setting will have not effect. Please reach out to your USD Search service administrator if you would like to enable certain plugin functionality. The list of plugins that are enabled for this USD Search instance could be retrieved using **/info/plugins** endpoint.

### Example


```python
import usd_search_client
from usd_search_client.models.plugins import Plugins
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
    api_instance = usd_search_client.AssetApi(api_client)
    url = 'url_example' # str | Asset URL which should be submitted for priority processing
    plugins = [usd_search_client.Plugins()] # List[Plugins] | List of plugins for which indexing needs to be re-done (optional)
    refresh_metadata = False # bool | refresh asset metadata (optional) (default to False)
    refresh_tags = False # bool | refresh asset tags (optional) (default to False)
    priority = usd_search_client.Priority() # Priority | processing job type (optional)

    try:
        # On-demand asset processing
        api_response = await api_instance.submit_for_processing_process_asset_get(url, plugins=plugins, refresh_metadata=refresh_metadata, refresh_tags=refresh_tags, priority=priority)
        print("The response of AssetApi->submit_for_processing_process_asset_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->submit_for_processing_process_asset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Asset URL which should be submitted for priority processing | 
 **plugins** | [**List[Plugins]**](Plugins.md)| List of plugins for which indexing needs to be re-done | [optional] 
 **refresh_metadata** | **bool**| refresh asset metadata | [optional] [default to False]
 **refresh_tags** | **bool**| refresh asset tags | [optional] [default to False]
 **priority** | [**Priority**](.md)| processing job type | [optional] 

### Return type

**object**

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

