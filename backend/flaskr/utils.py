import hashlib
import os
from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort


def generate_password(password):
    
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    
    return f"{salt}:{hashed}"


def check_password(stored_password, password):
    salt, stored_hash = stored_password.split(":")
    login_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return login_hash == stored_hash


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