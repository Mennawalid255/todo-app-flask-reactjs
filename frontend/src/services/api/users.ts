<<<<<<< HEAD
import { Permission, User } from "@/types/types";
import { useAuthStore } from "@/stores/auth-store";
import axios from "axios";

const authHeaders = () => {
  const token = useAuthStore.getState().token;

  return {
    Authorization: `Bearer ${token}`,
  };
};

export const getUsersAPI = async () => {
  const response = await axios.get<User[]>("http://localhost:5000/api/v1/users", {
    headers: authHeaders(),
=======
import { useAuthStore } from "@/stores/auth-store";
import { User } from "@/types/types";
import axios from "axios";

export const getUsersAPI = async () => {
  const token = useAuthStore.getState().token;

  const response = await axios.get<User[]>("http://localhost:5000/api/v1/users", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
  });

  return response.data;
};

export const deleteUserAPI = async (userId: number) => {
<<<<<<< HEAD
  await axios.delete(`http://localhost:5000/api/v1/users/${userId}`, {
    headers: authHeaders(),
  });
};

export const updateUserRoleAPI = async (data: {
  userId: number;
  role: User["role"];
}) => {
  const response = await axios.patch<User>(
    `http://localhost:5000/api/v1/users/${data.userId}/role`,
    { role: data.role },
    {
      headers: authHeaders(),
    },
  );

  return response.data;
};

export const updateUserPermissionsAPI = async (data: {
  userId: number;
  grants: Permission[];
  revokes: Permission[];
}) => {
  const response = await axios.patch<User>(
    `http://localhost:5000/api/v1/users/${data.userId}/permissions`,
    { grants: data.grants, revokes: data.revokes },
    {
      headers: authHeaders(),
    },
  );

  return response.data;
};
=======
  const token = useAuthStore.getState().token;

  await axios.delete(`http://localhost:5000/api/v1/users/${userId}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
