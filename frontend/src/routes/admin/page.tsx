import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Button, buttonVariants } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  ALL_PERMISSIONS,
  canManage,
  hasPermission,
  isAdminRole,
  permissionLabel,
  roleLabel,
} from "@/lib/roles";
import { useDeleteTaskMutation } from "@/services/mutations/tasks";
import { useCreateTagMutation } from "@/services/mutations/tags";
import {
  useDeleteUserMutation,
  useUpdateUserPermissionsMutation,
} from "@/services/mutations/users";
import { useGetAdminTasksQuery } from "@/services/queries/admin-tasks";
import { useGetTagsQuery } from "@/services/queries/tags";
import { useGetUsersQuery } from "@/services/queries/users";
import { useAuthStore } from "@/stores/auth-store";
import { Permission, PermissionOverrides, Status, User } from "@/types/types";
import { Shield, Trash } from "lucide-react";
import { FormEvent, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { toast } from "sonner";
import axios from "axios";

const statusLabel = (status: Status) => {
  const labels: Record<Status, string> = {
    "TaskStatus.PENDING": "Pending",
    "TaskStatus.IN_PROGRESS": "In Progress",
    "TaskStatus.COMPLETED": "Completed",
  };
  return labels[status];
};

const createDraftMap = (users: User[]) =>
  users.reduce<Record<number, PermissionOverrides>>((accumulator, user) => {
    accumulator[user.id] = {
      grants: [...user.customPermissions.grants],
      revokes: [...user.customPermissions.revokes],
    };
    return accumulator;
  }, {});

export const AdminPage = () => {
  const { role, token, userId, permissions } = useAuthStore();
  const [tagName, setTagName] = useState("");
  const [permissionDrafts, setPermissionDrafts] = useState<Record<number, PermissionOverrides>>({});

  const usersQuery = useGetUsersQuery();
  const tasksQuery = useGetAdminTasksQuery();
  const tagsQuery = useGetTagsQuery();
  const deleteUserMutation = useDeleteUserMutation();
  const updateUserPermissionsMutation = useUpdateUserPermissionsMutation();
  const deleteTaskMutation = useDeleteTaskMutation();
  const createTagMutation = useCreateTagMutation();

  const canManageData = canManage(permissions);
  const canCreateTags = hasPermission(permissions, "create_tags");
  const canDeleteUsers = hasPermission(permissions, "delete_users");
  const canDeleteTasks = hasPermission(permissions, "delete_any_task");
  const canManagePermissionOverrides = hasPermission(permissions, "manage_permissions");
  const canManageRoles = hasPermission(permissions, "manage_roles");

  useEffect(() => {
    const users = usersQuery.data ?? [];
    setPermissionDrafts(createDraftMap(users));
  }, [usersQuery.data]);

  if (!isAdminRole(role)) {
    return <Navigate to="/dashboard" />;
  }

  const handleCreateTag = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const cleanName = tagName.trim();
    if (!cleanName) return;
    await createTagMutation.mutateAsync(cleanName);
    setTagName("");
    toast.success("Tag created");
  };

  const handleDeleteUser = async (targetUserId: number) => {
    await deleteUserMutation.mutateAsync(targetUserId);
    toast.success("User deleted");
  };

  const handleDeleteTask = async (taskId: number) => {
    await deleteTaskMutation.mutateAsync({ token, taskId });
    toast.success("Task deleted");
  };

  const handleUpdateRole = async (targetUserId: number, newRole: string) => {
    try {
      await axios.patch(
        `http://localhost:5000/api/v1/users/${targetUserId}/role`,
        { role: newRole },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      usersQuery.refetch();
      toast.success("Role updated successfully");
    } catch {
      toast.error("Failed to update role");
    }
  };

  const handlePermissionSave = async (targetUserId: number) => {
    const draft = permissionDrafts[targetUserId] ?? { grants: [], revokes: [] };
    await updateUserPermissionsMutation.mutateAsync({
      userId: targetUserId,
      grants: draft.grants,
      revokes: draft.revokes,
    });
    toast.success("Permission overrides updated");
  };

  const toggleDraftPermission = (
    targetUserId: number,
    mode: keyof PermissionOverrides,
    permission: Permission,
  ) => {
    setPermissionDrafts((current) => {
      const existing = current[targetUserId] ?? { grants: [], revokes: [] };
      const source = new Set(existing[mode]);
      const oppositeMode = mode === "grants" ? "revokes" : "grants";
      const opposite = new Set(existing[oppositeMode]);

      if (source.has(permission)) {
        source.delete(permission);
      } else {
        source.add(permission);
        opposite.delete(permission);
      }

      return {
        ...current,
        [targetUserId]: {
          grants: mode === "grants" ? [...source] : [...opposite],
          revokes: mode === "revokes" ? [...source] : [...opposite],
        },
      };
    });
  };

  return (
    <div className="grid gap-6">
      <section className="rounded-md border bg-background p-5">
        <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="flex items-center gap-2">
              <Shield className="size-5" />
              <h1 className="text-2xl font-bold">Admin Dashboard</h1>
            </div>
            <p className="mt-1 text-sm text-muted-foreground">
              Signed in as {role ? roleLabel(role) : "Admin"}
            </p>
            <p className="mt-2 text-xs text-muted-foreground">
              Active permissions: {(permissions ?? []).map(permissionLabel).join(", ")}
            </p>
          </div>
          <Button asChild variant="outline">
            <a href="/dashboard">User Dashboard</a>
          </Button>
        </div>
      </section>

      <section className="rounded-md border bg-background p-5">
        <div className="mb-4 flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-lg font-semibold">Tags</h2>
            <p className="text-sm text-muted-foreground">
              Manager admins can create tags for task categorization.
            </p>
          </div>
          <form className="flex gap-2" onSubmit={handleCreateTag}>
            <Input
              className="w-48"
              disabled={!canCreateTags || createTagMutation.isPending}
              onChange={(event) => setTagName(event.target.value)}
              placeholder="Tag name"
              value={tagName}
            />
            <Button disabled={!canCreateTags || createTagMutation.isPending}>
              Add Tag
            </Button>
          </form>
        </div>
        <div className="flex flex-wrap gap-2">
          {(tagsQuery.data ?? []).map((tag) => (
            <span
              className="rounded-md border bg-muted/40 px-3 py-2 text-sm font-medium"
              key={tag.id}
            >
              {tag.name}
            </span>
          ))}
        </div>
      </section>

      <section className="rounded-md border bg-background p-5">
        <div className="mb-4">
          <h2 className="text-lg font-semibold">Users</h2>
          <p className="text-sm text-muted-foreground">
            Viewer admins can inspect users. Manager admins can delete accounts, update roles, and manage permissions.
          </p>
        </div>
        <div className="grid gap-4">
          {(usersQuery.data ?? []).map((user) => {
            const draft = permissionDrafts[user.id] ?? {
              grants: user.customPermissions.grants,
              revokes: user.customPermissions.revokes,
            };
            const isSelf = user.id === userId;
            const isProtectedRole = user.role === "admin" || user.role === "admin_manager";

            return (
              <div className="grid gap-4 rounded-md border p-4" key={user.id}>

                {/* User info + role dropdown + delete */}
                <div className="grid gap-3 md:grid-cols-[1fr_1fr_140px_140px_auto] md:items-center">
                  <div>
                    <p className="font-medium">{user.username}</p>
                    <p className="text-xs text-muted-foreground">ID {user.id}</p>
                  </div>
                  <p className="text-sm">{user.email}</p>
                  <span className="rounded-md bg-muted px-3 py-2 text-center text-xs font-medium">
                    {roleLabel(user.role)}
                  </span>

                  {/* Role dropdown — always visible, disabled for viewer */}
                  <select
                    defaultValue={user.role}
                    onChange={(e) => handleUpdateRole(user.id, e.target.value)}
                    disabled={!canManageRoles || isSelf || isProtectedRole}
                    className="rounded-md border px-2 py-1 text-sm bg-background disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <option value="user">User</option>
                    <option value="admin_viewer">Viewer Admin</option>
                    <option value="admin_manager">Manager Admin</option>
                  </select>

                  {/* Delete button — always visible, disabled for viewer */}
                  <DeleteConfirm
                    description={`This will permanently delete ${user.username} and all tasks owned by this account.`}
                    onConfirm={() => handleDeleteUser(user.id)}
                    title="Delete user?"
                    disabled={!canDeleteUsers || isSelf || isProtectedRole}
                  />
                </div>

                {/* Current permissions badges */}
                <div className="flex flex-wrap gap-2">
                  {user.permissions.map((permission) => (
                    <span
                      className="rounded-md border bg-muted/50 px-3 py-1 text-xs font-medium"
                      key={`${user.id}-${permission}`}
                    >
                      {permissionLabel(permission)}
                    </span>
                  ))}
                </div>

                {/* Grant/Revoke permission overrides */}
                <div className="grid gap-3">
                  <div>
                    <p className="text-sm font-medium">Permission Overrides</p>
                    <p className="text-xs text-muted-foreground">
                      Grant or revoke individual permissions per user.
                    </p>
                  </div>
                  <div className="grid gap-2">
                    {ALL_PERMISSIONS.map((permission) => {
                      const isGranted = draft.grants.includes(permission);
                      const isRevoked = draft.revokes.includes(permission);

                      return (
                        <div
                          className="grid gap-2 rounded-md border p-2 md:grid-cols-[1fr_auto_auto]"
                          key={`${user.id}-${permission}-override`}
                        >
                          <span className="text-sm">{permissionLabel(permission)}</span>
                          <Button
                            disabled={!canManagePermissionOverrides || isSelf}
                            onClick={() => toggleDraftPermission(user.id, "grants", permission)}
                            size="sm"
                            type="button"
                            variant={isGranted ? "default" : "outline"}
                          >
                            {isGranted ? "Granted" : "Grant"}
                          </Button>
                          <Button
                            disabled={!canManagePermissionOverrides || isSelf}
                            onClick={() => toggleDraftPermission(user.id, "revokes", permission)}
                            size="sm"
                            type="button"
                            variant={isRevoked ? "destructive" : "outline"}
                          >
                            {isRevoked ? "Revoked" : "Revoke"}
                          </Button>
                        </div>
                      );
                    })}
                  </div>
                  <Button
                    disabled={!canManagePermissionOverrides || isSelf || updateUserPermissionsMutation.isPending}
                    onClick={() => handlePermissionSave(user.id)}
                    type="button"
                  >
                    Save Permission Overrides
                  </Button>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <section className="rounded-md border bg-background p-5">
        <div className="mb-4">
          <h2 className="text-lg font-semibold">Tasks</h2>
          <p className="text-sm text-muted-foreground">
            Viewer admins can inspect all tasks. Manager admins can delete any task.
          </p>
        </div>
        <div className="grid gap-3">
          {(tasksQuery.data ?? []).length === 0 ? (
            <div className="rounded-md border border-dashed p-6 text-center text-sm text-muted-foreground">
              No tasks found
            </div>
          ) : (
            (tasksQuery.data ?? []).map((task) => (
              <div
                className="grid gap-3 rounded-md border p-4 md:grid-cols-[1fr_1fr_120px_auto] md:items-center"
                key={task.id}
              >
                <div>
                  <p className="font-medium">{task.title}</p>
                  <p className="text-xs text-muted-foreground">{task.content}</p>
                </div>
                <div>
                  <p className="text-sm">{task.username}</p>
                  <p className="text-xs text-muted-foreground">{task.userEmail}</p>
                </div>
                <div className="flex flex-wrap gap-2">
                  <span className="rounded-md bg-muted px-3 py-2 text-xs font-medium">
                    {task.tagName}
                  </span>
                  <span className="rounded-md bg-muted px-3 py-2 text-xs font-medium">
                    {statusLabel(task.status)}
                  </span>
                </div>
                <DeleteConfirm
                  description={`This will permanently delete "${task.title}".`}
                  onConfirm={() => handleDeleteTask(task.id)}
                  title="Delete task?"
                  disabled={!canDeleteTasks}
                />
              </div>
            ))
          )}
        </div>
      </section>
    </div>
  );
};

type DeleteConfirmProps = {
  description: string;
  onConfirm: () => void;
  title: string;
  disabled?: boolean;
};

const DeleteConfirm = ({ description, onConfirm, title, disabled }: DeleteConfirmProps) => {
  return (
    <AlertDialog>
      <AlertDialogTrigger asChild>
        <Button size="sm" variant="destructive" disabled={disabled}>
          <Trash />
          Delete
        </Button>
      </AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>{title}</AlertDialogTitle>
          <AlertDialogDescription>{description}</AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel>Cancel</AlertDialogCancel>
          <AlertDialogAction
            className={buttonVariants({ variant: "destructive" })}
            onClick={onConfirm}
          >
            Delete
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
};