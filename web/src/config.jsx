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

// If not set it uses the local 'api/' endpoint
export const apiUrl = process.env.REACT_APP_API_URL || "";

export const defaultEmbeddingFieldName = process.env.REACT_APP_DEFAULT_EMBEDDING_FIELD_NAME || "siglip2-embedding.embedding";
export const defaultEmbeddingDimension = process.env.REACT_APP_DEFAULT_EMBEDDING_DIMENSION || 1536;

// Default embedding configuration
export const defaultEmbeddingConfig = {
  field_name: defaultEmbeddingFieldName,
  dimension: 1536
};

// Server name to URL mapping configuration
// Expects a JSON string in format: {"server1": "http://url1", "server2": "http://url2"}
let serverMapping = {};
try {
  const mappingStr = process.env.REACT_APP_SERVER_MAPPING || "{}";
  serverMapping = JSON.parse(mappingStr);
} catch (error) {
  console.error("Failed to parse SERVER_MAPPING configuration:", error);
  serverMapping = {};
}
export const SERVER_MAPPING = serverMapping;

// Image processing configuration
export const IMAGE_SIZE = 224;

// Duplicate removal configuration
export const DUPLICATE_REMOVAL_THRESHOLD = process.env.REACT_APP_DUPLICATE_REMOVAL_THRESHOLD || 0.0001;

// Check if running on HTTPS (required for clipboard API)
export const IS_HTTPS = typeof window !== 'undefined' && window.location.protocol === 'https:';

// Feature flags configuration
export const FEATURE_FLAGS = {
  // Enable/disable feedback modal - enabled by default, can be disabled via env var
  ENABLE_FEEDBACK_MODAL: process.env.REACT_APP_ENABLE_FEEDBACK_MODAL === "true",
};

// Authentication configuration
export const AUTH_CONFIG = {
  // Enable/disable authentication methods - show Basic Auth by default, others opt-in
  ENABLE_NUCLEUS_AUTH: process.env.REACT_APP_ENABLE_NUCLEUS_AUTH === "true",
  ENABLE_API_KEY_AUTH: process.env.REACT_APP_ENABLE_API_KEY_AUTH === "true",
  ENABLE_BASIC_AUTH: process.env.REACT_APP_ENABLE_BASIC_AUTH !== "false",
  
  // Default values if provided
  DEFAULT_NUCLEUS_TOKEN: process.env.REACT_APP_DEFAULT_NUCLEUS_TOKEN || "",
  DEFAULT_API_KEY: process.env.REACT_APP_DEFAULT_API_KEY || "",
  DEFAULT_USERNAME: process.env.REACT_APP_DEFAULT_USERNAME || "",
  DEFAULT_PASSWORD: process.env.REACT_APP_DEFAULT_PASSWORD || "",
};
