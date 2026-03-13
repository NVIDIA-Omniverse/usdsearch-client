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



import Schema from "@omniverse/idl/schema";
import * as _data from "./data";

export class DiscoverySearch {
  constructor(transport) {
    this.transport = transport;
  }
  
  /*
    Finds an entry for specified origin and interface.
    A query can specify the required capabilities, connection settings and
    other metadata.
   */
  async find({query, }) {
    const _request = {query, version: _data.DiscoverySearchFindClientVersion.value, };
    if (!_data.DiscoverySearchFindRequest.validate(_request)) {
      throw new Error("Invalid DiscoverySearchFindRequest.");
    }
    return await this.transport.call({ interfaceName: "DiscoverySearch", methodName: "find", request: _request, schemas: { request: _data.DiscoverySearchFindRequest, response: _data.SearchResult }});
  }
  
  /*
    Retrieves all registered interfaces for this discovery service.
   */
  async findAll() {
    const _request = {version: _data.DiscoverySearchFindAllClientVersion.value, };
    if (!_data.DiscoverySearchFindAllRequest.validate(_request)) {
      throw new Error("Invalid DiscoverySearchFindAllRequest.");
    }
    return await this.transport.callMany({ interfaceName: "DiscoverySearch", methodName: "find_all", request: _request, schemas: { request: _data.DiscoverySearchFindAllRequest, response: _data.SearchResult }});
  }
  
}
DiscoverySearch[Schema.InterfaceName] = "DiscoverySearch";
DiscoverySearch[Schema.InterfaceOrigin] = "Discovery.idl.ts";
DiscoverySearch[Schema.InterfaceCapabilities] = _data.DiscoverySearchClientLocalCapabilities.value;

export class DiscoveryRegistration {
  constructor(transport) {
    this.transport = transport;
  }
  
  /*
    Registers a new service with specified connection settings and interfaces.
    The discovery keeps a subscription to ensure that registered service is
    still available.
    The service is removed from discovery as soon as it stops receiving health
    checks from the subscription.

    You can use `register_unsafe` to register a service without a subscription
    and health checks.
   */
  async register({manifest, }) {
    const _request = {manifest, version: _data.DiscoveryRegistrationRegisterClientVersion.value, };
    if (!_data.DiscoveryRegistrationRegisterRequest.validate(_request)) {
      throw new Error("Invalid DiscoveryRegistrationRegisterRequest.");
    }
    return await this.transport.callMany({ interfaceName: "DiscoveryRegistration", methodName: "register", request: _request, schemas: { request: _data.DiscoveryRegistrationRegisterRequest, response: _data.HealthCheck }});
  }
  
  /*
    Registers a new service without a health checking.
    It's a service responsibility to call `unregister_unsafe` when the provided
    functions become not available.
   */
  async registerUnsafe({manifest, }) {
    const _request = {manifest, version: _data.DiscoveryRegistrationRegisterUnsafeClientVersion.value, };
    if (!_data.DiscoveryRegistrationRegisterUnsafeRequest.validate(_request)) {
      throw new Error("Invalid DiscoveryRegistrationRegisterUnsafeRequest.");
    }
    return await this.transport.call({ interfaceName: "DiscoveryRegistration", methodName: "register_unsafe", request: _request, schemas: { request: _data.DiscoveryRegistrationRegisterUnsafeRequest, response: _data.HealthCheck }});
  }
  
  /*
    Removes the service registered with `register_unsafe` from the discovery.
   */
  async unregisterUnsafe({manifest, }) {
    const _request = {manifest, version: _data.DiscoveryRegistrationUnregisterUnsafeClientVersion.value, };
    if (!_data.DiscoveryRegistrationUnregisterUnsafeRequest.validate(_request)) {
      throw new Error("Invalid DiscoveryRegistrationUnregisterUnsafeRequest.");
    }
    return await this.transport.call({ interfaceName: "DiscoveryRegistration", methodName: "unregister_unsafe", request: _request, schemas: { request: _data.DiscoveryRegistrationUnregisterUnsafeRequest, response: _data.HealthCheck }});
  }
  
}
DiscoveryRegistration[Schema.InterfaceName] = "DiscoveryRegistration";
DiscoveryRegistration[Schema.InterfaceOrigin] = "Discovery.idl.ts";
DiscoveryRegistration[Schema.InterfaceCapabilities] = _data.DiscoveryRegistrationClientLocalCapabilities.value;
