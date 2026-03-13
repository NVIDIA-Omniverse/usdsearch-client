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



import Client, { ClientFactory, TransportName } from "./index";
import Marshaller from "../marshallers/marshaller.js";
import Stream from "../../stream.js";

export default class HttpFileClient extends Client {
  static [TransportName] = "http_file";

  static register() {
    ClientFactory.register(HttpFileClient, {});
  }

  static create({ name, params: paramsJSON, meta = {} }) {
    if (name !== HttpFileClient[TransportName]) {
      throw new Error(`Invalid transport name '${name}'.`);
    }

    const params = JSON.parse(paramsJSON);
    return new HttpFileClient(params);
  }

  constructor({ uri }) {
    super();
    this.uri = uri;
  }

  async call({ interfaceName, methodName, request, schemas }) {
    const marshaller = new Marshaller(null);

    let files = [...marshaller.introspect(request, schemas.request)];
    let file = null;
    if (files.length > 1) {
      throw new Error("Multiple files are not supported.");
    } else if (files.length === 1) {
      file = files[0];
    }

    const query = new URLSearchParams();
    for (const [key, value] of Object.entries(request)) {
      if (!file || file.name !== key) {
        query.set(key, value);
      }
    }

    const url = `${this.uri}/${interfaceName}/${methodName}/?${query}`;

    let data;
    if (file) {
      const stream = file.get();
      data = await stream.readAll();
    }

    const response = await fetch(url, { method: "POST", body: new Blob(data) });
    if (response.status >= 400) {
      throw new Error(`Error ${response.status}.`);
    }

    const result = {};
    for (const header of response.headers.keys()) {
      if (header.startsWith("Http-File-")) {
        const key = header.slice("Http-File-".length);
        result[key] = response.headers.get(header);
      }
    }

    files = [...marshaller.introspect(result, schemas.response)];
    if (files.length > 1) {
      throw new Error("Multiple files are not supported.");
    } else if (files.length === 1) {
      file = files[0];

      const reader = response.body.getReader();
      const stream = (result[file.name] = new Stream());
      stream.on("read", async () => {
        const chunk = await reader.read();
        await stream.write(chunk.value);
        if (chunk.done) {
          await stream.end();
        }
      });
    }

    return result;
  }
}
