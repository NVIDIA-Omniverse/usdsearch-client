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

export const NumberType = {
  kind: Symbol("Number"),
  validate: (data) => typeof data === "number",
};

export const StringType = {
  kind: Symbol("String"),
  validate: (data) => typeof data === "string",
};

export const BooleanType = {
  kind: Symbol("Boolean"),
  validate: (data) => typeof data === "boolean",
};

export const StreamType = {
  kind: Symbol("Stream"),
  validate: (data) =>
    data instanceof Stream ||
    (data && data.constructor && data.constructor.name === "Stream"),
};

const LiteralKind = Symbol("Literal");
export const LiteralType = (value) => ({
  kind: LiteralKind,
  value,
  validate: (data) => data === value,
});
LiteralType.kind = LiteralKind;

const OptionalKind = Symbol("Optional");
export const OptionalType = (type) => ({
  kind: OptionalKind,
  type,
  validate: (data) => typeof data === "undefined" || type.validate(data),
});
OptionalType.kind = OptionalKind;

const ArrayKind = Symbol("Array");
export const ArrayType = (type) => ({
  kind: ArrayKind,
  type,
  validate: (data) =>
    data instanceof Array && data.every((item) => type.validate(item)),
});
ArrayType.kind = ArrayKind;

const ObjectKind = Symbol("Object");
export const ObjectType = (fields) => ({
  kind: ObjectKind,
  fields,
  validate: (data) =>
    typeof data === "object" &&
    Object.entries(fields).every(([field, type]) => type.validate(data[field])),
});
ObjectType.kind = ObjectKind;

const MapKind = Symbol("Map");
export const MapType = (type) => ({
  kind: MapKind,
  type,
  validate: (data) =>
    typeof data === "object" &&
    Object.values(data).every((value) => type.validate(value)),
});
MapType.kind = MapKind;

const EnumKind = Symbol("Enum");
export const EnumType = (members) => ({
  ...members,
  members,
  kind: EnumKind,
  validate: (data) => Object.values(members).includes(data),
});
EnumType.kind = EnumKind;

export const InterfaceName = Symbol("InterfaceName");
export const InterfaceOrigin = Symbol("InterfaceOrigin");
export const InterfaceCapabilities = Symbol("InterfaceCapabilities");

const Schema = {
  Number: NumberType,
  String: StringType,
  Boolean: BooleanType,
  Stream: StreamType,
  Array: ArrayType,
  Object: ObjectType,
  Optional: OptionalType,
  Map: MapType,
  Enum: EnumType,
  Literal: LiteralType,
  InterfaceName: InterfaceName,
  InterfaceOrigin: InterfaceOrigin,
  InterfaceCapabilities: InterfaceCapabilities,
};

export default Schema;
