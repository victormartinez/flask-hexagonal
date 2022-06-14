from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete
from sqlalchemy.future import select

from flask_hexagonal.domain.templates import (
    DeleteTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    TemplateInterface,
)
from flask_hexagonal.infrastructure.database.models import DBTemplate
from flask_hexagonal.infrastructure.database.session import Session


class RetrieveDBTemplateRepository(RetrieveTemplateRepositoryInterface):
    def get(self, idx: UUID) -> TemplateInterface:
        # TODO: handle errors
        # TODO: separate DB conn from Data Access
        query = select(DBTemplate).filter(DBTemplate.id == idx)
        with Session.begin() as db_session:
            result = db_session.execute(query)
            result = result.scalars().first()
            if not result:
                raise ValueError("Not Found!")
            db_session.expunge_all()
            return result


class ListDBTemplateRepository(ListTemplateRepositoryInterface):
    def list(self) -> List[TemplateInterface]:
        # TODO: handle errors
        with Session.begin() as db_session:
            query = select(DBTemplate)
            result = db_session.execute(query)
            results = result.scalars().all()
            db_session.expunge_all()
            return results


class PersistDBTemplateRepository(PersistTemplateRepositoryInterface):
    def insert(
        self, name: str, tokens: List[str], external_id: str
    ) -> TemplateInterface:
        with Session.begin() as db_session:
            template = DBTemplate(name=name, tokens=tokens, external_id=external_id)
            db_session.add(template)

            db_session.expunge_all()
            db_session.commit()

            return template


class DeleteDBTemplateRepository(DeleteTemplateRepositoryInterface):
    def delete(self, idx: UUID) -> Optional[int]:
        with Session.begin() as db_session:
            query = delete(DBTemplate).where(DBTemplate.id == idx)
            result = db_session.execute(query)
            db_session.commit()

            db_session.expunge_all()
            return result.rowcount
