from sqlalchemy import select

from flaskr import create_app
from flaskr.db import db
from flaskr.models.user_model import UserModel
from flaskr.utils import generate_password


ADMIN_ACCOUNTS = [
    {
        "username": "viewer_admin",
        "email": "viewer.admin@example.com",
<<<<<<< HEAD
        "password": "Viewer123!",
=======
        "password": "viewer123",
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
        "role": "admin_viewer",
    },
    {
        "username": "manager_admin",
        "email": "manager.admin@example.com",
<<<<<<< HEAD
        "password": "Manager123!",
=======
        "password": "manager123",
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
        "role": "admin_manager",
    },
    {
        "username": "admin",
        "email": "admin@example.com",
<<<<<<< HEAD
        "password": "Admin123!",
        "role": "admin",
=======
        "password": "admin123",
        "role": "admin_manager",
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    },
]


def upsert_admin(account):
    admin = db.session.execute(
        select(UserModel).where(UserModel.email == account["email"])
    ).scalar_one_or_none()

    if admin:
        admin.username = account["username"]
        admin.role = account["role"]
        admin.password = generate_password(account["password"])
<<<<<<< HEAD
        admin.set_permission_overrides()
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
        return "updated"

    admin = UserModel(
        username=account["username"],
        email=account["email"],
        password=generate_password(account["password"]),
        role=account["role"],
    )
<<<<<<< HEAD
    admin.set_permission_overrides()
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    db.session.add(admin)
    return "created"


def create_admins():
    app = create_app()

    with app.app_context():
        for account in ADMIN_ACCOUNTS:
            status = upsert_admin(account)
            print(f"{account['email']} {status} as {account['role']}")

        db.session.commit()
        print("\nAdmin accounts:")
        for account in ADMIN_ACCOUNTS:
            print(f"{account['email']} / {account['password']} / {account['role']}")


if __name__ == "__main__":
    create_admins()
