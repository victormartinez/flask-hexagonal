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

    @message.setter
    def message(self, message: str) -> None:
        self.message = message

    @property
    def type(self) -> ExceptionType:
        raise NotImplementedError("'Exception.details' not implemented.")

    @type.setter
    def type(self, type: ExceptionType) -> None:
        self.type = type

    @property
    def details(self) -> Optional[Dict[str, str]]:
        raise NotImplementedError("'Exception.details' not implemented.")

    @details.setter
    def details(self, details: Optional[Dict[str, str]]) -> None:
        self.details = details


class FlaskHexagonalException(BaseException):
    def __init__(
        self,
        type: ExceptionType,
        message: str,
        details: Optional[Dict[str, str]] = None,
    ):
        self.type = type
        self.message = message
        self.details = details or {}
        super().__init__(message)
