import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createTaskAPI, deleteTaskAPI, updateTaskAPI } from "../api/tasks";

export const useCreateTaskMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createTaskAPI,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
    },
  });
};

export const useUpdateTaskMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: updateTaskAPI,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
    },
  });
};

export const useDeleteTaskMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: deleteTaskAPI,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["tasks"] });
<<<<<<< HEAD
      queryClient.invalidateQueries({ queryKey: ["admin-tasks"] });
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    },
  });
};
