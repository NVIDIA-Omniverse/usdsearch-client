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



import { AuthStatus } from "@omniverse/auth/data";
import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";
import DeviceCodeStatus from "./DeviceCodeStatus";
import Form from "./Form";
import FormError from "./FormError";
import FormSpinner from "./FormSpinner";
import { useDeviceFlowSubmit } from "./hooks/DeviceFlow";
import useNucleusSession from "./hooks/NucleusSession";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";

export interface DeviceCodeSubmitProps {
  code: string;
}

const DeviceCodeSubmit: React.FC<DeviceCodeSubmitProps> = ({ code }) => {
  const [loading, setLoading] = useState(true);
  const [status, setStatus] = useState<AuthStatus | null>(null);
  const [error, setError] = useState("");

  const session = useNucleusSession();

  const submitUserCode = useDeviceFlowSubmit();
  useEffect(() => {
    submitUserCode({ code })
      .then((result) => setStatus(result.status))
      .catch((error) => setError(error.message || error.toString()))
      .finally(() => setLoading(false));
  }, [code, submitUserCode]);

  if (!session.established) {
    return <Redirect to={"/"} />;
  }

  return (
    <Form>
      <NvidiaLogo />
      <OmniverseLogo />
      <DeviceCodeSubmitBody loading={loading} status={status} error={error} />
    </Form>
  );
};

interface DeviceCodeSubmitState {
  loading: boolean;
  status: AuthStatus | null;
  error: string;
}

const DeviceCodeSubmitBody: React.FC<DeviceCodeSubmitState> = ({ loading, status, error }) => {
  if (loading) {
    return <FormSpinner />;
  }
  if (error) {
    return <FormError>{error}</FormError>;
  }
  return <DeviceCodeStatus status={status!} />;
};

export default DeviceCodeSubmit;
