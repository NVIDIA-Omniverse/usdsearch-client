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



export interface StreamOptions {
  capacity?: number;
}

export default class Stream<T> {
  public static IDLE: symbol;
  public static READING: symbol;
  public static END: symbol;
  public static CLOSED: symbol;
  public readonly status: symbol;
  public readonly capacity: number;

  public constructor(options?: StreamOptions);

  public write(data: T): Promise<void>;
  public end(): Promise<void>;
  public error(err: Error): Promise<void>;
  public read(): Promise<T | typeof Stream.END>;
  public readAll(): Promise<T[]>;
  public close(): Promise<void>;
  public [Symbol.asyncIterator](): AsyncIterator<T>;

  public on(event: "write", callback: (data: T) => Promise<void>): void;
  public on(event: Event, callback: Callback): void;
  public once(event: "write", callback: (data: T) => Promise<void>): void;
  public once(event: Event, callback: Callback): void;
  public off(event: "write", callback: (data: T) => Promise<void>): void;
  public off(event: Event, callback: Callback): void;
}

export type Event = "write" | "read" | "end" | "close";
type Callback = () => Promise<void>;