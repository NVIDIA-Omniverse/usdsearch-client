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



import React, { useCallback } from "react";
import ButtonGroup from "./ButtonGroup";
import Form from "./Form";
import FormErrorList from "./FormErrorList";
import FormGroup from "./FormGroup";
import useCredentialServerCheck from "./hooks/CredentialServerCheck";
import useForm, { FormErrors } from "./hooks/Form";
import { useInput } from "./hooks/Input";
import Input from "./Input";
import LoginButton from "./LoginButton";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
import Spinner from "./Spinner";

export interface ServerFormProps {
  className?: string;
  loading?: boolean;
  errors?: string[];
  onStart?(fields: ServerFormFields): boolean;
  onSubmit?(fields: ServerFormFields): Promise<ServerFormFields>;
  onSuccess(result: ServerFormFields): void;
  onFail?(errors: string[]): void;
}

export interface ServerFormFields {
  server: string;
}

export type ServerFormResult = ServerFormFields & FormErrors;

const ServerForm: React.FC<ServerFormProps> = ({
  className,
  loading,
  errors,
  onStart,
  onSubmit,
  onSuccess,
  onFail,
}) => {
  const [server, setServer] = useInput("");

  const check = useCredentialServerCheck();
  const connect = useCallback(
    async ({ server }: ServerFormFields): Promise<ServerFormResult> => {
      const connection = await check(server);
      if (connection.ok) {
        return { server: connection.server };
      }
      return { server: connection.server, errors: connection.errors };
    },
    [check]
  );

  const form = useForm<ServerFormFields, ServerFormResult>({
    fields: {
      server,
    },
    onStart,
    onSubmit: onSubmit || connect,
    onSuccess,
    onFail,
  });

  return (
    <Form className={className}>
      <NvidiaLogo />
      <OmniverseLogo />

      <FormGroup>
        <FormErrorList errors={form.errors} />
        <FormErrorList errors={errors} />
      </FormGroup>

      <FormGroup>
        <Input autoFocus name={"server"} placeholder={"Type Server Name"} value={server} onChange={setServer} />
      </FormGroup>

      <ButtonGroup>
        <LoginButton disabled={loading || form.loading} onClick={form.submit}>
          {(loading || form.loading) && <Spinner />} Next
        </LoginButton>
      </ButtonGroup>
    </Form>
  );
};

export default ServerForm;
