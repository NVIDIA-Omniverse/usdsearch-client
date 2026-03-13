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



import styled from "styled-components";

const Button = styled.button`
  background: #e0e0e0;
  color: #6e6e6e;
  box-sizing: border-box;
  height: 30px;
  padding: 0 10px;
  min-width: 100px;
  border: 1px solid transparent;
  border-radius: 2px;
  box-shadow: 0 3px 5px -2px #222;
  font-family: unset;
  font-size: 11pt;
  cursor: pointer;
  outline: none;
  line-height: 1;

  &:not(&[disabled]):active {
    box-shadow: inset 0 2px 5px -3px #222;
    outline: none;
  }

  &[disabled] {
    cursor: default;
    filter: grayscale(80%) brightness(0.5);
  }

  & > svg.fa-spinner {
    margin-right: 0.5em;
  }
`;

export default Button;
