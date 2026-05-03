<<<<<<< HEAD
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.auth_controller import AuthController
from flaskr.schemas.schema import CurrentUserSchema, SignInSchema
=======
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.auth_controller import AuthController
from flaskr.schemas.schema import SignInSchema
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

bp = Blueprint("auth", __name__)


@bp.route("/auth/sign-in")
class SignIn(MethodView):
    @bp.arguments(SignInSchema)
    @bp.response(200)
    def post(self, data):
        return AuthController.sign_in(data)
<<<<<<< HEAD


@bp.route("/auth/me")
class CurrentUser(MethodView):
    @jwt_required()
    @bp.response(200, CurrentUserSchema)
    def get(self):
        return AuthController.me(get_jwt_identity())
=======
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
