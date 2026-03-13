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



import { faCheck } from "@fortawesome/free-solid-svg-icons/faCheck";
import React from "react";
import styled from "styled-components";
import Icon from "./Icon";

interface LoginSuccessProps {
  className?: string;
}

const LoginSuccess: React.FC<LoginSuccessProps> = ({ className, children }) => {
  if (!children) {
    children = (
      <>
        You have successfully logged in. <br/>
        You can continue to work in your application. <br/>
      </>
    );
  }

  return (
    <Authenticated className={className}>
      <AuthenticatedIcon icon={faCheck} />
      {children}
    </Authenticated>
  );
};

const Authenticated = styled.div`
  background: #e0e0e0;
  color: #6e6e6e;
  margin: 0 auto;
  max-width: 450px;
  text-align: center;
`;

const AuthenticatedIcon = styled(Icon)`
  display: block;
  margin: 0 auto;
  text-align: center;
  color: #71a376;
  font-size: 24pt;
  line-height: 48pt;
`;

export default LoginSuccess;
