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

import { useState, useEffect } from 'react';
import { loadImage } from '../utils/imageLoader';

/**
 * Custom hook for loading images with state management
 * @param {string} assetUrl - Asset URL to load image for
 * @param {Function} getHeaders - Function to get auth headers
 * @param {string} apiUrl - Base API URL
 * @param {boolean} enabled - Whether to start loading immediately
 * @returns {Object} - { imageData, isLoading, error }
 */
export const useImageLoader = (assetUrl, getHeaders, apiUrl, enabled = true) => {
  const [imageData, setImageData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [attemptedUrls] = useState(new Set());

  useEffect(() => {
    // Only load if we haven't attempted this exact URL before
    if (!assetUrl || !enabled || attemptedUrls.has(assetUrl)) {
      return;
    }
    
    if (!getHeaders) {
      return;
    }

    // apiUrl can be empty string (uses relative URLs to current host)
    const effectiveApiUrl = apiUrl || '';

    // Mark this URL as attempted immediately to prevent re-runs
    attemptedUrls.add(assetUrl);
    setIsLoading(true);
    setError(null);

    loadImage(assetUrl, getHeaders, effectiveApiUrl)
      .then(data => {
        setImageData(data);
      })
      .catch(err => {
        setError(err);
        setImageData(null);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, [assetUrl, enabled]); // Removed getHeaders and apiUrl from deps to prevent re-runs

  return {
    imageData,
    isLoading,
    error
  };
};

/**
 * Hook for managing multiple image loads
 * @param {string[]} assetUrls - Array of asset URLs
 * @param {Function} getHeaders - Function to get auth headers
 * @param {string} apiUrl - Base API URL
 * @returns {Object} - { images: Map, loadingStates: Map, errors: Map, progress }
 */
export const useMultipleImageLoader = (assetUrls, getHeaders, apiUrl) => {
  const [images, setImages] = useState(new Map());
  const [loadingStates, setLoadingStates] = useState(new Map());
  const [errors, setErrors] = useState(new Map());
  const [progress, setProgress] = useState({ loaded: 0, total: 0 });

  useEffect(() => {
    if (!assetUrls || assetUrls.length === 0) {
      setImages(new Map());
      setLoadingStates(new Map());
      setErrors(new Map());
      setProgress({ loaded: 0, total: 0 });
      return;
    }

    // Initialize loading states
    const initialLoadingStates = new Map();
    assetUrls.forEach(url => {
      if (url) {
        initialLoadingStates.set(url, true);
      }
    });
    setLoadingStates(initialLoadingStates);
    setProgress({ loaded: 0, total: assetUrls.filter(Boolean).length });

    // Load all images
    const loadPromises = assetUrls
      .filter(Boolean)
      .map(async (assetUrl) => {
        try {
          const imageData = await loadImage(assetUrl, getHeaders, apiUrl);
          
          // Update state atomically
          setImages(prev => new Map(prev).set(assetUrl, imageData));
          setLoadingStates(prev => new Map(prev).set(assetUrl, false));
          setProgress(prev => ({ ...prev, loaded: prev.loaded + 1 }));
          
        } catch (error) {
          console.error(`Failed to load image for ${assetUrl}:`, error);
          
          setErrors(prev => new Map(prev).set(assetUrl, error));
          setLoadingStates(prev => new Map(prev).set(assetUrl, false));
          setProgress(prev => ({ ...prev, loaded: prev.loaded + 1 }));
        }
      });

    // Wait for all images to complete (success or failure)
    Promise.allSettled(loadPromises);

  }, [assetUrls, getHeaders, apiUrl]);

  return {
    images,
    loadingStates,
    errors,
    progress
  };
};