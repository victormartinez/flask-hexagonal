from typing import List, Optional
from uuid import UUID

from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_hexagonal.domain.templates import (
    DeleteTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    TemplateInterface,
)
from flask_hexagonal.exceptions import ExceptionType, FlaskHexagonalException
from flask_hexagonal.infrastructure.database.models import DBTemplate
from flask_hexagonal.infrastructure.database.session import Session


class RetrieveDBTemplateRepository(RetrieveTemplateRepositoryInterface):
    def get(self, idx: UUID) -> TemplateInterface:
        try:
            query = select(DBTemplate).filter(DBTemplate.id == idx)
            with Session.begin() as db_session:
                result = db_session.execute(query)
                result = result.scalars().first()
                if not result:
                    raise FlaskHexagonalException(
                        type=ExceptionType.OBJECT_NOT_FOUND,
                        message=f"Template #{str(idx)} not found."
                    )
                db_session.expunge_all()
                return result
        except SQLAlchemyError as exc:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(exc))


class ListDBTemplateRepository(ListTemplateRepositoryInterface):
    def list(self) -> List[TemplateInterface]:
        try:
            with Session.begin() as db_session:
                query = select(DBTemplate)
                result = db_session.execute(query)
                results = result.scalars().all()
                db_session.expunge_all()
                return results
        except SQLAlchemyError as exc:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(exc))


class PersistDBTemplateRepository(PersistTemplateRepositoryInterface):
    def insert(
        self, name: str, tokens: List[str], external_id: str
    ) -> TemplateInterface:
        try:
            with Session.begin() as db_session:
                template = DBTemplate(name=name, tokens=tokens, external_id=external_id)
                db_session.add(template)

                db_session.expunge_all()
                db_session.commit()

                return template
        except SQLAlchemyError as exc:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(exc))


class DeleteDBTemplateRepository(DeleteTemplateRepositoryInterface):
    def delete(self, idx: UUID) -> Optional[int]:
        try:
            with Session.begin() as db_session:
                query = delete(DBTemplate).where(DBTemplate.id == idx)
                result = db_session.execute(query)
                db_session.commit()

                db_session.expunge_all()
                return result.rowcount
        except SQLAlchemyError as exc:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(exc))