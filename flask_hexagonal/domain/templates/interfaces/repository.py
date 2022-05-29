from uuid import UUID

from typing import List, Optional

from .entities import TemplateInterface, ExternalTemplateInterface


class RetrieveExternalTemplateRepositoryInterface:

    def get(self, idx: UUID) -> ExternalTemplateInterface:
        raise NotImplementedError("'RetrieveExternalTemplateRepositoryInterface.get_template' must be implemented.")


class ListExternalTemplateTokensRepositoryInterface:

    def list_tokens(self, template_idx: str) -> List[str]:
        raise NotImplementedError("'ListExternalTemplateTokensRepositoryInterface.list_tokens' must be implemented.")


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