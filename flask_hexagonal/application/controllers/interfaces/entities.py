from http import HTTPStatus

from pydantic import BaseModel
from typing import Optional, List, Dict

from flask import Response


class JsonResponse(BaseModel):

    content: str
    status: HTTPStatus
    headers: Optional[List[Dict[str, str]]]
    content_type: str = "application/json"


class Request(BaseModel):
    path: str
    query_string: bytes
    method: str
    data: bytes
    headers: Dict[str, str]