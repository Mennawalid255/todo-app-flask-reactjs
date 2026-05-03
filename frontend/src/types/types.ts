export type Tag = {
  id: number;
  name: string;
};

export type Role = "user" | "admin" | "admin_viewer" | "admin_manager";

<<<<<<< HEAD
export type Permission =
  | "manage_own_tasks"
  | "delete_own_account"
  | "view_users"
  | "view_all_tasks"
  | "delete_users"
  | "delete_any_task"
  | "create_tags"
  | "manage_roles"
  | "manage_permissions";

export type PermissionOverrides = {
  grants: Permission[];
  revokes: Permission[];
};

=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
export type User = {
  id: number;
  username: string;
  email: string;
  role: Role;
<<<<<<< HEAD
  permissions: Permission[];
  customPermissions: PermissionOverrides;
};

export type AuthSession = {
  token: string;
  role: Role;
  userId: number;
  username: string;
  permissions: Permission[];
  customPermissions: PermissionOverrides;
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
};

export type Status =
  | "TaskStatus.PENDING"
  | "TaskStatus.IN_PROGRESS"
  | "TaskStatus.COMPLETED";

export type Task = {
  id: number;
  title: string;
  content: string;
  status: Status;
  createdAt: Date;
  tagName: string;
};

export type AdminTask = Task & {
  userId: number;
  username: string;
  userEmail: string;
};
