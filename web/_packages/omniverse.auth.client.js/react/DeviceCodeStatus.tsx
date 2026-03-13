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



import { faCheck } from "@fortawesome/free-solid-svg-icons/faCheck";
import { faExclamationCircle } from "@fortawesome/free-solid-svg-icons/faExclamationCircle";
import { AuthStatus } from "@omniverse/auth/data";
import React from "react";
import styled from "styled-components";
import useRedirectURL from "./hooks/LoginRedirect";
import Icon from "./Icon";
import NavLink from "./NavLink";

export interface DeviceCodeStatusProps {
  status: AuthStatus;
}

const DeviceCodeStatus: React.FC<DeviceCodeStatusProps> = ({ status }) => {
  const loginRedirect = useRedirectURL();
  if (status === AuthStatus.OK) {
    return (
      <StyledDeviceCodeStatus>
        <DeviceCodeStatusIcon icon={faCheck} type={"success"} />
        <DeviceCodeStatusText>
          You have successfully logged in. <br />
          You can continue to work in your application.
        </DeviceCodeStatusText>
      </StyledDeviceCodeStatus>
    );
  } else if (status === AuthStatus.Expired || status === AuthStatus.InvalidToken) {
    return (
      <StyledDeviceCodeStatus>
        <DeviceCodeStatusIcon icon={faExclamationCircle} type={"error"} />
        <DeviceCodeStatusText>
          Your session has expired. <br />
          Please <NavLink to={loginRedirect}>log in</NavLink> again.
        </DeviceCodeStatusText>
      </StyledDeviceCodeStatus>
    );
  } else if (status === AuthStatus.NotFound) {
    return (
      <StyledDeviceCodeStatus>
        <DeviceCodeStatusIcon icon={faExclamationCircle} type={"error"} />
        <DeviceCodeStatusText>
          This user code is not found or expired. <br />
          Please try to authenticate in the application again.
        </DeviceCodeStatusText>
      </StyledDeviceCodeStatus>
    );
  } else if (status === AuthStatus.Disabled) {
    return (
      <StyledDeviceCodeStatus>
        <DeviceCodeStatusIcon icon={faExclamationCircle} type={"error"} />
        <DeviceCodeStatusText>Your account has been disabled.</DeviceCodeStatusText>
      </StyledDeviceCodeStatus>
    );
  } else {
    return (
      <StyledDeviceCodeStatus>
        <DeviceCodeStatusIcon icon={faExclamationCircle} type={"error"} />
        <DeviceCodeStatusText>Unknown error, please try again later ({status}).</DeviceCodeStatusText>
      </StyledDeviceCodeStatus>
    );
  }
};

const StyledDeviceCodeStatus = styled.div`
  display: flex;
  gap: 0.5em;
  padding: 0 15px;
`;

const DeviceCodeStatusIcon = styled(Icon)<{ type: "success" | "error" }>`
  font-size: 18pt;
  margin-top: 5px;
  color: ${({ type }) => (type === "success" ? "#76b900" : "#d46a6a")};
`;

const DeviceCodeStatusText = styled.div`
  font-size: 10pt;
`;

export default DeviceCodeStatus;
