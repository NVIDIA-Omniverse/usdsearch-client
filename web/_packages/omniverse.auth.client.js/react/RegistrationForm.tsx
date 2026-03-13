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



import React, { useRef } from "react";
import styled from "styled-components";
import { AuthenticationResult } from "./AuthForm";
import Button from "./Button";
import ButtonGroup from "./ButtonGroup";
import Form from "./Form";
import FormErrorList from "./FormErrorList";
import FormGroup from "./FormGroup";
import useCredentialRegistration from "./hooks/CredentialRegistration";
import useForm from "./hooks/Form";
import { useInput } from "./hooks/Input";
import Input from "./Input";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
import ServerName from "./ServerName";
import Spinner from "./Spinner";

interface RegistrationFormProps {
  server: string;
  className?: string;
  loading?: boolean;
  errors?: string[];
  extras?: Record<string, string>;
  nonce?: string;
  onSubmit?(fields: RegistrationFormFields): Promise<AuthenticationResult>;
  onStart?(fields: RegistrationFormFields): boolean;
  onSuccess?(result: AuthenticationResult): void;
  onFail?(errors: string[]): void;
  onCancel(): void;
}

export interface RegistrationFormFields {
  username: string;
  password: string;
  confirmPassword: string;
  server: string;
  firstName: string;
  lastName: string;
  email: string;
  nonce?: string;
  extras?: Record<string, string>;
}

const RegistrationForm: React.FC<RegistrationFormProps> = ({
  server,
  className,
  loading,
  errors,
  extras,
  nonce,
  onSubmit,
  onStart,
  onSuccess,
  onFail,
  onCancel,
}) => {
  const [username, setUsername] = useInput("");
  const [password, setPassword] = useInput("");
  const [confirmPassword, setConfirmPassword] = useInput("");
  const [firstName, setFirstName] = useInput("");
  const [lastName, setLastName] = useInput("");
  const [email, setEmail] = useInput("");

  const emailRef = useRef<HTMLInputElement>(null);

  const register = useCredentialRegistration();
  const form = useForm<RegistrationFormFields, AuthenticationResult>({
    fields: {
      username,
      password,
      confirmPassword,
      server,
      firstName,
      lastName,
      email,
      nonce,
      extras
    },
    onSubmit: async (fields) => {
      const errors: string[] = [];
      if (!emailRef.current?.checkValidity()) {
          errors.push("Email is not valid.");
      }

      if (!fields.password) {
        errors.push("Password is empty.");
      }

      if (fields.password !== fields.confirmPassword) {
        errors.push("Passwords don't match.");
      }

      if (errors.length > 0) {
          return { errors };
      }

      const submit = onSubmit || register;
      return submit(fields);
    },
    onStart,
    onSuccess,
    onFail,
  });

  return (
    <Form className={className}>
      <NvidiaLogo />
      <OmniverseLogo />

      <ServerName title={server}>{server}</ServerName>

      <FormGroup>
        <FormErrorList errors={errors} />
        <FormErrorList errors={form.errors} />
      </FormGroup>

      <FormGroup>
        <Input
          autoFocus
          name={"username"}
          value={username}
          disabled={loading || form.loading}
          onChange={setUsername}
          placeholder={"Username"}
        />
      </FormGroup>

      <FormGroup>
        <Input
          name={"password"}
          type={"password"}
          value={password}
          disabled={loading || form.loading}
          onChange={setPassword}
          placeholder={"Type Password"}
        />
      </FormGroup>

      <FormGroup>
        <Input
          name={"confirmPassword"}
          type={"password"}
          value={confirmPassword}
          disabled={loading || form.loading}
          onChange={setConfirmPassword}
          placeholder={"Confirm Password"}
        />
      </FormGroup>

      <FormGroup>
        <Input
          name={"firstName"}
          value={firstName}
          disabled={loading || form.loading}
          onChange={setFirstName}
          placeholder={"First Name"}
        />
      </FormGroup>

      <FormGroup>
        <Input
          name={"lastName"}
          value={lastName}
          disabled={loading || form.loading}
          onChange={setLastName}
          placeholder={"Last Name"}
        />
      </FormGroup>

      <FormGroup>
        <Input
          name={"email"}
          type={"email"}
          value={email}
          disabled={loading || form.loading}
          onChange={setEmail}
          placeholder={"Email"}
          ref={emailRef as any}
          required
        />
      </FormGroup>

      <RegistrationButtonGroup>
        <Button disabled={loading || form.loading} onClick={form.submit}>
          {(loading || form.loading) && <Spinner />} Create
        </Button>

        <Button disabled={loading || form.loading} onClick={onCancel}>
          Cancel
        </Button>
      </RegistrationButtonGroup>
    </Form>
  );
};

const RegistrationButtonGroup = styled(ButtonGroup)`
  flex-direction: row;
  justify-content: space-between;
`;

export default RegistrationForm;
