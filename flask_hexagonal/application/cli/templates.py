from datetime import datetime
from uuid import UUID
from typing import List

from pydantic import BaseModel

from flask_hexagonal.application.cli.interfaces.entities import CmdResponse, CmdError
from flask_hexagonal.exceptions import FlaskHexagonalException
from flask_hexagonal.domain.templates import service
from flask_hexagonal.domain.templates.interfaces.repository import (
    ListTemplateRepositoryInterface,
)


class TemplateOut(BaseModel):
    id: UUID
    name: str
    external_id: str
    tokens: List[str]
    created_at: datetime


def cmd_list_templates(repository: ListTemplateRepositoryInterface) -> CmdResponse:
    try:
        templates = service.list_templates(repository)
        return CmdResponse(
            data=[TemplateOut(**t.dict()) for t in templates]
        )
    except FlaskHexagonalException as exc:
        return CmdResponse(
            error=CmdError(
                message=exc.message,
                type=str(exc.type),
                details=exc.details,
            )
        )
