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



import { useCallback, useMemo, useRef, useState } from "react";
import useMounted from "./Mounted";

export interface FormSettings<F, T> {
  fields: F;
  onStart?: FormStartCallback<F>;
  onFail?: FormFailCallback;
  onSuccess?: FormSuccessCallback<T>;
  onSubmit: FormSubmitCallback<F, T>;
  onCancel?: FormCancelCallback;
}

export type FormStartCallback<F> = (fields: F) => boolean;
export type FormFailCallback = (errors: string[]) => void;
export type FormSuccessCallback<T> = (result: T) => void;
export type FormSubmitCallback<F, T> = (fields: F) => Promise<T | FormErrors>;
export type FormCancelCallback = () => void;
export type FormErrors = {
  errors?: string[];
};

export default function useForm<F, T>({
  fields: formFields,
  onStart,
  onSuccess,
  onFail,
  onSubmit,
  onCancel,
}: FormSettings<F, T>) {
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState<string[]>([]);
  const [result, setResult] = useState<T | null>(null);

  const fields = useRef<F>(formFields);
  fields.current = formFields;

  const mounted = useMounted();

  const callbacks = useRef({
    onStart,
    onSuccess,
    onFail,
    onSubmit,
    onCancel,
  });
  callbacks.current = { onStart, onSuccess, onFail, onSubmit, onCancel };

  const submit = useCallback(async () => {
    const { onStart, onSuccess, onFail, onSubmit } = callbacks.current;

    setLoading(true);
    setErrors([]);
    setResult(null);

    try {
      if (onStart) {
        const proceed = onStart(fields.current);
        if (!proceed) {
          return;
        }
      }

      const result = await onSubmit(fields.current);
      const errors = (result as FormErrors)?.errors;

      if (!mounted.current) {
        return;
      }

      setLoading(false);
      if (errors?.length) {
        setErrors(errors);
        if (onFail) {
          onFail(errors);
        }
      } else {
        setResult(result as T);
        if (onSuccess) {
          onSuccess(result as T);
        }
      }
    } catch (e) {
      if (mounted.current) {
        setLoading(false);
        setErrors([e instanceof Error ? e.message : (e as Object).toString()]);
      }

      if (process.env.NODE_ENV !== "test") {
        console.error(e);
      }
    }
  }, [mounted]);

  const cancel = useCallback(() => {
    const { onCancel } = callbacks.current;
    setLoading(false);
    if (onCancel) {
      onCancel();
    }
  }, []);

  return useMemo(
    () => ({
      fields: fields.current,
      result,
      submit,
      cancel,
      loading,
      setLoading,
      errors,
      setErrors,
    }),
    [loading, result, errors, submit, cancel]
  );
}
