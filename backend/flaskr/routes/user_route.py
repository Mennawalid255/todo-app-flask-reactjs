from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.schemas.schema import UserSchema
from flaskr.controllers.user_controller import UserController
from flaskr.decorators import admin_required

bp = Blueprint("users", __name__)


@bp.route("/users")
class Users(MethodView):
    @admin_required
    @bp.response(200, UserSchema(many=True))
    def get(self):
        """Admin only - get all users"""
        return UserController.get_all()

    @bp.arguments(UserSchema)
    @bp.response(201)
    def post(self, data):
        return UserController.create(data)


@bp.route("/users/<user_id>")
class UserById(MethodView):
    @admin_required
    @bp.response(200, UserSchema)
    def get(self, user_id):
        """Admin only - get user by id"""
        return UserController.get_by_id(user_id)


@bp.route("/users/account")
class UserAccount(MethodView):
    @jwt_required()
    @bp.response(204)
    def delete(self):
        """Any logged in user can delete their own account"""
        return UserController.delete()