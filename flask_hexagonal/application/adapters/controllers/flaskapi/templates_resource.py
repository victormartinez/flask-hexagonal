from http import HTTPStatus

from flask_restful import Resource
from flask import jsonify, make_response

from flask_hexagonal.domain.templates import service


class ListTemplatesResource(Resource):

    def get(self, *args, **kwargs):
        return make_response(
            jsonify({
                "success": True,
                "code": HTTPStatus.OK,
                "message": "[Flask] List of Templates",
                "data": service.list_templates(),
            }),
            HTTPStatus.OK,
        )
