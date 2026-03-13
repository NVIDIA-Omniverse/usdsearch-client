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



import { DeviceFlow } from "@omniverse/auth";
import { DeviceSubmit } from "@omniverse/auth/data";
import { useCallback } from "react";
import connect from "../Connection";
import useNucleusSession from "./NucleusSession";

export interface DeviceFlowSubmit {
  code: string;
}

export function useDeviceFlowSubmit() {
  const { getSession } = useNucleusSession();

  return useCallback(
    async ({ code }: DeviceFlowSubmit): Promise<DeviceSubmit> => {
      const session = await getSession();
      if (!session) {
        throw new Error("You must be authenticated to send the user code.");
      }

      let deviceFlow: DeviceFlow | null = null;
      try {
        deviceFlow = await connect(session.server, DeviceFlow);
      } catch (error) {
        throw new Error(`Failed to connect to the service. (${error})`);
      }

      try {
        return await deviceFlow.submit({ access_token: session.accessToken, user_code: code });
      } finally {
        if (deviceFlow) {
          await deviceFlow.transport.close();
        }
      }
    },
    [getSession]
  );
}
