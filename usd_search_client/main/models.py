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

from usd_search_client.models.deep_search_search_request_v2 import DeepSearchSearchRequestV2
from usd_search_client.models.deepsearch_api_routers_v2_models_search_result import DeepsearchApiRoutersV2ModelsSearchResult
from usd_search_client.models.search_response import SearchResponse

class BasicSearchRequest(DeepSearchSearchRequestV2):
    """Search request that is used when connecting to the /search endpoint of USD Search API.
    
    This is a basic search request that is used when connecting to the /search endpoint of USD Search API.
    It is used to search for items in the database.
    """
    pass

class BasicSearchResponse(DeepsearchApiRoutersV2ModelsSearchResult):
    """Search response that is received when connecting to the /search endpoint of USD Search API.
    
    This is a basic search response that is received when connecting to the /search endpoint of USD Search API.
    It is used to search for items in the database.
    """
    pass

class HybridSearchResponse(SearchResponse):
    """Search response that is received when connecting to the /search_hybrid endpoint of USD Search API.
    
    This is a search response that is received when connecting to the /search_hybrid endpoint of USD Search API.
    It is used to search for items in the database.
    """
    pass