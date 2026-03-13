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



import { Credentials } from "@omniverse/auth/client";
import { AuthStatus } from "@omniverse/auth/data";
import { useCallback } from "react";
import { Authentication, AuthenticationResult } from "../AuthForm";
import AuthMessages from "../AuthMessages";
import connect, { handleConnectionErrors } from "../Connection";

export default function useCredentialAuth() {
  return useCallback(
    async ({ username, password, server, nonce, extras }: Authentication): Promise<AuthenticationResult> => {
      let credentials: Credentials | null = null;

      if (!server) {
        return {
          errors: ["You have to specify the server."],
          server: "",
        };
      }

      return connect(server, Credentials, { auth: 0 })
        .then((conn) => (credentials = conn))
        .then((credentials) => credentials.auth({ username, password, nonce }))
        .then(
          (result): AuthenticationResult =>
            result.status === AuthStatus.OK
              ? {
                  server,
                  status: result.status,
                  accessToken: result.access_token,
                  refreshToken: result.refresh_token,
                  username: result.username,
                  profile: result.profile,
                  nonce: result.nonce,
                  extras,
                }
              : {
                  server,
                  status: result.status,
                  errors: [AuthMessages[result.status] ?? "Unknown error."],
                  nonce: result.nonce,
                }
        )
        .catch((error) => {
          return handleConnectionErrors(server, error);
        })
        .finally(() => {
          if (credentials) {
            credentials.transport.close();
          }
        });
    },
    []
  );
}
