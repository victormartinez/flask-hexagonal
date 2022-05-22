from falcon import App

from.templates_resource import ListTemplatesResource


def create_app(*args, **config):
    app = App()

    _configure_api(app)
    return app


def _configure_api(app: App) -> None:
    app.add_route('/api/v1/templates', ListTemplatesResource())
