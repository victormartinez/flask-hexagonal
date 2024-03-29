import json
from typing import Optional

from flask import Response, jsonify, make_response, request
from flask_restful import Resource

from flask_hexagonal.application.controllers.interfaces import Request
from flask_hexagonal.application.controllers.templates import (
    ActionController,
    CreateTemplateController,
    DeleteTemplateController,
    ListTemplatesController,
    RetrieveTemplateController,
)
from flask_hexagonal.infrastructure.memory.repositories import (
    DeleteMemoryTemplateRepository,
    ListMemoryTemplateRepository,
    PersistMemoryTemplateRepository,
    RetrieveMemoryTemplateRepository,
)


def to_request() -> Request:
    data = request.get_data()
    payload = json.loads(data) if data else None
    return Request(
        path=request.path,
        query_string=request.query_string,
        method=request.method,
        data=data,
        json_payload=payload,
        headers=request.headers,
        view_args=request.view_args,
    )


class BaseResource(Resource):

    GET_CONTROLLER: Optional[ActionController] = None
    POST_CONTROLLER: Optional[ActionController] = None
    DELETE_CONTROLLER: Optional[ActionController] = None

    def get(self, *args, **kwargs) -> Response:  # type: ignore
        if not self.GET_CONTROLLER:
            raise NotImplementedError("Resource.get not implemented.")
        parsed_request = to_request()
        response = self.GET_CONTROLLER.run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)

    def post(self, *args, **kwargs) -> Response:  # type: ignore
        if not self.POST_CONTROLLER:
            raise NotImplementedError("Resource.post not implemented.")
        parsed_request = to_request()
        response = self.POST_CONTROLLER.run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)

    def delete(self, *args, **kwargs) -> Response:  # type: ignore
        if not self.DELETE_CONTROLLER:
            raise NotImplementedError("Resource.delete not implemented.")
        parsed_request = to_request()
        response = self.DELETE_CONTROLLER.run(parsed_request)
        return make_response(jsonify(response.dict()), response.status)


class ListCreateTemplatesResource(BaseResource):
    GET_CONTROLLER = ListTemplatesController(ListMemoryTemplateRepository())
    POST_CONTROLLER = CreateTemplateController(PersistMemoryTemplateRepository())


class RetrieveDeleteTemplateResource(BaseResource):

    GET_CONTROLLER = RetrieveTemplateController(RetrieveMemoryTemplateRepository())
    DELETE_CONTROLLER = DeleteTemplateController(DeleteMemoryTemplateRepository())
