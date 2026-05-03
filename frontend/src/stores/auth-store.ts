<<<<<<< HEAD
import { Permission, PermissionOverrides, Role } from "@/types/types";
=======
import { Role } from "@/types/types";
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
import { create } from "zustand";
import { persist } from "zustand/middleware";

type State = {
  token: string | null;
  role: Role | null;
  userId: number | null;
  username: string | null;
<<<<<<< HEAD
  permissions: Permission[];
  customPermissions: PermissionOverrides | null;
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
  isLoggedIn: boolean;
};

type Action = {
<<<<<<< HEAD
  signIn: (
    token: string,
    role: Role,
    userId: number,
    username: string,
    permissions: Permission[],
    customPermissions: PermissionOverrides,
  ) => void;
  logout: () => void;
};

const emptyPermissionOverrides: PermissionOverrides = { grants: [], revokes: [] };

=======
  signIn: (token: string, role: Role, userId: number, username: string) => void;
  logout: () => void;
};

>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
export const useAuthStore = create<State & Action>()(
  persist(
    (set) => ({
      token: null,
      role: null,
      userId: null,
      username: null,
<<<<<<< HEAD
      permissions: [],
      customPermissions: null,
      isLoggedIn: false,
      signIn: (
        token: string,
        role: Role,
        userId: number,
        username: string,
        permissions: Permission[],
        customPermissions: PermissionOverrides,
      ) => {
        set({
          token,
          role,
          userId,
          username,
          permissions,
          customPermissions,
          isLoggedIn: true,
        });
      },
      logout: () => {
        set({
          token: null,
          role: null,
          userId: null,
          username: null,
          permissions: [],
          customPermissions: emptyPermissionOverrides,
          isLoggedIn: false,
        });
=======
      isLoggedIn: false,
      signIn: (token: string, role: Role, userId: number, username: string) => {
        set({ token, role, userId, username, isLoggedIn: true });
      },
      logout: () => {
        set({ token: null, role: null, userId: null, username: null, isLoggedIn: false });
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
      },
    }),
    { name: "session" },
  ),
);
