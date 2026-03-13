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



import { Meta, SupportedTransport } from "@omniverse/discovery/data";
import { default as ClientTransport } from "@omniverse/idl/connection/transport";
import WebSocketClient from "@omniverse/idl/connection/transport/websocket";
import {
  InterfaceCapabilities,
  InterfaceName,
  InterfaceOrigin,
} from "@omniverse/idl/schema";

export default class DiscoverySearch {
  constructor(uri: string, options?: DiscoverySearchOptions);
  find<T>(
    clientType: ClientType<T>,
    meta?: Meta,
    supportedTransport?: SupportedTransport[],
    capabilities?: { [method: string]: number },
    accessToken?: string,
  ): Promise<T & DiscoverySearchInfo>;

  close(): void;
}

export type DiscoverySearchOptions = ConnectOptions;

export interface DiscoverySearchInfo {
  [InterfaceCapabilities]?: Record<string, number>;
  [ServiceMeta]?: Record<string, string>;
}

export interface ClientType<T> {
  readonly [InterfaceName]: string;
  readonly [InterfaceOrigin]: string;
  new (transport: ClientTransport): T;
}

export class DiscoveryError extends Error {}

interface ConnectOptions {
  timeout?: number;

  /**
   * Forces to use secure connections.
   */
  secure?: boolean;

  /**
   * JSON Web Token to authenticate the connection.
   */
  accessToken?: string;
}

/**
 * Creates a WebSocketClient instance for communicating with the discovery service
 * prioritizing secure path-based routing.
 */
export function connect(
  uri: string,
  options?: ConnectOptions
): Promise<WebSocketClient>;
export function createPathBasedClient(
  uri: string,
  protocol?: string,
  accessToken?: string,
): Promise<WebSocketClient | undefined>;
export function createPortBasedClient(
  uri: string,
  accessToken?: string
): Promise<WebSocketClient | undefined>;

export const ServiceMeta: unique symbol;
