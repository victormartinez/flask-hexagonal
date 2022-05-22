from typing import List

from .entities import TemplateInterface, ExternalTemplateInterface


class ExternalTemplateRepositoryInterface:

    def get(self, idx: str) -> ExternalTemplateInterface:
        raise NotImplementedError("'ExternalTemplateRepositoryInterface.get_template' must be implemented.")

    def list_tokens(self, template_idx: str) -> List[str]:
        raise NotImplementedError("'ExternalTemplateRepositoryInterface.list_tokens' must be implemented.")


class TemplateRepositoryInterface:

    def get(self, idx: str) -> TemplateInterface:
        raise NotImplementedError("'TemplateRepositoryInterface.get' must be implemented.")

    def list(self) -> List[TemplateInterface]:
        raise NotImplementedError("'TemplateRepositoryInterface.list' must be implemented.")

    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        raise NotImplementedError("'TemplateRepositoryInterface.insert' must be implemented.")
