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


var _a;
import { AuthStatus } from "@omniverse/auth/data";
var AuthMessages = (_a = {},
    _a[AuthStatus.Disabled] = "This account is disabled by administrator.",
    _a[AuthStatus.Expired] = "The session is expired.",
    _a[AuthStatus.Exists] = "This user already exists.",
    _a[AuthStatus.NotFound] = "User is not found.",
    _a[AuthStatus.ReadOnly] = "The setting for this user can be changed only by the " +
        "system administrator or with the service configuration.",
    _a[AuthStatus.Denied] = "Wrong credentials or the user does not exist.",
    _a[AuthStatus.UsernameRequired] = "Username is required.",
    _a[AuthStatus.NotSupported] = "This authentication method is not supported.",
    _a[AuthStatus.InternalError] = "Internal server error has occurred. Please contact administrator or try again later.",
    _a[AuthStatus.ConnectionError] = "Cannot establish a connection to remote authentication servers. Try again later.",
    _a[AuthStatus.InvalidUsername] = "Username can only contain alphanumeric characters and underscores.",
    _a[AuthStatus.UnknownError] = "Unknown error has occurred. Please contact administrator.",
    _a[AuthStatus.InvalidToken] = "The provided token is invalid.",
    _a[AuthStatus.Subscribed] = "Failed to subscribe to authentication results.",
    _a[AuthStatus.InvalidRequest] = "Invalid request.",
    _a[AuthStatus.Pending] = "Please try again later.",
    _a);
export default AuthMessages;
