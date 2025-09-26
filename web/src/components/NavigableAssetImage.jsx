/**
 * SPDX-FileCopyrightText: Copyright (c) 2024-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
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

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Box, IconButton, Spinner } from '@chakra-ui/react';
import { ChevronLeftIcon, ChevronRightIcon } from '@chakra-ui/icons';
import { ImageWithSkeleton } from './ImageSkeleton';
import { loadImage, getCachedOffsets, loadProgressiveImages } from '../utils/imageLoader';

/**
 * Navigable asset image component with left-right arrow navigation
 * Supports img_offset parameter for viewing multiple images per asset
 */
const NavigableAssetImage = ({ 
  result,
  index,
  getHeaders,
  apiUrl,
  width = "100%",
  height = "120px",
  borderRadius = "md",
  ...imageProps 
}) => {
  const elementRef = useRef(null);
  const [currentOffset, setCurrentOffset] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [imageData, setImageData] = useState(null);
  const [error, setError] = useState(null);
  const [isHovered, setIsHovered] = useState(false);
  const [maxOffset, setMaxOffset] = useState(null); // null means unknown, 0 means only one image
  const [isLoadingProgressive, setIsLoadingProgressive] = useState(false);
  const [hasAttemptedProgressive, setHasAttemptedProgressive] = useState(false);
  const [hasLoadingError, setHasLoadingError] = useState(false);
  
  const assetUrl = result?.source?.base_key || result?.source?.url || result?.id;

  // Load image for current offset
  const loadCurrentImage = useCallback(async (offset) => {
    if (!assetUrl || !getHeaders) return;
    
    setIsLoading(true);
    setError(null);
    setHasLoadingError(false);
    
    try {
      const effectiveApiUrl = apiUrl || '';
      // Pass the result object only for offset 0 to enable vector image detection
      const resultForVectorDetection = offset === 0 ? result : null;
      const data = await loadImage(assetUrl, getHeaders, effectiveApiUrl, false, offset, resultForVectorDetection);
      setImageData(data);
    } catch (err) {
      setError(err);
      setImageData(null);
      // Set loading error state for non-404 errors
      if (err.status && err.status !== 404) {
        setHasLoadingError(true);
      }
    } finally {
      setIsLoading(false);
    }
  }, [assetUrl, getHeaders, apiUrl, result]);

  // Load image when currentOffset changes (including initial load at offset 0)
  useEffect(() => {
    loadCurrentImage(currentOffset);
  }, [currentOffset, loadCurrentImage]);

  // Handle case where we discover there's only one image and user is on a higher offset
  useEffect(() => {
    if (maxOffset === 0 && currentOffset > 0) {
      // Clear any error state from the failed higher offset and reset to offset 0
      setError(null);
      setHasLoadingError(false);
      setImageData(null); // Clear current image data to force reload
      setCurrentOffset(0);
      // The loadCurrentImage(0) will be triggered by the currentOffset change
    }
  }, [maxOffset, currentOffset]);

  // Progressive loading when user first navigates
  const startProgressiveLoading = useCallback(async () => {
    if (!assetUrl || !getHeaders || isLoadingProgressive || hasAttemptedProgressive) return;
    
    setIsLoadingProgressive(true);
    setHasAttemptedProgressive(true);
    
    try {
      const effectiveApiUrl = apiUrl || '';
      const { images, maxOffset: discoveredMax } = await loadProgressiveImages(
        assetUrl, 
        getHeaders, 
        effectiveApiUrl,
        1, // Start from offset 1
        20, // Max parallel requests (use global limit)
        result // Pass result for vector image detection on offset 0
      );
      
      setMaxOffset(discoveredMax);
      
      // If no additional images found, we only have offset 0
      if (discoveredMax < 1) {
        setMaxOffset(0); // Only one image (offset 0)
      }
    } catch (err) {
      console.error('Progressive loading failed:', err);
      setMaxOffset(0); // Only one image (offset 0)
    } finally {
      setIsLoadingProgressive(false);
    }
  }, [assetUrl, getHeaders, apiUrl, isLoadingProgressive, hasAttemptedProgressive, result]);

  // Get available offsets from cache
  const effectiveApiUrl = apiUrl || '';
  const availableOffsets = getCachedOffsets(assetUrl || '', effectiveApiUrl);
  const canGoLeft = currentOffset > 0;
  
  // Determine if we can go right and if arrow should be shown
  let canGoRight = false;
  let showRightArrow = false;
  
  if (maxOffset === null && !hasAttemptedProgressive) {
    // Haven't attempted discovery yet, show enabled right arrow
    canGoRight = true;
    showRightArrow = true;
  } else if (maxOffset === null && hasAttemptedProgressive) {
    // Discovery in progress, check cache
    canGoRight = availableOffsets.includes(currentOffset + 1);
    showRightArrow = canGoRight;
  } else if (maxOffset !== null) {
    // Discovery complete
    if (maxOffset === 0) {
      // Single image case - show disabled right arrow if we're on offset 0
      canGoRight = false;
      showRightArrow = currentOffset === 0;
    } else {
      // Multiple images - normal navigation
      canGoRight = currentOffset < maxOffset;
      showRightArrow = canGoRight;
    }
  }

  // Navigation handlers
  const handlePrevious = useCallback(() => {
    if (!canGoLeft) return;
    const newOffset = currentOffset - 1;
    setCurrentOffset(newOffset);
  }, [canGoLeft, currentOffset]);

  const handleNext = useCallback(() => {
    if (!canGoRight) return;
    
    const newOffset = currentOffset + 1;
    setCurrentOffset(newOffset);
    
    // If this is the first navigation and we haven't attempted progressive loading, start it
    if (!hasAttemptedProgressive) {
      startProgressiveLoading();
    }
  }, [canGoRight, currentOffset, hasAttemptedProgressive, startProgressiveLoading]);

  // Determine what to display
  let src = null;
  let hasError = false;
  let errorMessage = "No Image";

  if (imageData) {
    src = imageData;
  } else if (result?.source?.image && currentOffset === 0 && !isLoading) {
    // Use fallback base64 image only for offset 0 if API failed and we're not loading
    src = `data:image/png;base64,${result.source.image}`;
  } else if (error && !result?.source?.image) {
    hasError = true;
    
    if (error.status === 404) {
      errorMessage = currentOffset === 0 ? "Image Not Found" : "No More Images";
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

  const showNavigation = isHovered && (canGoLeft || showRightArrow);

  return (
    <Box 
      ref={elementRef}
      position="relative"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      width={width}
      height={height}
    >
      <ImageWithSkeleton
        src={src}
        alt="Asset thumbnail"
        isLoading={isLoading && !result?.source?.image}
        hasError={hasError}
        width="100%"
        height="100%"
        borderRadius={borderRadius}
        objectFit="cover"
        skeletonProps={{
          variant: "ghost"
        }}
        errorContent={errorMessage}
        {...imageProps}
      />
      
      {/* Navigation arrows - only visible on hover */}
      {showNavigation && (
        <>
          {/* Left arrow */}
          {canGoLeft && (
            <IconButton
              position="absolute"
              left="8px"
              top="50%"
              transform="translateY(-50%)"
              size="sm"
              icon={<ChevronLeftIcon />}
              onClick={(e) => {
                e.stopPropagation();
                handlePrevious();
              }}
              bg="rgba(0,0,0,0.7)"
              color="white"
              _hover={{ bg: "rgba(0,0,0,0.9)" }}
              aria-label="Previous image"
              isDisabled={isLoading}
            />
          )}
          
          {/* Right arrow */}
          {showRightArrow && (
            <IconButton
              position="absolute"
              right="8px"
              top="50%"
              transform="translateY(-50%)"
              size="sm"
              icon={<ChevronRightIcon />}
              onClick={(e) => {
                e.stopPropagation();
                if (canGoRight) {
                  handleNext();
                }
              }}
              bg="rgba(0,0,0,0.7)"
              color="white"
              _hover={{ bg: canGoRight ? "rgba(0,0,0,0.9)" : "rgba(0,0,0,0.7)" }}
              aria-label="Next image"
              isDisabled={isLoading || !canGoRight}
              opacity={canGoRight ? 1 : 0.5}
            />
          )}
        </>
      )}
      
      {/* Image counter - show if we know there are multiple images, if we're not on offset 0, or if we have a single image after discovery */}
      {(maxOffset !== null && maxOffset >= 0) || currentOffset > 0 ? (
        <Box
          position="absolute"
          top="8px"
          right="8px"
          bg="rgba(0,0,0,0.7)"
          color="white"
          px={2}
          py={1}
          borderRadius="md"
          fontSize="xs"
          fontWeight="bold"
        >
          {currentOffset + 1}{maxOffset !== null ? `/${maxOffset + 1}` : ''}
        </Box>
      ) : null}
      
      {/* Loading indicator for progressive loading */}
      {isLoadingProgressive && (
        <Box
          position="absolute"
          bottom="8px"
          left="8px"
          bg="rgba(0,0,0,0.7)"
          color="white"
          px={2}
          py={1}
          borderRadius="md"
          fontSize="xs"
          display="flex"
          alignItems="center"
          gap={1}
        >
          <Spinner size="xs" />
          Loading...
        </Box>
      )}
      
      {/* Error indicator for non-404 errors */}
      {hasLoadingError && (
        <Box
          position="absolute"
          bottom="8px"
          left="8px"
          bg="rgba(139,0,0,0.7)"
          color="white"
          px={2}
          py={1}
          borderRadius="md"
          fontSize="xs"
        >
          Error loading images
        </Box>
      )}
    </Box>
  );
};

export default NavigableAssetImage;