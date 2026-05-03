from flask_jwt_extended import create_access_token
from flask_smorest import abort
from sqlalchemy import select
from werkzeug.exceptions import HTTPException

from flaskr.db import db
from flaskr.models.user_model import UserModel
from flaskr.utils import check_password


class AuthController:
    @staticmethod
    def sign_in(data):
        try:
            email = data.get("email", "").lower().strip()
            password = data.get("password", "")

            user_registered = db.session.execute(
                select(UserModel).where(UserModel.email == email)
            ).scalar_one_or_none()

            if not user_registered:
                abort(401, message="Incorrect credentials")

            if not check_password(user_registered.password, password):
                abort(401, message="Incorrect credentials")

            token = create_access_token(
                identity=str(user_registered.id),
                additional_claims={
                    "role": user_registered.role,
                    "permissions": user_registered.permissions,
                },
            )

            return {
                "token": token,
                "role": user_registered.role,
                "userId": user_registered.id,
                "username": user_registered.username,
                "permissions": user_registered.permissions,
                "customPermissions": user_registered.custom_permissions,
            }

        except HTTPException:
            raise
        except Exception as e:
            print("ERROR:", str(e))
            abort(500, message=str(e))

    @staticmethod
    def me(user_id):
        try:
            return db.session.execute(
                select(UserModel).where(UserModel.id == int(user_id))
            ).scalar_one()
        except HTTPException:
            raise
        except Exception as e:
            print("ERROR:", str(e))
            abort(500, message=str(e))
