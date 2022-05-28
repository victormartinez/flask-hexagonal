from flask import Blueprint, Flask
from flask_restful import Api

from .templates import (
    ListTemplatesResource,
    CreateTemplateResource,
    RetrieveTemplateResource,
)



def create_app(*args, **config):
    app = Flask(__name__)

    _configure_api(app)
    return app


def _configure_api(app: Flask) -> None:
    bp = Blueprint("templates", __name__, url_prefix="/api/v1/templates")
    api = Api(bp)

    api.add_resource(ListTemplatesResource, "/")
    api.add_resource(CreateTemplateResource, "/")
    api.add_resource(RetrieveTemplateResource, "/<idx>")
    app.register_blueprint(bp)
