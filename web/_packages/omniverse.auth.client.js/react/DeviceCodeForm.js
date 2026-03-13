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
import { AuthStatus } from "@omniverse/auth/data";
import React, { useState } from "react";
import CodeInput from "react-code-input";
import { Redirect } from "react-router-dom";
import ButtonGroup from "./ButtonGroup";
import DeviceCodeStatus from "./DeviceCodeStatus";
import Form from "./Form";
import FormErrorList from "./FormErrorList";
import FormGroup from "./FormGroup";
import Headline from "./Headline";
import { useDeviceFlowSubmit } from "./hooks/DeviceFlow";
import useForm from "./hooks/Form";
import useNucleusSession from "./hooks/NucleusSession";
import LoginButton from "./LoginButton";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
import Spinner from "./Spinner";
import styled from "styled-components";
var DeviceCodeForm = function (_a) {
    var _b, _c;
    var _d = _a.initial, initial = _d === void 0 ? {} : _d, onStart = _a.onStart, onSubmit = _a.onSubmit, onSuccess = _a.onSuccess, onFail = _a.onFail;
    var _e = useState(initial.code || ""), code = _e[0], setCode = _e[1];
    var submitUserCode = useDeviceFlowSubmit();
    var form = useForm({
        fields: {
            code: code,
        },
        onStart: onStart,
        onSubmit: onSubmit || submitUserCode,
        onSuccess: onSuccess,
        onFail: onFail,
    });
    var session = useNucleusSession();
    if (!session.established) {
        return React.createElement(Redirect, { to: "/" });
    }
    return (React.createElement(StyledDeviceCodeForm, null,
        React.createElement(NvidiaLogo, null),
        React.createElement(OmniverseLogo, null),
        React.createElement(FormErrorList, { errors: form.errors }),
        ((_b = form.result) === null || _b === void 0 ? void 0 : _b.status) !== AuthStatus.OK && (React.createElement(Headline, null,
            "Please enter the verification code to log in. ",
            React.createElement("br", null),
            "(",
            session.server,
            ")")),
        form.result && React.createElement(DeviceCodeStatus, { status: form.result.status }),
        ((_c = form.result) === null || _c === void 0 ? void 0 : _c.status) !== AuthStatus.OK && (React.createElement(React.Fragment, null,
            React.createElement(CodeInputGroup, null,
                React.createElement(CodeInput, { name: "code", autoFocus: true, inputMode: "verbatim", inputStyle: inputStyle, forceUppercase: true, fields: 8, type: "text", value: code, disabled: form.loading, onChange: setCode })),
            React.createElement(ButtonGroup, null,
                React.createElement(LoginButton, { name: "submit", disabled: form.loading, onClick: form.submit },
                    form.loading && React.createElement(Spinner, null),
                    "Verify"))))));
};
var StyledDeviceCodeForm = styled(Form)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  width: 475px;\n"], ["\n  width: 475px;\n"])));
var CodeInputGroup = styled(FormGroup)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: flex;\n  justify-content: center;\n"], ["\n  display: flex;\n  justify-content: center;\n"])));
var inputStyle = {
    appearance: "textfield",
    borderRadius: "6px",
    border: "1px solid lightgrey",
    boxShadow: "rgba(0, 0, 0, 0.1) 0px 0px 10px 0px",
    margin: "4px",
    width: "42px",
    height: "42px",
    fontSize: "24px",
    fontFamily: "inherit",
    boxSizing: "border-box",
    color: "black",
    backgroundColor: "white",
    overflow: "visible",
    textAlign: "center"
};
export default DeviceCodeForm;
var templateObject_1, templateObject_2;
