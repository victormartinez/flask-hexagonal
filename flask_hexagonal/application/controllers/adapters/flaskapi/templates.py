import json

from flask_restful import Resource
from flask import make_response, request, jsonify

from flask_hexagonal.application.controllers.interfaces import Request
from flask_hexagonal.application.controllers.templates import (
    ListTemplatesController,
    CreateTemplateController,
    RetrieveTemplateController,
)

def to_request():
    data = request.get_data()
    payload = json.loads(data) if data else None
    return Request(
        path=request.path,
        query_string=request.query_string,
        method=request.method,
        data=data,
        json_payload=payload,
        headers=request.headers,
        view_args=request.view_args
    )


class ListTemplatesResource(Resource):

    def get(self, *args, **kwargs):
        req = to_request()
        response = ListTemplatesController().run(req)
        return make_response(jsonify(response.dict()), response.status)


class CreateTemplateResource(Resource):

    def post(self, *args, **kwargs):
        req = to_request()
        response = CreateTemplateController().run(req)
        return make_response(jsonify(response.dict()), response.status)


class RetrieveTemplateResource(Resource):

    def get(self, *args, **kwargs):
        req = to_request()
        response = RetrieveTemplateController().run(req)
        return make_response(jsonify(response.dict()), response.status)
