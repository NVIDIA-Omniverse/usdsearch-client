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
import React, { useCallback } from "react";
import styled from "styled-components";
import Button from "./Button";
import Spinner from "./Spinner";
var SSOButton = function (_a) {
    var _b = _a.loading, loading = _b === void 0 ? false : _b, setting = _a.setting, onClick = _a.onClick;
    var redirect = useCallback(function () {
        onClick(setting);
    }, [setting, onClick]);
    return (React.createElement(StyledSSOButton, { disabled: loading, onClick: redirect },
        loading ? React.createElement(Spinner, null) : setting.image && React.createElement(StyledPicture, { src: setting.image }),
        "Log in with ",
        setting.public_name));
};
export var StyledSSOButton = styled(Button)(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  position: relative;\n  background: #666;\n  color: white;\n  padding: 0 10px;\n  border-color: #909090;\n  margin: 0.25rem 0;\n  box-sizing: border-box;\n\n  & > svg.fa-spinner {\n    margin-right: 10px;\n  }\n"], ["\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  position: relative;\n  background: #666;\n  color: white;\n  padding: 0 10px;\n  border-color: #909090;\n  margin: 0.25rem 0;\n  box-sizing: border-box;\n\n  & > svg.fa-spinner {\n    margin-right: 10px;\n  }\n"])));
var StyledPicture = styled.img(templateObject_2 || (templateObject_2 = __makeTemplateObject(["\n  max-width: 100%;\n  max-height: 100%;\n  margin-right: 10px;\n  cursor: pointer;\n  width: 20px;\n  height: 20px;\n"], ["\n  max-width: 100%;\n  max-height: 100%;\n  margin-right: 10px;\n  cursor: pointer;\n  width: 20px;\n  height: 20px;\n"])));
export default SSOButton;
var templateObject_1, templateObject_2;
