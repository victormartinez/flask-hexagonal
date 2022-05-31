from http import HTTPStatus
from typing import List
from uuid import UUID

from pydantic import BaseModel, Extra
from pydantic.error_wrappers import ValidationError

from flask_hexagonal.domain.templates import service
from flask_hexagonal.infrastructure.memory.repositories import (
    RetrieveMemoryTemplateRepository,
    ListMemoryTemplateRepository,
    PersistMemoryTemplateRepository,
    DeleteMemoryTemplateRepository,
)
from flask_hexagonal.infrastructure.database.repositories import (
    ListDBTemplateRepository,
    PersistDBTemplateRepository,
    DeleteDBTemplateRepository,
    RetrieveDBTemplateRepository,
)
from .interfaces import (
    Request, 
    Response, 
    ErrorResponseDetails,
    ActionController,
)


class TemplateIn(BaseModel):
    name: str
    tokens: List[str]
    external_id: str

    class Config:
        extra = Extra.forbid


class ListTemplatesController(ActionController):

    def run(self, _: Request) -> Response:
        data = {
            "templates": [
                t.dict() for t in service.list_templates(ListMemoryTemplateRepository())
            ]
        }
        return Response(status=HTTPStatus.OK, data=data)


class RetrieveTemplateController(ActionController):

    def run(self, request: Request) -> Response:
        try:
            template_id = request.view_args.get("id")
            template = service.get_template(UUID(template_id), RetrieveMemoryTemplateRepository())
            return Response(
                status=HTTPStatus.OK if template else HTTPStatus.NOT_FOUND,
                data=template.dict()
            )
        except ValueError:
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The provided id is invalid.",
                    type="ValueError",
                )
            )


class CreateTemplateController(ActionController):
    
    def run(self, request: Request) -> Response:
        try:
            template_in = TemplateIn(**request.json_payload)
            result = service.create_template(
                template_in.name,
                template_in.tokens,
                template_in.external_id,
                PersistMemoryTemplateRepository(),
            )
            return Response(
                status=HTTPStatus.CREATED,
                data=result.dict(),
            )
        except ValidationError as exc:
            details = {
                ".".join(err["loc"]): err["msg"]
                for err in exc.errors()
            }
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The payload has one or more invalid fields.",
                    type="ValidationError",
                    details=details
                )
            )


class DeleteTemplateController(ActionController):
    
    def run(self, request: Request) -> Response:
        try:
            template_id = request.view_args.get("id")
            result = service.delete_template(template_id, DeleteMemoryTemplateRepository())
            return Response(
                status=HTTPStatus.NO_CONTENT if result else HTTPStatus.NOT_FOUND
            )
        except ValueError:
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The provided id is invalid.",
                    type="ValueError",
                )
            )