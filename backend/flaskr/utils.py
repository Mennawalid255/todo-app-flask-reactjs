import bcrypt
from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort

PEPPER = "mysupersecretpepper123"

def generate_password(password):
    password_peppered = (password + PEPPER).encode()
    hashed = bcrypt.hashpw(password_peppered, bcrypt.gensalt())
    return hashed.decode("utf-8")  # store as string in DB


def check_password(stored_password, password):
    password_peppered = (password + PEPPER).encode()
    return bcrypt.checkpw(password_peppered, stored_password.encode("utf-8"))


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