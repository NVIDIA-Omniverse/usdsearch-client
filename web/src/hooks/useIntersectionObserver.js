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

import { useEffect, useRef, useState } from 'react';

/**
 * Hook to observe element intersection with viewport
 * @param {Object} options - Intersection observer options
 * @param {string|number} rootMargin - Root margin (e.g., "200px" or "50%")
 * @param {number|number[]} threshold - Intersection threshold(s)
 * @param {Element} root - Root element for intersection (null for viewport)
 * @returns {[React.RefObject, boolean]} - [ref to attach to element, isIntersecting]
 */
export const useIntersectionObserver = ({
  rootMargin = '0px',
  threshold = 0.1,
  root = null
} = {}) => {
  const [isIntersecting, setIsIntersecting] = useState(false);
  const targetRef = useRef(null);

  useEffect(() => {
    const element = targetRef.current;
    if (!element) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsIntersecting(entry.isIntersecting);
      },
      {
        root,
        rootMargin,
        threshold
      }
    );

    observer.observe(element);

    return () => {
      observer.unobserve(element);
    };
  }, [rootMargin, threshold, root]);

  return [targetRef, isIntersecting];
};

/**
 * Hook to get visibility status of multiple elements
 * @param {Object} options - Intersection observer options
 * @returns {[Function, Map]} - [registerElement function, visibilityMap]
 */
export const useMultipleIntersectionObserver = ({
  rootMargin = '0px',
  threshold = 0.1,
  root = null
} = {}) => {
  const [visibilityMap, setVisibilityMap] = useState(new Map());
  const observerRef = useRef(null);
  const elementsRef = useRef(new Map());

  useEffect(() => {
    observerRef.current = new IntersectionObserver(
      (entries) => {
        setVisibilityMap(prev => {
          const newMap = new Map(prev);
          entries.forEach(entry => {
            const id = entry.target.dataset.observerId;
            if (id) {
              newMap.set(id, entry.isIntersecting);
            }
          });
          return newMap;
        });
      },
      {
        root,
        rootMargin,
        threshold
      }
    );

    return () => {
      if (observerRef.current) {
        observerRef.current.disconnect();
      }
    };
  }, [rootMargin, threshold, root]);

  const registerElement = (id, element) => {
    if (!element || !observerRef.current) return;

    // Unobserve previous element with same id
    const prevElement = elementsRef.current.get(id);
    if (prevElement) {
      observerRef.current.unobserve(prevElement);
    }

    // Set data attribute for identification
    element.dataset.observerId = id;
    
    // Store and observe new element
    elementsRef.current.set(id, element);
    observerRef.current.observe(element);
  };

  return [registerElement, visibilityMap];
};