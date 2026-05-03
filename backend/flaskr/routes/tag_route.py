from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flaskr.controllers.tag_controller import TagController
<<<<<<< HEAD
from flaskr.security import permission_required
from flaskr.schemas.schema import TagSchema
=======
from flaskr.schemas.schema import TagSchema
from flaskr.utils import role_required
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f

bp = Blueprint("tags", __name__)


@bp.route("/tags")
class Tags(MethodView):
    @bp.response(200, TagSchema(many=True))
    def get(self):
        return TagController.get_all()

    @bp.arguments(TagSchema)
    @jwt_required()
<<<<<<< HEAD
    @permission_required("create_tags")
    @bp.response(201)
    def post(self, data):
=======
    @role_required("admin", "admin_manager")
    @bp.response(201)
    def post(self, data):
        """Admin route (JWT + admin role required)"""
>>>>>>> 66c23344d9e2eba372aec5ca34b92d3cf77b8b5f
        return TagController.create(data)
