from datetime import datetime
from typing import Any, Dict, List
from uuid import UUID


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

    def dict(self) -> Dict[Any, Any]:
        raise NotImplementedError("Missing method 'dict()'.")
