from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from flask_hexagonal.application.cli.interfaces.entities import CmdError, CmdResponse
from flask_hexagonal.domain.templates import service
from flask_hexagonal.domain.templates.interfaces.repository import (
    ListTemplateRepositoryInterface,
)
from flask_hexagonal.exceptions import FlaskHexagonalException


class TemplateData(BaseModel):
    id: UUID
    name: str
    external_id: str
    tokens: List[str]
    created_at: datetime


class TemplateOut(BaseModel):
    data: List[TemplateData]


def cmd_list_templates(repository: ListTemplateRepositoryInterface) -> CmdResponse:
    try:
        templates = service.list_templates(repository)
        out = TemplateOut(data=[TemplateData(**t.dict()) for t in templates])
        return CmdResponse(data=out)
    except FlaskHexagonalException as exc:
        return CmdResponse(
            error=CmdError(
                message=exc.message,
                type=str(exc.type),
                details=exc.details,
            )
        )
