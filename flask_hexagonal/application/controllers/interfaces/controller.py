from .entities import Response, Request


class ActionController:

    def run(self, request: Request) -> Response:
        raise NotImplementedError()
