from uuid import UUID

from typing import List, Optional

from .entities import TemplateInterface


class RetrieveTemplateRepositoryInterface:

    def get(self, idx: UUID) -> TemplateInterface:
        raise NotImplementedError("'RetrieveTemplateRepositoryInterface.get' must be implemented.")

class ListTemplateRepositoryInterface:
    def list(self) -> List[TemplateInterface]:
        raise NotImplementedError("'ListTemplateRepositoryInterface.list' must be implemented.")


class PersistTemplateRepositoryInterface:
    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        raise NotImplementedError("'PersistTemplateRepositoryInterface.insert' must be implemented.")


class DeleteTemplateRepositoryInterface:

    def delete(self, idx: UUID) -> Optional[int]:
        raise NotImplementedError("'DeleteTemplateRepositoryInterface.delete' must be implemented.")