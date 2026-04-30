from sqlalchemy import select

from flaskr import create_app
from flaskr.db import db
from flaskr.models.user_model import UserModel
from flaskr.utils import generate_password


ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"


def create_admin():
    app = create_app()

    with app.app_context():
        admin = db.session.execute(
            select(UserModel).where(UserModel.email == ADMIN_EMAIL)
        ).scalar_one_or_none()

        if admin:
            admin.role = "admin"
            admin.password = generate_password(ADMIN_PASSWORD)
            print("Existing admin account updated")
        else:
            admin = UserModel(
                username=ADMIN_USERNAME,
                email=ADMIN_EMAIL,
                password=generate_password(ADMIN_PASSWORD),
                role="admin",
            )
            db.session.add(admin)
            print("Admin account created")

        db.session.commit()
        print(f"Email: {ADMIN_EMAIL}")
        print(f"Password: {ADMIN_PASSWORD}")


if __name__ == "__main__":
    create_admin()
