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



import DiscoverySearch, { ClientType, DiscoveryError } from "@omniverse/discovery";

export default async function connect<T>(
  server: string,
  clientType: ClientType<T>,
  capabilities: Record<string, number> = {}
): Promise<T> {
  const discovery = new DiscoverySearch(server);
  try {
    const supportedTransport = undefined;
    const client = await discovery.find(clientType, { deployment: "external" }, supportedTransport, capabilities);
    if (!client) {
      throw new DiscoveryError();
    }
    return client;
  } finally {
    discovery.close();
  }
}

export function handleConnectionErrors(server: string, error: Error) {
  console.error(error);
  if (error instanceof Event && error.type === "error") {
    return {
      server,
      errors: [`Cannot connect to the authentication service. (${error.message})`],
    };
  }
  if (error instanceof DiscoveryError) {
    return {
      server,
      errors: [`Cannot connect to the authentication service. (${error.message})`],
    };
  }
  return {
    server,
    errors: [`Unexpected error. Try again later.`],
  };
}
