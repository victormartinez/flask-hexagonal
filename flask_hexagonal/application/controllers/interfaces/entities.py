from http import HTTPStatus
from pydantic import BaseModel
from typing import Optional, Dict, Any


class ErrorResponseDetails(BaseModel):

    message: str
    type: str
    details: Optional[Dict[str, str]] = {}


class Response(BaseModel):

    status: HTTPStatus
    content_type: str = "application/json"
    data: Optional[Dict[str, str]] = {}
    error: Optional[ErrorResponseDetails] = None


class Request(BaseModel):
    path: str
    query_string: bytes
    method: str
    data: bytes
    json_payload: Optional[Dict[Any, Any]] = {}
    headers: Optional[Dict[str, str]] = {}
    view_args: Dict[str, str] = {}
