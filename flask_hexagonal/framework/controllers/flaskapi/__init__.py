from flask import Blueprint, Flask
from flask_restful import Api

from .templates import ListCreateTemplatesResource, RetrieveDeleteTemplateResource


def create_app() -> Flask:
    app = Flask(__name__)

    _configure_api(app)
    return app


def _configure_api(app: Flask) -> None:
    bp = Blueprint("templates", __name__, url_prefix="/api/v1/templates")
    api = Api(bp)

    api.add_resource(ListCreateTemplatesResource, "/")
    api.add_resource(RetrieveDeleteTemplateResource, "/<id>")
    app.register_blueprint(bp)
