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



import React, { useMemo } from "react";
import styled from "styled-components";
import ButtonGroup from "./ButtonGroup";
import Form from "./Form";
import FormErrorList from "./FormErrorList";
import FormGroup from "./FormGroup";
import useCredentialSettings from "./hooks/CredentialSettings";
import useForm from "./hooks/Form";
import { useInput } from "./hooks/Input";
import useSSORedirect from "./hooks/SSORedirect";
import useSSOSettings from "./hooks/SSOSettings";
import { default as OmniverseInput } from "./Input";
import LoginButton from "./LoginButton";
import NvidiaLogo from "./NvidiaLogo";
import OmniverseLogo from "./OmniverseLogo";
import Spinner from "./Spinner";
import SSOButtonGroup from "./SSOButtonGroup";
import SSOSplitter from "./SSOSplitter";
import Headline from "./Headline";

export interface InvitationFormProps {
  username: string;
  server: string;
  ssoRedirectBackTo?: string;
  onSubmit(newPassword: string): Promise<void>;
}

interface InvitationFormFields {
  newPassword: string;
  confirmNewPassword: string;
}

const InvitationForm: React.FC<InvitationFormProps> = ({
  username,
  server,
  ssoRedirectBackTo = window.location.origin + "/sso",
  onSubmit,
}) => {
  const [newPassword, setNewPassword] = useInput("");
  const [confirmNewPassword, setConfirmNewPassword] = useInput("");

  const credentialSettings = useCredentialSettings(server);
  const ssoSettings = useSSOSettings(server);
  const redirect = useSSORedirect(server, ssoRedirectBackTo);

  const ssoAvailable = useMemo(
    () => Boolean(username.includes("@") && ssoSettings?.settings && ssoSettings.settings.length > 0),
    [username, ssoSettings]
  );
  const credentialsAvailable = useMemo(
    () => Boolean(!username.includes("@") && credentialSettings?.settings?.is_ui_visible),
    [username, credentialSettings]
  );

  const form = useForm({
    fields: {
      newPassword,
      confirmNewPassword,
    },
    onSubmit: submit,
  });

  async function submit({ newPassword, confirmNewPassword }: InvitationFormFields) {
    if (!newPassword) {
      throw new Error("You should specify a new password.");
    }

    if (newPassword !== confirmNewPassword) {
      throw new Error("Passwords don't match.");
    }

    return onSubmit(newPassword);
  }

  if (!credentialSettings || !ssoSettings) {
    return (
      <Form>
        <NvidiaLogo />
        <OmniverseLogo />
      </Form>
    );
  }

  return (
    <Form>
      <NvidiaLogo />
      <OmniverseLogo />

      {form.errors && (
        <FormGroup>
          <FormErrorList errors={form.errors} />
        </FormGroup>
      )}

      <Headline>
        Welcome to Omniverse! <br />
        Your username is: <br />"{username}" <br /> on <br /> <b>{server}</b>
      </Headline>

      <Caption credentialsAvailable={credentialsAvailable} ssoAvailable={ssoAvailable} />

      {credentialsAvailable && (
        <>
          <FormGroup>
            <OmniverseInput
              autoFocus
              type={"password"}
              placeholder={"Type Password"}
              name={"newPassword"}
              disabled={form.loading}
              value={newPassword}
              onChange={setNewPassword}
            />
          </FormGroup>

          <FormGroup>
            <OmniverseInput
              type={"password"}
              placeholder={"Confirm Password"}
              name={"confirmNewPassword"}
              disabled={form.loading}
              value={confirmNewPassword}
              onChange={setConfirmNewPassword}
            />
          </FormGroup>

          <ButtonGroup>
            <LoginButton name={"submit"} disabled={form.loading} onClick={form.submit}>
              {form.loading && <Spinner />}
              Log in
            </LoginButton>
          </ButtonGroup>
        </>
      )}

      {credentialsAvailable && ssoAvailable && <SSOSplitter>or</SSOSplitter>}
      {ssoAvailable && ssoSettings.settings && <SSOButtonGroup ssoSettings={ssoSettings.settings} onClick={redirect} />}
    </Form>
  );
};

const Caption: React.FC<{
  credentialsAvailable: boolean;
  ssoAvailable: boolean;
}> = ({ credentialsAvailable, ssoAvailable }) => {
  if (credentialsAvailable && ssoAvailable) {
    return <StyledCaption>Please continue by providing a new password or logging in with SSO.</StyledCaption>;
  }
  if (credentialsAvailable) {
    return <StyledCaption>Please continue by providing a new password.</StyledCaption>;
  }
  if (ssoAvailable) {
    return <StyledCaption>Please continue by logging in with SSO.</StyledCaption>;
  }
  return null;
};

const StyledCaption = styled.div`
  font-weight: 400;
  font-size: 11pt;
  position: relative;
  text-align: center;
  padding: 1em 0.5em;
  margin: 0 1em;
  border-top: 1px solid #bbbbbb;
  z-index: 1;
`;

export default InvitationForm;
