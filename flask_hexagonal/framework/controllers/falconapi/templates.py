import json
from typing import Any, Dict, Optional

import falcon

from flask_hexagonal.application.controllers.interfaces import Request
from flask_hexagonal.application.controllers.templates import (
    ActionController,
    CreateTemplateController,
    DeleteTemplateController,
    ListTemplatesController,
    RetrieveTemplateController,
)
from flask_hexagonal.infrastructure.database.repositories import (
    DeleteDBTemplateRepository,
    ListDBTemplateRepository,
    PersistDBTemplateRepository,
    RetrieveDBTemplateRepository,
)


def to_request(request: falcon.Request, view_args: Dict[str, Any]) -> Request:
    return Request(
        path=request.path,
        query_string=request.query_string,
        method=request.method,
        headers=request.headers,
        json_payload=request.get_media(default_when_empty={}),
        data=None,
        view_args=view_args,
    )


class BaseResource:

    GET_CONTROLLER: Optional[ActionController] = None
    POST_CONTROLLER: Optional[ActionController] = None
    DELETE_CONTROLLER: Optional[ActionController] = None

    def on_get(
        self, req: falcon.Request, resp: falcon.Response, **kwargs: Dict[Any, Any]
    ) -> None:
        if not self.GET_CONTROLLER:
            raise NotImplementedError("Resource.get not implemented.")
        parsed_request = to_request(req, view_args=kwargs)
        response = self.GET_CONTROLLER.run(parsed_request)

        resp.text = json.dumps(response.dict())
        resp.status = response.status

    def on_post(
        self, req: falcon.Request, resp: falcon.Response, **kwargs: Dict[Any, Any]
    ) -> None:
        if not self.POST_CONTROLLER:
            raise NotImplementedError("Resource.post not implemented.")
        parsed_request = to_request(req, view_args=kwargs)
        response = self.POST_CONTROLLER.run(parsed_request)

        resp.text = json.dumps(response.dict())
        resp.status = response.status

    def on_delete(
        self, req: falcon.Request, resp: falcon.Response, **kwargs: Dict[Any, Any]
    ) -> None:
        if not self.DELETE_CONTROLLER:
            raise NotImplementedError("Resource.delete not implemented.")
        parsed_request = to_request(req, view_args=kwargs)
        response = self.DELETE_CONTROLLER.run(parsed_request)

        resp.text = json.dumps(response.dict())
        resp.status = response.status


class ListCreateTemplatesResource(BaseResource):
    GET_CONTROLLER = ListTemplatesController(ListDBTemplateRepository())
    POST_CONTROLLER = CreateTemplateController(PersistDBTemplateRepository())


class RetrieveDeleteTemplateResource(BaseResource):
    GET_CONTROLLER = RetrieveTemplateController(RetrieveDBTemplateRepository())
    DELETE_CONTROLLER = DeleteTemplateController(DeleteDBTemplateRepository())
