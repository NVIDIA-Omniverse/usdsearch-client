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
var Button = styled.button(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  background: #e0e0e0;\n  color: #6e6e6e;\n  box-sizing: border-box;\n  height: 30px;\n  padding: 0 10px;\n  min-width: 100px;\n  border: 1px solid transparent;\n  border-radius: 2px;\n  box-shadow: 0 3px 5px -2px #222;\n  font-family: unset;\n  font-size: 11pt;\n  cursor: pointer;\n  outline: none;\n  line-height: 1;\n\n  &:not(&[disabled]):active {\n    box-shadow: inset 0 2px 5px -3px #222;\n    outline: none;\n  }\n\n  &[disabled] {\n    cursor: default;\n    filter: grayscale(80%) brightness(0.5);\n  }\n\n  & > svg.fa-spinner {\n    margin-right: 0.5em;\n  }\n"], ["\n  background: #e0e0e0;\n  color: #6e6e6e;\n  box-sizing: border-box;\n  height: 30px;\n  padding: 0 10px;\n  min-width: 100px;\n  border: 1px solid transparent;\n  border-radius: 2px;\n  box-shadow: 0 3px 5px -2px #222;\n  font-family: unset;\n  font-size: 11pt;\n  cursor: pointer;\n  outline: none;\n  line-height: 1;\n\n  &:not(&[disabled]):active {\n    box-shadow: inset 0 2px 5px -3px #222;\n    outline: none;\n  }\n\n  &[disabled] {\n    cursor: default;\n    filter: grayscale(80%) brightness(0.5);\n  }\n\n  & > svg.fa-spinner {\n    margin-right: 0.5em;\n  }\n"])));
export default Button;
var templateObject_1;
