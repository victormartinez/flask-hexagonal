from falcon import App

from .templates import ListCreateTemplatesResource, RetrieveDeleteTemplateResource


def create_app() -> App:
    app = App()

    _configure_api(app)
    return app


def _configure_api(app: App) -> None:
    app.add_route("/api/v1/templates/", ListCreateTemplatesResource())
    app.add_route("/api/v1/templates/{id}", RetrieveDeleteTemplateResource())
