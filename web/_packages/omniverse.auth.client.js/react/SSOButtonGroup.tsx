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



import { SSOSettings } from "@omniverse/auth/data";
import React from "react";
import styled from "styled-components";
import SSOButton from "./SSOButton";

export interface SSOButtonsProps {
  loading?: boolean;
  ssoSettings: SSOSettings[];
  onClick(sso: SSOSettings): void;
}

const SSOButtonGroup: React.FC<SSOButtonsProps> = ({ loading = false, ssoSettings, onClick }) => {
  return ssoSettings && ssoSettings.length > 0 ? (
    <SSOSettingList>
      {ssoSettings.map((setting) => (
        <SSOButton key={setting.type} setting={setting} loading={loading} onClick={onClick} />
      ))}
    </SSOSettingList>
  ) : null;
};

const SSOSettingList = styled.div`
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  margin: 5px 15px;
`;

export default SSOButtonGroup;
