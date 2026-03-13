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



import EventEmitter from "./emitter";
import Queue from "./queue";

export default class Stream {
  static IDLE = Symbol("IDLE");
  static READING = Symbol("READING");
  static CLOSED = Symbol("CLOSED");
  static END = Symbol("END");

  constructor({ capacity = 0 } = {}) {
    this.queue = new Queue(capacity);
    this.status = Stream.IDLE;
    this.events = new EventEmitter(["read", "write", "close", "end"]);
  }

  get capacity() {
    return this.queue.capacity;
  }

  async write(data) {
    if (this.status === Stream.CLOSED) {
      throw Stream.CLOSED;
    }
    if (this.status === Stream.END) {
      throw Stream.END;
    }

    await this.queue.put(data);
    this.events.emit("write", data);
  }

  async end() {
    await this.queue.put(Stream.END);
  }

  async error(err) {
    await this.queue.put(err);
  }

  async close() {
    this.status = Stream.CLOSED;
    await this.queue.put(Stream.CLOSED);
    this.queue = new Queue();
    this.events.emit("close");
  }

  async read() {
    if (this.status === Stream.IDLE) {
      this.status = Stream.READING;
    } else if (this.status === Stream.CLOSED) {
      throw Stream.CLOSED;
    }

    this.events.emit("read");

    const item = await this.queue.get();
    if (item === Stream.CLOSED) {
      throw Stream.CLOSED;
    }

    if (item instanceof Error) {
      throw item;
    }

    if (item === Stream.END) {
      this.status = Stream.END;
      this.events.emit("end");
    }
    return item;
  }

  async *[Symbol.asyncIterator]() {
    while (true) {
      const item = await this.read();
      if (item === Stream.END) {
        break;
      } else {
        yield item;
      }
    }
  }

  async readAll() {
    const buffer = [];
    while (true) {
      const item = await this.read();
      if (item === Stream.END) {
        break;
      } else {
        buffer.push(item);
      }
    }
    return buffer;
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
