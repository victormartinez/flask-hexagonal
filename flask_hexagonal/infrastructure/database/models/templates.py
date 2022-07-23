import uuid
from typing import Any, Dict

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

from flask_hexagonal.infrastructure.database.base import Base


class DBTemplate(Base):
    __tablename__ = "templates"
    id = sa.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    name = sa.Column(sa.String, nullable=False)
    tokens = sa.Column(sa.JSON, nullable=False)
    external_id = sa.Column(sa.String, index=True, nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    updated_at = sa.Column(
        sa.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    def dict(self) -> Dict[Any, Any]:
        return {
            "id": str(self.id),
            "name": self.name,
            "tokens": self.tokens,
            "external_id": self.external_id,
            "created_at": self.created_at,
        }
