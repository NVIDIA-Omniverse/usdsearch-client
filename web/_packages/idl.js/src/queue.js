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



export default class Queue {
  constructor(capacity = 0) {
    this.getters = [];
    this.putters = [];
    this.buffer = [];
    this.capacity = capacity;
  }

  get length() {
    return this.buffer.length;
  }

  put = (data) => {
    return new Promise((resolve) => {
      const getter = this.getters.pop();
      if (getter) {
        getter(data);
        resolve();
      } else if (!this.capacity || this.buffer.length < this.capacity) {
        this.buffer = [data].concat(this.buffer);
        resolve();
      } else {
        const putter = () => {
          resolve();
          return data;
        };
        this.putters = [putter].concat(this.putters);
      }
    });
  };

  get = () => {
    return new Promise((resolve) => {
      if (this.buffer.length) {
        const item = this.buffer.pop();
        resolve(item);
      } else {
        const putter = this.putters.pop();
        if (putter) {
          const item = putter();
          resolve(item);
        } else {
          this.getters = [resolve].concat(this.getters);
        }
      }
    });
  };
}
