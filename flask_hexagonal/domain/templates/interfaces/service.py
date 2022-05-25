from typing import List

from .entities import TemplateInterface


class TemplateServiceInterface:

    def list_templates(self) -> List[TemplateInterface]:
        raise NotImplementedError()

    def get_template(self, id: str) -> TemplateInterface:
        raise NotImplementedError()

    def import_template(self, external_id: str) -> TemplateInterface:
        raise NotImplementedError()

    def validate_tokens(self, external_id: str, requested_tokens: List[str]) -> None:
        raise NotImplementedError()
