/**
 * SPDX-FileCopyrightText: Copyright (c) 2024-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
 * SPDX-License-Identifier: MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */

import React from 'react';
import { useImageLoader } from '../hooks/useImageLoader';
import { ImageWithSkeleton } from './ImageSkeleton';

/**
 * Asset image component that loads images from /v3/images API
 * Falls back to base64 image data if available
 */
const AssetImage = ({ 
  result,
  getHeaders,
  apiUrl,
  width = "100%",
  height = "120px",
  borderRadius = "md",
  ...imageProps 
}) => {
  // Get asset URL for API call
  const assetUrl = result?.source?.base_key || result?.source?.url || result?.id;
  
  // Check if we have base64 image data as fallback
  const fallbackImage = result?.source?.image;
  
  // Load image from API
  const { imageData, isLoading, error } = useImageLoader(
    assetUrl, 
    getHeaders, 
    apiUrl, 
    !!assetUrl // Only enable if we have an asset URL
  );

  // Determine what to display
  let src = null;
  let hasError = false;
  let errorMessage = "No Image";

  if (imageData) {
    // Use API image data
    src = imageData;
  } else if (fallbackImage && !isLoading) {
    // Use fallback base64 image if API failed and we're not loading
    src = `data:image/png;base64,${fallbackImage}`;
  } else if (error && !fallbackImage) {
    // Show error state only if no fallback available
    hasError = true;
    
    // Customize error message based on error type
    if (error.status === 404) {
      errorMessage = "Image Not Found";
    } else if (error.status === 403) {
      errorMessage = "Access Denied";
    } else if (error.status >= 400 && error.status < 500) {
      errorMessage = "Invalid Request";
    } else if (error.status >= 500) {
      errorMessage = "Server Error";
    } else {
      errorMessage = "Load Failed";
    }
  }

  return (
    <ImageWithSkeleton
      src={src}
      alt="Asset thumbnail"
      isLoading={isLoading && !fallbackImage}
      hasError={hasError}
      width={width}
      height={height}
      borderRadius={borderRadius}
      objectFit="cover"
      skeletonProps={{
        variant: "ghost"
      }}
      errorContent={errorMessage}
      {...imageProps}
    />
  );
};

export default AssetImage;