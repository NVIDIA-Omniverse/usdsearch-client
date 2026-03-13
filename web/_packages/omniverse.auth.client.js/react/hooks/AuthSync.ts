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



import { useCallback, useState } from "react";
import { useHistory, useLocation } from "react-router-dom";
import { AuthenticationResult } from "../AuthForm";
import useNucleusSession from "./NucleusSession";

export default function useAuthSync() {
  const [result, setResult] = useState<AuthenticationResult | null>();
  const location = useLocation();
  const search = new URLSearchParams(location.search);
  const redirectURL = decodeURI(search.get("redirect") || "");
  const history = useHistory();

  const { setSession } = useNucleusSession();
  const sync = useCallback(
    async (auth: AuthenticationResult) => {
      setSession({ server: auth.server!, accessToken: auth.accessToken!, refreshToken: auth.refreshToken! });

      const redirectTo = (auth.extras && auth.extras.redirect) || redirectURL;
      const nonce = auth.nonce;
      if (redirectTo && !nonce) {
        // `nonce` argument is only used by new clients that
        // don't need to run an HTTP server for receiving authentication results.
        await sendAuth(redirectTo, auth);
      }
      setResult(auth);

      const navigateURL = auth.extras && auth.extras.navigate;
      if (navigateURL) {
        if (navigateURL.startsWith("http")) {
          window.location.href = navigateURL;
        } else {
          history.push(navigateURL);
        }
      }
    },
    [redirectURL, setSession, history]
  );

  return {
    redirectURL,
    result,
    sync,
  };
}

async function sendAuth(url: string, auth: AuthenticationResult): Promise<void> {
  const { extras, ...body } = auth;
  let response;
  try {
    response = await fetch(url, {
      body: JSON.stringify(body),
      method: "POST",
    });
  } catch (error) {
    console.error(error);
    throw new Error(
      "Unable to send results back to the application that initiated the authentication. " +
        "This error message is expected if your client was released prior to year 2021."
    );
  }

  if (!response.ok) {
    throw new Error(
      "Unable to send results back to the application that initiated the authentication. " +
        "This error message is expected if your client was released prior to year 2021."
    );
  }
}
