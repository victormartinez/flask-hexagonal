from typing import List, Type
from uuid import UUID

from sqlalchemy.future import select

from flask_hexagonal.infrastructure.database.models import DBTemplate
from flask_hexagonal.infrastructure.database.session import Session
from flask_hexagonal.domain.templates import (
    ListTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    TemplateInterface,
)


class RetrieveDBTemplateRepository(RetrieveTemplateRepositoryInterface):

    def get(self, idx: UUID) -> TemplateInterface:
        # TODO: handle errors
        # TODO: separate DB conn from Data Access
        query = select(DBTemplate).filter(DBTemplate.id == idx)
        with Session.begin() as db_session:
            result = db_session.execute(query)
            return result.scalars().first()


class ListDBTemplateRepository(ListTemplateRepositoryInterface):

    def list(self) -> List[TemplateInterface]:
        # TODO: handle errors
        with Session.begin() as db_session:
            query = select(DBTemplate)
            result = db_session.execute(query)
            return result.scalars().all()


class PersistDBTemplateRepository(PersistTemplateRepositoryInterface):

    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        with Session.begin() as db_session:
            template = DBTemplate(name=name, tokens=tokens, external_id=external_id)
            db_session.add(template)
            db_session.commit()
            return template
