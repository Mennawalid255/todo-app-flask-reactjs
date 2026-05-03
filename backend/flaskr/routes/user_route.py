from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
<<<<<<< HEAD

from flaskr.controllers.user_controller import UserController
from flaskr.schemas.schema import PermissionOverrideSchema, RoleUpdateSchema, UserSchema
from flaskr.security import permission_required
=======
from flaskr.schemas.schema import UserSchema
from flaskr.controllers.user_controller import UserController
from flaskr.decorators import role_required
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

bp = Blueprint("users", __name__)


@bp.route("/users")
class Users(MethodView):
<<<<<<< HEAD
    @jwt_required()
    @permission_required("view_users")
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return UserController.get_all()

    @bp.arguments(UserSchema)
    @bp.response(201)
    def post(self, data):
        return UserController.create(data)


@bp.route("/users/<user_id>")
class UserById(MethodView):
<<<<<<< HEAD
    @jwt_required()
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
    @bp.response(200, UserSchema)
    def get(self, user_id):
        return UserController.get_by_id(user_id)

    @jwt_required()
<<<<<<< HEAD
    @permission_required("delete_users")
    @bp.response(204)
    def delete(self, user_id):
        return UserController.delete_by_id(user_id)


@bp.route("/users/<user_id>/role")
class UserRole(MethodView):
    @jwt_required()
    @permission_required("manage_roles")
    @bp.arguments(RoleUpdateSchema)
    @bp.response(200, UserSchema)
    def patch(self, data, user_id):
        return UserController.update_role(user_id, data)


@bp.route("/users/<user_id>/permissions")
class UserPermissions(MethodView):
    @jwt_required()
    @permission_required("manage_permissions")
    @bp.arguments(PermissionOverrideSchema)
    @bp.response(200, UserSchema)
    def patch(self, data, user_id):
        return UserController.update_permissions(user_id, data)


=======
    @role_required("admin", "admin_manager")
    @bp.response(204)
    def delete(self, user_id):
        """Manager admin route (JWT + manager role required)"""
        return UserController.delete_by_id(user_id)


>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
@bp.route("/users/account")
class UserAccount(MethodView):
    @jwt_required()
    @bp.response(204)
    def delete(self):
<<<<<<< HEAD
        return UserController.delete()
=======
        """Any logged in user can delete their own account"""
        return UserController.delete()
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
