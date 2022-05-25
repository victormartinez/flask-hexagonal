from typing import List

from flask_hexagonal.domain.templates import (
    TemplateRepositoryInterface,
    TemplateInterface,
)


class DBTemplateRepository(TemplateRepositoryInterface):

    def get(self, idx: str) -> TemplateInterface:
        raise NotImplementedError("'TemplateRepositoryInterface.get' must be implemented.")

    def list(self) -> List[TemplateInterface]:
        raise NotImplementedError("'TemplateRepositoryInterface.list' must be implemented.")

    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        raise NotImplementedError("'TemplateRepositoryInterface.insert' must be implemented.")
