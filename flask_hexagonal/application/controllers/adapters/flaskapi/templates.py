from flask_restful import Resource
from flask import make_response

from flask_hexagonal.application.controllers import (
    JsonResponse,
    Request,
    ListTemplatesController,
)


class ListTemplatesResource(Resource):

    def get(self, *args, **kwargs):
        request = Request()
        response: JsonResponse = ListTemplatesController().run(request)
        return make_response(response.content, response.status)
