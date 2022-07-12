from enum import Enum
from typing import Dict, List, Optional


class ExceptionType(Enum):
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    DATABASE_ERROR = "DATABASE_ERROR"
    DATABASE_INTEGRITY_ERROR = "DATABASE_INTEGRITY_ERROR"


class BaseException(Exception):
    ...


class FlaskHexagonalException(BaseException):
    def __init__(
        self,
        type: ExceptionType,
        message: str,
        errors: Optional[List[Dict[str, str]]] = None,
    ):
        self.type = type
        self.message = message
        self.errors = errors or []
        super().__init__(message)
