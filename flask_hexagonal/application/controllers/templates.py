import json
from http import HTTPStatus

from flask_hexagonal.domain.templates import TemplateService
from flask_hexagonal.infrastructure.database.repositories import DBTemplateRepository

from .interfaces import Request, JsonResponse, ActionController


class ListTemplatesController(ActionController):

    def run(self, request: Request) -> JsonResponse:
        service = TemplateService(repository=DBTemplateRepository())
        return JsonResponse(
            content=json.dump({
                "success": True,
                "code": HTTPStatus.OK,
                "message": "List of Templates",
                "data": service.list_templates(),
            }),
            status=HTTPStatus.OK,
        )
