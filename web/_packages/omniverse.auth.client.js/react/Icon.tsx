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



import { FontAwesomeIcon, FontAwesomeIconProps } from "@fortawesome/react-fontawesome";
import React from "react";
import styled from "styled-components";

export interface IconProps extends FontAwesomeIconProps {
  clickable?: boolean;
  disabled?: boolean;
}

export type PredefinedIconProps = Omit<IconProps, "icon">;

/**
 * Icons from Font Awesome.
 * https://fontawesome.com/icons?d=gallery
 */
const Icon: React.FC<IconProps> = React.forwardRef<HTMLElement, IconProps>(
  ({ clickable: $clickable = false, disabled: $disabled = false, ...props }, ref) => {
    return (
      <StyledIcon
        forwardedRef={ref as any}
        clickable={$clickable}
        disabled={$disabled}
        aria-hidden={$clickable ? "false" : "true"}
        fixedWidth={true}
        {...props}
      />
    );
  }
);
Icon.displayName = "Icon";

export const StyledIcon = styled(({ clickable, disabled, ...props }: IconProps) => <FontAwesomeIcon {...props} />)`
  display: inline-block;
  cursor: ${({ clickable, disabled }) => (clickable && !disabled ? "pointer" : "unset")};
  pointer-events: ${({ disabled }) => (disabled ? "none" : "all")};
  user-select: none;
`;

export default Icon;
