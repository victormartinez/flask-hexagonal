from typing import List


class TemplatesException(Exception):

    @property
    def message(self) -> str:
        raise NotImplementedError("'Exception.message' not implemented.")

    @property
    def details(self) -> List[str]:
        raise NotImplementedError("'Exception.details' not implemented.")


class TokenValidationError(TemplatesException):

    def __init__(self, message: str, details: List[str] = None):
        self.message = message
        self.details = details or []


class TemplateImportError(TemplatesException):

    def __init__(self, message: str, details: List[str] = None):
        self.message = message
        self.details = details or []
