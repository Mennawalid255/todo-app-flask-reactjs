from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.auth_controller import AuthController
from flaskr.schemas.schema import CurrentUserSchema, SignInSchema

bp = Blueprint("auth", __name__)


@bp.route("/auth/sign-in")
class SignIn(MethodView):
    @bp.arguments(SignInSchema)
    @bp.response(200)
    def post(self, data):
        return AuthController.sign_in(data)


@bp.route("/auth/me")
class CurrentUser(MethodView):
    @jwt_required()
    @bp.response(200, CurrentUserSchema)
    def get(self):
        return AuthController.me(get_jwt_identity())
