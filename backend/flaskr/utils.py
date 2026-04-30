from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort
from werkzeug.security import generate_password_hash, check_password_hash


def generate_password(password):
    return generate_password_hash(password, salt_length=10)


def check_password(password_hash, password):
    return check_password_hash(password_hash, password)


def role_required(*allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role not in allowed_roles:
                abort(403, message="Permission denied")

            return fn(*args, **kwargs)

        return decorator

    return wrapper
