from flask import Blueprint, Flask
from flask_restful import Api

from .templates_resource import ListTemplatesResource



def create_app(*args, **config):
    app = Flask(__name__)

    _configure_api(app)
    return app


def _configure_api(app: Flask) -> None:
    bp = Blueprint("templates", __name__, url_prefix="/api/v1/templates")
    api = Api(bp)

    api.add_resource(ListTemplatesResource, "/")
    app.register_blueprint(bp)
