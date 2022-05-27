from flask_restful import Resource
from flask import make_response, request

from flask_hexagonal.application.controllers import (
    JsonResponse,
    Request,
    ListTemplatesController,
)

def to_request():
    return Request(
        path=request.path,
        query_string=request.query_string,
        method=request.method,
        data=request.data,
        headers=request.headers,
    )


class ListTemplatesResource(Resource):

    def get(self, *args, **kwargs):
        req = to_request()
        response: JsonResponse = ListTemplatesController().run(req)
        return make_response(response.content, response.status)
