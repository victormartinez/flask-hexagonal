from http import HTTPStatus
from typing import Any, Dict, Optional

from pydantic import BaseModel


class ErrorResponseDetails(BaseModel):

    message: str
    type: str
    details: Optional[Dict[str, str]] = {}


class Response(BaseModel):

    status: HTTPStatus
    content_type: str = "application/json"
    data: Optional[Dict[str, Any]] = {}
    error: Optional[ErrorResponseDetails] = None


class Request(BaseModel):
    path: str
    query_string: bytes
    method: str
    data: Optional[bytes]
    json_payload: Optional[Dict[Any, Any]] = {}
    headers: Optional[Dict[str, str]] = {}
    view_args: Dict[str, str] = {}
