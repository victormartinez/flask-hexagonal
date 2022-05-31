from uuid import UUID
from datetime import datetime
from typing import List, Dict, Any

from pydantic import BaseModel


class MemoryTemplate(BaseModel):

    id: UUID
    name: str
    tokens: List[str]
    external_id: str
    created_at: datetime

    def dict(self) -> Dict[Any, Any]:
        return {
            "id": str(self.id),
            "name": self.name,
            "tokens": self.tokens,
            "external_id": self.external_id,
            "created_at": (self.created_at),
        }
