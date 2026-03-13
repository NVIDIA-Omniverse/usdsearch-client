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
var SSOSplitter = styled.div(templateObject_1 || (templateObject_1 = __makeTemplateObject(["\n  text-align: center;\n  text-transform: uppercase;\n  font-size: 10pt;\n  flex: 0 0 100%;\n  margin: 1rem 0 0.75rem 0;\n  position: relative;\n\n  &:before {\n    position: absolute;\n    width: 50px;\n    height: 50%;\n    left: 15px;\n    top: 0;\n    bottom: 0;\n    border-bottom: 1px solid #969696;\n    content: \" \";\n  }\n\n  &:after {\n    position: absolute;\n    width: 50px;\n    height: 50%;\n    right: 15px;\n    top: 0;\n    bottom: 0;\n    border-bottom: 1px solid #969696;\n    content: \" \";\n  }\n"], ["\n  text-align: center;\n  text-transform: uppercase;\n  font-size: 10pt;\n  flex: 0 0 100%;\n  margin: 1rem 0 0.75rem 0;\n  position: relative;\n\n  &:before {\n    position: absolute;\n    width: 50px;\n    height: 50%;\n    left: 15px;\n    top: 0;\n    bottom: 0;\n    border-bottom: 1px solid #969696;\n    content: \" \";\n  }\n\n  &:after {\n    position: absolute;\n    width: 50px;\n    height: 50%;\n    right: 15px;\n    top: 0;\n    bottom: 0;\n    border-bottom: 1px solid #969696;\n    content: \" \";\n  }\n"])));
export default SSOSplitter;
var templateObject_1;
