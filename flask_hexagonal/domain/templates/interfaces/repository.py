from typing import Optional, Sequence
from uuid import UUID

from .entities import TemplateInterface


class BaseRepository:
    ...


class RetrieveTemplateRepositoryInterface(BaseRepository):
    def get(self, idx: UUID) -> TemplateInterface:
        raise NotImplementedError(
            "'RetrieveTemplateRepositoryInterface.get' must be implemented."
        )


class ListTemplateRepositoryInterface(BaseRepository):
    def list(self) -> Sequence[TemplateInterface]:
        raise NotImplementedError(
            "'ListTemplateRepositoryInterface.list' must be implemented."
        )


class PersistTemplateRepositoryInterface(BaseRepository):
    def insert(
        self, name: str, tokens: Sequence[str], external_id: str
    ) -> TemplateInterface:
        raise NotImplementedError(
            "'PersistTemplateRepositoryInterface.insert' must be implemented."
        )


class DeleteTemplateRepositoryInterface(BaseRepository):
    def delete(self, idx: UUID) -> Optional[int]:
        raise NotImplementedError(
            "'DeleteTemplateRepositoryInterface.delete' must be implemented."
        )
