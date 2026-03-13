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



import { SSO } from "@omniverse/auth/client";
import { SSOSettings } from "@omniverse/auth/data";
import { useCallback, useEffect, useState } from "react";
import connect from "../Connection";
import { callAPI } from "../util/API";

export default function useSSOSettings(server: string) {
  const [settings, setSettings] = useState<SSOSettings[] | null>(null);
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
            http: () => httpSSOSettings(server),
            ws: () => wsSSOSettings(server),
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

async function httpSSOSettings(server: string): Promise<SSOSettings[]> {
  const response = await fetch(`https://${server}/omni/auth/api/sso/settings`, { cache: "force-cache" });
  const json = await response.json();
  return json.settings;
}

async function wsSSOSettings(server: string): Promise<SSOSettings[]> {
  let sso: SSO | null = null;
  try {
    sso = await connect(server, SSO, { get_settings: 0 });
    const settings = await sso.getSettings();
    return await settings.readAll();
  } finally {
    if (sso) {
      await sso.transport.close();
    }
  }
}
