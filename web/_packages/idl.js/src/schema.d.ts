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



import Stream from "./stream";

export interface SchemaType<T = any> {
  kind: symbol;
  validate(data: T): boolean;
}

export type NumberType = SchemaType<number>;
export type StringType = SchemaType<string>;
export type BooleanType = SchemaType<boolean>;
export type StreamType = SchemaType<Stream<ArrayBuffer>>;
export type LiteralType = <T extends number | string | boolean>(literal: T) => ({
  kind: symbol,
  value: T,
  validate(data: T): boolean;
});
export type OptionalType = <T extends SchemaType>(type: T) => ({
  kind: symbol;
  type: T;
  validate(data: any): boolean;
});

export type ArrayType = <T extends SchemaType>(type: T) => ({
  kind: symbol;
  type: T;
  validate(data: any): boolean;
});

export type ObjectType = <T extends { [field: string]: SchemaType }>(fields: T) => ({
  kind: symbol;
  fields: T;
  validate(data: object): boolean;
});

export type MapType = <T extends SchemaType>(type: T) => ({
  kind: symbol;
  type: T;
  validate(data: object): boolean;
});

export type EnumType = <T extends { [field: string]: string | number }>(members: T) => T & ({
  kind: symbol;
  members: T;
  validate(data: object): boolean;
});

export const InterfaceName: unique symbol;
export const InterfaceOrigin: unique symbol;
export const InterfaceCapabilities: unique symbol;

declare var Schema: {
  Number: NumberType,
  String: StringType,
  Boolean: BooleanType,
  Stream: StreamType,
  Literal: LiteralType,
  Optional: OptionalType,
  Array: ArrayType,
  Object: ObjectType,
  Map: MapType,
  Enum: EnumType,
  InterfaceName: typeof InterfaceName,
  InterfaceOrigin: typeof InterfaceOrigin,
  InterfaceCapabilities: typeof InterfaceCapabilities,
}

export default Schema;