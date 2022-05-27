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
        return JsonResponse(
            content=json.dump({
                "success": True,
                "code": HTTPStatus.OK,
                "message": "List of Templates",
                "data": service.list_templates(ListDBTemplateRepository()),
            }),
            status=HTTPStatus.OK,
        )
