import json
import uuid
from datetime import datetime
from typing import List, Optional
from uuid import UUID

from redis import RedisError

from flask_hexagonal.domain.templates import (
    DeleteTemplateRepositoryInterface,
    ListTemplateRepositoryInterface,
    PersistTemplateRepositoryInterface,
    RetrieveTemplateRepositoryInterface,
    TemplateInterface,
)
from flask_hexagonal.exceptions import ExceptionType, FlaskHexagonalException
from flask_hexagonal.infrastructure.memory.client import redis_client
from flask_hexagonal.infrastructure.memory.models.templates import MemoryTemplate


class RetrieveMemoryTemplateRepository(RetrieveTemplateRepositoryInterface):
    def get(self, idx: UUID) -> TemplateInterface:
        try:
            value = redis_client.get(str(idx))
            if not value:
                raise FlaskHexagonalException(
                    type=ExceptionType.OBJECT_NOT_FOUND,
                    message=f"Template #{str(idx)} not found."
                )
            data = json.loads(value)
            return MemoryTemplate(**data)
        except RedisError as err:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(err))


class ListMemoryTemplateRepository(ListTemplateRepositoryInterface):
    def list(self) -> List[TemplateInterface]:
        try:
            result = []
            for key in redis_client.scan_iter("*"):
                idx = key.decode()
                data = json.loads(redis_client.get(idx))

                data["id"] = UUID(data["id"])
                data["created_at"] = datetime.fromisoformat(data["created_at"])
                result.append(MemoryTemplate(**data))
            return result
        except RedisError as err:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(err))


class PersistMemoryTemplateRepository(PersistTemplateRepositoryInterface):
    def insert(self, name: str, tokens: List[str], external_id: str) -> TemplateInterface:
        try:
            data = {
                "id": uuid.uuid4(),
                "name": name,
                "tokens": tokens,
                "external_id": external_id,
                "created_at": datetime.utcnow(),
            }
            template = MemoryTemplate(**data)

            data["id"] = str(data["id"])
            data["created_at"] = data["created_at"].isoformat()
            redis_client.set(str(data["id"]), json.dumps(data))
            return template
        except RedisError as err:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(err))


class DeleteMemoryTemplateRepository(DeleteTemplateRepositoryInterface):
    def delete(self, idx: UUID) -> Optional[int]:
        try:
            value = redis_client.getdel(str(idx))
            return 1 if value else 0
        except RedisError as err:
            raise FlaskHexagonalException(type=ExceptionType.DATABASE_ERROR, message=str(err))
