from datetime import datetime
from http import HTTPStatus
from typing import List
from uuid import UUID

from pydantic import BaseModel, Extra
from pydantic.error_wrappers import ValidationError

from flask_hexagonal.domain.templates import service
from flask_hexagonal.domain.templates.interfaces.repository import (
    DeleteTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
)

from .interfaces import ActionController, ErrorResponseDetails, Request, Response


class TemplateIn(BaseModel):
    name: str
    tokens: List[str]
    external_id: str

    class Config:
        extra = Extra.forbid


class TemplateOut(BaseModel):
    id: UUID
    name: str
    external_id: str
    tokens: List[str]
    created_at: datetime


class ListTemplatesController(ActionController):
    def __init__(self, repository: ListTemplateRepositoryInterface):
        self.repository = repository

    def run(self, _: Request) -> Response:
        data = [
            TemplateOut(**t.dict())
            for t in service.list_templates(self.repository)
        ]
        return Response(status=HTTPStatus.OK, data=data)


class RetrieveTemplateController(ActionController):
    def __init__(self, repository: RetrieveTemplateRepositoryInterface):
        self.repository = repository

    def run(self, request: Request) -> Response:
        try:
            template_id = request.view_args.get("id")
            template = service.get_template(UUID(template_id), self.repository)
            return Response(
                status=HTTPStatus.OK if template else HTTPStatus.NOT_FOUND,
                data=TemplateOut(**template.dict()),
            )
        except ValueError:
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The provided id is invalid.",
                    type="ValueError",
                ),
            )


class CreateTemplateController(ActionController):
    def __init__(self, repository: PersistTemplateRepositoryInterface):
        self.repository = repository

    def run(self, request: Request) -> Response:
        try:
            template_in = TemplateIn(**request.json_payload)
            result = service.create_template(
                template_in.name,
                template_in.tokens,
                template_in.external_id,
                self.repository,
            )
            return Response(
                status=HTTPStatus.CREATED,
                data=TemplateOut(**result.dict()),
            )
        except ValidationError as exc:
            details = {".".join(err["loc"]): err["msg"] for err in exc.errors()}
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The payload has one or more invalid fields.",
                    type="ValidationError",
                    details=details,
                ),
            )


class DeleteTemplateController(ActionController):
    def __init__(self, repository: DeleteTemplateRepositoryInterface):
        self.repository = repository

    def run(self, request: Request) -> Response:
        try:
            template_id = request.view_args.get("id")
            result = service.delete_template(template_id, self.repository)
            return Response(
                status=HTTPStatus.NO_CONTENT if result else HTTPStatus.NOT_FOUND
            )
        except ValueError:
            return Response(
                status=HTTPStatus.BAD_REQUEST,
                error=ErrorResponseDetails(
                    message="The provided id is invalid.",
                    type="ValueError",
                ),
            )
