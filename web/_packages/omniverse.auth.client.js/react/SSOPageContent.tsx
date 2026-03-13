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



import { AuthStatus } from "@omniverse/auth/data";
import React from "react";
import { AuthenticationResult } from "./AuthForm";
import FormError from "./FormError";
import LoginSuccess from "./LoginSuccess";

export interface SSOPageContentProps {
  auth?: AuthenticationResult | null;
  error?: Error | null;
}

const SSOPageContent: React.FC<SSOPageContentProps> = ({ auth, error }) => {
  if (error) {
    return <FormError>{error.message ?? error.toString()}</FormError>;
  }

  if (!auth) {
    return <FormError>Service is not responding.</FormError>;
  }

  if (auth.errors && auth.errors.length) {
    return (
      <>
        {auth.errors.map((error) => (
          <FormError key={error}>{error}</FormError>
        ))}
      </>
    );
  }

  if (auth.status === AuthStatus.OK) {
    return <LoginSuccess />;
  }

  return <>{auth.status}</>;
};

export default SSOPageContent;
