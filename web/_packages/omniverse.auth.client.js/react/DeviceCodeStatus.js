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


var __makeTemplateObject = (this && this.__makeTemplateObject) || function (cooked, raw) {
    if (Object.defineProperty) { Object.defineProperty(cooked, "raw", { value: raw }); } else { cooked.raw = raw; }
    return cooked;
};
import { faCheck } from "@fortawesome/free-solid-svg-icons/faCheck";
import { faExclamationCircle } from "@fortawesome/free-solid-svg-icons/faExclamationCircle";
import { AuthStatus } from "@omniverse/auth/data";
import React from "react";
import styled from "styled-components";
import useRedirectURL from "./hooks/LoginRedirect";
import Icon from "./Icon";
import NavLink from "./NavLink";
var DeviceCodeStatus = function (_a) {
    var status = _a.status;
    var loginRedirect = useRedirectURL();
    if (status === AuthStatus.OK) {
        return (React.createElement(StyledDeviceCodeStatus, null,
            React.createElement(DeviceCodeStatusIcon, { icon: faCheck, type: "success" }),
            React.createElement(DeviceCodeStatusText, null,
                "You have successfully logged in. ",
                React.createElement("br", null),
                "You can continue to work in your application.")));
    }
    else if (status === AuthStatus.Expired || status === AuthStatus.InvalidToken) {
        return (React.createElement(StyledDeviceCodeStatus, null,
            React.createElement(DeviceCodeStatusIcon, { icon: faExclamationCircle, type: "error" }),
            React.createElement(DeviceCodeStatusText, null,
                "Your session has expired. ",
                React.createElement("br", null),
                "Please ",
                React.createElement(NavLink, { to: loginRedirect }, "log in"),
                " again.")));
    }
    else if (status === AuthStatus.NotFound) {
        return (React.createElement(StyledDeviceCodeStatus, null,
            React.createElement(DeviceCodeStatusIcon, { icon: faExclamationCircle, type: "error" }),
            React.createElement(DeviceCodeStatusText, null,
                "This user code is not found or expired. ",
                React.createElement("br", null),
                "Please try to authenticate in the application again.")));
    }
    else if (status === AuthStatus.Disabled) {
        return (React.createElement(StyledDeviceCodeStatus, null,
            React.createElement(DeviceCodeStatusIcon, { icon: faExclamationCircle, type: "error" }),
            React.createElement(DeviceCodeStatusText, null, "Your account has been disabled.")));
    }
    else {
        return (React.createElement(StyledDeviceCodeStatus, null,
            React.createElement(DeviceCodeStatusIcon, { icon: faExclamationCircle, type: "error" }),
            React.createElement(DeviceCodeStatusText, null,
                "Unknown error, please try again later (",
                status,
                ").")));
    }
};
var StyledDeviceCodeStatus = styled.div(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: flex;\n  gap: 0.5em;\n  padding: 0 15px;\n"], ["\n  display: flex;\n  gap: 0.5em;\n  padding: 0 15px;\n"])));
var DeviceCodeStatusIcon = styled(Icon)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  font-size: 18pt;\n  margin-top: 5px;\n  color: ", ";\n"], ["\n  font-size: 18pt;\n  margin-top: 5px;\n  color: ", ";\n"])), function (_a) {
    var type = _a.type;
    return (type === "success" ? "#76b900" : "#d46a6a");
});
var DeviceCodeStatusText = styled.div(templateObject_3 || (templateObject_3 = __makeTemplateObject(["\n  font-size: 10pt;\n"], ["\n  font-size: 10pt;\n"])));
export default DeviceCodeStatus;
var templateObject_1, templateObject_2, templateObject_3;
