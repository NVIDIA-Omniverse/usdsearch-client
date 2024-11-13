# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# coding: utf-8

"""
    USD Search and Asset Graph Search APIs

    # USD Search API Overview **USD Search API** is a collection of cloud-native microservices that enable developers, creators, and workflow specialists to efficiently search through vast collections of OpenUSD data, images, and other assets using natural language or image-based inputs. With these production-ready microservices, developers can deploy USD Search API onto their own infrastructure.  With USD Search API’s artificial intelligence (AI) features, you can quickly locate untagged and unstructured 3D data and digital assets, saving time navigating unstructured, untagged 3D data. USD Search API is capable of searching and indexing 3D asset databases, as well as navigating complex 3D scenes to perform spatial searches, without requiring manual tagging of assets. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import json
import re
import ssl
from typing import Optional, Union

import aiohttp
import aiohttp_retry

from usd_search_client.exceptions import ApiException, ApiValueError

RESTResponseType = aiohttp.ClientResponse

ALLOW_RETRY_METHODS = frozenset({'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE'})

class RESTResponse(io.IOBase):

    def __init__(self, resp) -> None:
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = None

    async def read(self):
        if self.data is None:
            self.data = await self.response.read()
        return self.data

    def getheaders(self):
        """Returns a CIMultiDictProxy of the response headers."""
        return self.response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.response.headers.get(name, default)


class RESTClientObject:

    def __init__(self, configuration) -> None:

        # maxsize is number of requests to host that are allowed in parallel
        maxsize = configuration.connection_pool_maxsize

        ssl_context = ssl.create_default_context(
            cafile=configuration.ssl_ca_cert
        )
        if configuration.cert_file:
            ssl_context.load_cert_chain(
                configuration.cert_file, keyfile=configuration.key_file
            )

        if not configuration.verify_ssl:
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

        connector = aiohttp.TCPConnector(
            limit=maxsize,
            ssl=ssl_context
        )

        self.proxy = configuration.proxy
        self.proxy_headers = configuration.proxy_headers

        # https pool manager
        self.pool_manager = aiohttp.ClientSession(
            connector=connector,
            trust_env=True
        )

        retries = configuration.retries
        self.retry_client: Optional[aiohttp_retry.RetryClient]
        if retries is not None:
            self.retry_client = aiohttp_retry.RetryClient(
                client_session=self.pool_manager,
                retry_options=aiohttp_retry.ExponentialRetry(
                    attempts=retries,
                    factor=2.0,
                    start_timeout=0.1,
                    max_timeout=120.0
                )
            )
        else:
            self.retry_client = None

    async def close(self):
        await self.pool_manager.close()
        if self.retry_client is not None:
            await self.retry_client.close()

    async def request(
        self,
        method,
        url,
        headers=None,
        body=None,
        post_params=None,
        _request_timeout=None
    ):
        """Execute request

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in [
            'GET',
            'HEAD',
            'DELETE',
            'POST',
            'PUT',
            'PATCH',
            'OPTIONS'
        ]

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}
        # url already contains the URL query string
        timeout = _request_timeout or 5 * 60

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            "method": method,
            "url": url,
            "timeout": timeout,
            "headers": headers
        }

        if self.proxy:
            args["proxy"] = self.proxy
        if self.proxy_headers:
            args["proxy_headers"] = self.proxy_headers

        # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                if body is not None:
                    body = json.dumps(body)
                args["data"] = body
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':
                args["data"] = aiohttp.FormData(post_params)
            elif headers['Content-Type'] == 'multipart/form-data':
                # must del headers['Content-Type'], or the correct
                # Content-Type which generated by aiohttp
                del headers['Content-Type']
                data = aiohttp.FormData()
                for param in post_params:
                    k, v = param
                    if isinstance(v, tuple) and len(v) == 3:
                        data.add_field(
                            k,
                            value=v[1],
                            filename=v[0],
                            content_type=v[2]
                        )
                    else:
                        data.add_field(k, v)
                args["data"] = data

            # Pass a `bytes` or `str` parameter directly in the body to support
            # other content types than Json when `body` argument is provided
            # in serialized form
            elif isinstance(body, str) or isinstance(body, bytes):
                args["data"] = body
            else:
                # Cannot generate the request from given parameters
                msg = """Cannot prepare a request message for provided
                         arguments. Please check that your arguments match
                         declared content type."""
                raise ApiException(status=0, reason=msg)

        pool_manager: Union[aiohttp.ClientSession, aiohttp_retry.RetryClient]
        if self.retry_client is not None and method in ALLOW_RETRY_METHODS:
            pool_manager = self.retry_client
        else:
            pool_manager = self.pool_manager

        r = await pool_manager.request(**args)

        return RESTResponse(r)





