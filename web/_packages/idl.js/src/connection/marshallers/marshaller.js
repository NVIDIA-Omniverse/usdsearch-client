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



import { ObjectType, OptionalType, StreamType } from "../../schema.js";
import { SerializerFactory } from "../serializers";

export const MarshallerName = Symbol("MarshallerName");

export default class Marshaller {
  static [MarshallerName] = "bs"; // Binary separately

  constructor(serializer) {
    this.serializer = serializer;
  }

  async marshal(data, schema) {
    const marshaling = { ...data };

    const binary = [];
    const fields = [];

    for (const binaryField of this.introspect(marshaling, schema)) {
      fields.push(binaryField);
      binary.push(binaryField.get());
      binaryField.delete();
    }

    const content = await this.serializer.serialize(marshaling, schema);

    for (let i = 0; i < binary.length; i++) {
      const field = fields[i];
      const blob = binary[i];
      field.set(blob);
    }

    return [content, fields];
  }

  async unmarshal(data) {
    return this.serializer.deserialize(data);
  }

  *introspect(data, schema) {
    for (const [field, type] of Object.entries(schema.fields)) {
      if (type.kind === StreamType.kind) {
        yield new BinaryField(field, data);
      } else if (
        type.kind === OptionalType.kind &&
        type.type.kind === StreamType.kind
      ) {
        yield new BinaryField(field, data);
      } else if (type.kind === ObjectType.kind) {
        yield* this.introspect(data[field], type);
      }
    }
  }
}

export class BinaryField {
  constructor(name, owner) {
    this.name = name;
    this.owner = owner;
  }

  get() {
    return this.owner[this.name];
  }

  set(value) {
    this.owner[this.name] = value;
  }

  delete() {
    delete this.owner[this.name];
  }
}

export class MarshallerFactory {
  static marshallers = {};

  static register(marshallerType) {
    MarshallerFactory.marshallers[marshallerType[MarshallerName]] =
      marshallerType;
  }

  static create(marshallerName, serializerName) {
    const serializer = SerializerFactory.create(serializerName);
    const marshallerType = MarshallerFactory.marshallers[marshallerName];
    if (!marshallerType) {
      throw new Error(`Marshaller ${marshallerName} is not registered.`);
    }
    return new marshallerType(serializer);
  }
}

MarshallerFactory.register(Marshaller);
