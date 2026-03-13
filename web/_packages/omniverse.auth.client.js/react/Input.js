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
import styled from "styled-components";
var Input = styled.input(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  display: block;\n  font-family: inherit;\n  font-size: 14px;\n  box-sizing: border-box;\n  width: 100%;\n  padding: 5px 15px;\n  border-radius: 3px;\n  border: none;\n  background: ", ";\n  color: #6e6e6e;\n  z-index: 1;\n\n  &::placeholder {\n    color: ", ";\n  }\n"], ["\n  display: block;\n  font-family: inherit;\n  font-size: 14px;\n  box-sizing: border-box;\n  width: 100%;\n  padding: 5px 15px;\n  border-radius: 3px;\n  border: none;\n  background: ", ";\n  color: #6e6e6e;\n  z-index: 1;\n\n  &::placeholder {\n    color: ", ";\n  }\n"])), function (_a) {
    var disabled = _a.disabled;
    return (disabled ? "#a5a5a5" : "#e0e0e0");
}, function (_a) {
    var disabled = _a.disabled;
    return (disabled ? "#909090" : "#bbb");
});
export default Input;
var templateObject_1;
