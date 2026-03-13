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



import EventEmitter from "../../emitter";

export default class Client {
  constructor() {
    this.events = new EventEmitter(["prepare", "close", "error"]);
    this.prepared = false;
  }

  async prepare() {
    this.prepared = true;
    this.events.emit("prepare");
  }

  async close() {
    this.prepared = false;
    this.events.emit("close");
  }

  async call({ interfaceName, methodName, request, schemas }) {
    throw new Error("Not implemented.");
  }

  async callMany({ interfaceName, methodName, request, schemas }) {
    throw new Error("Not implemented.");
  }

  on(event, callback) {
    this.events.on(event, callback);
  }

  once(event, callback) {
    this.events.once(event, callback);
  }

  off(event, callback) {
    this.events.off(event, callback);
  }
}

export const TransportName = Symbol("TransportName");

export class TransportError extends Error {
  constructor(message, code = -1) {
    super();
    this.message = message;
    this.code = code;
  }
}

export class ClientFactory {
  static registered = {};

  static register(client, meta, options) {
    const transportName = client[TransportName];

    let registered;
    if (transportName in ClientFactory.registered) {
      registered = ClientFactory.registered[transportName];
    } else {
      registered = ClientFactory.registered[transportName] = [];
    }

    registered.push({ name: transportName, meta, options, type: client });
  }

  static create(settings) {
    const transportName = settings.name;
    if (!(transportName in ClientFactory.registered)) {
      throw new Error(
        `Client with '${transportName}' transport name is not registered.`,
      );
    }

    const registered = ClientFactory.registered[transportName];
    const receivedMeta = settings.meta || {};

    for (const { meta, options, type } of registered) {
      if (metaEqual(meta, receivedMeta)) {
        return type.create(settings, options);
      }
    }

    throw new Error(
      `Meta for specified '${transportName}' transport is not registered.`,
    );
  }

  static getSupported() {
    const supported = [];
    for (const registered of Object.values(ClientFactory.registered)) {
      for (const { name, meta = {} } of registered) {
        supported.push({ name, meta });
      }
    }
    return supported;
  }
}

function metaEqual(a, b) {
  if (Object.keys(a).length !== Object.keys(b).length) {
    return false;
  }

  for (const key of Object.keys(a)) {
    if (a[key] !== b[key]) {
      return false;
    }
  }
  return true;
}
