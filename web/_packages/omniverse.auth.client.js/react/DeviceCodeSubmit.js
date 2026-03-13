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


import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";
import DeviceCodeStatus from "./DeviceCodeStatus";
import Form from "./Form";
import FormError from "./FormError";
import FormSpinner from "./FormSpinner";
import { useDeviceFlowSubmit } from "./hooks/DeviceFlow";
import useNucleusSession from "./hooks/NucleusSession";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
var DeviceCodeSubmit = function (_a) {
    var code = _a.code;
    var _b = useState(true), loading = _b[0], setLoading = _b[1];
    var _c = useState(null), status = _c[0], setStatus = _c[1];
    var _d = useState(""), error = _d[0], setError = _d[1];
    var session = useNucleusSession();
    var submitUserCode = useDeviceFlowSubmit();
    useEffect(function () {
        submitUserCode({ code: code })
            .then(function (result) { return setStatus(result.status); })
            .catch(function (error) { return setError(error.message || error.toString()); })
            .finally(function () { return setLoading(false); });
    }, [code, submitUserCode]);
    if (!session.established) {
        return React.createElement(Redirect, { to: "/" });
    }
    return (React.createElement(Form, null,
        React.createElement(NvidiaLogo, null),
        React.createElement(OmniverseLogo, null),
        React.createElement(DeviceCodeSubmitBody, { loading: loading, status: status, error: error })));
};
var DeviceCodeSubmitBody = function (_a) {
    var loading = _a.loading, status = _a.status, error = _a.error;
    if (loading) {
        return React.createElement(FormSpinner, null);
    }
    if (error) {
        return React.createElement(FormError, null, error);
    }
    return React.createElement(DeviceCodeStatus, { status: status });
};
export default DeviceCodeSubmit;
