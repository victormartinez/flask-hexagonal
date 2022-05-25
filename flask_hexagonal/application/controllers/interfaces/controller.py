from .entities import JsonResponse, Request


class ActionController:

    def run(self, request: Request) -> JsonResponse:
        raise NotImplementedError()
