from .entities import Request, Response


class ActionController:
    def run(self, request: Request) -> Response:
        raise NotImplementedError()
