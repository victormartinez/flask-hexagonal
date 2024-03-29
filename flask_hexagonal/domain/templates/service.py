from typing import List, Optional, Sequence
from uuid import UUID

from flask_hexagonal.domain.templates.interfaces.repository import (
    DeleteTemplateRepositoryInterface,
)

from .interfaces import (
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    TemplateInterface,
)


def list_templates(
    repository: ListTemplateRepositoryInterface,
) -> Sequence[TemplateInterface]:
    return repository.list()


def get_template(
    id: UUID, repository: RetrieveTemplateRepositoryInterface
) -> TemplateInterface:
    return repository.get(id)


def delete_template(
    id: UUID, repository: DeleteTemplateRepositoryInterface
) -> Optional[int]:
    return repository.delete(id)


def create_template(
    name: str,
    tokens: List[str],
    external_id: str,
    repository: PersistTemplateRepositoryInterface,
) -> TemplateInterface:
    return repository.insert(name, tokens, external_id)
