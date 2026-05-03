from functools import wraps

from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort


def role_required(*allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if get_jwt().get("role") not in allowed_roles:
                abort(403, message="Permission denied")
            return fn(*args, **kwargs)

        return decorator

    return wrapper
