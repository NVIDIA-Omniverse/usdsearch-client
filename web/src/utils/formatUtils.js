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

/**
 * Utility functions for formatting data
 */

/**
 * Format file size in human readable format
 * @param {number} size - Size in bytes
 * @returns {string} Formatted size string
 */
export const formatFileSize = (size) => {
  if (!size || size === 0) return "0 bytes";
  
  const bytes = parseInt(size, 10);
  if (isNaN(bytes)) return "Unknown";
  
  const kb = bytes / 1024;
  const mb = kb / 1024;
  const gb = mb / 1024;
  const tb = gb / 1024;
  
  if (tb >= 1) return `${tb.toFixed(2)} TB`;
  if (gb >= 1) return `${gb.toFixed(2)} GB`;
  if (mb >= 1) return `${mb.toFixed(2)} MB`;
  if (kb >= 1) return `${kb.toFixed(2)} KB`;
  return `${bytes} bytes`;
};

/**
 * Format date string to locale string
 * @param {string} dateString - ISO date string
 * @returns {string} Formatted date string
 */
export const formatDate = (dateString) => {
  if (!dateString) return "Unknown";
  try {
    return new Date(dateString).toLocaleString();
  } catch (error) {
    return dateString;
  }
};

/**
 * Find the highest scoring vector image from search result explanations
 * @param {Object} result - Search result object
 * @returns {string|null} Image URL or null if no vector images found
 */
export const getHighestScoringVectorImage = (result) => {
  if (!result?.metadata?.explanations) {
    return null;
  }

  let highestScore = -1;
  let highestScoringImage = null;

  // Iterate through all explanations
  result.metadata.explanations.forEach(explanation => {
    // Check if this explanation has matched_vectors
    if (explanation.matched_vectors && Array.isArray(explanation.matched_vectors)) {
      explanation.matched_vectors.forEach(vectorMatch => {
        // Check if this vector match has an image attribute and a score
        if (vectorMatch.image && vectorMatch.score > highestScore) {
          highestScore = vectorMatch.score;
          highestScoringImage = vectorMatch.image;
        }
      });
    }
  });

  return highestScoringImage;
};