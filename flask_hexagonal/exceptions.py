from enum import Enum
from typing import Dict, Optional


class ExceptionType(Enum):
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    DATABASE_ERROR = "DATABASE_ERROR"
    DATABASE_INTEGRITY_ERROR = "DATABASE_INTEGRITY_ERROR"


class BaseException(Exception):
    @property
    def message(self) -> str:
        raise NotImplementedError("'Exception.message' not implemented.")

    @property
    def type(self) -> ExceptionType:
        raise NotImplementedError("'Exception.details' not implemented.")

    @property
    def details(self) -> Optional[Dict[str, str]]:
        raise NotImplementedError("'Exception.details' not implemented.")


class FlaskHexagonalException(BaseException):
    def __init__(
        self,
        type: ExceptionType,
        message: str,
        details: Optional[Dict[str, str]] = None,
    ):
        self._type = type
        self._message = message
        self._details = details or {}
        super().__init__(message)

    @property
    def message(self) -> str:
        return self._message

    @property
    def type(self) -> ExceptionType:
        return self._type

    @property
    def details(self) -> Optional[Dict[str, str]]:
        return self._details
