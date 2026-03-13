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



import { Auth, AuthStatus } from "@omniverse/auth/data";
import AuthMessages from "../AuthMessages";
import {
  encodeResetPasswordPayload,
  GenerateResetPasswordPayloadError,
  GenerateResetPasswordPayloadOptions,
  resetPassword,
  ResetPasswordError,
  ResetPasswordPayload
} from "./ResetPassword";


export type InvitationPayload = ResetPasswordPayload;

export function encodeInvitationPayload(
  server: string,
  username: string,
  adminToken: string,
  { state }: GenerateResetPasswordPayloadOptions = {}
): Promise<string> {
  try {
    return encodeResetPasswordPayload(server, username, adminToken, { state });
  } catch (error) {
    if (error instanceof GenerateResetPasswordPayloadError) {
      throw new GenerateInvitationPayloadError(error.result);
    }
    throw error;
  }
}

export class GenerateInvitationPayloadError extends Error {
  public readonly messages: { [status: string]: string } = {
    ...AuthMessages,
    [AuthStatus.Denied]: "You don't have access to generate tokens for this user.",
  };
  public readonly result: { status: AuthStatus };

  constructor(result: { status: AuthStatus }) {
    super();
    this.result = result;
    this.message = this.messages[result.status] || DefaultErrorMessage(result.status);
  }
}

export function decodeInvitationPayload(encoded: string): InvitationPayload {
  const json: InvitationPayload = JSON.parse(atob(encoded));
  if (!json.username || !json.token || !json.server) {
    throw new Error("Invalid invitation payload.");
  }
  return json;
}

export async function inviteUser(password: string, payload: InvitationPayload): Promise<Auth> {
  try {
    return resetPassword(password, payload);
  } catch (error) {
    if (error instanceof ResetPasswordError) {
      throw new InvitationError(error.result);
    }
    throw error;
  }
}

export class InvitationError extends Error {
  public readonly messages: { [status: string]: string } = {
    ...AuthMessages,
    [AuthStatus.Expired]: "The link has expired.",
  };
  public readonly result: { status: AuthStatus };

  constructor(result: { status: AuthStatus }) {
    super();
    this.result = result;
    this.message = this.messages[result.status] || DefaultErrorMessage(result.status);
  }
}

export const DefaultErrorMessage = (status: string) => `Unknown error, please contact administrator (${status}).`;