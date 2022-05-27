import json
from http import HTTPStatus

from flask_hexagonal.domain.templates import service
from flask_hexagonal.infrastructure.database.repositories import (
    RetrieveDBTemplateRepository,
    ListDBTemplateRepository,
    PersistDBTemplateRepository,
)
from .interfaces import Request, JsonResponse, ActionController


class ListTemplatesController(ActionController):

    def run(self, request: Request) -> JsonResponse:
        results = service.list_templates(ListDBTemplateRepository())
        return JsonResponse(
            content=json.dumps({
                "success": True,
                "code": HTTPStatus.OK,
                "message": "List Templates",
                "data": results,
            }),
            status=HTTPStatus.OK,
        )
