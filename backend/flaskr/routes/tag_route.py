from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flaskr.controllers.tag_controller import TagController
from flaskr.security import permission_required
from flaskr.schemas.schema import TagSchema

bp = Blueprint("tags", __name__)


@bp.route("/tags")
class Tags(MethodView):
    @bp.response(200, TagSchema(many=True))
    def get(self):
        return TagController.get_all()

    @bp.arguments(TagSchema)
    @jwt_required()
    @permission_required("create_tags")
    @bp.response(201)
    def post(self, data):
        return TagController.create(data)
