import json
from typing import List, Optional
from uuid import UUID
from datetime import datetime
import uuid

from flask_hexagonal.infrastructure.memory.client import redis_client
from flask_hexagonal.domain.templates import (
    ListTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    DeleteTemplateRepositoryInterface,
    TemplateInterface,
)
from flask_hexagonal.infrastructure.memory.models.templates import MemoryTemplate


class RetrieveMemoryTemplateRepository(RetrieveTemplateRepositoryInterface):

    def get(self, idx: UUID) -> TemplateInterface:
        # TODO: handle errors
        # TODO: separate DB conn from Data Access
        value = redis_client.get(str(idx))
        data = json.loads(value)
        return MemoryTemplate(**data)


class ListMemoryTemplateRepository(ListTemplateRepositoryInterface):

    def list(self) -> List[TemplateInterface]:
        # TODO: handle errors
        result = []
        for key in redis_client.scan_iter("*"):
            idx = key.decode()
            data = json.loads(redis_client.get(idx))

            data["id"] = UUID(data["id"])
            data["created_at"] = datetime.fromisoformat(data["created_at"])
            result.append(MemoryTemplate(**data))
        return result


class PersistMemoryTemplateRepository(PersistTemplateRepositoryInterface):

    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        data = {
            "id": uuid.uuid4(),
            "name": name,
            "tokens": tokens,
            "external_id": external_id, 
            "created_at": datetime.utcnow()
        }
        template = MemoryTemplate(**data)

        data["id"] = str(data["id"])
        data["created_at"] = data["created_at"].isoformat()
        redis_client.set(str(data["id"]), json.dumps(data))
        return template


class DeleteMemoryTemplateRepository(DeleteTemplateRepositoryInterface):

    def delete(self, idx: UUID) -> Optional[int]:
        value = redis_client.getdel(str(idx))
        return 1 if value else 0
