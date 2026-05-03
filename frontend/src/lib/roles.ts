<<<<<<< HEAD
import { Permission, Role } from "@/types/types";

export const ALL_PERMISSIONS: Permission[] = [
  "manage_own_tasks",
  "delete_own_account",
  "view_users",
  "view_all_tasks",
  "delete_users",
  "delete_any_task",
  "create_tags",
  "manage_roles",
  "manage_permissions",
];
=======
import { Role } from "@/types/types";
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

export const isAdminRole = (role: Role | null) =>
  role === "admin" || role === "admin_viewer" || role === "admin_manager";

<<<<<<< HEAD
export const hasPermission = (
  permissions: Permission[] | null | undefined,
  permission: Permission,
) => (permissions ?? []).includes(permission);

export const canManage = (permissions: Permission[] | null | undefined) =>
  hasPermission(permissions, "delete_users") ||
  hasPermission(permissions, "delete_any_task") ||
  hasPermission(permissions, "create_tags");
=======
export const canManage = (role: Role | null) =>
  role === "admin" || role === "admin_manager";
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

export const roleLabel = (role: Role) => {
  const labels: Record<Role, string> = {
    user: "User",
<<<<<<< HEAD
    admin: "System Admin",
=======
    admin: "Manager Admin",
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    admin_viewer: "Viewer Admin",
    admin_manager: "Manager Admin",
  };

  return labels[role];
};
<<<<<<< HEAD

export const permissionLabel = (permission: Permission) => {
  const labels: Record<Permission, string> = {
    manage_own_tasks: "Manage Own Tasks",
    delete_own_account: "Delete Own Account",
    view_users: "View Users",
    view_all_tasks: "View All Tasks",
    delete_users: "Delete Users",
    delete_any_task: "Delete Any Task",
    create_tags: "Create Tags",
    manage_roles: "Manage Roles",
    manage_permissions: "Manage Permissions",
  };

  return labels[permission];
};
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
