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



import { SchemaType } from "../../schema";
import Stream from "../../stream";

export const TransportName: unique symbol;

export default abstract class Client {
  public static readonly [TransportName]: string;
  public static create(
    settings: TransportSettings,
    options?: TransportOptions
  ): Client;

  protected prepared: boolean;
  public prepare(): Promise<void>;
  public close(): Promise<void>;
  public abstract call<TData extends object, TResult>(
    request: Request<TData>
  ): Promise<TResult>;
  public abstract callMany<TData extends object, TResult>(
    request: Request<TData>
  ): Promise<Stream<TResult>>;

  public off(event: "prepare" | "close", callback: () => void): void;
  public off(event: "error", callback: (error: Error) => void): void;

  public on(event: "prepare" | "close", callback: () => void): void;
  public on(event: "error", callback: (error: Error) => void): void;

  public once(event: "prepare" | "close", callback: () => void): void;
  public once(event: "error", callback: (error: Error) => void): void;
}

export interface Request<TData extends object> {
  interfaceName: string;
  methodName: string;
  request: TData;
  schemas: {
    request: SchemaType;
    response: SchemaType;
  };
}

export type TransportEvent = "prepare" | "close" | "error";
export type Callback = () => void;

export interface TransportSettings {
  name: string;
  params: string;
  meta?: TransportMeta;
}

export type TransportMeta = { [key: string]: string };
export type TransportOptions = { [name: string]: any };

export declare class TransportError extends Error {
  constructor(message: string, code?: number);
}

export interface ClientType<T extends Client> {
  new (...args: any[]): T;
}

export interface SupportedTransport {
  name: string;
  meta?: TransportMeta;
}

export declare class ClientFactory {
  public static register<T extends Client>(
    client: ClientType<T>,
    meta: TransportMeta,
    options?: TransportOptions
  ): void;

  public static create<T extends Client>(settings: TransportSettings): T;
  public static getSupported(): SupportedTransport[];
}
