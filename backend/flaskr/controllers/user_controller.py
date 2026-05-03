<<<<<<< HEAD
from flask_jwt_extended import get_jwt, get_jwt_identity
from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from werkzeug.exceptions import HTTPException

from flaskr.db import db
from flaskr.models.user_model import UserModel
from flaskr.security import has_permission, validate_permissions, validate_role
from flaskr.utils import generate_password
=======
from flask_jwt_extended import get_jwt_identity
from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from flaskr.db import db
from flaskr.models.user_model import UserModel
from flaskr.utils import generate_password
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import HTTPException
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f


class UserController:
    @staticmethod
    def get_all():
        try:
            return db.session.execute(select(UserModel)).scalars().all()
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching users")

    @staticmethod
    def get_by_id(user_id):
        try:
<<<<<<< HEAD
            current_user_id = int(get_jwt_identity())
            claims = get_jwt()

            if current_user_id != int(user_id) and not has_permission(claims, "view_users"):
                abort(403, message="Permission denied")

            return db.session.execute(
                select(UserModel).where(UserModel.id == int(user_id))
            ).scalar_one()
        except ValueError:
            abort(400, message="Invalid user id")
        except NoResultFound:
            abort(404, message="User not found")
        except HTTPException:
            raise
=======
            return db.session.execute(
                select(UserModel).where(UserModel.id == user_id)
            ).scalar_one()
        except NoResultFound:
            abort(404, message="User not found")
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching user")

    @staticmethod
    def create(data):
        try:
<<<<<<< HEAD
            data["email"] = data["email"].lower().strip()
            data["username"] = data["username"].strip()

=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
            user_registered = db.session.execute(
                select(UserModel).where(
                    (UserModel.username == data["username"])
                    | (UserModel.email == data["email"])
                )
            ).scalar_one_or_none()

            if user_registered:
                if user_registered.username == data["username"]:
                    abort(409, message="Username already registered")
                if user_registered.email == data["email"]:
                    abort(409, message="Email already registered")

            new_user = UserModel(**data)
<<<<<<< HEAD
            new_user.password = generate_password(data["password"])
            new_user.set_permission_overrides()
=======

            new_user.password = generate_password(data["password"])
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

            db.session.add(new_user)
            db.session.commit()
        except HTTPException:
<<<<<<< HEAD
            raise
        except Exception as e:
            print("ERROR:", e)
=======
            raise                 
        except Exception as e:
            print("ERROR:", e)       
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
            db.session.rollback()
            abort(500, message=str(e))

    @staticmethod
    def delete_by_id(user_id):
        try:
            current_user_id = int(get_jwt_identity())
            target_user_id = int(user_id)

            if current_user_id == target_user_id:
                abort(400, message="Admins should use account deletion for their own account")

            user = db.session.execute(
                select(UserModel).where(UserModel.id == target_user_id)
            ).scalar_one()

            if user.role in ["admin", "admin_manager"]:
                abort(400, message="Manager admin accounts cannot be deleted here")

            db.session.delete(user)
            db.session.commit()
        except ValueError:
            abort(400, message="Invalid user id")
        except NoResultFound:
            abort(404, message="User not found")
        except SQLAlchemyError:
            db.session.rollback()
<<<<<<< HEAD
            abort(500, message="Internal server error while deleting user")

    @staticmethod
    def delete():
        try:
            current_user_id = int(get_jwt_identity())
            user = db.session.execute(
                select(UserModel).where(UserModel.id == current_user_id)
            ).scalar_one()

            db.session.delete(user)
            db.session.commit()
        except NoResultFound:
            abort(404, message="User not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while deleting account")

    @staticmethod
    def update_role(user_id, data):
        try:
            current_user_id = int(get_jwt_identity())
            claims = get_jwt()
            target_user_id = int(user_id)
            new_role = data["role"]

            if current_user_id == target_user_id:
                abort(400, message="You cannot change your own role")

            validate_role(new_role)

            user = db.session.execute(
                select(UserModel).where(UserModel.id == target_user_id)
            ).scalar_one()

            if user.role in ["admin", "admin_manager"] and claims.get("role") != "admin":
                abort(403, message="Only the top-level admin can change manager admin roles")

            user.role = new_role
            db.session.add(user)
            db.session.commit()
            return user
        except ValueError:
            abort(400, message="Invalid user id")
        except NoResultFound:
            abort(404, message="User not found")
        except HTTPException:
            raise
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while updating role")

    @staticmethod
    def update_permissions(user_id, data):
        try:
            current_user_id = int(get_jwt_identity())
            claims = get_jwt()
            target_user_id = int(user_id)
            grants = data.get("grants", [])
            revokes = data.get("revokes", [])

            if current_user_id == target_user_id:
                abort(400, message="You cannot change your own permissions")

            validate_permissions(grants)
            validate_permissions(revokes)

            user = db.session.execute(
                select(UserModel).where(UserModel.id == target_user_id)
            ).scalar_one()

            if user.role in ["admin", "admin_manager"] and claims.get("role") != "admin":
                abort(403, message="Only the top-level admin can change manager admin permissions")

            user.set_permission_overrides(grants=grants, revokes=revokes)
            db.session.add(user)
            db.session.commit()
            return user
        except ValueError:
            abort(400, message="Invalid user id")
        except NoResultFound:
            abort(404, message="User not found")
        except HTTPException:
            raise
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while updating permissions")
=======
            abort(500, message="Internal server error while deleting user")
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
