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



import { faUser } from "@fortawesome/free-solid-svg-icons/faUser";
import jwtDecode, { JwtPayload } from "jwt-decode";
import React from "react";
import styled from "styled-components";
import useRedirectURL from "./hooks/LoginRedirect";
import useNucleusSession from "./hooks/NucleusSession";
import Icon from "./Icon";
import NavLink from "./NavLink";

const Header: React.FC = () => {
  const session = useNucleusSession();
  const logout = useRedirectURL({ redirect: "/logout" });

  if (!session.established) {
    return null;
  }

  return (
    <StyledHeader>
      <Username refreshToken={session.refreshToken} />
      <NavLink to={logout}>Log out</NavLink>
    </StyledHeader>
  );
};

const Username: React.FC<{ refreshToken: string }> = React.memo(({ refreshToken }) => {
  const payload = jwtDecode<JwtPayload>(refreshToken);
  const username = payload.sub;
  return (
    <StyledUsername>
      <Icon icon={faUser} />
      {username}
    </StyledUsername>
  );
});

const StyledHeader = styled.header`
  display: flex;
  padding: 1em;
  gap: 2rem;
`;

const StyledUsername = styled.div`
  display: inline-flex;
  align-items: center;
  gap: 0.25em;
  font-size: 9pt;
  margin-left: auto;
  color: #2d2d2d;
`;

export default Header;
