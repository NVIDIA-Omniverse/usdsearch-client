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



export default class Serializer {
  async serialize(data) {
    throw new Error("Not implemented.");
  }

  async deserialize(data) {
    throw new Error("Not implemented.");
  }
}

export const SerializerName = Symbol("SerializerName");

export function fromStringToArrayBuffer(str) {
  return new TextEncoder().encode(str).buffer;
}

export function fromArrayBufferToString(buffer) {
  return new TextDecoder().decode(buffer);
}

export function concatBuffers(...buffers) {
  const result = new Uint8Array(
    new ArrayBuffer(
      buffers.reduce((size, buffer) => size + buffer.byteLength, 0),
    ),
  );

  let offset = 0;
  for (const buffer of buffers) {
    result.set(new Uint8Array(buffer), offset);
    offset += buffer.byteLength;
  }
  return result.buffer;
}

export class SerializerFactory {
  static serializers = {};

  static register(serializerType) {
    SerializerFactory.serializers[serializerType[SerializerName]] =
      serializerType;
  }

  static create(serializerName) {
    const serializerType = SerializerFactory.serializers[serializerName];
    if (!serializerType) {
      throw new Error(`Serializer ${serializerName} is not registered.`);
    }
    return new serializerType();
  }
}
