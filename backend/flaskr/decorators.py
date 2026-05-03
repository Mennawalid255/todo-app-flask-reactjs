from functools import wraps
<<<<<<< HEAD

from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_smorest import abort


=======
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask_smorest import abort


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("role") != "admin":
            abort(403, message="Admins only")
        return fn(*args, **kwargs)
    return wrapper

>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
def role_required(*allowed_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
<<<<<<< HEAD
            if get_jwt().get("role") not in allowed_roles:
                abort(403, message="Permission denied")
=======
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role not in allowed_roles:
                abort(403, message="Permission denied")

>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
            return fn(*args, **kwargs)

        return decorator

<<<<<<< HEAD
    return wrapper
=======
    return wrapper
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
