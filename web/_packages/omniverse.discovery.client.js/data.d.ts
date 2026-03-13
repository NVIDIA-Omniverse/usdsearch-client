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





export type Capabilities = {
  [function_name: string]: number,
};

export type DiscoverySearchServerRemoteCapabilities = Capabilities;

export class DiscoverySearchServerLocalCapabilities {
  public static value: {'find': 2, 'find_all': 2};
}

export type DiscoverySearchServerCapabilities = DiscoverySearchServerRemoteCapabilities;

export type DiscoverySearchClientRemoteCapabilities = Capabilities;

export class DiscoverySearchClientLocalCapabilities {
  public static value: {'find': 2, 'find_all': 2};
}

export type DiscoverySearchClientCapabilities = DiscoverySearchClientLocalCapabilities;

export type DiscoverySearchFindAllServerRemoteVersion = number;

export class DiscoverySearchFindAllServerLocalVersion {
  public static value: 2;
}

export type DiscoverySearchFindAllServerVersion = DiscoverySearchFindAllServerRemoteVersion;

export type DiscoverySearchFindAllClientRemoteVersion = number;

export class DiscoverySearchFindAllClientLocalVersion {
  public static value: 2;
}

export type DiscoverySearchFindServerRemoteVersion = number;

export class DiscoverySearchFindServerLocalVersion {
  public static value: 2;
}

export type DiscoverySearchFindServerVersion = DiscoverySearchFindServerRemoteVersion;

export type DiscoverySearchFindClientRemoteVersion = number;

export class DiscoverySearchFindClientLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationServerRemoteCapabilities = Capabilities;

export class DiscoveryRegistrationServerLocalCapabilities {
  public static value: {'register': 2, 'register_unsafe': 2, 'unregister_unsafe': 2};
}

export type DiscoveryRegistrationServerCapabilities = DiscoveryRegistrationServerRemoteCapabilities;

export type DiscoveryRegistrationClientRemoteCapabilities = Capabilities;

export class DiscoveryRegistrationClientLocalCapabilities {
  public static value: {'register': 2, 'register_unsafe': 2, 'unregister_unsafe': 2};
}

export type DiscoveryRegistrationClientCapabilities = DiscoveryRegistrationClientLocalCapabilities;

export type DiscoveryRegistrationUnregisterUnsafeServerRemoteVersion = number;

export class DiscoveryRegistrationUnregisterUnsafeServerLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationUnregisterUnsafeServerVersion = DiscoveryRegistrationUnregisterUnsafeServerRemoteVersion;

export type DiscoveryRegistrationUnregisterUnsafeClientRemoteVersion = number;

export class DiscoveryRegistrationUnregisterUnsafeClientLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationRegisterUnsafeServerRemoteVersion = number;

export class DiscoveryRegistrationRegisterUnsafeServerLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationRegisterUnsafeServerVersion = DiscoveryRegistrationRegisterUnsafeServerRemoteVersion;

export type DiscoveryRegistrationRegisterUnsafeClientRemoteVersion = number;

export class DiscoveryRegistrationRegisterUnsafeClientLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationRegisterServerRemoteVersion = number;

export class DiscoveryRegistrationRegisterServerLocalVersion {
  public static value: 2;
}

export type DiscoveryRegistrationRegisterServerVersion = DiscoveryRegistrationRegisterServerRemoteVersion;

export type DiscoveryRegistrationRegisterClientRemoteVersion = number;

export class DiscoveryRegistrationRegisterClientLocalVersion {
  public static value: 2;
}

export type Meta = {
  [field: string]: string,
};

export enum HealthStatus {
  OK = "OK",
  Closed = "CLOSED",
  Denied = "DENIED",
  AlreadyExists = "ALREADY_EXISTS",
  InvalidSettings = "INVALID_SETTINGS",
  InvalidCapabilities = "INVALID_CAPABILITIES",
}

export type ServiceInterface = {
  origin: string,
  name: string,
  capabilities?: Capabilities,
};

export type TransportSettings = {
  name: string,
  params: string,
  meta: Meta,
};

export type ServiceInterfaceMap = {
  [interface_name: string]: ServiceInterface,
};

export type SupportedTransport = {
  name: string,
  meta?: Meta,
};

export type SearchResult = {
  found: boolean,
  version?: number,
  service_interface?: ServiceInterface,
  transport?: TransportSettings,
  meta?: Meta,
};

export type DiscoverySearchFindAllClientVersion = DiscoverySearchFindAllClientLocalVersion;

export type DiscoverySearchFindClientVersion = DiscoverySearchFindClientLocalVersion;

export type DiscoverInterfaceQuery = {
  service_interface: ServiceInterface,
  supported_transport?: SupportedTransport[],
  meta?: Meta,
};

export type HealthCheck = {
  status: HealthStatus,
  time: string,
  version?: number,
  message?: string,
  meta?: Meta,
};

export type DiscoveryRegistrationUnregisterUnsafeClientVersion = DiscoveryRegistrationUnregisterUnsafeClientLocalVersion;

export type Manifest = {
  interfaces: ServiceInterfaceMap,
  transport: TransportSettings,
  token: string,
  meta?: Meta,
};

export type DiscoveryRegistrationRegisterUnsafeClientVersion = DiscoveryRegistrationRegisterUnsafeClientLocalVersion;

export type DiscoveryRegistrationRegisterClientVersion = DiscoveryRegistrationRegisterClientLocalVersion;



export type DiscoverySearchFindRequest = {
  query: DiscoverInterfaceQuery,
};

export type DiscoverySearchFindAllRequest = {
};

export type DiscoveryRegistrationRegisterRequest = {
  manifest: Manifest,
};

export type DiscoveryRegistrationRegisterUnsafeRequest = {
  manifest: Manifest,
};

export type DiscoveryRegistrationUnregisterUnsafeRequest = {
  manifest: Manifest,
};
