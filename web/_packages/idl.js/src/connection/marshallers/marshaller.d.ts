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



import Serializer from "../serializers/index";
import { SchemaType } from "../../schema";

export const MarshallerName: unique symbol;

export default class Marshaller {
  public static readonly [MarshallerName]: string;
  constructor(serializer: Serializer);
  public marshal(data: object, schema: SchemaType): Promise<[ArrayBuffer, BinaryField[]]>;
  public unmarshal(data: ArrayBuffer): Promise<object>;
  public introspect(data: object, schema: SchemaType): Iterator<BinaryField>;
}

export interface BinaryField {
  get(): ArrayBuffer;
  set(value: ArrayBuffer): void;
  delete(): void;
}

export interface MarshallerType<T extends Marshaller> {
  new (...args: any[]): T;
}

export class MarshallerFactory {
  public static register<T extends Marshaller>(marshallerType: MarshallerType<T>): void;
  public static create<T extends Marshaller>(marshallerName: string, serializerName: string): T;
}