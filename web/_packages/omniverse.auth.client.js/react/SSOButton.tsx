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
import React, { useCallback } from "react";
import styled from "styled-components";
import Button from "./Button";
import Spinner from "./Spinner";

export interface SSOButtonProps {
  loading?: boolean;
  setting: SSOSettings;
  onClick(setting: SSOSettings): void;
}

const SSOButton: React.FC<SSOButtonProps> = ({ loading = false, setting, onClick }) => {
  const redirect = useCallback(() => {
    onClick(setting);
  }, [setting, onClick]);

  return (
    <StyledSSOButton disabled={loading} onClick={redirect}>
      {loading ? <Spinner /> : setting.image && <StyledPicture src={setting.image} />}
      Log in with {setting.public_name}
    </StyledSSOButton>
  );
};

export const StyledSSOButton = styled(Button)`
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  background: #666;
  color: white;
  padding: 0 10px;
  border-color: #909090;
  margin: 0.25rem 0;
  box-sizing: border-box;

  & > svg.fa-spinner {
    margin-right: 10px;
  }
`;

const StyledPicture = styled.img`
  max-width: 100%;
  max-height: 100%;
  margin-right: 10px;
  cursor: pointer;
  width: 20px;
  height: 20px;
`;

export default SSOButton;
