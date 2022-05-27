from typing import List

from .exceptions import (
    TemplateImportError,
    TokenValidationError,
)
from .interfaces import (
    ListExternalTemplateTokensRepositoryInterface,
    RetrieveExternalTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    ExternalTemplateInterface,
    TemplateInterface,
    TemplateServiceInterface,
)


class TemplateService(TemplateServiceInterface):
    
    def list_templates(self, repository: ListTemplateRepositoryInterface) -> List[TemplateInterface]:
        return repository.list()

    def get_template(self, id: str, repository: RetrieveTemplateRepositoryInterface) -> TemplateInterface:
        return repository.get()

    def import_template(self, external_id: str, external_repository: RetrieveExternalTemplateRepositoryInterface, repository: PersistTemplateRepositoryInterface) -> TemplateInterface:
        try:
            external_template: ExternalTemplateInterface = external_repository.get(external_id)
            return repository.insert(
                external_template.name,
                external_template.tokens,
                external_template.id,
            )
        except Exception as exc:
            raise TemplateImportError("", [])

    def validate_tokens(self, external_id: str, requested_tokens: List[str], external_repository: ListExternalTemplateTokensRepositoryInterface) -> None:
        template_tokens = external_repository.list_tokens(external_id)
        missing_tokens = set(template_tokens).difference(requested_tokens)
        if len(missing_tokens) > 0:
            raise TokenValidationError("", [])
