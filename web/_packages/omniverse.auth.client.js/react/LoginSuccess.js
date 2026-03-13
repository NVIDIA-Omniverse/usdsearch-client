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
import React from "react";
import styled from "styled-components";
import Icon from "./Icon";
var LoginSuccess = function (_a) {
    var className = _a.className, children = _a.children;
    if (!children) {
        children = (React.createElement(React.Fragment, null,
            "You have successfully logged in. ",
            React.createElement("br", null),
            "You can continue to work in your application. ",
            React.createElement("br", null)));
    }
    return (React.createElement(Authenticated, { className: className },
        React.createElement(AuthenticatedIcon, { icon: faCheck }),
        children));
};
var Authenticated = styled.div(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  background: #e0e0e0;\n  color: #6e6e6e;\n  margin: 0 auto;\n  max-width: 450px;\n  text-align: center;\n"], ["\n  background: #e0e0e0;\n  color: #6e6e6e;\n  margin: 0 auto;\n  max-width: 450px;\n  text-align: center;\n"])));
var AuthenticatedIcon = styled(Icon)(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  display: block;\n  margin: 0 auto;\n  text-align: center;\n  color: #71a376;\n  font-size: 24pt;\n  line-height: 48pt;\n"], ["\n  display: block;\n  margin: 0 auto;\n  text-align: center;\n  color: #71a376;\n  font-size: 24pt;\n  line-height: 48pt;\n"])));
export default LoginSuccess;
var templateObject_1, templateObject_2;
