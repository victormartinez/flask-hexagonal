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

    def _init__(self, Session: Type[Session] = Session):
        self.Session = Session

    def get(self, idx: UUID) -> TemplateInterface:
        # TODO: handle errors
        query = select(DBTemplate).filter(DBTemplate.id == idx)
        with self.Session.begin() as db_session:
            result = db_session.execute(query)
            return result.scalars().first()


class ListDBTemplateRepository(ListTemplateRepositoryInterface):

    def _init__(self, Session: Type[Session] = Session):
        self.Session = Session

    def list(self) -> List[TemplateInterface]:
        # TODO: handle errors
        with self.Session.begin() as db_session:
            query = select(DBTemplate)
            result = db_session.execute(query)
            return result.scalars().all()


class PersistDBTemplateRepository(PersistTemplateRepositoryInterface):

    def _init__(self, Session: Type[Session] = Session):
        self.Session = Session

    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        with self.Session.begin() as db_session:
            template = DBTemplate(name=name, tokens=tokens, external_id=external_id)
            db_session.add(template)
            db_session.commit()
            return template
