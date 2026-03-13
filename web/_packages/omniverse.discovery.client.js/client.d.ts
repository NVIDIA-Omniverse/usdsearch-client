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



import Client from "@omniverse/idl/connection/transport";
import Stream from "@omniverse/idl/stream";
import { InterfaceName, InterfaceOrigin, InterfaceCapabilities } from "@omniverse/idl/schema";
import * as data from "./data";

export class DiscoverySearch {
  public readonly transport: Client;
  constructor(transport: Client);

  
  /*
    Finds an entry for specified origin and interface.
    A query can specify the required capabilities, connection settings and
    other metadata.
   */
  public find(request: data.DiscoverySearchFindRequest): Promise<data.SearchResult>;
  
  /*
    Retrieves all registered interfaces for this discovery service.
   */
  public findAll(request?: data.DiscoverySearchFindAllRequest): Promise<Stream<data.SearchResult>>;
  

  public static readonly [InterfaceName]: string;
  public static readonly [InterfaceOrigin]: string;
  public static readonly [InterfaceCapabilities]?: { [method: string]: number };
}

export class DiscoveryRegistration {
  public readonly transport: Client;
  constructor(transport: Client);

  
  /*
    Registers a new service with specified connection settings and interfaces.
    The discovery keeps a subscription to ensure that registered service is
    still available.
    The service is removed from discovery as soon as it stops receiving health
    checks from the subscription.

    You can use `register_unsafe` to register a service without a subscription
    and health checks.
   */
  public register(request: data.DiscoveryRegistrationRegisterRequest): Promise<Stream<data.HealthCheck>>;
  
  /*
    Registers a new service without a health checking.
    It's a service responsibility to call `unregister_unsafe` when the provided
    functions become not available.
   */
  public registerUnsafe(request: data.DiscoveryRegistrationRegisterUnsafeRequest): Promise<data.HealthCheck>;
  
  /*
    Removes the service registered with `register_unsafe` from the discovery.
   */
  public unregisterUnsafe(request: data.DiscoveryRegistrationUnregisterUnsafeRequest): Promise<data.HealthCheck>;
  

  public static readonly [InterfaceName]: string;
  public static readonly [InterfaceOrigin]: string;
  public static readonly [InterfaceCapabilities]?: { [method: string]: number };
}
