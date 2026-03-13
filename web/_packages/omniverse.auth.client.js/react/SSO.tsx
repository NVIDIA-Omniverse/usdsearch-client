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



import { SSO } from "@omniverse/auth";
import { Auth, AuthStatus, SSORedirect, SSOSettings } from "@omniverse/auth/data";
import React, { useEffect } from "react";
import { AuthenticationResult } from "./AuthForm";
import connect from "./Connection";
import { callAPI } from "./util/API";

export interface SSOPageProps {
  children?: React.ReactNode;
  params: string;
  search?: string;
  onAuth(result: AuthenticationResult): void;
  onError(error: Error): void;
}

const SSOAuth: React.FC<SSOPageProps> = ({ params, search = "", children, onAuth, onError }) => {
  if (!search) {
    search = window.location.search;
  }

  useEffect(() => {
    authenticate(params, search).then(onAuth).catch(onError);
  }, [params, search, onAuth, onError]);

  return <>{children}</>;
};

export default SSOAuth;

interface SSORedirectOptions {
  settings: SSOSettings;
  server: string;
  redirectBackTo: string;
  extras?: SSOExtras;
  nonce?: string;
}

export interface SSOState {
  type?: string;
  server: string;
  redirectBackTo?: string;
  nonce?: string;
  extras?: SSOExtras;
}

export interface SSOExtras {
  [key: string]: string;
}

export async function redirectToSSO({ settings, server, redirectBackTo, extras, nonce }: SSORedirectOptions) {
  if (!redirectBackTo.endsWith("/")) {
    redirectBackTo += "/";
  }

  const type = settings.type;
  const params: SSOState = {
    type,
    redirectBackTo,
    server,
    extras,
    nonce,
  };
  const state = await encodeState(params);

  redirectBackTo += state;

  const result = await callAPI({
    http: () => httpRedirectSSO(server, type, state, nonce),
    ws: () => wsRedirectSSO(server, type, state, nonce),
  });

  let url = result.redirect;
  url = url.replace("{redirect_url}", encodeURIComponent(redirectBackTo));
  url = url.replace("{redirect_url_state}", btoa(redirectBackTo));
  window.location.assign(url);
}

async function httpRedirectSSO(server: string, type: string, state?: string, nonce?: string): Promise<SSORedirect> {
  const params = new URLSearchParams();
  params.set("type", type);
  if (state) {
    params.set("state", state);
  }
  if (nonce) {
    params.set("nonce", nonce);
  }

  const response = await fetch(`https://${server}/omni/auth/api/sso/redirect?${params}`);
  return await response.json();
}

async function wsRedirectSSO(server: string, type: string, state?: string, nonce?: string): Promise<SSORedirect> {
  const sso = await connect(server, SSO, { redirect: 0 });
  try {
    const result = await sso.redirect({ type, state, nonce });
    if (result.status !== AuthStatus.OK) {
      throw result;
    }
    return result;
  } finally {
    await sso.transport.close();
  }
}

export async function authenticate(encodedSSO: string, urlSearchParams: string): Promise<AuthenticationResult> {
  const { server, type, nonce, extras } = decodeState(encodedSSO);
  if (!type) {
    throw new Error("The authentication type is not specified.");
  }

  return await authenticateSSO(server, type, urlSearchParams, nonce, extras);
}

export async function encodeState(params: SSOState): Promise<string> {
  const json = JSON.stringify(params);
  return await new Promise<string>((resolve, reject) => {
    const reader = new FileReader();
    reader.onerror = reject;
    reader.onloadend = () => {
      const result = (reader.result as string).split(",");
      const data = result[1];
      resolve(data.replace(/=/g, ""));
    };
    reader.readAsDataURL(new Blob([json]));
  });
}

export function decodeState(state: string): SSOState {
  const json = atob(state);
  return JSON.parse(json) as SSOState;
}

export async function authenticateSSO(
  server: string,
  type: string,
  query: string,
  nonce?: string,
  extras?: SSOExtras
): Promise<AuthenticationResult> {
  const search = new URLSearchParams(query);
  const params = Array.from(search.entries()).reduce<{
    [key: string]: string;
  }>((all, [name, value]) => {
    all[name] = value.replace(/ /g, "+");
    return all;
  }, {});

  const auth = await callAPI({
    http: () => httpAuthenticateSSO(server, type, params, nonce),
    ws: () => wsAuthenticateSSO(server, type, params, nonce),
  });

  return {
    accessToken: auth.access_token,
    refreshToken: auth.refresh_token,
    status: auth.status,
    username: auth.username,
    profile: auth.profile,
    nonce: auth.nonce,
    server,
    extras,
  };
}

async function httpAuthenticateSSO(
  server: string,
  type: string,
  params: Record<string, string>,
  nonce?: string
): Promise<Auth> {
  const response = await fetch(`https://${server}/omni/auth/api/sso/${type.toLowerCase()}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ ...params, nonce }),
  });
  return await response.json();
}

async function wsAuthenticateSSO(
  server: string,
  type: string,
  params: Record<string, string>,
  nonce?: string
): Promise<Auth> {
  const sso = await connect(server, SSO, { auth: 0 });
  try {
    return await sso.auth({ type, params, nonce });
  } finally {
    await sso.transport.close();
  }
}
