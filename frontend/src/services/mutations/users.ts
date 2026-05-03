import { useMutation, useQueryClient } from "@tanstack/react-query";
<<<<<<< HEAD

import {
  deleteUserAPI,
  updateUserPermissionsAPI,
  updateUserRoleAPI,
} from "../api/users";

const invalidateAdminData = (queryClient: ReturnType<typeof useQueryClient>) => {
  queryClient.invalidateQueries({ queryKey: ["admin-users"] });
  queryClient.invalidateQueries({ queryKey: ["admin-tasks"] });
};
=======
import { deleteUserAPI } from "../api/users";
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

export const useDeleteUserMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: deleteUserAPI,
    onSuccess: () => {
<<<<<<< HEAD
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
=======
      queryClient.invalidateQueries({ queryKey: ["admin-users"] });
      queryClient.invalidateQueries({ queryKey: ["admin-tasks"] });
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    },
  });
};
