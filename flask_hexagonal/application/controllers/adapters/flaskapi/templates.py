import json

from flask_restful import Resource
from flask import make_response, request, jsonify

from flask_hexagonal.application.controllers.interfaces import Request
from flask_hexagonal.application.controllers.templates import (
    ActionController,
    ListTemplatesController,
    CreateTemplateController,
    RetrieveTemplateController,
    DeleteTemplateController,
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

class BaseResource(Resource):

    CONTROLLER: ActionController = None

    def get(self, *args, **kwargs):
        if not self.CONTROLLER:
            raise NotImplementedError('Resource.get not implemented.')
        parsed_request = to_request()
        response = self.CONTROLLER().run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)

    def post(self, *args, **kwargs):
        if not self.CONTROLLER:
            raise NotImplementedError('Resource.post not implemented.')
        parsed_request = to_request()
        response = self.CONTROLLER().run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)

    def delete(self, *args, **kwargs):
        if not self.CONTROLLER:
            raise NotImplementedError('Resource.delete not implemented.')
        parsed_request = to_request()
        response = self.CONTROLLER().run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)


class ListTemplatesResource(BaseResource):
    CONTROLLER = ListTemplatesController


class CreateTemplateResource(BaseResource):
    CONTROLLER = CreateTemplateController


class RetrieveDeleteTemplateResource(BaseResource):

    def get(self, *args, **kwargs):
        self.CONTROLLER = RetrieveTemplateController
        return super().get(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.CONTROLLER = DeleteTemplateController
        return super().get(*args, **kwargs)
