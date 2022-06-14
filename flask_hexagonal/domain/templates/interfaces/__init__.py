from .entities import TemplateInterface
from .repository import (
    DeleteTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
)

__all__ = (
    "ListTemplateRepositoryInterface",
    "RetrieveTemplateRepositoryInterface",
    "PersistTemplateRepositoryInterface",
    "DeleteTemplateRepositoryInterface",
    "TemplateInterface",
)
