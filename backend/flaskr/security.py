import json
from functools import wraps
from typing import Iterable

from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort


ROLE_PERMISSIONS = {
    "user": {
        "manage_own_tasks",
        "delete_own_account",
    },
    "admin_viewer": {
        "manage_own_tasks",
        "delete_own_account",
        "view_users",
        "view_all_tasks",
    },
    "admin_manager": {
        "manage_own_tasks",
        "delete_own_account",
        "view_users",
        "view_all_tasks",
        "delete_users",
        "delete_any_task",
        "create_tags",
        "manage_roles",
        "manage_permissions",
    },
    "admin": {
        "manage_own_tasks",
        "delete_own_account",
        "view_users",
        "view_all_tasks",
        "delete_users",
        "delete_any_task",
        "create_tags",
        "manage_roles",
        "manage_permissions",
    },
}

ALL_PERMISSIONS = sorted(
    {permission for permissions in ROLE_PERMISSIONS.values() for permission in permissions}
)
VALID_ROLES = tuple(ROLE_PERMISSIONS.keys())


def normalize_permission_overrides(data):
    if not data:
        return {"grants": [], "revokes": []}

    grants = sorted(
        {permission for permission in data.get("grants", []) if permission in ALL_PERMISSIONS}
    )
    revokes = sorted(
        {permission for permission in data.get("revokes", []) if permission in ALL_PERMISSIONS}
    )
    return {"grants": grants, "revokes": revokes}


def parse_permission_overrides(raw_value):
    if not raw_value:
        return {"grants": [], "revokes": []}

    if isinstance(raw_value, dict):
        return normalize_permission_overrides(raw_value)

    try:
        return normalize_permission_overrides(json.loads(raw_value))
    except (TypeError, json.JSONDecodeError):
        return {"grants": [], "revokes": []}


def serialize_permission_overrides(data):
    return json.dumps(normalize_permission_overrides(data))


def permissions_for_role(role, overrides=None):
    permissions = set(ROLE_PERMISSIONS.get(role, set()))
    normalized = normalize_permission_overrides(overrides)
    permissions.update(normalized["grants"])
    permissions.difference_update(normalized["revokes"])
    return sorted(permissions)


def permission_required(*required_permissions):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            granted_permissions = set(claims.get("permissions", []))
            if not all(permission in granted_permissions for permission in required_permissions):
                abort(403, message="Permission denied")
            return fn(*args, **kwargs)

        return decorator

    return wrapper


def has_permission(claims: dict, permission: str) -> bool:
    return permission in set(claims.get("permissions", []))


def validate_role(role: str):
    if role not in VALID_ROLES:
        abort(400, message=f"Role must be one of: {', '.join(VALID_ROLES)}")


def validate_permissions(permissions: Iterable[str]):
    invalid = sorted({permission for permission in permissions if permission not in ALL_PERMISSIONS})
    if invalid:
        abort(400, message=f"Invalid permissions: {', '.join(invalid)}")
