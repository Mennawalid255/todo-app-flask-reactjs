import { useMutation, useQueryClient } from "@tanstack/react-query";

import {
  deleteUserAPI,
  updateUserPermissionsAPI,
  updateUserRoleAPI,
} from "../api/users";

const invalidateAdminData = (queryClient: ReturnType<typeof useQueryClient>) => {
  queryClient.invalidateQueries({ queryKey: ["admin-users"] });
  queryClient.invalidateQueries({ queryKey: ["admin-tasks"] });
};

export const useDeleteUserMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: deleteUserAPI,
    onSuccess: () => {
      invalidateAdminData(queryClient);
    },
  });
};

export const useUpdateUserRoleMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateUserRoleAPI,
    onSuccess: () => {
      invalidateAdminData(queryClient);
    },
  });
};

export const useUpdateUserPermissionsMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateUserPermissionsAPI,
    onSuccess: () => {
      invalidateAdminData(queryClient);
    },
  });
};
