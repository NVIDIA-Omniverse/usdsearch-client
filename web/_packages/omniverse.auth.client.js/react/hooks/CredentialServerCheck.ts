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



import { Credentials } from "@omniverse/auth";
import { useCallback } from "react";
import connect from "../Connection";

export interface CredentialServerCheck {
  ok: boolean;
  server: string;
  errors?: string[];
}

export default function useCredentialServerCheck() {
  return useCallback(async (server: string): Promise<CredentialServerCheck> => {
    server = server.trim();
    if (!server) {
      return {
        ok: false,
        server,
        errors: ["You have to specify the server."],
      };
    }

    const omniverseProtocol = "omniverse://";
    const omniverse = server.indexOf(omniverseProtocol);
    if (omniverse !== -1) {
      server = server.substring(omniverse + omniverseProtocol.length);
      server = server.substring(0, server.indexOf("/"));
    } else {
      const match = server.match("https?://");
      if (match) {
        const [protocol] = match;
        server = server.substring(protocol.length);
        server = server.substring(0, server.indexOf("/"));
      }
    }

    let resolvedServer = await getCanonicalName(server);
    if (!resolvedServer) {
      console.log(`Cannot resolve the hostname, proceed with ${server}...`);
      resolvedServer = server;
    }

    try {
      const response = await fetch(`https://${resolvedServer}/omni/auth/api`);
      if (response.ok) {
        return {
          ok: true,
          server: resolvedServer,
        };
      }
    } catch (error) {}

    try {
      const connection = await connect(resolvedServer, Credentials, { auth: 0 });
      await connection.transport.close();
      return {
        ok: true,
        server: resolvedServer,
      };
    } catch (error) {
      console.log(error);
      return {
        ok: false,
        server,
        errors: [`Failed to connect to the server. (${error})`],
      };
    }
  }, []);
}

export async function getCanonicalName(server: string): Promise<string> {
  if (["127.0.0.1", "localhost"].includes(server)) {
    return server;
  }

  try {
    const response = await fetch(`http://${server}/_sys/canonical-name-json`);
    const data = await response.json();
    return data.fqdn ? data.fqdn : "";
  } catch (error) {
    return "";
  }
}
