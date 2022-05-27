from uuid import UUID
from datetime import datetime
from typing import List


class TemplateInterface:

    @property
    def id(self) -> UUID:
        raise NotImplementedError("Missing property 'id'.")

    @property
    def name(self) -> str:
        raise NotImplementedError("Missing property 'name'.")

    @property
    def external_id(self) -> str:
        raise NotImplementedError("Missing property 'external_id'.")

    @property
    def tokens(self) -> List[str]:
        raise NotImplementedError("Missing property 'tokens'.")

    @property
    def created_at(self) -> datetime:
        raise NotImplementedError("Missing property 'created_at'.")


class ExternalTemplateInterface:

    @property
    def id(self) -> str:
        raise NotImplementedError("Missing property 'id'.")

    @property
    def name(self) -> str:
        raise NotImplementedError("Missing property 'name'.")

    @property
    def tokens(self) -> List[str]:
        raise NotImplementedError("Missing property 'tokens'.")
