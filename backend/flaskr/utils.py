import re

from flask_smorest import abort
from werkzeug.security import check_password_hash, generate_password_hash


PASSWORD_POLICY_MESSAGE = (
    "Password must be at least 8 characters and include uppercase, lowercase, "
    "a number, and a special character."
)


def validate_password_strength(password: str):
    if len(password) < 8:
        abort(400, message=PASSWORD_POLICY_MESSAGE)

    checks = [
        re.search(r"[A-Z]", password),
        re.search(r"[a-z]", password),
        re.search(r"\d", password),
        re.search(r"[^A-Za-z0-9]", password),
    ]

    if not all(checks):
        abort(400, message=PASSWORD_POLICY_MESSAGE)


def generate_password(password):
    validate_password_strength(password)
    return generate_password_hash(password, method="scrypt")


def check_password(stored_password, password):
    return check_password_hash(stored_password, password)
