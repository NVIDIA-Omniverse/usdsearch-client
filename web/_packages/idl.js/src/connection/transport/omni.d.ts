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



import Client, { Request, TransportName, TransportSettings } from "./index";
import Stream from "../../stream";

export default class OmniClientTransport extends Client {
  public static readonly [TransportName]: string;
  public static register(): void;
  public static create(
    settings: TransportSettings,
    args: any[]
  ): OmniClientTransport;

  protected prepared: boolean;
  public readonly url: string;

  constructor(options: OmniClientParams);
  public static create(settings: TransportSettings): OmniClientTransport;
  public prepare(): Promise<void>;
  public close(): Promise<void>;
  public call<TData extends object, TResult>(
    request: Request<TData>
  ): Promise<TResult>;
  public callMany<TData extends object, TResult>(
    request: Request<TData>
  ): Promise<Stream<TResult>>;

  public off(event: "prepare" | "close", callback: () => void): void;
  public off(event: "error", callback: (error: Error) => void): void;

  public on(event: "prepare" | "close", callback: () => void): void;
  public on(event: "error", callback: (error: Error) => void): void;

  public once(event: "prepare" | "close", callback: () => void): void;
  public once(event: "error", callback: (error: Error) => void): void;
}

export interface OmniClientParams {
  url: string;
}
