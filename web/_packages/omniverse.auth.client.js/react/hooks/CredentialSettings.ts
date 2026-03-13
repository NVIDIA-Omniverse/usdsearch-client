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
import { CredentialSettings } from "@omniverse/auth/data";
import { useCallback, useEffect, useState } from "react";
import connect from "../Connection";
import { callAPI } from "../util/API";

export default function useCredentialSettings(server: string): {
  settings: CredentialSettings | null;
  errors: string[];
  retry: () => unknown;
} {
  const [settings, setSettings] = useState<CredentialSettings | null>(null);
  const [errors, setErrors] = useState<string[]>([]);
  const [queryDate, setQueryDate] = useState(() => new Date());

  const retry = useCallback(() => {
    setQueryDate(new Date());
  }, []);

  useEffect(() => {
    let subscribed = true;
    setSettings(null);
    setErrors([]);

    let debounced: number;
    if (server) {
      debounced = window.setTimeout(async () => {
        try {
          const settings = await callAPI({
            http: () => httpCredentialSettings(server),
            ws: () => wsCredentialSettings(server),
          });

          if (subscribed) {
            setSettings(settings);
          }
        } catch (error) {
          setErrors([`Failed to connect to the server (${error}).`]);
          console.warn(error);
        }
      }, 300);
    }

    return () => {
      subscribed = false;
      if (debounced) {
        clearTimeout(debounced);
      }
    };
  }, [server, queryDate]);

  return { settings, errors, retry };
}

async function httpCredentialSettings(server: string): Promise<CredentialSettings> {
  const response = await fetch(`https://${server}/omni/auth/api/sso/settings`, { cache: "force-cache" });
  const json = await response.json();
  return {
    can_register: json.can_register,
    is_ui_visible: json.can_use_credentials,
    login_url: json.login_url,
  };
}

async function wsCredentialSettings(server: string): Promise<CredentialSettings> {
  let credentials: Credentials | null = null;
  try {
    credentials = await connect(server, Credentials, { get_settings: 0 });
    return await credentials.getSettings();
  } finally {
    if (credentials) {
      await credentials.transport.close();
    }
  }
}
