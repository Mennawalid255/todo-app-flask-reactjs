import { Permission, PermissionOverrides, Role } from "@/types/types";
import { create } from "zustand";
import { persist } from "zustand/middleware";

type State = {
  token: string | null;
  role: Role | null;
  userId: number | null;
  username: string | null;
  permissions: Permission[];
  customPermissions: PermissionOverrides | null;
  isLoggedIn: boolean;
};

type Action = {
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

export const useAuthStore = create<State & Action>()(
  persist(
    (set) => ({
      token: null,
      role: null,
      userId: null,
      username: null,
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
      },
    }),
    { name: "session" },
  ),
);
