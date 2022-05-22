from typing import List

from .exceptions import (
    TemplateImportError,
    TokenValidationError,
)
from .interfaces import (
    ExternalTemplateRepositoryInterface,
    TemplateRepositoryInterface,
    ExternalTemplateInterface,
    TemplateInterface,
    TemplateServiceInterface,
)


class TemplateService(TemplateServiceInterface):
    
    def __init__(self, repository: TemplateRepositoryInterface, external_repository: ExternalTemplateRepositoryInterface):
        self.repository = repository
        self.external_repository = external_repository

    def list_templates(self) -> List[TemplateInterface]:
        return self.repository.list()

    def get_template(self, id: str) -> TemplateInterface:
        return self.repository.get()

    def import_template(self, external_id: str) -> TemplateInterface:
        try:
            external_template: ExternalTemplateInterface = self.external_repository.get(external_id)
            return self.repository.insert(
                external_template.name,
                external_template.tokens,
                external_template.id,
            )
        except Exception as exc:
            raise TemplateImportError("", [])

    def validate_tokens(self, external_id: str, requested_tokens: List[str]) -> None:
        template_tokens = self.external_repository.list_tokens(external_id)
        missing_tokens = set(template_tokens).difference(requested_tokens)
        if len(missing_tokens) > 0:
            raise TokenValidationError("", [])
