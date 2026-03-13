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


import { AuthStatus } from "@omniverse/auth/data";
import React from "react";
import FormError from "./FormError";
import LoginSuccess from "./LoginSuccess";
var SSOPageContent = function (_a) {
    var _b;
    var auth = _a.auth, error = _a.error;
    if (error) {
        return React.createElement(FormError, null, (_b = error.message) !== null && _b !== void 0 ? _b : error.toString());
    }
    if (!auth) {
        return React.createElement(FormError, null, "Service is not responding.");
    }
    if (auth.errors && auth.errors.length) {
        return (React.createElement(React.Fragment, null, auth.errors.map(function (error) { return (React.createElement(FormError, { key: error }, error)); })));
    }
    if (auth.status === AuthStatus.OK) {
        return React.createElement(LoginSuccess, null);
    }
    return React.createElement(React.Fragment, null, auth.status);
};
export default SSOPageContent;
