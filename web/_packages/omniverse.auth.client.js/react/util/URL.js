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


export function joinURL() {
    var args = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        args[_i] = arguments[_i];
    }
    return args.reduce(function (path, value, index) {
        if (!value) {
            return path;
        }
        if (index !== 0 && !value.startsWith("/")) {
            value = "/" + value;
        }
        if (index !== args.length - 1 && value.endsWith("/")) {
            value = value.substring(0, value.length - 1);
        }
        return path + value;
    }, "");
}
export function getBaseURL() {
    var _a;
    var base = document.getElementById("public-url");
    var baseURL = (_a = base === null || base === void 0 ? void 0 : base.href) !== null && _a !== void 0 ? _a : window.location.href;
    if (baseURL) {
        if (baseURL === "/") {
            baseURL = "";
        }
        else {
            if (baseURL.endsWith("/")) {
                baseURL = baseURL.substr(0, baseURL.length - 1);
            }
        }
    }
    return baseURL;
}
