import { z } from "zod";

const FormSchema = z.object({
  username: z
    .string()
    .min(1, { message: "Username is required" })
    .max(20, { message: "Max length is 20 characters" }),
  email: z
    .string()
    .min(1, { message: "Email is required" })
    .email({ message: "Not a valid email" }),
<<<<<<< HEAD
  password: z
    .string()
    .min(8, { message: "Password must be at least 8 characters" })
    .regex(/[A-Z]/, { message: "Password must contain an uppercase letter" })
    .regex(/[a-z]/, { message: "Password must contain a lowercase letter" })
    .regex(/\d/, { message: "Password must contain a number" })
    .regex(/[^A-Za-z0-9]/, {
      message: "Password must contain a special character",
    }),
=======
  password: z.string().min(1, { message: "Password is required" }),
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
});

export const SignInFormSchema = FormSchema.omit({ username: true });

export const CreateAccountFormSchema = FormSchema;

export type TSignInFormSchema = z.infer<typeof SignInFormSchema>;

export type TCreateAccountFormSchema = z.infer<typeof CreateAccountFormSchema>;
