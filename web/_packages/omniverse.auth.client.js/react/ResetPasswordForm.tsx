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



import React from "react";
import ButtonGroup from "./ButtonGroup";
import Form from "./Form";
import FormErrorList from "./FormErrorList";
import FormGroup from "./FormGroup";
import useForm from "./hooks/Form";
import { useInput } from "./hooks/Input";
import Input from "./Input";
import LoginButton from "./LoginButton";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
import Spinner from "./Spinner";

export interface ResetPasswordFormProps {
  payload: string;
  onSubmit(newPassword: string, payload: string): Promise<void>;
}

interface ResetPasswordFormFields {
  newPassword: string;
  confirmNewPassword: string;
}

const ResetPasswordForm: React.FC<ResetPasswordFormProps> = ({ payload, onSubmit }) => {
  const [newPassword, setNewPassword] = useInput("");
  const [confirmNewPassword, setConfirmNewPassword] = useInput("");

  const form = useForm({
    fields: {
      newPassword,
      confirmNewPassword
    },
    onSubmit: submit
  });

  async function submit({ newPassword, confirmNewPassword }: ResetPasswordFormFields) {
    if (!newPassword) {
      throw new Error("You should specify a new password.");
    }

    if (newPassword !== confirmNewPassword) {
      throw new Error("Passwords don't match.");
    }

    return onSubmit(newPassword, payload);
  }

  return (
    <Form>
      <NvidiaLogo/>
      <OmniverseLogo/>

      <FormGroup>{form.errors && <FormErrorList errors={form.errors}/>}</FormGroup>

      <FormGroup>
        <Input
          autoFocus
          type={"password"}
          placeholder={"New Password"}
          name={"newPassword"}
          disabled={form.loading}
          value={newPassword}
          onChange={setNewPassword}
        />
      </FormGroup>

      <FormGroup>
        <Input
          type={"password"}
          placeholder={"Confirm New Password"}
          name={"confirmNewPassword"}
          disabled={form.loading}
          value={confirmNewPassword}
          onChange={setConfirmNewPassword}
        />
      </FormGroup>

      <ButtonGroup>
        <LoginButton name={"submit"} disabled={form.loading} onClick={form.submit}>
          {form.loading && <Spinner/>}
          Reset password
        </LoginButton>
      </ButtonGroup>
    </Form>
  );
};

export default ResetPasswordForm;
